# -*- coding: utf-8 -*-
"""
Created on May 20, 2024

针对哥白尼数据空间生态系统 Copernicus Data Space Ecosystem（CDSE）
使用OData API批量下载数据

过程参考：微信公众号——海研人
https://mp.weixin.qq.com/s/8vWCMYy_pkwauVkwZd3rYQ

过程参考：微信公众号——小y只会写bug
https://mp.weixin.qq.com/s/aEbsusU8FIrJTRorQR1oPQ

过程参考：CSDN——hyzhao_RS
https://blog.csdn.net/mrzhy1/article/details/132921422

OData API官方文档
https://documentation.dataspace.copernicus.eu/APIs/OData.html

Access token官方文档（已无python方法，参考“海研人”代码）
https://documentation.dataspace.copernicus.eu/APIs/Token.html

@author:辽宁省自然资源卫星应用技术中心 技术组
"""

import os
import sys
import pandas as pd
import requests
import json
import datetime
from tqdm import tqdm

# 基础设置
############################################################################
# 1 所需卫星数据
query_satellite = 'SENTINEL-2'

# 2 检索时文件名需包括的字符串，可以是产品类型，如：SLC；可以是产品级别，如：L2A；也可以是区块代码，如：RVQ
query_contains = 'L2A'

# 3 起始日期
query_startDate = '2023-09-01'
query_endDate = '2023-09-15'

# 4 检索区域 在如下网站绘制geojson文件 https://geojson.io/#map=2/0/20
map_geojson = 'map.geojson'

# 5 expand option，暂时未开发此功能
query_expand = ''

# 6 哥白尼数据空间生态系统账号密码 在如下网站申请：https://dataspace.copernicus.eu/
CDSE_email = '您的账号'
CDSE_password = '您的密码'

# 7 数据保存路径
output_dir = 'D:/Data/'
############################################################################


# 获取CDSE的Access token
def get_access_token(username: str, password: str) -> str:
    data = {
        "client_id": "cdse-public",
        "username": username,
        "password": password,
        "grant_type": "password",
        }
    try:
        r = requests.post(
            "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
            data=data,
        )
        r.raise_for_status()
    except Exception as e:
        raise Exception(
            f"Access token creation failed. Reponse from the server was: {r.json()}"
            )
    return r.json()["access_token"]


# 获取ROI的坐标字符串
# Disclaimers:
# 1.MULTIPOLYGON is currently not supported.
# 2.Polygon must start and end with the same point.
# 3.Coordinates must be given in EPSG 4326
def get_coordinates(geojson):
    with open(geojson, 'r') as f:
        data = f.read()
    geojson_data = json.loads(data)
    coordinates = geojson_data['features'][0]['geometry']['coordinates'][0]
    coordinates_string = ''
    for i in range(len(coordinates)):
        coordinates_string = coordinates_string + str(coordinates[i][0]) + ' ' + str(coordinates[i][1]) + ', '
    coordinates_string = coordinates_string[:-2]
    return coordinates_string


# 获取查询链接 检索条件之间要加 and
def get_https_request(satellite, contains, start_date, end_date, geojson, expand):
    # 基础前缀
    base_prefix = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter="
    # 检索条件
    collection = "Collection/Name eq '" + satellite + "' and contains(Name,'" + contains + "')"
    roi_coordinates = get_coordinates(geojson)
    geographic_criteria = "OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((" + roi_coordinates + "))') "
    content_date = (
            "ContentDate/Start gt " + start_date + "T00:00:00.000Z and " +
            "ContentDate/Start lt " + end_date + "T00:00:00.000Z"
    )
    # Top option specifies the maximum number of items returned from a query.
    # The default value is set to 20.
    # The acceptable arguments for this option: Integer <0,1000>
    top_option = "&$top=1000"
    # The expand option enables users to see the full metadata of each returned result.
    # The acceptable arguments for this option: Attributes, Assets and Locations.
    # Expand assets allows to list additional assets of products, including quicklooks
    # Expand Locations allows users to see full list of available products’ forms (compressed/uncompressed)
    # and locations from which they can be downloaded
    # 暂时不开发expand_option功能，expand为空，但保留expand_option语句
    if not expand:
        # 最终检索链接
        https_request = (
                base_prefix + collection + " and " + geographic_criteria + " and " + content_date + top_option
        )
    else:
        expand_option = "&$expand=" + expand
        # 最终检索链接
        https_request = (
                base_prefix + collection + " and " + geographic_criteria + " and " + content_date + top_option +
                expand_option
        )
    return https_request


# 下载数据
def download_data(token, id, name, length, output):
    url = f"https://download.dataspace.copernicus.eu/odata/v1/Products({id})/$value"
    headers = {"Authorization": f"Bearer {token}"}
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url, headers=headers, stream=True)
    try:
        print('[', datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'), '] '+'开始下载: '+name)
        with open(output, "wb") as file:
            if length is not None:
                # 使用total参数设置进度条的总长度
                pbar = tqdm(total=length, unit="B", unit_scale=True, desc=name)
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        # 更新进度条
                        pbar.update(len(chunk))
                # 确保进度条完成
                pbar.close()
        print('[', datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'), '] '+'下载成功: '+name)
        response.close()
    except Exception as e:
        print('[', datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'), '] '+'下载失败: '+name)
        print(f"发生了一个异常: {e}")


# 将文件名后缀改为.zip
def get_file_name(name):
    file_name = ''
    if query_satellite == 'SENTINEL-1':
        file_name = name.replace(".SAFE", ".zip")
    elif query_satellite == 'SENTINEL-2':
        file_name = name.replace(".SAFE", ".zip")
    elif query_satellite == 'SENTINEL-3':
        file_name = name.replace(".SEN3", ".zip")
    elif query_satellite == 'SENTINEL-5P':
        file_name = name.replace(".nc", ".zip")
    elif query_satellite == 'SENTINEL-6':
        file_name = name.replace(".SEN6", ".zip")
    return file_name


# 进行检索
request_url = get_https_request(
    query_satellite, query_contains, query_startDate, query_endDate, map_geojson, query_expand
)
JSON = requests.get(request_url).json()
if 'detail' in JSON:
    print(JSON['detail']['message'])
    sys.exit()
elif 'value' in JSON:
    df = pd.DataFrame.from_dict(JSON['value'])
    # print(df.columns)
    if len(df) == 0:
        print('未查询到数据')
        sys.exit()
    # 原始数据id列表
    data_id_list = df.Id
    # 原始数据name列表
    data_name_list = df.Name
    # 原始数据length列表
    date_content_length = df.ContentLength
else:
    print('存在未知查询错误')
    sys.exit()

for i in range(len(data_id_list)):
    print(data_name_list[i])
    data_id = data_id_list[i]
    data_name = get_file_name(data_name_list[i])
    data_length = date_content_length[i]
    # 判断数据保存路径是否存在，如不存在则创建数据保存路径
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, data_name)
    # 判断文件是否已经下载，如已经下载则跳过，不再下载
    if os.path.exists(output_file) and os.path.getsize(output_file) == data_length:
        print(output_file + ' 已经存在，跳过下载')
    else:
        access_token = get_access_token(CDSE_email, CDSE_password)
        download_data(access_token, data_id, data_name, data_length, output_file)

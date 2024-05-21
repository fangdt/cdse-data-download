# -*- coding: utf-8 -*-

import pandas as pd
import requests
import json
import re
from datetime import datetime


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


# 检查输入起始日期和截止日期格式
def check_date_range(start_date_str, end_date_str):
    # 定义日期格式的正则表达式
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    # 检查起始日期和截止日期的格式，
    # 起始日期格式错误，返回值1
    if not date_pattern.match(start_date_str):
        return 1
    # 截止日期格式错误，返回值2
    if not date_pattern.match(end_date_str):
        return 2
    # 尝试解析日期，并检查它们的有效性
    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        # 确保起始日期在截止日期之前或相同，如果起始日期在截止日期之后，返回值3
        if start_date > end_date:
            return 3
        # 如果一切正常，返回值9
        return 9
    except ValueError:
        # 如果解析日期时发生错误（例如，2月30日），返回值4
        return 4


# 获取查询链接，检索条件之间要加 and
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


# 更改文件名称后缀，将其均改为.zip
def chang_extension(query_satellite, name):
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


# 获取数据ID、NAME和Length
def get_datas(url):
    res = requests.get(url)
    data_json = res.json()
    res.close()
    if 'value' in data_json:
        df = pd.DataFrame.from_dict(data_json['value'])
        # 获取成功，但为查询到数据，返回值1
        if len(df) == 0:
            return 1
        # 获取成功，并查询到数据，返回原始数据id,name,length列表
        id_list = df.Id
        name_list = df.Name
        length_list = df.ContentLength
        return id_list, name_list, length_list
    else:
        # 获取失败，返回值2
        return 2

# CDSE 数据下载工具 v2.0

## 项目背景

2023年5月1日，利用第三方 [sentinelsat][link1] 库，写了一个界面化的哨兵卫星数据下载工具。可好景不长，哥白尼开放数据访问中心（[Copernicus Open Access Hub][link2]）在2023年10月底关闭了，原来写的工具已经无法使用了。为了能够在新的网站——哥白尼数据空间生态系统（[Copernicus Data Space Ecosystem][link3]）批量下载哨兵卫星数据，2024年5月，利用网站提供的 [OData][link4] 的API，编写了这个——CDSE 数据下载工具。

## 使用说明

**1. 如果您有Python环境：**  

您只需要下载cdse-data-download.py这一个文件，安装pandas、requests、tqdm等第三方支持库，设置好您的CDSE账户、所需下载卫星平台、卫星名称包含文字、起止日期、GeoJSON文件、保存位置等，运行即可。  

**2. 如果您没有Python环境，且为windows 10及以上操作系统**  

您可以clone项目，或者直接下载 [Releases][link5] 中已经编译好的windows界面化工具。

## 如何使用

### CDSE 账户
账户和密码需要在哥白尼数据空间生态系统（[Copernicus Data Space Ecosystem][link3]）注册。

### 查询设置
卫星平台和产品类型按需选择，起止日期和截止日期格式为：YYYY-MM-DD，例如：2024-05-01

#### 卫星平台和产品类型
+ SENTINEL-1（哨兵一号）
  + Level 0
    + IW_RAW：原始影像
  + Level 1
    + IW_SLC：单视复数影像，Single Look Complex
    + IW_GRDH：地距多视影像，Ground Range Detected
    + IW_ETA：扩展时序注释数据集，The Extended Timing Annotation Dataset
  + 注：IW：Interferometric Wide swath


+ SENTINEL-2（哨兵二号）  
  + Level 1C
    + MSIL1C：大气层顶部 (TOA) 反射率图像
  + Level 2A
    + MSIL2A：经大气校正的表面反射率 (SR) 产品
  + 注：MSI：MultiSpectral Instrument


+ SENTINEL-3（哨兵三号）
  + OLCI：Ocean and Land Colour Instrument
    + Level 1B
      + OL_1_EFR：全分辨率 TOA 反射率
      + OL_1_ERR：降低分辨率 TOA 反射率
    + Level 2
      + OL_2_LFR：全分辨率陆地和大气地球物理产品
      + OL_2_LRR：低分辨率陆地和大气地球物理产品
      + OL_2_WFR：全分辨率水和大气地球物理产品
      + OL_2_WRR：低分辨率水和大气地球物理产品
  + SLSTR：Sea and Land Surface Temperature Radiometer
    + Level 1
      + SL_1_RBT：亮度温度和辐射率
    + Level 2
      + SL_2_AOD：气溶胶光学深度
      + SL_2_FRP：火灾辐射功率
      + SL_2_LST：地表温度参数
      + SL_2_WST：海面温度参数
  + SYNERGY
    + Level 2
      + SY_2_AOD：超像素分辨率的陆地和海洋全球气溶胶参数（4.5 km x 4.5 km）
      + SY_2_SYN：陆地表面反射率和气溶胶参数
      + SY_2_VG1：1 km 类植物产品 TOA 反射率
      + SY_2_VGP：1 km 类植物产品 1 天合成表面反射率和 NDVI


+ SENTINEL-5P（哨兵五号）
  + Level 2
    + OFFL_L2__AER_AI：紫外线气溶胶指数
    + OFFL_L2__AER_LH：气溶胶层高度（中等气压）
    + OFFL_L2__CLOUD：云量、反照率、云顶大气压
    + OFFL_L2__CH4：甲烷（CH4）总柱含量
    + OFFL_L2__CO：一氧化碳（CO）总柱含量
    + OFFL_L2__HCHO：甲醛（HCHO）总柱含量
    + OFFL_L2__NO2：二氧化氮（NO2）总柱含量、对流层柱含量
    + OFFL_L2__O3：臭氧（O3）总柱含量
    + OFFL_L2__SO2：二氧化硫（SO2）总柱含量
  + 注：OFFL：OFFLINE，离线数据流


+ SENTINEL-6（哨兵六号）
  + Level 1
    + P4_1B_LR：1B 级低分辨率（LR）产品
  + Level 2
    + P4_2__LR：低分辨率（LR）产品
  + 注：P4：Poseidon-4，波塞冬-4 或 海神-4


### GeoJSON文件
GeoJSON文件为任务区范围文件，可在网站 [geojson.io][link6] 上获取。  
获取方法：进入网站后，划定任务区域，点击Save，保存为GeoJSON格式文件即可。

### 保存位置
填写下载数据的文件夹保存路径。

### 数据查询
用于显示数据查询结果。

### 控制面板
#### 查询
可以查询覆盖任务区范围的数据产品，并将产品名称显示在"数据查询"框内。
1. 选择正确的卫星平台、产品类型；
2. 填写起始日期、截止日期；
3. 选择输入GeoJSON文件；
4. 点击"查询"按钮。

#### 下载
下载查询到数据产品，将其保存在"保存位置"文件夹内。  
注：点击"下载"按钮前，应先点击"查询"按钮查询数据，只有当"数据查询"框内有产品名称时，点击"下载"按钮才能工作。
1. 填写 CDSE 账号和密码；
2. 选择数据保存位置文件夹；
3. 点击"下载"按钮，开始下载数据。

#### 清空
将"数据查询"框内显示文本清空。

#### 导出
将"数据查询"框内显示文本导出TXT文件。

#### 关于
显示工具的版本、开发、主页等信息。

### 下载状态
显示当前下载文件文件名、当前文件下载进度和所有文件下载进度等信息。

## 参考资料
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

[link1]:https://sentinelsat.readthedocs.io/
[link2]:https://scihub.copernicus.eu/
[link3]:https://dataspace.copernicus.eu/
[link4]:https://documentation.dataspace.copernicus.eu/APIs/OData.html
[link5]:https://github.com/fangdt/cdse-data-download/releases
[link6]:http://geojson.io/#map=2/0/20
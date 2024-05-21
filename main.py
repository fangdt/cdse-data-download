# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Slot, QTimer
import os
import sys
from datetime import datetime
import ui_main
import query
import download

# 基础设置
############################################################################
# 1 所需卫星数据
query_satellite = ''

# 2 检索时文件名需包括的字符串，可以是产品类型，如：SLC；可以是产品级别，如：L2A；也可以是区块代码，如：RVQ
query_contains = ''

# 3 起始与截止日期
query_startDate = ''
query_endDate = ''

# 4 检索区域 在如下网站绘制geojson文件 https://geojson.io/#map=2/0/20
map_geojson = ''

# 5 expand option，暂时未开发此功能
query_expand = ''

# 6 哥白尼数据空间生态系统账号密码 在如下网站申请：https://dataspace.copernicus.eu/
CDSE_email = ''
CDSE_password = ''

# 7 数据保存路径
output_dir = ''
############################################################################

# 卫星平台与数据类型
############################################################################
plat_list = ['SENTINEL-1', 'SENTINEL-2', 'SENTINEL-3', 'SENTINEL-5P', 'SENTINEL-6']
S1_type_list = ['IW_RAW', 'IW_SLC', 'IW_GRDH', 'IW_ETA']
S2_type_list = ['MSIL1C', 'MSIL2A']
S3_type_list = ['OL_1_EFR', 'OL_1_ERR', 'OL_2_LFR', 'OL_2_LRR', 'OL_2_WFR', 'OL_2_WRR',
                'SL_1_RBT', 'SL_2_AOD', 'SL_2_FRP', 'SL_2_LST', 'SL_2_WST',
                'SY_2_AOD', 'SY_2_SYN', 'SY_2_VG1', 'SY_2_VGP']
S5P_type_list = ['OFFL_L2__AER_AI', 'OFFL_L2__AER_LH', 'OFFL_L2__CLOUD',
                 'OFFL_L2__CH4', 'OFFL_L2__CO', 'OFFL_L2__HCHO',
                 'OFFL_L2__NO2', 'OFFL_L2__O3', 'OFFL_L2__SO2']
S6_type_list = ['P4_1B_LR', 'P4_2__LR']
############################################################################

# 等待下载数据列表
############################################################################
data_id_list = []
data_name_list = []
date_content_length = []
############################################################################

# 等待下载数据列表
############################################################################
access_token = ''
datas_len = 0
single_progress = 0
total_progress = 0
############################################################################


class MyWindow(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.comboBox.addItems(plat_list)
        self.comboBox_2.addItems(S1_type_list)
        self.comboBox.currentIndexChanged.connect(self.change_combo)
        self.pushButton.clicked.connect(self.get_geojson)
        self.pushButton_2.clicked.connect(self.get_save_path)
        self.pushButton_3.clicked.connect(self.get_query)
        self.pushButton_4.clicked.connect(self.get_download)
        self.pushButton_5.clicked.connect(self.text_clear)
        self.pushButton_6.clicked.connect(self.save_query_result)
        self.pushButton_7.clicked.connect(self.about_box)
        self.cmd = os.getcwd()
        # 创建查询工作线程实例
        self.query_thread = QueryThread(self)
        # 连接信号到槽函数
        self.query_thread.query_result_sig.connect(self.query_result_display)
        # 创建下载工作线程实例
        self.download_thread = DownloadThread(self)
        # 连接信号到槽函数
        self.download_thread.download_sig.connect(self.download_display)
        self.download_thread.download_complete_sig.connect(self.download_complete_message)
        # 创建单个文件下载定时器
        self.single_timer = QTimer(self)
        self.single_timer.timeout.connect(self.update_single_progress)
        # 创建所有文件下载定时器
        self.total_timer = QTimer(self)
        self.total_timer.timeout.connect(self.update_total_progress)

    @Slot()  # 声明这个方法是一个槽函数
    def start_query(self):
        # 启动查询工作线程
        self.query_thread.start()

    @Slot(str)  # 声明这个方法是一个槽函数
    def query_result_display(self, result):
        # 在QTextBrowser中显示结果
        self.textBrowser.append(result)
        # 停止线程
        # self.query_thread.quit()
        # 等待线程结束
        # self.query_thread.wait()

    @Slot()  # 声明这个方法是一个槽函数
    def start_download(self):
        # 启动下载工作线程
        self.download_thread.start()
        # 每1秒更新一次进度
        self.single_timer.start(1000)
        self.total_timer.start(1000)

    @Slot(str)  # 声明这个方法是一个槽函数
    def download_display(self, result):
        # 在QTextBrowser_2中显示结果
        self.textBrowser_2.append(result)
        # 停止线程
        # self.download_thread.quit()
        # 等待线程结束
        # self.download_thread.wait()

    @Slot()  # 声明这个方法是一个槽函数
    def download_complete_message(self):
        # 创建一个QMessageBox实例
        download_complete_message = QMessageBox(self)
        # 设置消息框的标题和文本
        download_complete_message.setWindowTitle("任务完成")
        download_complete_message.setText("下载任务已完成，谢谢使用！")
        # 设置消息框的图标（这里使用Information图标）
        download_complete_message.setIcon(QMessageBox.Icon.Information)
        # 显示消息框，并等待用户关闭它
        download_complete_message.exec()

    # 更新当前文件下载进度
    def update_single_progress(self):
        progress = single_progress
        self.progressBar.setValue(progress)
        # 只有当所有文件下载完成时
        if total_progress >= 100:
            # 下载完成时停止定时器
            self.single_timer.stop()

    # 更新所有文件下载进度
    def update_total_progress(self):
        progress = total_progress
        self.progressBar_2.setValue(progress)
        if progress >= 100:
            # 下载完成时停止定时器
            self.total_timer.stop()

    # 设置comboBox_2随comboBox变化
    def change_combo(self):
        platform = self.comboBox.currentText()
        if platform == 'SENTINEL-1':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(S1_type_list)
        elif platform == 'SENTINEL-2':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(S2_type_list)
        elif platform == 'SENTINEL-3':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(S3_type_list)
        elif platform == 'SENTINEL-5P':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(S5P_type_list)
        elif platform == 'SENTINEL-6':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(S6_type_list)

    # 获取ROI的GeoJSON文件
    def get_geojson(self):
        file = QFileDialog()
        file.setDirectory(self.cmd)
        a_file, _ = file.getOpenFileName(None, '选择文件', '.', 'GeoJSON文件(*.geojson)')
        self.lineEdit_5.setText(a_file)

    # 获取下载数据保存位置
    def get_save_path(self):
        fold = QFileDialog()
        fold.setDirectory(self.cmd)
        path = fold.getExistingDirectory()
        self.lineEdit_6.setText(path)

    # 数据查询
    def get_query(self):
        global query_satellite
        query_satellite = self.comboBox.currentText()
        global query_contains
        query_contains = self.comboBox_2.currentText()
        global query_startDate
        query_startDate = self.lineEdit_3.text()
        global query_endDate
        query_endDate = self.lineEdit_4.text()
        global map_geojson
        map_geojson = self.lineEdit_5.text()
        if not query_startDate:
            self.textBrowser.clear()
            self.textBrowser.append(f'WARNING: 请输入起始日期：格式为 2024-05-01')
        elif not query_endDate:
            self.textBrowser.clear()
            self.textBrowser.append(f'WARNING: 请输入截止日期：格式为 2024-05-01')
        elif not map_geojson:
            self.textBrowser.clear()
            self.textBrowser.append(f'WARNING: 请选择GeoJSON文件')
        else:
            self.textBrowser.clear()
            self.textBrowser.append(f'正在查询，请稍后……')
            # 开始查询
            self.start_query()

    # 数据下载
    def get_download(self):
        self.download_thread.quit()
        global single_progress, total_progress
        single_progress = 0
        total_progress = 0
        global CDSE_email
        CDSE_email = self.lineEdit.text()
        global CDSE_password
        CDSE_password = self.lineEdit_2.text()
        global output_dir
        output_dir = self.lineEdit_6.text()
        if datas_len == 0:
            self.textBrowser_2.clear()
            self.textBrowser_2.append(f'请先查询数据')
        elif not CDSE_email:
            self.textBrowser_2.clear()
            self.textBrowser_2.append(f'WARNING: 请输入 CDSE 账号')
        elif not CDSE_password:
            self.textBrowser_2.clear()
            self.textBrowser_2.append(f'WARNING: 请输入 CDSE 密码')
        elif not output_dir:
            self.textBrowser_2.clear()
            self.textBrowser_2.append(f'WARNING: 请输入保存位置')
        else:
            global access_token
            try:
                # 获取 access_token
                access_token = download.get_access_token(CDSE_email, CDSE_password)
                self.textBrowser_2.clear()
                # 开始下载
                self.start_download()
            except Exception as e:
                self.textBrowser_2.clear()
                self.textBrowser_2.append(f'WARNING: 发生了一个异常: {e}, 请检查账户或密码是否正确')

    # 清空数据查询窗口显示内容
    def text_clear(self):
        self.textBrowser.clear()

    # 保存数据查询窗口显示内容为txt文本
    def save_query_result(self):
        text = self.textBrowser.toPlainText()
        fold = QFileDialog()
        fold.setDirectory(self.cmd)
        filename, filetype = fold.getSaveFileName(None, '保存文件', '.txt', 'TXT(*.txt)')
        if filename != "":
            file = open(filename, 'w', encoding='utf-8')
            file.write(text)

    # 关于窗口
    def about_box(self):
        about_title = '关于 CDSE 数据下载工具'
        about_version = '版本：V2.0.20240520'
        about_copyright = '开发：辽宁省自然资源卫星应用技术中心 技术组'
        about_link = 'https://liaoning.sasclouds.com/web/home'
        about_website = "官网：<a href='%s'>辽宁省自然资源卫星遥感服务平台</a>" % about_link
        about_tel = '电话：024-86586307'
        about_link2 = 'https://github.com/fangdt/cdse-data-download'
        about_page = "主页：<a href='%s'>cdse-data-download</a>" % about_link2
        about_content = (
                about_version + '<br>' +
                about_copyright + '<br>' +
                about_website + '<br>' +
                about_tel + '<br>' +
                about_page
        )
        QMessageBox.about(self, about_title, about_content)


# 查询线程
class QueryThread(QThread):
    # 定义一个信号来传递查询结果
    query_result_sig = Signal(str)

    def run(self):
        if query.check_date_range(query_startDate, query_endDate) == 1:
            self.query_result_sig.emit(f'WARNING: 输入起始日期格式错误，格式为 2024-05-01')
        elif query.check_date_range(query_startDate, query_endDate) == 2:
            self.query_result_sig.emit(f'WARNING: 输入截止日期格式错误，格式为 2024-05-01')
        elif query.check_date_range(query_startDate, query_endDate) == 3:
            self.query_result_sig.emit(f'WARNING: 起始日期不能在截止日期之后')
        elif query.check_date_range(query_startDate, query_endDate) == 4:
            self.query_result_sig.emit(f'WARNING: 起始日期或截止日期无效')
        else:
            request_url = query.get_https_request(
                query_satellite, query_contains, query_startDate, query_endDate, map_geojson, query_expand
            )
            if query.get_datas(request_url) == 1:
                self.query_result_sig.emit(f'未查询到数据')
            elif query.get_datas(request_url) == 2:
                self.query_result_sig.emit(f'存在未知查询错误')
            else:
                global data_id_list, data_name_list, date_content_length
                data_id_list, data_name_list, date_content_length = query.get_datas(request_url)
                global datas_len
                datas_len = len(data_id_list)
                for i in range(datas_len):
                    data_name = query.chang_extension(query_satellite, data_name_list[i])
                    self.query_result_sig.emit(data_name)
                self.query_result_sig.emit(f'数据查询完成，共查询到 %d 条数据' % datas_len)


# 下载线程
class DownloadThread(QThread):
    # 定义一个信号来传递下载状态
    download_sig = Signal(str)
    # 定义一个信号来传递下载完成状态
    download_complete_sig = Signal()

    def run(self):
        total_length = sum(date_content_length)
        for i in range(len(data_id_list)):
            data_id = data_id_list[i]
            data_name = query.chang_extension(query_satellite, data_name_list[i])
            data_length = date_content_length[i]
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file = os.path.join(output_dir, data_name)
            if os.path.exists(output_file) and os.path.getsize(output_file) == data_length:
                self.download_sig.emit(data_name + ' 已经存在，跳过下载')
            else:
                token = download.get_access_token(CDSE_email, CDSE_password)
                j = i + 1
                response = download.download_response(data_id, token)
                try:
                    start_time = datetime.now().strftime('%H:%M:%S')
                    self.download_sig.emit(f'[ %s ] 正在下载第 %d 条数据：' % (start_time, j))
                    self.download_sig.emit(data_name)
                    data_loading_length = 0
                    with open(output_file, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                file.write(chunk)
                                data_loading_length += len(chunk)
                            global single_progress, total_progress
                            single_progress = int((data_loading_length / data_length) * 100)
                            total_loading_length = sum(date_content_length[:i]) + data_loading_length
                            total_progress = int((total_loading_length / total_length) * 100)
                    complete_time = datetime.now().strftime('%H:%M:%S')
                    self.download_sig.emit(f'[ %s ] 第 %d 条数据下载完成' % (complete_time, j))
                    response.close()
                except Exception as e:
                    self.download_sig.emit(f'WARNING: 发生了一个异常: {e}')
        self.download_complete_sig.emit()


if __name__ == "__main__":
    # 在 PySide6 中，通常不需要显式地设置任何属性来启用高DPI支持，因为 Qt 6 已经默认支持它。
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

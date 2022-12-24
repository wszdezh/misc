# -*- coding: utf-8 -*-
import json
import xmltodict
import re, os, sys
import zipfile
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer, QCoreApplication, QThread, pyqtSignal
from my_win import Ui_Form

json_path = './PageConfig/theme2/json/'
xml_path = './PageConfig/theme2/xml/'
zip_name = 'tmp.zip'

'''
csv to xlsx：
		import pandas as pd
		csv = pd.read_csv('x.csv', encoding='utf-8') #gbk
		csv.to_excel(x.xlsx, sheet_name='data')
xlsx to csv:
		xls = pd.read_excel('x.xlsx', index_col=0)
		xls.to_csv('x.csv', encoding='utf-8')
获取xlsx内容：
        import xlrd
        import numpy as np
        workbook = xlrd.open_workbook(filePath)
        sheet = workbook.sheet_by_index(0)
        row = sheet.nrows
        col = sheet.ncols
        mt = np.zeros([row,col], np.float)
        for i in range(row):
            for j in range(col)
                mt[i][j] = float(sheet.cell(i,j).value)

创建文本并写入内容：
        seq = ['xxx\n']
        with open(fileName, 'w') as f:
            f.writelines(seq)
'''


# xml转json的函数
def xmltojson(xmlstr):
    xmlparse = xmltodict.parse(xmlstr)
    str = json.dumps(xmlparse, ensure_ascii = False, indent=1)
    # str = json.dumps(xmlparse, indent=1)
    return str

def file_handle(strfile):
    with open(xml_path + strfile + '.xml','r', encoding = 'UTF-8') as f_xml:
        data_xml = f_xml.read()

    with open(json_path + strfile + '.json', 'w', encoding = 'UTF-8') as f_json:
        data_json = xmltojson(data_xml)
        f_json.write(data_json)

    with open(json_path + strfile + '.json', 'r', encoding='UTF-8') as f_json2:
        alllines = f_json2.readlines()

    with open(json_path + strfile + '.json', 'w', encoding='UTF-8') as f_json3:
        for line in alllines:
            tmp = re.sub("\"@","\"_",line)
            # if tmp.find('\\u') != -1:
            #     tmp = tmp.encode('utf-8').decode('unicode_escape')
            f_json3.writelines(tmp)

def resource_path(relative_path):
    """
    :param relative_path:
    :return:# 生成资源文件目录访问路径
    """
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class handleThread(QThread):
    trigger1 = pyqtSignal(int)
    def __init__(self, parent=None):
        super(handleThread, self).__init__()

    def run(self):
        self.handle()


    def handle(self):
        if not os.path.exists(xml_path):
            sys.exit(0)

        if not os.path.exists(json_path):
            os.makedirs(json_path)

        files = os.listdir(xml_path)
        for file in files:
            if file.endswith('.xml'):
                file_handle(file[:-4])

        self.trigger1.emit(1)
        zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for dir_path, dir_name, file_names in os.walk('./'):  # 通过os.walk()遍历所有子目录
            print(dir_path)
            for file_name in file_names:
                if file_name.find('tmp') != -1 or file_name.find('xml_to_json') != -1 or file_name.find('WiseConf.kczip') != -1:
                    continue
                zp.write(os.path.join(dir_path, file_name))
        zp.close()

        self.trigger1.emit(2)
        file = resource_path(r'aes_encrypt.exe')
        # print(file)
        os.system(file + ' ' + zip_name +' WiseConf.kczip')

        if os.path.exists('./tmp.zip'):
            os.remove('./tmp.zip')

        sys.exit(0)

class my_win(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(my_win, self).__init__(parent)
        self.setupUi(self)
        QTimer.singleShot(1000, self.create_thread)


    def create_thread(self):
        self.thread = handleThread()
        self.thread.start()
        self.thread.trigger1.connect(self.modify_text)

    def modify_text(self, flg):
        print(flg)
        if flg == 1:
            self.label.setText(QCoreApplication.translate("Form", "打包中..."))
            self.label.repaint()
        elif flg == 2:
            self.label.setText(QCoreApplication.translate("Form", "OVER，下次再见..."))
            self.label.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = my_win()
    w.show()
    sys.exit(app.exec_())


# create by Landis at 2020.01.15
# !/usr/bin/python
# coding=utf-8

import unicodedata
import xlrd
import json
import xml.dom.minidom
import os
import codecs
import ctypes
import time
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from enum import Enum
from tkinter.filedialog import (askopenfilename, askdirectory)

# -------------------------------- 公共变量 ---------------------------------------
show_toast_Lab = None                   # UI上界面显示Log日志
pub_folder_select_type = None               # 文件类型选择,是文件还是文件夹整个转化
pub_excel_path_input = None                 # Excel输入路径
pub_data_path_output = None                 # 转化文件输出路径
pub_encrypt_file_path = None                # 加密文件路径
pub_data_convert_type = None                # 转化类型选择
pub_excel_data_type =[]
pub_excel_select_type = '.xls .xlsx .xlsm'
pub_excel_change_type = ["json", "xml"]

class LabLv(Enum):
    INFO = 'black'
    WARN = 'orange'
    ERROR = 'red'
    SUCCESS = 'green'
    SKIP = 'blue'
# -------------------------------- ExcelToJson Deal Tool ---------------------------------------

def dealExcelDataToXml(excel_file):
    xmlData = readExcelData(r'' + excel_file)
    ori_data = xmlData.sheets()[0]

    data_doc = xml.dom.minidom.Document()
    info = data_doc.createElement('info')
    data_doc.appendChild(info)

    excel_name = os.path.basename(str(excel_file))
    file_name = excel_name.split('.')[0]

    for data_nrow in range(1, ori_data.nrows):
        if data_nrow == 0:
            continue
        item = data_doc.createElement('node')
        count = 0
        for data_ncol in range(0, ori_data.ncols):
            key = ori_data.cell(0, data_ncol).value
            value = ori_data.cell(data_nrow, data_ncol).value
            if data_ncol == 0:
                if not is_number(value):
                    showLogInfo(excel_name + '表,首列：' + key + '应为数值, 不被转化', LabLv.ERROR)
                    count += 1
                    continue
            if len(str(value)) == 0:
                showLogInfo(excel_name + '表,第' + str(data_nrow + 1) + '行,' + key + '数值为空,请检查', LabLv.ERROR)
                count +=1
                continue
            item.setAttribute(key, str(value))
            count += 1

        if count == ori_data.ncols and bool(item._attrs):
            info.appendChild(item)

    saveFile(pub_data_path_output.get(), file_name, data_doc.toprettyxml(), "xml")


def dealExcelDataToJson(excel_file):
    workbook = readExcelData(r'' + excel_file)
    ori_data = workbook.sheet_by_name(workbook.sheet_names()[0])
    info_name = ori_data.row_values(0)
    new_data = []

    excel_name = os.path.basename(str(excel_file))
    file_name = excel_name.split('.')[0]

    for data_nrow in range(ori_data.nrows):
        if data_nrow == 0:
            continue
        count = 0
        new_cow_data = {}
        for data_ncol in ori_data.row_values(data_nrow):
            if count == 0:
                if not is_number(data_ncol):
                    showLogInfo(excel_name + '表,首列：' + info_name[count] + '应为数值, 不被转化', LabLv.ERROR)
                    count += 1
                    continue
            if len(str(data_ncol)) == 0:
                showLogInfo(excel_name + '表,第' + str(data_nrow + 1) + '行,' + info_name[count] + '数值为空,请检查', LabLv.ERROR)
                count += 1
                continue
            new_cow_data[info_name[count]] = str(data_ncol)
            count += 1

        if count == ori_data.ncols and len(new_cow_data) > 0:
            new_data.append(new_cow_data)
            # new_data[ori_data.row_values(data_nrow)[0]] = new_cow_data

    json_data = json.dumps(new_data, indent=4).encode("utf-8").decode('unicode_escape')
    saveFile(pub_data_path_output.get(), file_name, json_data, "json")


def readExcelData(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        showLogInfo(u'表格读取失败：%s' % e, LabLv.ERROR)
        return None


def saveFile(file_path, file_name, data, file_type):
    output = codecs.open(file_path + "/" + file_name + "." + file_type, 'w', "utf-8")
    output.write(data)
    output.close()
    showLogInfo(file_name + '.' + file_type + '  已转化', LabLv.SUCCESS)


# 判断是否为数字
def is_number(data):
    try:
        float(data)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(data)
        return True
    except (TypeError, ValueError):
        pass

    return False

# --------------------------------- Create Resources Folder------------------------------
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)



# ------------------------------------- Window ------------------------------------------
def selectPath():
    if pub_folder_select_type.get() == 1:
        inputFile = askopenfilename(filetypes=[('Excel files', pub_excel_select_type)])
    else:
        inputFile = askdirectory()
    if len(inputFile) != 0:
        pub_excel_path_input.set(os.path.normpath(inputFile))
        showLogInfo('当前选择路径文件:' + pub_excel_path_input.get())
        normalFile = os.path.normpath(inputFile)
        if len(pub_data_path_output.get()) == 0:
            if os.path.isdir(inputFile):
                pub_data_path_output.set(normalFile)
            elif os.path.isfile(inputFile):
                pub_data_path_output.set(os.path.dirname(normalFile))
            showLogInfo('初始默认输出路径:' + pub_data_path_output.get())


def outputPath():
    outputFile_ = askdirectory()
    if len(outputFile_) != 0:
        pub_data_path_output.set(os.path.normpath(outputFile_))
        showLogInfo('当前输出路径：' + pub_data_path_output.get())


def encryptFilePath():
    messagebox.showinfo('提示', '暂未支持数据加密，敬请期待')
    # pub_encrypt_file_path.set(os.path.normpath(askopenfilename())) # 暂未使用


def refreshEncryptBtn(encrypt_btn, encrypt_btn_state):
    state = NORMAL if encrypt_btn_state.get() == 1 else DISABLED
    encrypt_btn['state'] = state


def showLogInfo(msg, lab_lv=LabLv.INFO):
    show_toast_Lab.config(state=NORMAL)
    realtime = time.strftime("%H:%M:%S")
    text_var = realtime + '    ' + msg + '\n'
    show_toast_Lab.insert('end', text_var, str(lab_lv))
    show_toast_Lab.see(END)
    show_toast_Lab.config(state=DISABLED)


def dataBoxItemClick():
    if os.path.isdir(pub_excel_path_input.get()):
        for root, ds, fs in os.walk(pub_excel_path_input.get()):
            for fileName in fs:
                convertDateByExcelFile(os.path.join(root, fileName))
    elif os.path.isfile(pub_excel_path_input.get()):
        convertDateByExcelFile(pub_excel_path_input.get())
    else:
        showLogInfo('转换的文件路径未选择，请确认', LabLv.WARN)


def convertDateByExcelFile(excel_file):
    excel_type = os.path.splitext(excel_file)[-1][1:]
    excel_name = os.path.basename(str(excel_file))
    if '~$' in excel_name:
        showLogInfo(excel_name + '缓存文件，忽略', LabLv.SKIP)
        return
    if len(excel_type) == 0:
        return

    if excel_type in pub_excel_select_type:
        if pub_data_convert_type.get() == pub_excel_change_type[0]:
            dealExcelDataToJson(excel_file)
        elif pub_data_convert_type.get() == pub_excel_change_type[1]:
            dealExcelDataToXml(excel_file)


def onGUI():
    global pub_excel_path_input
    pub_excel_path_input = StringVar()
    global pub_folder_select_type
    pub_folder_select_type = IntVar()
    Label(window, text="目标路径:").grid(row=0, column=0)
    Entry(window, textvariable=pub_excel_path_input, state='disabled').grid(row=0, column=1)
    Button(window, text="浏览", command=lambda: selectPath()).grid(row=0, column=2)
    Checkbutton(window, text='仅读文件', variable=pub_folder_select_type, onvalue=1, offvalue=0).grid(row=0, column=3)

    global pub_data_path_output
    pub_data_path_output = StringVar()
    Label(window, text="输出路径:").grid(row=1, column=0)
    Entry(window, textvariable=pub_data_path_output, state='disabled').grid(row=1, column=1)
    Button(window, text="浏览", command=lambda: outputPath()).grid(row=1, column=2)

    global pub_encrypt_file_path
    pub_encrypt_file_path = StringVar()
    encrypt_btn_state = IntVar()
    Label(window, text="加密文件:").grid(row=2, column=0)
    Entry(window, textvariable=pub_encrypt_file_path, state='disabled').grid(row=2, column=1)
    encrypt_btn = Button(window, text="浏览", state='disabled', command=lambda: encryptFilePath())
    encrypt_btn.grid(row=2, column=2)
    Checkbutton(window, text='是否加密', variable=encrypt_btn_state, command=lambda: refreshEncryptBtn(encrypt_btn, encrypt_btn_state), onvalue=1, offvalue=0).grid(row=2, column=3)

    global pub_data_convert_type
    pub_data_convert_type = StringVar()
    dataBoxList = ttk.Combobox(window, width=8, state='readonly', textvariable=pub_data_convert_type)
    dataBoxList["values"] = pub_excel_change_type
    dataBoxList.current(0)
    dataBoxList.grid(row=3, column=3)

    Button(window, width=35, text="开始转换", command=lambda: dataBoxItemClick()).grid(row=3, column=0, columnspan=3)

    global show_toast_Lab
    show_toast_Lab = Text(window, width=50, state=DISABLED)
    show_toast_Lab.grid(row=4, column=0, columnspan=4)
    # ------提前注册文本颜色
    for lv in LabLv:
        show_toast_Lab.tag_config(str(lv), foreground=lv.value)

def onCreateWindow():
    window.title("Table Tool")
    # -------- 状态栏显示的应用图标
    iconFile = resource_path(os.path.join('Resources', 'GetRight.ico'))
    my_ppid = 'company.product.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_ppid)
    window.iconbitmap(iconFile)
    # -------- 状态栏显示的应用图标
    window.geometry()
    onGUI()
    window.mainloop()

window = Tk()

onCreateWindow()

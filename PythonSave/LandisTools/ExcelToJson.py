# create by landis at 2020.01.15
# !/usr/bin/python
# coding=utf-8

import PythonFile
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
from tkinter.filedialog import (askopenfilename, askdirectory)

# -------------------------------- 公共变量 ---------------------------------------
show_toast_Lab = None                   # UI上界面显示Log日志
pub_folder_select_type = None               # 文件类型选择,是文件还是文件夹整个转化
pub_excel_path_input = None                 # Excel输入路径
pub_data_path_output = None                 # 转化文件输出路径
pub_encrypt_file_path = None                # 加密文件路径
pub_data_convert_type = None                # 转化类型选择

# -------------------------------- ExcelToJson Tool ---------------------------------------

def dealExcelDataToXml(excel_file):
    xmlData = readExcelData(r'' + excel_file)
    ori_data = xmlData.sheets()[0]

    doc = xml.dom.minidom.Document()
    info = doc.createElement('info')
    doc.appendChild(info)

    for data_nrow in range(1, ori_data.nrows):
        item = doc.createElement('item')
        for data_ncol in range(0, ori_data.ncols):
            key = ori_data.cell(0, data_ncol).value
            value = ori_data.cell(data_nrow, data_ncol).value
            if isinstance(value, float):
                value = '%0d' % value
            item.setAttribute(key, value)

        info.appendChild(item)

    saveFile('E:/Test_Save', '123', doc.toprettyxml(), "xml")



def dealExcelDataToJson(excel_file):
    workbook = readExcelData(r'' + excel_file)
    ori_data = workbook.sheet_by_name(workbook.sheet_names()[0])
    info_name = ori_data.row_values(0)
    new_data = {}

    for i in range(ori_data.nrows):
        if i == 0:
            continue
        count = 0
        new_cow_data = {}
        for j in ori_data.row_values(i):
            new_cow_data[info_name[count]] = str(j)
            count += 1
        new_data[ori_data.row_values(i)[0]] = new_cow_data

    json_data = json.dumps(new_data, indent=4, sort_keys=True).encode("utf-8").decode('unicode_escape')
    saveFile('E:/Test_Save', '123', json_data, "json")


def readExcelData(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(u'excel表格读取失败：%s' % e)
        return None


def saveFile(file_path, file_name, data, filetype):
    output = codecs.open(file_path + "/" + file_name + "." + filetype, 'w', "utf-8")
    output.write(data)
    output.close()


# dealExcelDataToJson(PythonFile.testfile)
# dealExcelDataToXml(PythonFile.testfile)
# ---------------------------------------------------------------------------------------


def selectPath():
    if pub_folder_select_type.get() == 1:
        path_ = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    else:
        path_ = askdirectory()
    pub_excel_path_input.set(path_)
    if len(pub_excel_path_input.get()) != 0:
        showLogInfo('当前选择的路径为:' + pub_excel_path_input.get())
    # if path_ != '':
    #     excel_file_name = os.path.basename(str(path_))
    #     excel_name = excel_file_name.split('.')[0]
    #     excel_type = excel_file_name.split('.')[1]


def outputPath():
    outputFile_ = askdirectory()
    pub_data_path_output.set(outputFile_)


def encryptFilePath():
    messagebox.showinfo('提示','暂未支持数据加密，敬请期待')
    # pub_encrypt_file_path.set(askopenfilename()) # 暂未使用


def refreshencryptBtn(encrypt_btn, encrypt_btn_state):
    state = NORMAL if encrypt_btn_state.get() == 1 else DISABLED
    encrypt_btn['state'] = state
    showLogInfo('123')


def showLogInfo(info):
    show_toast_Lab.config(state=NORMAL)
    realtime = time.strftime("%H:%M:%S")
    text_var = realtime + '    ' + info + '\n'
    show_toast_Lab.insert('end', text_var)
    show_toast_Lab.see(END)
    show_toast_Lab.config(state=DISABLED)


def dataBoxItemClick():
    showLogInfo(pub_data_convert_type.get())



def onGUI():
    global pub_excel_path_input
    pub_excel_path_input = StringVar()
    global pub_folder_select_type
    pub_folder_select_type = IntVar()
    Label(window, text="目标路径:").grid(row=0, column=0)
    Entry(window, textvariable=pub_excel_path_input, state='disabled').grid(row=0, column=1)
    Button(window, text="浏览", command=lambda: selectPath()).grid(row=0, column=2)
    Checkbutton(window, text='仅文件', variable=pub_folder_select_type, onvalue=1, offvalue=0).grid(row=0, column=3)

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
    Checkbutton(window, text='是否加密', variable=encrypt_btn_state, command=lambda: refreshencryptBtn(encrypt_btn, encrypt_btn_state), onvalue=1, offvalue=0).grid(row=2, column=3)


    global pub_data_convert_type
    pub_data_convert_type = StringVar()
    databoxList = ttk.Combobox(window, width=8, state='readonly', textvariable=pub_data_convert_type)
    databoxList["values"] = ("json", "xml")
    databoxList.current(0)
    databoxList.grid(row=3, column=3)

    Button(window, width=35, text="开始转换", command=lambda: dataBoxItemClick()).grid(row=3, column=0, columnspan=3)

    global show_toast_Lab
    show_toast_Lab = Text(window, width=50, state=DISABLED)
    show_toast_Lab.grid(row=4, column=0, columnspan=4)


def onCreateWindow():
    window.title("Table Tool")
    # -------- 状态栏显示的应用图标
    my_ppid = 'company.product.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_ppid)
    window.iconbitmap(default=os.getcwd() + '/Resources/Icon/GetRight.ico')
    # -------- 状态栏显示的应用图标
    window.geometry()
    onGUI()
    window.mainloop()

window = Tk()

onCreateWindow()



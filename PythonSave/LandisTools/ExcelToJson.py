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
from tkinter.filedialog import (askopenfilename, askdirectory)


# -------------------------------- ExcelToJson Tool ---------------------------------------

def dealExcelDataToXml():
    xmlData = readExcelData(r'' + PythonFile.testfile)
    ori_data = xmlData.sheets()[0]
    nrows = ori_data.nrows
    ncols = ori_data.ncols

    doc = xml.dom.minidom.Document()
    info = doc.createElement('info')
    doc.appendChild(info)

    for nrow in range(1, nrows):
        item = doc.createElement('item')
        for ncol in range(0, ncols):
            key = ori_data.cell(0, ncol).value
            value = ori_data.cell(nrow, ncol).value
            if isinstance(value, float):
                value = '%0d' % value
            item.setAttribute(key.encode('utf-8').decode('unicode_escape'), value.encode('utf-8').decode('unicode_escape'))

        info.appendChild(item)

    f = codecs.open('E:/Test_Save/123.xml', 'w', "utf-8")
    f.write(doc.toprettyxml())
    f.close()



def dealExcelDataToJson():
    workbook = xlrd.open_workbook(r'' + PythonFile.testfile)
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
    saveFile('E:/Test_Save', '123', json_data)


def readExcelData(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(u'excel表格读取失败：%s' % e)
        return None


def saveFile(file_path, file_name, data):
    output = codecs.open(file_path + "/" + file_name + ".json", 'w', "utf-8")
    output.write(data)
    output.close()


# dealExcelDataToJson()
dealExcelDataToXml()
# ---------------------------------------------------------------------------------------


def selectPath(enter_path, folder_type):
    if folder_type.get() == 1:
        path_ = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    else:
        path_ = askdirectory()
    enter_path.set(path_)
    # if path_ != '':
    #     excel_file_name = os.path.basename(str(path_))
    #     excel_name = excel_file_name.split('.')[0]
    #     excel_type = excel_file_name.split('.')[1]


def outputPath(output_path):
    outputFile_ = askdirectory()
    output_path.set(outputFile_)


def encryptFilePath(enter_path):
    messagebox.showinfo('提示','暂未支持加密功能，敬请期待')
    return
    enter_path.set(askopenfilename())


def refreshencryptBtn(encrypt_btn, encrypt_btn_state):
    state = NORMAL if encrypt_btn_state.get() == 1 else DISABLED
    encrypt_btn['state'] = state
    showLogInfo('123')


def showLogInfo(info):
    toast_info_textUI.config(state=NORMAL)
    realtime = time.strftime("%Y-%m-%d %H:%M:%S")
    text_var = realtime + '    ' + info + '\n'
    toast_info_textUI.insert('end', text_var)
    toast_info_textUI.see(END)
    toast_info_textUI.config(state=DISABLED)


def startChangeExcel():
    showLogInfo(123)

def onGUI():
    excel_path = StringVar()
    folder_type = IntVar()
    Label(window, text="目标路径:").grid(row=0, column=0)
    Entry(window, textvariable=excel_path, state='disabled').grid(row=0, column=1)
    Button(window, text="浏览", command=lambda: selectPath(excel_path, folder_type)).grid(row=0, column=2)
    Checkbutton(window, text='仅文件', variable=folder_type, onvalue=1, offvalue=0).grid(row=0, column=3)

    output_path = StringVar()
    Label(window, text="输出路径:").grid(row=1, column=0)
    Entry(window, textvariable=output_path, state='disabled').grid(row=1, column=1)
    Button(window, text="浏览", command=lambda: outputPath(output_path)).grid(row=1, column=2)

    encrypt_file_path = StringVar()
    encrypt_btn_state = IntVar()
    Label(window, text="加密文件:").grid(row=2, column=0)
    Entry(window, textvariable=encrypt_file_path, state='disabled').grid(row=2, column=1)
    encrypt_btn = Button(window, text="浏览", state='disabled', command=lambda: encryptFilePath(encrypt_file_path))
    encrypt_btn.grid(row=2, column=2)
    Checkbutton(window, text='是否加密', variable=encrypt_btn_state, command=lambda: refreshencryptBtn(encrypt_btn, encrypt_btn_state), onvalue=1, offvalue=0).grid(row=2, column=3)



    global toast_info_textUI
    toast_info_textUI = Text(window, width=50)
    toast_info_textUI.grid(row=4, column=0,columnspan=4)


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



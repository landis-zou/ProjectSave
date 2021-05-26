# create by landis at 2020.01.15
# !/usr/bin/python
# coding=utf-8

import xlrd
import PythonFile
import json
import os
import codecs
import ctypes
from tkinter import *
from tkinter.filedialog import (askopenfilename, askdirectory)


# -------------------------------- ExcelToJson Tool ---------------------------------------


def dealExcelData():
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


# dealExcelData()
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
    enter_path.set(askopenfilename())


def refreshencryptBtn(encrypt_btn, encrypt_btn_state):
    state = NORMAL if encrypt_btn_state.get() == 1 else DISABLED
    encrypt_btn['state'] = state


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

    toast_info_lab = Label(window,width=10,height=20)
    toast_info_lab.grid(row=3, column=0)


def onCreateWindow():
    my_ppid = 'company.product.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_ppid)
    window.title("Table Tool")
    window.iconbitmap(default=os.getcwd() + '/Resources/Icon/GetRight.ico')
    window.geometry()
    onGUI()
    window.mainloop()


# def showLogInfo(result):


window = Tk()

toast_info_lab = None

onCreateWindow()



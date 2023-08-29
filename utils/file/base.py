# 先定义名字,中文表对应导出英文名称
import os.path

from common import const
from openpyxl import load_workbook


def getMetaXlsxPath():
    return os.path.join(const.CFG_DIR_PATH, const.META_NAME)


def readMetaXlsx():
    wb = load_workbook(filename=getMetaXlsxPath())
    sheet = wb['Sheet1']

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) != 2:
            print("error:meta data row not equal 2", row)
            exit(-1)

        key = row[0]
        value = row[1]

        if key is None:
            continue

        if const.META_BASE_MAP.get(key):
            print(f"error:key:{key} is repeat")
            exit(-1)

        if value is None:
            print(f"error: key:{key},but value is none")
            exit(-1)

        const.META_BASE_MAP[key] = value

    wb.close()
    print(const.META_BASE_MAP)

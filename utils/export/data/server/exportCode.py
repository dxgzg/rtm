from common import const
from utils.export.data.server.code_template.go import *
from utils.file.base import getExportNameByFileNameExist
from utils.strconv import strconv


def exportGoCode(file_name):
    export_name = getExportNameByFileNameExist(file_name)
    tableName = strconv.initialUpper(export_name)
    fields = ""

    field_name_list = const.TABLE_DEFINE_MAP[file_name]
    for tableCfgObj in field_name_list:
        fieldName = tableCfgObj.field_english_name
        field = strconv.initialUpper(fieldName) + f''' `json:"{fieldName}"`'''
        fields += field + "\n"

    GO_TEMPLATE_CODE.replace(TABLE_NAME_REPLACE, tableName)
    GO_TEMPLATE_CODE.replace(TABLE_FIELDS_REPLACE, fields)

    print(fields)
    # print(GO_TEMPLATE_CODE)

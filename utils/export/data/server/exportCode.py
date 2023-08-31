import os

from common import const
from common.const import EXPORT_SERVER_CODE_PATH
from utils.export.data.server.code_template.go import *
from utils.file.base import getExportNameByFileNameExist, writeExportFile
from utils.strconv import strconv


def exportGoCode(file_name):
    fields = ""

    field_name_list = const.TABLE_DEFINE_MAP[file_name]
    for tableCfgObj in field_name_list:
        fieldName = tableCfgObj.field_english_name
        field = strconv.initialUpper(fieldName) + f''' `json:"{fieldName}"`'''
        fields += field + "\n"

    export_name = getExportNameByFileNameExist(file_name)
    tableName = strconv.initialUpper(export_name)
    tableManger = tableName+"Manager"
    tableMap = tableName+"Map"

    go_code_file = GO_TEMPLATE_CODE.replace(TABLE_NAME_REPLACE, tableName)
    go_code_file = go_code_file.replace(TABLE_FIELDS_REPLACE, fields)
    go_code_file = go_code_file.replace(TABLE_MANGER_REPLACE, tableManger)
    go_code_file = go_code_file.replace(TABLE_MAP_REPLACE, tableMap)
    # print(go_code_file)

    export_code_path = os.path.join(EXPORT_SERVER_CODE_PATH,export_name+".go")

    writeExportFile(export_code_path,go_code_file)



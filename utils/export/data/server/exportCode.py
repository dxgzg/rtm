import os

from common import const
from common.const import EXPORT_SERVER_CODE_PATH
from utils.export.data.server.code_template.go import *
from utils.export.data.server.code_template.go_helper import *
from utils.file.base import getExportNameByFileNameExist, writeExportFile, getTableManagerName, getTableMapName, \
    getTableDataName
from utils.strconv import strconv


def exportGoCode(file_name):
    fields = ""

    field_name_list = const.TABLE_DEFINE_MAP[file_name]
    for tableCfgObj in field_name_list:
        field_name = tableCfgObj.field_english_name
        field_type = tableCfgObj.field_type

        field = strconv.initialUpper(field_name) + f''' {field_type} `json:"{field_name}"`'''
        fields += field + "\n"

    export_name = getExportNameByFileNameExist(file_name)
    tableName = strconv.initialUpper(export_name)
    tableManager = getTableManagerName(tableName)
    tableMap = getTableMapName(tableName)

    go_code_file = GO_TEMPLATE_CODE.replace(TABLE_NAME_REPLACE, tableName)
    go_code_file = go_code_file.replace(TABLE_FIELDS_REPLACE, fields)
    go_code_file = go_code_file.replace(TABLE_MANGER_REPLACE, tableManager)
    go_code_file = go_code_file.replace(TABLE_MAP_REPLACE, tableMap)
    go_code_file = go_code_file.replace(FIELD_JSON_TAG_REPLACE, getTableDataName(export_name))
    # print(go_code_file)

    export_code_path = os.path.join(EXPORT_SERVER_CODE_PATH, export_name + ".go")

    writeExportFile(export_code_path, go_code_file)


def exportGoHelperCode():
    tableManagers = ""
    tableNewManagers = ""
    tableLoads = ""

    for file_name, export_name in const.META_BASE_MAP.items():
        tableName = strconv.initialUpper(export_name)
        tableManager = getTableManagerName(tableName)

        tableManagers += f"*{tableManager}\n"
        tableNewManagers = f"c.{tableManager}=New{tableManager}(c)\n"
        tableLoads = f'if err := c.Load{tableName}(path + "{export_name}.json");err!=nil{{return err}}'

    go_helper_code_file = HELPER_TEMP.replace(HELPER_VERSION_REPLACE, tableManagers)
    go_helper_code_file = go_helper_code_file.replace(HELPER_NEW_MANAGER_REPLACE, tableNewManagers)
    go_helper_code_file = go_helper_code_file.replace(HELPER_LOAD_REPLACE, tableLoads)

    # print(go_helper_code_file)
    export_code_path = os.path.join(EXPORT_SERVER_CODE_PATH, "Helper.go")
    writeExportFile(export_code_path, go_helper_code_file)

import json
import os

from common import const
from utils.export.data.server.exportCode import exportGoCode
from utils.file.base import getExportNameByFilePathExist
from utils.file.base import getExportNameByFileNameExist
from utils.file.base import writeExportFile
from utils.file.base import getTableDataName


def getServerDistDataPath():
    return const.EXPORT_SERVER_DATA_PATH


def procServerData(file_name, export_name):
    field_name_list = const.TABLE_DEFINE_MAP[file_name]
    field_value_list = const.TABLE_DATA_MAP[file_name]

    data_list = []
    for field_values in field_value_list:
        data_map = {}
        for i, field_value in enumerate(field_values):
            field_name_obj = field_name_list[i]

            field_type = field_name_obj.field_type
            if field_type == "string":
                field_value = str(field_value)
            data_map[field_name_obj.field_english_name] = field_value
        data_list.append(data_map)

    export_data = {getTableDataName(export_name): data_list}
    json_str = json.dumps(export_data, indent=4)
    data_path = os.path.join(getServerDistDataPath(), export_name + ".json")

    writeExportFile(data_path, json_str)


def exportServerData(file_name):
    export_file_name = getExportNameByFileNameExist(file_name)

    print("file name:", file_name, " english name:", export_file_name)

    procServerData(file_name, export_file_name)

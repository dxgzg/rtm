import json
import os

from common import const


def getServerDistDataPath():
    return const.EXPORT_SERVER_DATA_PATH


# export_name is table english name
def procServerData(file_name, export_name):
    field_name_list = const.TABLE_DEFINE_MAP[file_name]
    field_value_list = const.TABLE_DATA_MAP[file_name]
    if len(field_name_list) != len(field_value_list):
        print(f"error field_name_list length is not equals field_value_list fileName:{file_name}")
        exit(-1)

    data_list = []
    for i in range(len(field_name_list)):
        field_value = field_value_list[i]
        field_english_name_map = {}

        for j, field_name_obj in enumerate(field_name_list):
            field_english_name_map[field_name_obj.field_english_name] = field_value[j]
        data_list.append(field_english_name_map)

    export_data = {export_name + "Data": data_list}
    json_str = json.dumps(export_data, indent=4)
    data_path = os.path.join(getServerDistDataPath(), export_name + ".json")
    with open(data_path, "w") as json_file:
        json_file.write(json_str)


def exportServerData():
    for file_name_path in const.TABLE_DEFINE_MAP:
        chinese_file_name = os.path.basename(file_name_path).replace(".xlsx", "")

        export_file_name = const.META_BASE_MAP[chinese_file_name]
        if export_file_name is None or export_file_name == "":
            print(f"error file_name_path:{file_name_path} not exist meta data")
            exit(-1)

        print("chinese name:", chinese_file_name, " english name:", export_file_name)

        procServerData(file_name_path, export_file_name)

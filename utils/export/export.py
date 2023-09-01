from common import const
from common.language import *
from utils.export.data.server.exportCode import exportGoCode, exportGoHelperCode
from utils.export.data.server.exportData import exportServerData


def export(client_code_type=CSHARP_LANGUAGE, server_code_type=GO_LANGUAGE):
    for file_name in const.TABLE_DEFINE_MAP:
        exportServerData(file_name)
        exportServerCode(file_name, server_code_type)

    if server_code_type == GO_LANGUAGE:
        exportGoHelperCode()


def exportServerCode(file_name, server_code_type=GO_LANGUAGE):
    if server_code_type == GO_LANGUAGE:
        exportGoCode(file_name)

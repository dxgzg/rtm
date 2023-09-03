import os.path
import subprocess
# from sys import platform

from common import const
from common.language import *
from utils.export.data.server.exportCode import exportGoCode, exportGoHelperCode
from utils.export.data.server.exportData import exportServerData


def formatGoCode():
    #  todo linux开发
    # if platform.system() == 'Linux':

    # gofumptPath = linuxGofumptPath()
    #
    # subprocess.call([gofumptPath, "-l", "-w", define.go_out_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # else:
    gofumpt_path = os.path.join(const.THREE_RD_PATH, "gofumpt.exe")
    subprocess.run(f"{gofumpt_path} -l -w {const.EXPORT_SERVER_CODE_PATH}", stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


def formatCode(code_type):
    if code_type == GO_LANGUAGE:
        formatGoCode()


def export(client_code_type=CSHARP_LANGUAGE, server_code_type=GO_LANGUAGE):
    for file_name in const.TABLE_DEFINE_MAP:
        exportServerData(file_name)
        exportServerCode(file_name, server_code_type)

    # 导出helper代码
    if server_code_type == GO_LANGUAGE:
        exportGoHelperCode()
        formatCode(GO_LANGUAGE)


def exportServerCode(file_name, server_code_type=GO_LANGUAGE):
    if server_code_type == GO_LANGUAGE:
        exportGoCode(file_name)

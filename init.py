from common import const
from utils.file.base import readMetaXlsx, mkdir
from utils.file.cfgxlsx import readAllCfgData


def init():
    # 若没有，则新建导出文件夹
    mkdir(const.EXPORT_SERVER_DATA_PATH)
    mkdir(const.EXPORT_SERVER_CODE_PATH)

    # 读表资源
    readMetaXlsx()
    readAllCfgData()

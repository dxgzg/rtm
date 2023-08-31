from common import const
from utils.file.base import readMetaXlsx, mkdir
from utils.file.cfgxlsx import readAllCfgData


def init():
    mkdir(const.EXPORT_SERVER_DATA_PATH)
    mkdir(const.EXPORT_SERVER_CODE_PATH)

    readMetaXlsx()
    readAllCfgData()

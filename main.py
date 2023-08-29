# from utils.file.base import getBaseCfgPath
from utils.export.data.server.exportData import exportServerData
from utils.file.base import readMetaXlsx
from utils.file.cfgxlsx import readAllCfgData


def init():
    readMetaXlsx()
    readAllCfgData()
    exportServerData()


if __name__ == '__main__':
    init()


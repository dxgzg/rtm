from init import init
from utils.export.data.server.exportData import exportServerData


def proc():
    exportServerData()


if __name__ == '__main__':
    init()
    proc()

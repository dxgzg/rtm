from init import init
from utils.export.data.server.exportData import exportServerData
from utils.export.export import export


def process():
    export()


if __name__ == '__main__':
    init()
    process()

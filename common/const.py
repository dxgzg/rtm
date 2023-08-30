# 元数据路径与名字
CFG_DIR_PATH = "./test/cfgxls"
META_NAME = "meta.xlsx"

# 元数据存储
META_BASE_MAP = {}  # key:table chinese name,value:table english name

# 资源代码定义及资源
TABLE_DEFINE_MAP = {}  # 表格资源定义,名字、类型等定义,key: fileName,value:tableCfgObj
TABLE_DATA_MAP = {}  # key:fileName,value:每一行数据的数组

# 导出路径
EXPORT_SERVER_DATA_PATH = "./dist/server"

# golang 导出类型检查
EXPORT_GO_CODE_TYPE = {"str": "string", "string": "string",
                       "int": "int32", "int8": "int8", "int32": "int32", "int64": "int64",
                       "uint": "uint32", "uint32": "uint32", "uint64": "uint64"}

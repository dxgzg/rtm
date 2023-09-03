import chardet


def checkEncoding(data_path):
    # 检测文件编码方式
    with open(data_path, "rb") as f:
        encoding = chardet.detect(f.read())["encoding"]
        print(encoding)

#     checkEncoding("./dist/server/code/Helper.go")

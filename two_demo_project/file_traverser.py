import sys

from .utils.file_scanner import FileScanner
def main():
    if len(sys.argv) < 2:
        print("用法：python -m two_demo_project.file_traverser 文件夹路径")
        return
    target =  sys.argv[1]
    scanner =FileScanner(target)
    if not scanner.is_valid():
        print(f"错误：{target}不是有效文件")
        return
    files = scanner.scan("*.txt")
    print(f"共找到了{len(files)}个文件")
    for f in files:
        print(f.resolve())
if __name__ =="__main__":
    main()
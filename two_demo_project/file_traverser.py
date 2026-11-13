import sys
import json
from .utils.file_scanner import FileScanner
def main():
    if len(sys.argv) < 2:
        print("用法：python -m two_demo_project.file_traverser 文件夹路径 [文件类型]")
        print("示例：python -m two_demo_project.file_traverser two_demo_project *.py")        
        return
    target =  sys.argv[1]
    file_pattern = sys.argv[2] if len(sys.argv)>=3  else  "*"
    scanner =FileScanner(target)
    if not scanner.is_valid():
        print(f"错误：{target}不是有效文件夹")
        return
    files = scanner.scan(file_pattern)
    print(f"共找到了{len(files)}个文件")
    for f in files:
        print(f.resolve())
    result ={
        "scan_path":target,
        "file_count":len(files),
        "file_list":[str(f) for f in files]
    }
    with open("scan_result.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    

if __name__ =="__main__":
    main()
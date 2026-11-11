##### 2026.11.9 Day1

\#创建坏境 python -m venv venv

\#激活坏境 venv\\Scripts\\activate

\#安装环境 python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

\#运行项目 python 脚本名.py

##### 2026.11.10 Day2

VENV\_DEMO\\TWO\_DEMO\_PROJECT

│  main.py

│  \_\_init\_\_.py

│

├─utils

│  │  checker.py

│  │  cleaner.py

│  │  \_\_init\_\_.py

### 2026.11.11 Day3

新增two\_demo\_project\\utils\\textprocessor.py,封装TextProcessor。

支持最小校验长度，内置清洗文本，校验合法性两个实例方法。

运行方式：python -m two\_demo\_project.main


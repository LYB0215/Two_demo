# two_demo_project

Python 虚拟环境与包结构练习项目。

## 环境准备

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装依赖（清华镜像）
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

## 目录结构

```
venv_demo/
├── two_demo_project/       # 根包
│   ├── __init__.py
│   ├── main.py             # 入口脚本
│   └── utils/              # 子包
│       ├── __init__.py
│       ├── cleaner.py      # 文本清洗函数
│       └── checker.py      # 校验函数（使用相对导入）
├── venv/                   # 虚拟环境（不入库）
├── .gitignore
├── README.md
└── requirements.txt
```

## 运行方式

**正确：在项目根目录用模块方式启动**

```bash
python -m two_demo_project.main
```

输出：

```
测试用例1:校验结果 True
测试用例2:校验结果 False
测试用例3:校验结果 False
```

**错误：进入 utils 目录直接运行脚本**

```bash
python checker.py
```

会报错：

```
ImportError: attempted relative import with no known parent package
```

## Day2 相对导入练习

1. 相对导入（`from .xxx import`）只能在包内部使用，脚本必须作为模块启动，不能直接独立运行。
2. `-m` 参数后跟点号分隔的模块路径，例如 `two_demo_project.main`，不能写文件路径，也不能加 `.py` 后缀。
3. 包目录必须包含 `__init__.py`，Python 才会把它识别为包。

## 常见问题

- `__pycache__` 和 `.pyc` 是 Python 运行脚本时自动生成的字节码缓存，不需要手动维护，已通过 `.gitignore` 忽略。
- `venv/` 是本地虚拟环境，体积大且与机器绑定，不提交到仓库。
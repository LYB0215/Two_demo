from two_demo_project.utils.checker import is_valid

test_texts = [
    "这是一段长度足够的测试文本，用来校验功能是否正常",
    "短文本",
    ""
]

for idx,text in enumerate(test_texts,1):
    result = is_valid(text)
    print(f"测试用例{idx}:校验结果{result}")
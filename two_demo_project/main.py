from .utils.text_processor import TextProcessor

processor = TextProcessor(10)

test1 = "  这是一段很长的测试文本，用来验证长度是否达标，超过五十个字符就会返回真  \n"
test2 = "短文本"
test3 = ""

print("测试1长度:",len(processor.clean_text(test1)),"结果:", processor.is_valid(test1))  
print("测试2长度:",len(processor.clean_text(test2)),"结果:", processor.is_valid(test2))  
print("测试3长度:",len(processor.clean_text(test3)),"结果:", processor.is_valid(test3))  

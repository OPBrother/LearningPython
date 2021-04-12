"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
"""
import random


def generate_code(core_len=4):
    code_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_last = len(code_chars) - 1
    code = ''
    for _ in range(core_len):
        index = random.randint(0, chars_last)
        code += code_chars[index]
    return code


code = generate_code()
print(code)
def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

demo(gl_nums, gl_dict)      # 将元组和字典赋到元组里
demo(*gl_dict, **gl_dict)   # 分别将元组和字典传递到元组和字典


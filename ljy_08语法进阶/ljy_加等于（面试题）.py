def demo(num, num_list):
    print("函数开始")

    # +=本质上等于列表的extend方法 数据的引用不变
    num += num

    # 外部列表改变 本质上使用了extend方法
    # 如果使用 num_list = num_list + num_list 外部列表数据不变
    num_list += num_list
    print(num)
    print(num_list)

    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

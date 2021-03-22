def measure():
    print("测量开始...")
    temp = 30
    wetness = 50
    print("测量结束...")
#    return (temp,wetness) 返回一个元组
    return temp, wetness         # 可以不用括号
'''
reslut=measure()
print(reslut)
# 单独拿出 这种方法不方便
print(reslut[0])
print(reslut[1])
'''
# 可以使用多个变量，一次接受函数的返回结果
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)


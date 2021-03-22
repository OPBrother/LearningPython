

# x = yield 返回值


def dog(name):
    print('道哥%s准备吃东西拉' % name)
    while True:
        # x拿到的是yield接收到的值
        x = yield None
        print('道哥%s吃了 %s' % (name, x))


g = dog('alex')

# next(g)
# next(g)
# next(g)

g.send(None)        # 等于next(g)
g.send('一根骨头')

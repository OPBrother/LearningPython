import pandas as pd

#                                                   默认','
data = pd.read_csv('piaofang.csv', header=None, sep=',')     # 不能让第一行作为列名

# data中拿到 2，3列数据
data = data.loc[:, [2, 3]]


# 多类型电影分开
# 科幻/惊悚    5,389
# 科幻    5,389
# 惊悚    5,389

def func1(item):
    # 把每个类别处理
    return item.split('/')[0]

def func2(item):
    if "/" in item:
        return item.split('/')[1]
    else:
        return "e"
    # 把每个类别处理
    return item.split('/')[0]


data[4] = data[2].map(func1)
data[5] = data[2].map(func2)

# 把数据拆分
data_1 = data.loc[:, [4, 3]]
data_2 = data.loc[:, [5, 3]]
data_2 = data_2.loc[data_2[5] != 'e']

data_2 = data_2.rename(columns={5: 4})   # 把列名换过来
data = data_1.append(data_2)

# 计算每一种类型的平均值       保留俩位小数
data = data.groupby(4).mean().round(2)
print(data)

data.to_csv('票房需要用到的数据.csv')
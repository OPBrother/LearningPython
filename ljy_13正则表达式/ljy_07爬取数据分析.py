import pandas as pd
import matplotlib.pyplot as plt

# 引入数据                      处理表头        处理行索引
df = pd.read_csv("data.csv", header=None, index_col=0)


# 把红球号码拿出来
red_ball = df.loc[:, 1:6]

# 把蓝球号码拿出来
bule_ball = df.loc[:, 7]

# 作数据统计
# 统计每个号码出现的次数
red_ball_count = pd.value_counts(red_ball.values.flatten())
bule_ball_count = pd.value_counts(bule_ball.values)

# 可视化展示 -> 制作成图表
# fig, ax = plt.subplots(2, 1) # 一次创建很多个图表

# 饼状图展示
# ax[0].pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={"width": 0.3})
# ax[1].pie(bule_ball_count, labels=bule_ball_count.index, radius=0.5, wedgeprops={"width": 0.2})

# ax[0].pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={"width": 0.3})
# ax[0].pie(bule_ball_count, labels=bule_ball_count.index, radius=0.5, wedgeprops={"width": 0.2})

plt.pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={"width": 0.3})
plt.pie(bule_ball_count, labels=bule_ball_count.index, radius=0.5, wedgeprops={"width": 0.2})
plt.show()      # 图表展示


from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/index')
def index():
    # 读取csv文件中的内容，发送到页面
    data = pd.read_csv("票房需要用到的数据.csv")
    data = data.rename(columns={"4": "name", "3": "value"})
    data = data.to_dict(orient='record')             # 把数据变成列表里装着字典
    return render_template('show.html', data=data)


if __name__ == '__main__':
    app.run()

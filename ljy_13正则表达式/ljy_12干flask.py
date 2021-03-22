from flask import Flask, render_template, request

# 创建应用程序
app = Flask(__name__)

'''# 路由
@app.route('/')     # 当前访问 http://127.0.0.1:5000/
def index():          # 函数名随便
    return "你好我叫赛利亚！"       # 返回的数据->响应

@app.route('/jay')
def jay():
    return "周杰伦"'''

# @app.route('/index')
# def index():
#     s = '我叫周杰伦'
#     lst = ['狂战士', '狱血魔神', '帝血噬天', '生死战']
#
#     return render_template("hello.html", jay=s, lst=lst)        # 自动找到templas文件夹里面的hello.html

# 通过一个案例来学习如何从页面接受数据
# 登陆验证


@app.route('/index')
def index():
    return render_template('login.html')


@app.route('/login',methods=['POST'])
def login():
    # 接受到用户名和密码
    username = request.form.get("username")
    password = request.form.get("pwd")
    if username == 'linjunyu' and password == "123":
        return "成功"
    else:
        return render_template("login.html", msg= "登录失败")





if __name__ == '__main__':
    app.run()           # 启动应用程序
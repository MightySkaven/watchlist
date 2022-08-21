from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')  #一个视图函数可以绑定多个URL,通过附加多个装饰器来实现
@app.route('/index')
@app.route('/home')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/user/<name>')  #可以在URL中定义变量部分，下面的函数会处理所有/user/name的请求
def user_page(name):
    return 'User page'
@app.route('/user/<name>')  #可以返回用户名字，使用markupsafe避免恶意代码
def user_page_name(name):
    return f'User: {escape(name)}'
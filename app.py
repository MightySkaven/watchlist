from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

name = 'Yuanyi Liu'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')  #一个视图函数可以绑定多个URL,通过附加多个装饰器来实现
@app.route('/index')
@app.route('/home')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
def index():
    return render_template('index.html', name=name, movies=movies)
@app.route('/user/<name>')  #可以在URL中定义变量部分，下面的函数会处理所有/user/name的请求
def user_page(name):
    return 'User page'
@app.route('/user/<name>')  #可以返回用户名字，使用markupsafe避免恶意代码
def user_page_name(name):
    return f'User: {escape(name)}'


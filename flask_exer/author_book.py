#coding=utf-8

from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)

class Config():
    # SQLALCHEMY配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql://liguang:123456@127.0.0.1:3306/author_book'

    # 设置SQLALCHEMY自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "dadsfasfasfasfas"

app.config.from_object(Config)

db = SQLAlchemy(app)

#创建flask脚本管理对象
manager = Manager(app)
#创建数据库迁移对象
Migrate(app,db)

#向manager对象中添加数据库的操作命令
manager.add_command("db",MigrateCommand)


#定义数据库模型
class Author(db.Model):

    """作者"""
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")
    email = db.Column(db.String(64),unique=True)


class Book(db.Model):
    """数据"""
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))

#创建表单模型类
class AuthorBookForm(FlaskForm):
    '''作者数据表单模型类'''
    author_name = StringField(label="作者",validators=[DataRequired("作者必填")])
    book_name = StringField(label="书籍",validators=[DataRequired("书籍必填")])
    submit = SubmitField(label="保存")
@app.route("/",methods=["GET","POST"])
def index():

    #创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():

        #验证表单成功
        author_name = form.author_name.data
        book_name = form.book_name.data

        #保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        # book = Book(name=book_name,author_id=author.id)
        book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()


    #查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html",authors=author_li,form=form)

# @app.route("/delete_book",methods=["POST"])
# def delete_book():
#     '''删除数据'''
#     #提取参数
#     req_dict = request.get_json()
#     book_id = req_dict.get("book_id")
#
#     #删除数据
#     book = Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     # return redirect(url_for("index"))
#     # "Content-Type":"application/json"
#     return jsonify(code=0,message="ok")

#delete_book?book_id=xx
@app.route("/delete_book",methods=["GET"])
def delete_book():
    '''删除数据'''
    #提取参数
    book_id = request.args.get("book_id")

    #删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    # return redirect(url_for("index"))
    # "Content-Type":"application/json"
    return redirect(url_for("index"))




if __name__ == '__main__':

    # db.drop_all()
    # db.create_all()
    #
    # # 生成数据
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi,au_qian,au_san])
    # db.session.commit()
    #
    #
    # bk_xi = Book(name='吞噬星空',author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒',author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅',author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨',author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian,bk_san])
    # db.session.commit()
    # app.run(debug=True)

    #通过manager对象启动
    manager.run()

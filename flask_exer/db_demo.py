#coding=utf-8

from flask import Flask,render_template,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    #SQLALCHEMY配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql://liguang:123456@127.0.0.1:3306/liguang_flask'

    #设置SQLALCHEMY自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

#创建数据库sqlalchemy工具对象
db =  SQLAlchemy(app)


#创建数据库模型类
class User(db.Model):
    '''用户表'''
    #数据库命名规范
    #ihome = ih_user   数据库表名缩写_表名
    #tbl_user  tbl_表名
    __tablename__ = "tbl_users"
    id = db.Column(db.Integer,primary_key=True) #整型的主键，一般会默认设置为自增主键
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(128),unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        '''定义之后让显示的对象更直观'''
        return "User Object:name=%s" % self.name




class Role(db.Model):
    '''用户角色表'''
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)

    users = db.relationship("User",backref="role")

    def __repr__(self):
        '''定义之后让显示的对象更直观'''
        return "Role Object:name=%s" % self.name


if __name__ == '__main__':
    #清除数据库里的所有数据
    db.drop_all()
    #创建所有的表
    db.create_all()

    role1 = Role(name="admin")
    db.session.add(role1)
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()


    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()


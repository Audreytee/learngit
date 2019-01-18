"""
 Created by yan on 2018/8/30 14:53
 蓝图的相关初始化工作
"""
from flask import render_template

__author__ = 'yan'

from app.web.blueprint import web


# 必须首先导入执行以下，否则没有引入，会有循环导入


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

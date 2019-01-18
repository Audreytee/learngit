"""
蓝图不是拆分文件的，而是管理很多的文件逻辑
"""
import json

from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from app.web.blueprint import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm


# 非线程隔离，全局计数器
# @web.route('/test')
# def test1():
#     from app.libs.none_local import n
#     print(n.v)
#     n.v=2
#     print('...............')
#     print(getattr(request,'v',None))
#     setattr(request,'v',2)
#     # print(request.v)
#     print('................')
#     return ''


# q和page是参数
# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
# def search(q,page):
def search():
    """
    :param q: 关键字还是isbn
    :param page: 分页相关
    :return:
    """
    # Request:HTTP 请求相关信息，查询参数，POST参数，remote_ip
    # Response:
    # q ,page = request.args['q'],request.args['page']
    # q和page合法校验。q:至少有一个字符，长度限制，page ：正整数，一个最大值

    # 验证层，参数校验
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data  # 没有传递page，会获取到默认值1
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            # 第一次的亲密接触api:http://127.0.0.1:81/book/search/9787501524044/1
            # 第一次的亲密接触api:http://127.0.0.1:81/book/search?q=9787501524044&page=1
            # 如果没有导入，快捷导入：alt+enter

            yushu_book.search_by_isbn(q)
            # ret = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(ret,q)
        else:
            yushu_book.search_by_keyword(q, page)
            # ret = YuShuBook.search_by_keyword(q,page)
            # result = BookViewModel.package_collection(ret,q)
        books.fill(yushu_book, q)

        # 主要是这种返回的思路，带上响应头
        # return json.dumps(result,ensure_ascii=False),200,{'content-type':'application/json'}）
        # API：数据用json格式返回给客户端
        return json.dumps(books, default=lambda o: o.__dict__)  # 把不能序列化的类，转换为可以序列化的
        # return jsonify(books)
    return jsonify(form.errors)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 曲书记的详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)


@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)

# @web.route('/test1')
# def test1():
# print(id(current_app))
#     from flask import request
#     from app.libs.none_local import n
#     print(n.v)
#     n.v = 2
#     print('-----------------')
#     print(getattr(request, 'v', None))
#     setattr(request, 'v', 2)
#     print('-----------------')
#     return ''

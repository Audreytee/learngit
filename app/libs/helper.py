def is_isbn_or_key(word):
    """
    p判断输入的参数是isbn还事关键字
       检索的数据，不需要区分关键字和isbn搜索的区分
           q:普通+isbn
               isbn，不保留，13个0-9的数字组成
               isbn10 10个0-9 的数字组成，含有一些‘-’
           page
               start
               count
       :return:
       """
    isbn_or_key = 'key'
    if len(word) == 13 or word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    # 3个条件的结果会不会耗时，尽量把假的放钱，和耗时的放后边
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
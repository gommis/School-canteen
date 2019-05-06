from bottle import run, route, view, get, post, request
from itertools import count

class Comic:

    _ids = count (0)

    def __init__(self,comic_name, comic_num): 
        self.id = next(self._ids)
        self.comic_name = comic_name
        self.comic_num = comic_num


comics = [
    Comic("Sushi Roll", 3),
    Comic("Pie", 9),
    Comic("Soda", 13)
    ]

@route('/')
@view ('index')
def index():
    pass


@route('/card')
@view ('card')
def card():
    data = dict (book_info = comics)
    return data

@route('/buy_comic/<comic_id>')
@view ('buy_comic')
def buy_comic(comic_id):

    comic_id = int(comic_id)
    found_book = None
    for comic in comics:
        if comic.id == comic_id:
            found_book = comic
    data = dict (comic = found_book)
    found_book.comic_num = found_book.comic_num - 1
    return data




@route('/re_stock/<comic_id>')
@view ('re_stock')
def re_stock(comic_id):
    
    comic_id = int(comic_id)
    found_book = None
    for comic in comics:
        if comic.id == comic_id:
            found_book = comic
    data = dict (comic = found_book)
    found_book.comic_num = found_book.comic_num + 1
    return data



@route('/re_stock')
@view ('re_stock')
def index():
    pass


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)
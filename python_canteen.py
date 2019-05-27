from bottle import run, route, view, get, post, request
from itertools import count

class Food:

    _ids = count (0)

    def __init__(self,food_name, food_num, food_price): 
        self.id = next(self._ids)
        self.food_name = food_name
        self.food_num = food_num
        self.food_price = food_price


foods = [
    Food("Mini pizza", 3, "$3"),
    Food("Sushi roll", 9, "$4"),
    Food("Pie", 13, "$3.50")
    ]

@route('/')
@view ('index')
def index():
    pass


@route('/card')
@view ('card')
def card():
    data = dict (food_info = foods)
    return data

@route('/purchase_food/<food_id>')
@view ('purchase_food')
def buy_food(food_id):

    food_id = int(food_id)
    found_food = None
    for food in foods:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_num = found_food.food_num - 1
    return data


@route('/re_stock_food/<food_id>')
@view ('re_stock_food')
def re_stock_food(food_id):

    food_id = int(food_id)
    found_food = None
    for food in foods:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_num = found_food.food_num + 1
    return data


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)
from bottle import run, route, view, get, post, request
from itertools import count

class Food:

    _ids = count (0)
    #The list with all the different things that will be displayed on the cards e.g. food number and food price ect
    def __init__(self,food_name, food_num, food_price, food_sold): 
        self.id = next(self._ids)
        self.food_name = food_name
        self.food_num = food_num
        self.food_price = food_price
        self.food_sold = food_sold

#List of all the different foods, their price, their quantity and the number of items that have been sold.
foods = [
    Food("Mini pizza", 3, "$3", 0),
    Food("Sushi roll", 9, "$4", 0),
    Food("Pie", 13, "$3.50", 0)
    ] 
#The home page, card has a brief description of the website
@route('/')
@view ('index')
def index():
    pass

#The cards that displays the food, price, quantity and quantity sold.
@route('/card')
@view ('card')
def card():
    data = dict (food_info = foods)
    return data

# Purchase food success
@route('/purchase_food/<food_id>')
@view ('purchase_food')
def buy_food(food_id):
#For loop takes one of the total number of food items that are left
    food_id = int(food_id)
    found_food = None
    for food in foods:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_num = found_food.food_num - 1
    found_food.food_sold = found_food.food_sold + 1
    return data

#Restocking food succession code
@route('/re_stock_food/<food_id>')
@view ('re_stock_food')
def re_stock_food(food_id):
#For loop adds one more food item to the total count of the food items
    food_id = int(food_id)
    found_food = None
    for food in foods:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_num = found_food.food_num + 1
    return data


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)
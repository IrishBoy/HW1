import random


global name_list
name_list = ['Swikers',
             'Tmix',
             'Daunty',
             'Pars',
             'Krench Fries',
             'D&Ds',
             'Krinky way']
global banknotes
banknotes = dict.fromkeys([50, 100, 200, 500], 0)
global change
change = dict.fromkeys([10, 5, 2, 1], 400)
global cur_user_credit
cur_user_credit = int()
global products_am
products_am = {a: 15 for a in name_list}
global products_price
products_price = {a: random.randint(51, 100) for a in name_list}

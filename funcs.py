import glvar


def menu():
    print("Hello, i am vend machine, here u can see, what i have:\n")
    for prod in glvar.products_am:
        if glvar.products_am[prod]:
            print(f'{prod}, {glvar.products_price[prod]} Rubles\n')


def service(prod_am, coins):
    ser_flag_prod = 0
    ser_flag_coin = 0
    for am in prod_am:
        if prod_am[am]:
            ser_flag_prod += 1
    for coin in coins:
        if coins[coin]:
            ser_flag_coin += 1
    return(ser_flag_coin * ser_flag_prod)


def av_count_change(coins, summ):
    loc_user_credit = int(summ)
    cur_change = {}
    for coin in coins:
        cur_change_am = loc_user_credit // coin
        coin_now = coin
        if cur_change_am >= coins[coin]:
            cur_change_am = coins[coin]
            loc_user_credit -= coin * cur_change_am
            cur_change[coin_now] = cur_change.get(coin_now, cur_change_am)
        else:
            loc_user_credit -= coin * cur_change_am
            cur_change[coin_now] = cur_change.get(coin_now, cur_change_am)
    return(cur_change)


def count_dic(account):
    summ_now = 0
    for cash in account:
        summ_now += cash * account[cash]
    return(summ_now)


def count_change(credit, price, coins):
    change_for_now = credit - price
    cur_change = {}
    for coin in coins:
        coin_now = coin
        cur_change_am = change_for_now // coin
        if cur_change_am >= coins[coin]:
            cur_change_am = coins[coin]
            change_for_now -= coin * cur_change_am
            cur_change[coin_now] = cur_change.get(coin_now, cur_change_am)
        else:
            change_for_now -= coin * cur_change_am
            cur_change[coin_now] = cur_change.get(coin_now, cur_change_am)
    return(cur_change)


def check_change(credit, prices, am, change):
    flag_av_c = 0
    for price in prices:
        if am[price]:
            now_chahge = count_change(credit, prices[price], change)
            if count_dic(now_chahge) == credit - prices[price]:
                flag_av_c += 1
    return(flag_av_c)


def check_price(credit, prices):
    flag_av_p = 0
    for price in prices:
        if credit >= prices[price]:
            flag_av_p += 1
    return(flag_av_p)


def give_product(name):
    print(f"Here is ur{name}\n")
    return

from funcs import service
from funcs import av_count_change
from funcs import count_dic
from funcs import check_change
from funcs import check_price
from funcs import give_product
from funcs import menu
from menuadmfun import refill_machine
from menuadmfun import refill_change
from menuadmfun import machine_acc
from menuadmfun import res_machine_acc
import glvar


def adm_menu():
    choices_admin = {
        1: refill_machine,
        2: refill_change,
        3: machine_acc,
        4: res_machine_acc
    }
    while True:
        ans_adm = str(input("Hello u r in admin menu, now u can:\n"
                            "Set the remaining quantity of "
                            "all products to maximum(1)\n"
                            "Set the remaining amount of each"
                            "coin denomination to maximum(2)\n"
                            "Print the number of banknotes in"
                            "the cash accepting module(3)\n "
                            "and reset their counters(4)\n"
                            "Return back to main menu(5)\n"))
        if ans_adm == '5':
            break
        else:
            try:
                ans_adm = int(ans_adm)
                value = choices_admin[ans_adm]
                choice = choices_admin.get(int(ans_adm))
                choice()
            except ValueError:
                    print("I do no understand, waht u want, try one more time")
            except KeyError:
                    print("I do no understand, waht u want, try one more time")
    return
# done


def av_menu():
    print("That is what u can buy with the money u entred "
          "and change i have:\n")
    cur_av_prod = []
    for prod in glvar.products_am:
        change_prod = glvar.cur_user_credit - glvar.products_price[prod]
        if (glvar.products_am[prod] and
                glvar.cur_user_credit >= glvar.products_price[prod] and
                check_change(change_prod,
                             glvar.products_price,
                             glvar.products_am, glvar.change)):
            cur_av_prod.append(prod)
            print(f'{prod}, {glvar.products_price[prod]} Rubles\n')
    return(cur_av_prod)
# done


def ban_int():
    cur_op_credit = 0
    cur_op_banknotes = {a: 0 for a in glvar.banknotes}
    while True:
        cur_ban = str(input("Enter ur banknote(50,100,200,500),"
                            "if u wnat to end, type '0'\n"))
        if cur_ban.isdigit() and int(cur_ban) in glvar.banknotes:
            cur_op_banknotes[int(cur_ban)] += 1
            cur_op_credit += int(cur_ban)
            glvar.banknotes[int(cur_ban)] += 1
        elif cur_ban == '0':
            if (check_change(glvar.cur_user_credit + cur_op_credit,
                             glvar.products_price, glvar.products_am,
                             glvar.change) and
                    check_price(glvar.cur_user_credit + cur_op_credit,
                                glvar.products_price) and
                    av_count_change(glvar.change,
                                    glvar.cur_user_credit + cur_op_credit)):
                glvar.cur_user_credit += cur_op_credit
                break
            else:
                print("Sorry, i have no change or"
                      " u have entered a little money here is ur money\n")
                print(cur_op_credit)
                glvar.cur_user_credit -= cur_op_credit
                if glvar.cur_user_credit < 0:
                    glvar.cur_user_credit = 0
                cur_op_credit = 0
                for banknote in cur_op_banknotes:
                    glvar.banknotes[banknote] -= cur_op_banknotes[banknote]
                    cur_op_banknotes[banknote] = 0
                return
        else:
            print("Value is not supported, try another one")
# done


def prod_select():
    while True:
        print(f"U have {glvar.cur_user_credit} rubles")
        cur_av = av_menu()
        ans_select = str(input("What do u want?(Type the name)"
                               "or return to main menu(0)\n"))
        if ans_select in glvar.name_list and ans_select in cur_av:
            glvar.cur_user_credit -= glvar.products_price[ans_select]
            glvar.products_am[ans_select] -= 1
            give_product(ans_select)
        elif ans_select.isdigit() and int(ans_select) == 0:
            break
        else:
            print("I do not understand, what u want, try one more time")
    return
# done


def get_change():
    cur_change = av_count_change(glvar.change,
                                 glvar.cur_user_credit)
    print(f"Here is ur change:{count_dic(cur_change)}")
    for coin in cur_change:
        if cur_change[coin]:
            glvar.change[coin] -= cur_change[coin]
            print(f"{cur_change[coin] * coin} with {coin} rubles")
    glvar.cur_user_credit = 0
# done


while True:
    choices = {
        1: ban_int,
        2: menu,
        3: prod_select,
        4: get_change
    }
    flag = service(glvar.products_am, glvar.change)
    if not flag:
        ans_ser = str(input("Sorry, i need service operations\n"))
        if ans_ser == 'svrop17':
            adm_menu()
    else:
        print(f'Ur credit now:{glvar.cur_user_credit}')
        ans_wahl = str(input(("Do u want to insert a banknote(1)"
                              " see available products(2)"
                              " select a product(3)"
                              " or get the change(4)"
                              "(finish the session)?\n")))
        if ans_wahl == 'srvop17':
            adm_menu()
        else:
            try:
                ans_wahl = int(ans_wahl)
                value = choices[ans_wahl]
                choice = choices.get(int(ans_wahl))
                choice()
            except ValueError:
                print("I do not understand, waht u want, try one more time")
            except KeyError:
                print("I do not understand, waht u want, try one more time")

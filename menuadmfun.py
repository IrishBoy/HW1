import glvar


def refill_machine():
    for am in glvar.products_am:
        glvar.products_am[am] = 15
    print('\n')
    return


def refill_change():
    for coin in glvar.change:
        glvar.change[coin] = 400
    print('\n')
    return
# done


def machine_acc():
    for banknote in glvar.banknotes:
        print(f"{glvar.banknotes[banknote]} by {banknote}")
    print('\n')
    return
# done


def res_machine_acc():
    for banknote in glvar.banknotes:
        glvar.banknotes[banknote] = 0
    print('\n')
    return

def store_manager_set_cost(item_name, cost):
    if item_name in inventory:
        item_info = inventory[item_name]
        inventory[item_name] = [item_info[0], cost]
        return cost
    else:
        inventory[item_name] = [0, cost]
        return cost


def store_manager_add_item(item_name, item_qty):
    if item_qty <= 0:
        return -1
    if item_name in inventory:
        inventory[item_name][0] += item_qty
    else:
        return -1

    return item_qty


def store_manager_remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        return 1
    return -1


def store_manager_get_qty(item_name):
    if item_name in inventory:
        return inventory[item_name][0]
    return 0


def store_manager_increment_item(item_name, item_qty):
    return store_manager_add_item(item_name, item_qty)


def store_manager_decrement_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in inventory:
        current_qty = inventory[item_name][0]
        if item_qty >= current_qty:
            return -1

        inventory[item_name][0] -= item_qty
        return item_qty

    return -1


def shopper_add_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in cart:
        cart[item_name] += item_qty
    else:
        cart[item_name] = item_qty

    return item_qty


def shopper_remove_item(item_name):
    if item_name in cart:
        del cart[item_name]
        return 1

    return -1


def shopper_increment_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in cart:
        cart[item_name] += item_qty
        return item_qty

    return -1


def shopper_decrement_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in cart:
        current_qty = cart[item_name]

        if item_qty >= current_qty:
            del cart[item_name]
            return current_qty

        cart[item_name] -= item_qty
        return item_qty

    return -1


def shopper_get_order_amount():
    total_amount = 0

    for item_name, item_qty in cart.items():
        if item_name in inventory:
            cost = inventory[item_name][1]
            total_amount += cost * item_qty

    return round_amount(total_amount)


def round_amount(total_cost):
    return "{:.2f}".format(round(total_cost, 2))


def run_command(command):
    cmd = command.split()
    cmd_type = cmd[0]

    if cmd_type == 'CMD':
        role = cmd[1]
        cmd = cmd[2]

        if role == 'SM':
            if cmd == 'SET_COST':
                item_name = cmd[3]
                cost = float(cmd[4])
                return store_manager_set_cost(item_name, cost)
            elif cmd == 'ADD':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return store_manager_add_item(item_name, item_qty)
            elif cmd == 'REMOVE':
                item_name = cmd[3]
                return store_manager_remove_item(item_name)
            elif cmd == 'GET_QTY':
                item_name = cmd[3]
                return store_manager_get_qty(item_name)
            elif cmd == 'INCR':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return store_manager_increment_item(item_name, item_qty)
            elif cmd == 'DCR':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return store_manager_decrement_item(item_name, item_qty)

        elif role == 'S':
            if cmd == 'ADD':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return shopper_add_item(item_name, item_qty)
            elif cmd == 'REMOVE':
                item_name = cmd[3]
                return shopper_remove_item(item_name)
            elif cmd == 'INCR':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return shopper_increment_item(item_name, item_qty)
            elif cmd == 'DCR':
                item_name = cmd[3]
                item_qty = int(cmd[4])
                return shopper_decrement_item(item_name, item_qty)
            elif cmd == 'GET_ORDER_AMOUNT':
                return shopper_get_order_amount()

    return -1


def get_input():
    test_cases = int(input())
    for _ in range(test_cases):
        command = input()
        while command != 'END':
            print(run_command(command))
            command = input()


inventory = {}
cart = {}
get_input()


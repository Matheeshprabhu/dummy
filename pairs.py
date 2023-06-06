def sm_add_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in inventory:
        inventory[item_name] += item_qty
    else:
        inventory[item_name] = item_qty

    return item_qty


def sm_remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        return 1

    return -1


def sm_get_qty(item_name):
    if item_name in inventory:
        return inventory[item_name]

    return 0


def sm_increment_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in inventory:
        inventory[item_name] += item_qty
        return item_qty

    return -1


def sm_decrement_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in inventory:
        current_qty = inventory[item_name]

        if item_qty >= current_qty:
            del inventory[item_name]
            return current_qty

        inventory[item_name] -= item_qty
        return item_qty

    return -1


def sm_set_cost(item_name, cost):
    if item_name in inventory:
        item_info = inventory[item_name]
        inventory[item_name] = (item_info[0], cost)
        return cost
    else:
        inventory[item_name] = (0, cost)
        return cost


def s_add_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in cart:
        cart[item_name] += item_qty
    else:
        cart[item_name] = item_qty

    return item_qty


def s_remove_item(item_name):
    if item_name in cart:
        del cart[item_name]
        return 1

    return -1


def s_increment_item(item_name, item_qty):
    if item_qty <= 0:
        return -1

    if item_name in cart:
        cart[item_name] += item_qty
        return item_qty

    return -1


def s_decrement_item(item_name, item_qty):
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


def s_get_order_amount():
    total_amount = 0

    for item_name, item_qty in cart.items():
        if item_name in inventory:
            cost = inventory[item_name]['cost']
            total_amount += cost * item_qty

    return round_amount(total_amount)


def round_amount(amount):
    return round(amount, 2)


def process_command(command):
    cmd_parts = command.split()
    cmd_type = cmd_parts[0]

    if cmd_type == 'CMD':
        role = cmd_parts[1]
        cmd = cmd_parts[2]

        if role == 'SM':
            if cmd == 'ADD':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return sm_add_item(item_name, item_qty)
            elif cmd == 'REMOVE':
                item_name = cmd_parts[3]
                return sm_remove_item(item_name)
            elif cmd == 'GET_QTY':
                item_name = cmd_parts[3]
                return sm_get_qty(item_name)
            elif cmd == 'INCR':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return sm_increment_item(item_name, item_qty)
            elif cmd == 'DCR':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return sm_decrement_item(item_name, item_qty)
            elif cmd == 'SET_COST':
                item_name = cmd_parts[3]
                cost = float(cmd_parts[4])
                return sm_set_cost(item_name, cost)
        elif role == 'S':
            if cmd == 'ADD':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return s_add_item(item_name, item_qty)
            elif cmd == 'REMOVE':
                item_name = cmd_parts[3]
                return s_remove_item(item_name)
            elif cmd == 'INCR':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return s_increment_item(item_name, item_qty)
            elif cmd == 'DCR':
                item_name = cmd_parts[3]
                item_qty = int(cmd_parts[4])
                return s_decrement_item(item_name, item_qty)
            elif cmd == 'GET_ORDER_AMOUNT':
                return s_get_order_amount()

    return -1


# Main function to process the input
def process_input():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        command = input()
        while command != 'END':
            result = process_command(command)
            print(inventory)
            print(result)
            command = input()


# Run the program
inventory = {}
cart = {}
process_input()

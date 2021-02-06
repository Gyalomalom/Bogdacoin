# He bought? Pump eet


bogchain = []


def get_last_bog_value():
    """ Returns last blockchain value"""
    if len(bogchain) < 1:
        return None
    return bogchain[-1]


def pump_et(pump_amount, last_pump=[1]):
    if last_pump is None:
        last_pump = [1]
    bogchain.append([last_pump, pump_amount])


def get_pump_value():
    return float(input('Pump it by this amount: '))


def get_user_choice():
    return input('Your choice: ')


def print_bogchain_elements():
    for bog in bogchain:
        print('Outputting block')
        print(bog)


def verify_chain():
    bog_index = 0
    is_valid = True
    for bog in bogchain:
        if bog_index == 0:
            bog_index += 1
            continue
        elif bog[0] == bogchain[bog_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        bog_index += 1
    return is_valid


while True:
    print('What do you want:')
    print('1: Pump eet.')
    print('2: See the BOGchain.')
    print('3: Load the FUD. ')
    print('4: Quit bogchain.')
    user_choice = get_user_choice()
    if user_choice == '1':
        pp_amount = get_pump_value()
        pump_et(pp_amount, get_last_bog_value())
    elif user_choice == '2':
        print_bogchain_elements()
    elif user_choice == '3':
        if len(bogchain) >= 1:
            bogchain[0] = [2]
    elif user_choice == '4':
        break
    else:
        print('Input invalid, no pumps for you')
    if not verify_chain():
        print('Bogchain bogged!')
        break

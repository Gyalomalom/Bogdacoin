# He bought? Pump eet

genesis_block = {
        'previous_hash': 'IgorBogdanoff',
        'id': 0,
        'pumps': []
    }
bogchain = []
open_pumps = []
owner = 'Igor Bogdanoff'


def get_last_bog_value():
    """ Returns last blockchain value"""
    if len(bogchain) < 1:
        return None
    return bogchain[-1]


def pump_et(recipient, sender=owner, amount=1.0):

    # dictionary

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_pumps.append(transaction)


def mine_et():
    last_bog = bogchain[-1]
    block = {
        'previous_hash': 'XYZ',
        'id': len(bogchain),
        'pumps': open_pumps

    }
    bogchain.append(block)


def get_pump_value():
    tx_recipient = input('Recipient name: ')
    pump_amount = float(input('Pump it by this amount: '))
    # tuple
    return tx_recipient, pump_amount


def get_user_choice():
    return input('Your choice: ')


def print_bogchain_elements():
    for bog in bogchain:
        print('Outputting block')
        print(bog)
    else:
        print('-' * 20)


def verify_chain():
    is_valid = True
    for bog_index in range(len(bogchain)):
        if bog_index == 0:
            continue
        elif bogchain[bog_index][0] == bogchain[bog_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True


while waiting_for_input:
    print('What do you want:')
    print('1: Pump eet.')
    print('2: See the BOGchain.')
    print('3: Load the FUD. ')
    print('4: Quit bogchain.')
    user_choice = get_user_choice()
    if user_choice == '1':
        pp_data = get_pump_value()
        recipient, amount = pp_data
        pump_et(recipient, amount=amount)
        print(open_pumps)
    elif user_choice == '2':
        print_bogchain_elements()
    elif user_choice == '3':
        if len(bogchain) >= 1:
            bogchain[0] = [2]
    elif user_choice == '4':
        waiting_for_input = False
    else:
        print('Input invalid, no pumps for you')
    if not verify_chain():
        print('Bogchain bogged!')
        break


else:
    print('QUANTUM IMMORTALITY ACTIVATED')
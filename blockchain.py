# He bought? Pump eet

genesis_block = {
        'previous_hash': 'IgorBogdanoff',
        'id': 0,
        'pumps': []
    }
bogchain = [genesis_block]
open_pumps = []
owner = 'Igor Bogdanoff'
participants = {'Igor Bogdanoff'}


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
    participants.add(sender)
    participants.add(recipient)


def hash_bog(bog):
    return '-'.join([str(bog[key]) for key in bog])


def mine_et():
    last_bog = bogchain[-1]
    hashed_bog = hash_bog(last_bog)
    print(hashed_bog)
    bog = {
        'previous_hash': hashed_bog,
        'id': len(bogchain),
        'pumps': open_pumps

    }
    bogchain.append(bog)


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
    for (index, bog) in enumerate(bogchain):
        if index == 0:
            continue
        if bog['previous_hash'] != hash_bog(bogchain[index - 1]):
            return False
    return True


waiting_for_input = True


while waiting_for_input:
    print('What do you want:')
    print('1: Pump eet.')
    print('2: See the BOGchain.')
    print('3: Mine new bog.')
    print('4: See participants.')
    print('H: Hack eet. ')
    print('Q: Quit the Bogchain.')
    user_choice = get_user_choice()
    if user_choice == '1':
        pp_data = get_pump_value()
        recipient, amount = pp_data
        pump_et(recipient, amount=amount)
        print(open_pumps)
    elif user_choice == '2':
        print_bogchain_elements()
    elif user_choice == '3':
        mine_et()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'H':
        if len(bogchain) >= 1:
            bogchain[0] = {
                'previous_hash': 'IgorBogdanoff',
                'id': 0,
                'pumps': [{'sender': 'Mazo', 'recipient': 'Tomikesz', 'amount': '42069'}]
        }
    elif user_choice == 'Q':
        waiting_for_input = False
    else:
        print('Input invalid, no pumps for you')
    if not verify_chain():
        print('Bogchain bogged!')
        break


else:
    print('QUANTUM IMMORTALITY ACTIVATED')
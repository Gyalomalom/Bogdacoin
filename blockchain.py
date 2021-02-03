# He bought? Pump eet


bogchain = []


def get_last_bog_value():
    """ Returns last blockchain value"""
    return bogchain[-1]


def pump_et(pump_amount, last_pump=[1]):
    bogchain.append([last_pump, pump_amount])
    print(bogchain)


def get_pump_input():
    return float(input('Pump it by this amount: '))


pp_amount = float(input('Pump it by this amount: '))
pump_et(pp_amount)
pp_amount = float(input('Pump it by this amount: '))
pump_et(pp_amount, get_last_bog_value())
pp_amount = float(input('Pump it by this amount: '))
pump_et(pp_amount, get_last_bog_value())

print(bogchain)

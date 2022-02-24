house_price = 1000000
income = input('What is your income ? : $ ')
if int(income) > 100000 :
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f'Down payment : $ {down_payment}')
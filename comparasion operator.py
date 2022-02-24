name = input("what is your name ? : ")
if len(name) < 3 :
    print('Name must be 3 characters.')
    name = input("what is your name ? : ")
elif len(name) > 50 :
    print('Name must be max 50 characters.')
    name = input("what is your name ? : ")
else :
    print('Thats good, proceed further.')
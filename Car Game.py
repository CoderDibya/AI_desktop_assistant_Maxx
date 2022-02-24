command = ''
started = False
while True :
        command = input('> ').lower()
        if command == 'start':
            if started :
                print('Car is already on start.')
            else:
                started = True
                print('You are ready to go.')
        elif command=='stop':
            if not started:
                print('Car is already on stop.')
            else:
                started = False
                print('Your ride is over.')
        elif command== 'help':
            print('Start : to start the car. \nStop : to stop the car. \nQuit :to exit the game.')
        elif command== 'quit':
            break
        else:
            print("I don't understand your command")

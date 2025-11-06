print('Welcome to SMIT TechFest!')
print('Event organized by Marco Pollo Simuangco of APPDAET BTCS2')

num_participants = int(input('How many participants will register? '))
if num_participants <= 0:
    print('Invalid number of participants')
else:
    participants = []
    for i in range(num_participants):
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")
        participants.append({'name': name, 'track': track})

    print ('\nRegistered participants:')
    count = 1
    for participant in participants :
        print(f"\t{count}. {participant['name']} - {participant['track']}")
        count += 1
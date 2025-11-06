#TASK 1 - REGISTRATION SETUP
print('Welcome to SMIT TechFest!')
print('Event organized by Marco Pollo Simuangco of APPDAET BTCS2')

num_participants = int(input('How many participants will register? '))
if num_participants <= 0:
    print('Invalid number of participants')
else:
#TASK 2 - COLLECT PARTICIPANT INFORMATION
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
#TASK 3 - TRACK DIVERSITY REPORT
    unique_tracks = {participant['track'] for participant in participants}
    if len(unique_tracks) < 2:
        print('Not enough variety in tracks.')
    else:
        tracks_list = ", ".join(unique_tracks)
        print('\nTracks offered in this event:', tracks_list)
#TASK 4 - DUPLICATE NAME DETECTION
    found = set()
    dup = set()
    for participant in participants:
        if participant['name'] in found:
            dup.add(participant['name'])
        else:
            found.add(participant['name'])

    if dup:
        if len(dup) == 1:
            name = next(iter(dup))
            print(f'\nDuplicate name Found: {name}')
        else:
            print("\nDuplicate names Found:", ", ".join(dup))
    else:
        print('\nNo duplicate names.')
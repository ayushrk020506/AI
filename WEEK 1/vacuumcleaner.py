print("Ayush R Kallingal\n1WN24CS057")
room = {
    'A': input("Enter status of Room A (Clean/Dirty): "),
    'B': input("Enter status of Room B (Clean/Dirty): ")
}

position = input("Enter vacuum position (A/B): ")

while room['A'] == 'Dirty' or room['B'] == 'Dirty':

    print("\nVacuum is in Room", position)

    if room[position] == 'Dirty':
        print("Room is Dirty")
        print("Sucking dirt...")
        room[position] = 'Clean'

    else:
        print("Room is Clean")

        if position == 'A':
            print("Moving Right")
            position = 'B'
        else:
            print("Moving Left")
            position = 'A'

print("\nBoth rooms are clean!")
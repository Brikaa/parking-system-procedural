import parking

def show_vehicles():
    for vehicle in parking.vehicles:
        print('ID: ' + vehicle['id'])
        print('Model name: ' + vehicle['model_name'])
        print('Model year: ' + vehicle['model_year'])
        print('Arrival date: ' + vehicle['arrival_date'].strftime('%d/%m/%y at %H:%M:%S'))
        print()

def handle_park_in():
    if parking.is_full():
        print("Full parking, can't park in")
        return
    model_name = input('Model name: ')
    model_year = input('Model year: ')
    parking.park_in_vehicle(model_name, model_year)

def handle_park_out():
    vehicle_id = input('Vehicle ID to park out: ')
    fees = parking.park_out_vehicle(vehicle_id)
    if fees == -1:
        print('The specified vehicle was not found')
        return
    print(f'Parked out the vehicle, with fees {fees}')
    if fees == 0:
        print('The vehicle received free parking because it stayed for less than an hour')

if __name__ == '__main__':
    no_slots_str = input('Enter the number of slots: ')
    while not no_slots_str.isnumeric():
        no_slots_str = input('Please provide an integer number of slots: ')
    no_slots = int(no_slots_str)
    parking.initialize_available_slots(no_slots)

    while True:
        choice_str = input('''
1. Park in vehicle
2. Park out vehicle
3. Show available slots
4. Show vehicles
5. Show statistics
6. Exit
\n''')
        while not choice_str.isnumeric():
            choice_str = input('Please enter a valid choice: ')

        choice = int(choice_str)
        if choice == 1:
            handle_park_in()
        elif choice == 2:
            handle_park_out()
        elif choice == 3:
            print(', '.join(map(str, parking.available_slots)))
        elif choice == 4:
            show_vehicles()
        elif choice == 5:
            print(f'Total number of vehicle: {parking.total_no_vehicles}\nTotal Income: {parking.total_income}')
        elif choice == 6:
            break
        else:
            print('Invalid choice')

from datetime import datetime

HOURLY_FEE = 5

vehicles = []
available_slots = []
total_slots = 0
total_no_vehicles = 0
total_income = 0

def initialize_available_slots(no_available_slots):
    global total_slots
    for i in range(no_available_slots, 0, -1):
        available_slots.append(i)
    total_slots = no_available_slots

def find_vehicle_by_id(vehicle_id):
    for index, vehicle in enumerate(vehicles):
        if vehicle['id'] == vehicle_id:
            return index
    return -1

def is_full():
    return len(vehicles) == total_slots

def park_in_vehicle(model_name, model_year, park_in_date):
    global total_no_vehicles
    slot_number = available_slots.pop()
    vehicles.append({
        'id': str(slot_number),
        'slot_number': slot_number,
        'model_name': model_name,
        'model_year': model_year,
        'arrival_date': park_in_date
    })
    total_no_vehicles += 1

def park_out_vehicle(vehicle_id, park_out_date):
    global total_income
    vehicle_index = find_vehicle_by_id(vehicle_id)
    if vehicle_index == -1:
        return -1
    vehicle = vehicles[vehicle_index]
    if vehicle['arrival_date'] > park_out_date:
        raise Exception('The park-out date cannot be before the park-in date')
    available_slots.append(vehicle['slot_number'])
    time_delta = park_out_date - vehicle['arrival_date']
    time_delta_hours = int(time_delta.total_seconds() / (60 * 60))
    fees = time_delta_hours * HOURLY_FEE
    total_income += fees
    return fees

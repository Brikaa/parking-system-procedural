from datetime import datetime

HOURLY_FEE = 5

vehicles = []
available_slots = []
total_slots = 0
total_no_vehicles = 0
total_income = []

def initialize_available_slots(no_available_slots):
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

def park_in_vehicle(model_name, model_year):
    slot_number = available_slots.pop()
    vehicles.append({
        'id': str(slot_number),
        'slot_number': slot_number,
        'model_name': model_name,
        'model_year': model_year,
        'arrival_date': datetime.now()
    })
    total_no_vehicles += 1

def park_out_vehicle(vehicle_id):
    vehicle_index = find_vehicle_by_id(vehicle_id)
    if vehicle_index == -1:
        return -1
    vehicle = vehicles.pop(vehicle_index)
    available_slots.push(vehicle['slot_number'])
    time_delta = datetime.now() - vehicle['arrival_date']
    time_delta_hours = int(time_delta.seconds / (60 * 60))
    return time_delta_hours * HOURLY_FEE

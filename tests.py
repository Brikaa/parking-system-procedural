from datetime import datetime
import parking

if __name__ == '__main__':
    parking.initialize_available_slots(5)
    parking.park_in_vehicle('Nissan', '2020', datetime(2022, 1, 1, 1, 1))
    parking.park_in_vehicle('Sentra', '2021', datetime(2022, 1, 1, 2, 2))
    parking.park_in_vehicle('Hammer', '2025', datetime(2022, 1, 1, 3, 3))
    assert parking.park_out_vehicle('1', datetime(2022, 1, 1, 2, 1)) == parking.HOURLY_FEE
    assert parking.park_out_vehicle('2', datetime(2022, 1, 1, 3, 2)) == parking.HOURLY_FEE
    assert parking.park_out_vehicle('3', datetime(2022, 1, 2, 3, 3)) == parking.HOURLY_FEE * 24
    print('All tests passed successfully')

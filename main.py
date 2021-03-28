import time
from collections import OrderedDict

from src.parking_lot import ParkingLot
from src.vehicle import Vehicle


def main():

    rate_card = {
        '2 wheeler': OrderedDict({
            0: 20,
            1: 50,
            3: 80,
        }),
        '4 wheeler': OrderedDict({
            0: 30,
            1: 70,
            3: 100,
        })
    }
"""
    Slot: 0 -1 hours
    Slot: 1 - 2 days
        '2 wheeler': [
        ]

class TimeSlotInterface:
    @abstractmethod
    def calculate_amount(duration) -> int

class Daily(TimeSlotInterface):
    price:
        
    
    for rate_card:
        attrs = (time_unit, price, start, end, type)
        timeSlotInteface = Factory(type)
        amount = timeSlotInteface.calculate()
    
"""


    capacity = {
        '2 wheeler': 5,
        '4 wheeler': 2
    }

    parking_lot = ParkingLot(rate_card=rate_card, capacity=capacity)

    vehicle1 = Vehicle('ABC1234', '2 wheeler')
    parking_lot.enter_vehicle(vehicle1)
    time.sleep(5)
    print(parking_lot.exit_vehicle(vehicle1))
    print(parking_lot.parking_history(vehicle1))
    
    vehicle2 = Vehicle('XYZ1234', '4 wheeler')
    parking_lot.enter_vehicle(vehicle2)
    time.sleep(3)
    print(parking_lot.exit_vehicle(vehicle2))
    parking_lot.enter_vehicle(vehicle2)
    time.sleep(3)
    print(parking_lot.exit_vehicle(vehicle2))
    print(parking_lot.parking_history(vehicle2))

    vehicle2 = Vehicle('XYZ1235', '4 wheeler')
    parking_lot.enter_vehicle(vehicle2)
    vehicle2 = Vehicle('XYZ1235', '4 wheeler')
    parking_lot.enter_vehicle(vehicle2)
    print(parking_lot.parking_history(vehicle2))


if __name__ == '__main__':
    main()

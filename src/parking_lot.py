from datetime import datetime
from typing import Dict, List

from src.exceptions import ParkingLotFullException, VehicleTypeNotSupportedException, ParkingRecordNotFound
from src.parking_record import ParkingRecord
from src.vehicle import Vehicle


class Spot(object):
    pass


class Parking(object):

    parking_records: Dict[Vehicle, List[ParkingRecord]]

    """
    {
        vehicle: [
        ]
    }
    """

    def __init__(self):
        self.parking_records = {}

    def exit(self, vehicle: Vehicle, exit_time: datetime):

        if vehicle not in self.parking_records:
            raise ParkingRecordNotFound

        record = self.parking_records.get(vehicle)[-1]

        record.exit_time = exit_time

        return record.duration()

    def create(self, vehicle: Vehicle):
        record = ParkingRecord(vehicle, datetime.now())

        if vehicle not in self.parking_records:
            self.parking_records[vehicle] = []

        self.parking_records[vehicle].append(record)

    def get_records(self, vehicle: Vehicle):
        return self.parking_records.get(vehicle, [])


class ParkingLot:

    capacity: dict

    rate_card: dict

    vehicle_count: Dict[str, int]

    parking: Parking

    def __init__(self, rate_card: dict, capacity: dict):
        self.rate_card = rate_card
        self.capacity = capacity
        self.parking = Parking()
        self.vehicle_count = {}
        self.parking = Parking()

    def enter_vehicle(self, vehicle: Vehicle):

        if self.is_full(vehicle.type):
            raise ParkingLotFullException

        self.parking.create(vehicle)

        if vehicle.type not in self.vehicle_count:
            self.vehicle_count[vehicle.type] = 0
        self.vehicle_count[vehicle.type] += 1

    def exit_vehicle(self, vehicle: Vehicle):
        self.vehicle_count[vehicle.type] -= 1
        duration = self.parking.exit(vehicle, datetime.now())
        return self._calculate_amount(duration, vehicle.type)

    def parking_history(self, vehicle: Vehicle):
        return self.parking.get_records(vehicle)

    def is_full(self, vehicle_type):
        if vehicle_type not in self.capacity.keys():
            raise VehicleTypeNotSupportedException

        return self.capacity[vehicle_type] == self.get_count(vehicle_type)

    def get_count(self, vehicle_type):
        if vehicle_type not in self.vehicle_count:
            return 0

        return self.vehicle_count.get(vehicle_type)

    def _calculate_amount(self, duration, vehicle_type):
        total_time = duration.total_seconds()
        amount = 0
        for key in self.rate_card[vehicle_type].keys():
            if total_time < key:
                break
            amount += self.rate_card[vehicle_type][key]
            total_time -= key

        return amount


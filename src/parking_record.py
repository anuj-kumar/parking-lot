from datetime import datetime
from typing import Optional

from src.vehicle import Vehicle


class ParkingRecord:

    vehicle: Vehicle

    entry_time: datetime

    exit_time: datetime

    def __init__(self, vehicle: Vehicle, entry_time: datetime, exit_time: Optional[datetime] = None):
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.exit_time = exit_time

    def duration(self):
        return self.exit_time - self.entry_time

    def __repr__(self):
        return "{} {} {}".format(self.vehicle.number, self.entry_time, self.exit_time)

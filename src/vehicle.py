from dataclasses import dataclass


@dataclass
class Vehicle:

    number: str

    type: str

    def __hash__(self):
        return hash(self.number)

# Hostel Visiting Recording System

class Resident:
    def _init_(self, name, room):
        self.name = name
        self.room = room

    def _str_(self):
        return f"Resident: {self.name}, Room: {self.room}"
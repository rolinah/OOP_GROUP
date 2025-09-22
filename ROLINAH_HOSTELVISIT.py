# Hostel Visiting Recording System

class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"Resident: {self.name}, Room: {self.room}"


class Visitor:
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id

    def __str__(self):
        return f"Visitor: {self.name} (ID: {self.visitor_id})"


class Hostel:
    def __init__(self, hostel_name):
        self.hostel_name = hostel_name
        self.visits = []  # List to store visit records

    def record_visit(self, visitor, resident):
        """Record a visit made by a visitor to a resident."""
        visit_record = {
            'visitor_name': visitor.name,
            'visitor_id': visitor.visitor_id,
            'resident_name': resident.name,
            'resident_room': resident.room
        }
        self.visits.append(visit_record)
        print(f"Visit recorded: {visitor.name} visited {resident.name} (Room {resident.room})")

    def show_visits(self):
        """Display all visit records."""
        print(f"\nHostel: {self.hostel_name} - Total Visits: {len(self.visits)}")
        print("=" * 50)
        for i, visit in enumerate(self.visits, start=1):
            print(f"{i}. Visitor: {visit['visitor_name']} (ID: {visit['visitor_id']}) "
                  f"→ Resident: {visit['resident_name']} (Room {visit['resident_room']})")


# ---- Example Usage ----

# Create residents
resident1 = Resident("Rolinah Asiimwe", "B12")
resident2 = Resident("Hearty Mangeni", "C03")
resident3 = Resident("Bazanye David", "D05")


# Create visitors
visitor1 = Visitor("Kavuma Henry", "V101")
visitor2 = Visitor("Kukundakwe Godrinar", "V102")
visitor3 = Visitor("Tamale Davis", "V103")
# Create a hostel
my_hostel = Hostel("St.Matthews Hostel")

# Record visits
my_hostel.record_visit(visitor1, resident1)
my_hostel.record_visit(visitor2, resident2)
my_hostel.record_visit(visitor3, resident3)


# Show visit records
my_hostel.show_visits()

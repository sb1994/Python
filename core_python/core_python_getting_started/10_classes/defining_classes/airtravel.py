from pprint import pprint as pp

"""Model For aircraft flights"""


class Flight:
    """A flight with a particular passanger aircraft"""

    # pass  # pass is a statment

    # create the initialization method

    # use underscore to avoid clash
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code is '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invaild airline code is '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invaild route number '{number}'")
        self._number = number
        # inherit the object
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    # Instance methods
    def number(self):
        return self._number

    def airline(self):
        # returns the first 2 chars
        return self._number[:2]


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def num_rows(self):
        return self._num_rows

    def num_seats_per_row(self):
        return self._num_seats_per_row

    def seating_plan(self):
        return (
            range(1, self._num_seats_per_row + 1),
            "ABCDEFGHJK"[: self._num_seats_per_row],
        )


"""Main Program"""
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
#! Not recommended to access the property directly i.e f._name
# print(f.number())


# can access the aircraft data through the flight object
# print(f.aircraft_model())


pp(f._seating)
# check the validation
# f1 = Flight("060")

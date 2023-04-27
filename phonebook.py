
class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name1, phone_number1 in self.numbers.items():
            for name2, phone_number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if phone_number1.startswith(phone_number2):
                    return False
        return True

    def get_names(self):
        return True

    def get_phone_number(self):
        return True

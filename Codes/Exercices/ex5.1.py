"""
This code is desire to create a base classe "Telephone" and derive a class
"ElectronicPhone" from it. In Telephone, create a string member "phonetype", and 
"""
class Telephone:
    def __init__(self, number, phonetype):
        self.number = number
        self.phonetype = phonetype

    def ring(self):
        print("Ringing the {0}".format(self.phonetype))

class ElectronicPhone(Telephone):
    def __init__(self, number):
        super().__init__(number, 'digital')


phone = ElectronicPhone('123-456-7890')
phone.ring()

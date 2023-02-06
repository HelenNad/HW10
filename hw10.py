from collections import UserDict

class Field:
    def __init__(self):
        return self.value 
       
class Name:
    def __init__(self, name):
        self.value = name
    

class Phone:
    value = []
    def phone (self, phone):
        Phone.value.append(phone)
    

class Record (Name, Phone):

    def __init__(self,name, phone):
        self.name = name
        self.phones = phone

    def name(self):
        return Name.value

    def phone(self):
        return Phone.value

    def add_phone (self,phone):
        self.phones.append(phone) 

        
    def chenge_phone (self, phone, ph):
        if phone in self.phones:
            ind = self.phones.index(phone)
            self.phones[ind] = ph
    
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value] = record
        return self.data


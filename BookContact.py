# Classes
from Contact import Contact
import csv

class BookContact:

    def __init__(self):
        self._contacts = {}
        self._count = 0
        self._getData() 

    def addContact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts[self._count] = (contact)
        self._count += 1
        self._saveData()
        print("The number {} has been successfully add".format(phone))

    def updateContact(self, search, name, phone, email):
        count = int(search) - 1
        self._contacts[count] = Contact(name, phone, email)
        self._saveData()
        print("The id {} has been successfully update".format(search))

    def listAllContacts(self):
        if len(self._contacts) > 0:
            response = ["Contact List:\n"]
            response += ["{} => [{}]\n".format((key + 1), value.formatContact())
                        for key, value in self._contacts.items()]
            print(''.join(response))
        else:
            print("The Contact list is EMPTY")

    def searchElement(self, element):
        response = self._search(element)
        if response:
            print(response.formatContact())
            return True
        else:
            response = "No exist Data with the search {}".format(element)
            print(response)
            return response

    def _search(self, element):
        for key, value in self._contacts.items():
            if ((str(key + 1) == element) or (value.getName() == element or value.getPhone() == element or value.getEmail() == element)):
                return (value)

    def deleteElement(self, element):
        response = self._search(element)
        if response:
            self._delete(response)
            self._saveData()
            print("Element delete")
        else:
            print("No exist Data with the search {}".format(element))

    def _delete(self, element):
        for key, value in self._contacts.items():
            if (value == element):
                self._contacts = self._removekey(key)
                

    def _removekey(self, key):
        tempData = dict(self._contacts)
        del tempData[key]
        return tempData
    
    def _saveData(self):
        with open("contacts.csv", 'w+') as file:
            writer = csv.writer(file)
            writer.writerow(('name', 'phone', 'email'))
            for key, contact in self._contacts.items():
                writer.writerow((contact.getName(), contact.getPhone(), contact.getEmail()))

    def _getData(self):
        with open("contacts.csv", 'r') as file:
            reader = csv.reader(file)
            print(reader)
            for key, value in enumerate(reader):
                if key == 0:
                    continue
                self.addContact(value[0], value[1], value[2])
                

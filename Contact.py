class Contact:
    
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email
    
    def formatContact(self):
        return "Name: {} | Phone: {} | Email: {}".format(self._name, self._phone, self._email)

    def getName(self):
        return self._name
    
    def getPhone(self):
        return self._phone
    
    def getEmail(self):
        return self._email
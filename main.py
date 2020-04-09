# -*- codign: utf-8 -*-

from BookContact import BookContact

bookContact = BookContact()

def run():
    while True:
        option = int(input(printMenu()))
        switch(option)

def printMenu():
    optionsMenu = [
        'Add Contact',
        'Update Contact',
        'Search Contact',
        'Delete Contact',
        'List Contact',
        'Exit'
    ]
    
    print("██████╗  ██████╗  ██████╗ ██╗  ██╗     ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗████████╗")
    print("██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝")
    print("██████╔╝██║   ██║██║   ██║█████╔╝     ██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║        ██║   ")
    print("██╔══██╗██║   ██║██║   ██║██╔═██╗     ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║        ██║   ")
    print("██████╔╝╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╗   ██║   ")
    print("╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ")
    content = ["\n\tWelcome at your BookContact\n\n\tSelect an option:\n\n"]
    content += ["\t\t{}. {}\n".format(num + 1, optionsMenu[num]) for num in range(0, len(optionsMenu))]
    return ''.join(content)

def switch(option):
    return {
        1: addContact,
        2: updateContact,
        3: searchContact,
        4: deleteContact,
        5: listContact,
        6: exitSoftware
    }[option]()


def addContact():
    name = str(input("Write a name for the phone number:\n"))
    number = str(input("Write a phone number:\n"))
    email = str(input("Write an email:\n"))
    bookContact.addContact(name, number,email)

def updateContact():
    search = str(input("Get a value to search:\n"))
    response = bookContact.searchElement(search)
    if response is True:
        name = str(input("Write a name for the phone number:\n"))
        number = str(input("Write a phone number:\n"))
        email = str(input("Write an email:\n"))
        bookContact.updateContact(search, name, number,email)
    else:
        print(response)

def searchContact():
    search = str(input("Get a value to search:\n"))
    bookContact.searchElement(search)

def deleteContact():
    search = str(input("Get a ID to search:\n"))
    bookContact.deleteElement(search)

def listContact():
    bookContact.listAllContacts()

def exitSoftware():
    exit()

if __name__ == "__main__":
    run()
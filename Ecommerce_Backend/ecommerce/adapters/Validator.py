import re 
regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regexContact = '[6-9][0-9]{9}'

class Validator:
    @staticmethod
    def validateEmail(email):
        return re.search(regexEmail,email)

    @staticmethod
    def validateContact(contact):
        return re.search(regexContact,contact)
    
    @staticmethod
    def validateName(name):
        return True if name else False

    @staticmethod
    def validateNumber(number):
        return isinstance(number, int) and number >= 0 




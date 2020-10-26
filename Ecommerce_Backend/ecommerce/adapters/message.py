class MessageAdapter:
    
    @staticmethod
    def sendMessage(contact,msg):
        print(contact + " : " +msg)
        return (contact + " : " +msg)
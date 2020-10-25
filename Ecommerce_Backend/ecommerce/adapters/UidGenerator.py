class UidGenerator:
   __instance = None
    
   @staticmethod 
   def getInstance():
      if UidGenerator.__instance == None:
         UidGenerator()
      return UidGenerator.__instance

   def __init__(self):
      self.__counter=0
      if UidGenerator.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         UidGenerator.__instance = self

   def generate(self):
       self.__counter+=1
       return self.__counter

   def validate(self,id):
        return self.__counter>=id   

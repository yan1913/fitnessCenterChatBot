# Accessing the attribute set in the parent class
class ballgames:
    def __init__(self,name,avail,price):
         self.name= name
         self.avail= avail
         self.price= price
        
    def sport(self):
        return "{}{}{}".format(self.name,self.avail,self.price)
    
class indoor(ballgames):
    pass

ballgames_1=indoor("basketball","weekdays",20)
ballgames_2=indoor("volleyball","weekends",15)

print (ballgames_1.avail)
print (ballgames_2.avail)
    
    
    
    


# USING THE INIT METHOD

class ballgames:
    def __init__(self,name,avail,price):
        self.name= name
        self.avail= avail
        self.price= price
        
    def sport(self):
        return "{}{}{}".format(self.name,self.avail,self.price)
    
ballgames_1=ballgames("basketball","weekdays",20)
ballgames_2=ballgames("volleyball","weekends",15)
    
print (ballgames_1.avail)
print (ballgames_2.avail)
    
    
    
    
print (ballgames_1.sport())
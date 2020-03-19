# Passing in an extra attribute and another sub-class
# attribute expected calories to be burnt(exp-cal) and sub-class indoor
class ballgames:
    def __init__(self,name,avail,price):
        self.name= name
        self.avail= avail
        self.price= price
        
    def sport(self):
        return "{}{}{}".format(self.name,self.avail,self.price)
    
 
# ballgames_1=indoor("basketball","weekdays",20,2000)
# ballgames_2=indoor("volleyball","weekends",15,1800)

class indoor(ballgames):
    def __init__(self,name,avail,price,exp_cal):
        super().__init__(name,avail,price)
        self.exp_cal=exp_cal
ballgames_1=indoor("Basketball","weekdays",20,2000)  
ballgames_2=indoor("volleyball","weekends",15,1800)
        
    
    
    
    
print (ballgames_1.avail)
print (ballgames_2.exp_cal)
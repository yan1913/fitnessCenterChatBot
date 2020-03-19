#  sub-class instructor was added and i can print any of the attributes of instructor
#     I can also print a list of ballgames and add ballgames to the available ones
class ballgames:
    def __init__(self,name,avail,price):
         self.name= name
         self.avail= avail
         self.price= price
        
    def sport(self):
         return "{}{}{}".format(self.name,self.avail,self.price)
class indoor(ballgames):
    
    
    def __init__(self,name,avail,price,exp_cal):
        super().__init__(name,avail,price)
        self.exp_cal=exp_cal
ballgames_1=indoor("Basketball","weekdays","20",2000)  
ballgames_2=indoor("volleyball","weekends",15,1800)
        

 

        
class instructor(ballgames):
    
    
    def __init__(self,name,avail,price,ballgames=None):
        super().__init__(name,avail,price)
        if ballgames is None:
            self.ballgames=[]
        else:
            self.ballgames=ballgames
        
    def add_ball(self,ball):
        if ball not in self.ballgames:
            self.ballgames.append(ball)
                
    def remove_ball(self,ball):
        if ball in self.ballgames:
            self.ballgames.append(ball)
                
#     def remove_ball (self,ball):
#         if ball in self.ballgames:
#             self.ballgames.remove(ball)
        
    def print_balls(self):
        for ball in self.ballgames:
#             print(ball.nameprice())
                
            ballgames_1=indoor("basketball","weekdays",20,2000)
            ballgames_2=indoor("volleyball","weekends",15,1800)
    
    
        
instr_1=instructor("sonde", "weekdays", 50, [ballgames_1])
        
print(instr_1.name)
        
instr_1.add_ball(ballgames_1)

instr_1.print_balls()
        
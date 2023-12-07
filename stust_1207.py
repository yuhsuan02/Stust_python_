class Sports:
    def _init_(self,name):
        self._name=name
    @property
    def sports_name(self):
        return self._name
    
    @sports_name.setter
    def sports_name(self,value):
        self._name=value
        
    def practive(self):
        print("Doing  Sports practice")
        
class LandSports(Sports):
    def _init_(self,name,field):
        super()._init(name) 
        self._field=field
    @property 
    def landsports_field(self):
        return self._field
    
    def practive(self):
        print("Doing Land Sports practice")
        
class WaterSports(Sports):
    def _init_(self,name,activity):
        super()._init(name) 
        self._activity=activity
        
    @property 
    def watersports_activity(self):
        return self._activity
    
    def practive(self):
        print("Doing Water Sports practice")
    
if __name__=="__main_":
    baseball=LandSports("baseball","baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice())
    
    water_skiing= WaterSports("Water Skiing", "Strap on your skis and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_activity)
    print(water_skiing.practive)
    
    
    sports=Sports("Softball")
    print(sports.sports_name)
    print(sports.practive())
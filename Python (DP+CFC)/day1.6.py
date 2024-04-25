# About Class
class partyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("So Far",self.x)
    
an=partyAnimal()    
an.party()
an.party()
partyAnimal.party(an)



        
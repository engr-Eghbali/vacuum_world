global EnvMap = array([0,0,1,0],
                      [1,1,0,0],
                      [0,1,0,0],
                      [1,0,0,1])
global log    = array(["","","",""],
                      ["","","",""],
                      ["","","",""],
                      ["","","",""])                      
global percept=[2,1,1]
global distanceSens=1
global flag=0

while flag !=1:
    def discusion(percept):
        action=""
        if percept[2]==1:
            action="suck"
        else:
            moves=0
            for i in range(1,distanceSens):
                                
                if log[percept[0]+i,percept[1]]==0 or log[percept[0]+i,percept[1]]=="":
                    action="down"
                    moves=i
                if log[percept[0]-i,percept[1]]==0 or log[percept[0]-i,percept[1]]=="":   
                    action="up"
                    moves=i
                if log[percept[0],percept[1]+i]==0 or log[percept[0],percept[1]+i]=="":
                    action="right"
                    moves=i
                if log[percept[0],percept[1]-i]==0 or log[percept[0],percept[1]-i]=="":
                    action="left"    
                    moves=i

                if log[percept[0]+i,percept[1]]==1:
                    action="down"
                    moves=i
                    break
                if log[percept[0]-i,percept[1]]==1:   
                    action="up"
                    moves=i
                    break
                if log[percept[0],percept[1]+i]==1:
                    action="right"
                    moves=i
                    break
                if log[percept[0],percept[1]-i]==1:
                    action="left"    
                    moves=i
                    break
            


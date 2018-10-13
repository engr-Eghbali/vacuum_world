import random
EnvMap = [[0,0,1,0],
          [1,1,0,0],
          [0,1,0,0],
          [1,0,0,1]]
log    = [[-1,-1,-1,-1],
          [-1,-1,-1,-1],
          [-1,-1,-1,-1],
          [-1,-1,-1,-1]]
percept=[2,1,1]
distanceSens=1
flag=0
moves=0

while flag !=1:
    def discusion(percept):

        action=random.choice(["left","right","up","down"])
        log[percept[0]][percept[1]]=percept[2]
        print(log)

        if percept[2]==1:
            action="suck"
        else:
            i=1
            if log[percept[0]+i][percept[1]]==0 or log[percept[0]+i][percept[1]]==-1 and percept[0]<len(EnvMap):
                action="down"
                moves=i
            if log[percept[0]-i][percept[1]]==0 or log[percept[0]-i][percept[1]]==-1 and percept[0]>0:   
                action="up"
                moves=i
            if log[percept[0]][percept[1]+i]==0 or log[percept[0]][percept[1]+i]==-1 and percept[1]<len(EnvMap[0]):
                action="right"
                moves=i
            if log[percept[0]][percept[1]-i]==0 or log[percept[0]][percept[1]-i]==-1 and percept[1]>0:
                action="left"    
                moves=i

            if log[percept[0]+i][percept[1]]==1:
                action="down"
                moves=i
              
            if log[percept[0]-i][percept[1]]==1:   
                action="up"
                moves=i
              
            if log[percept[0]][percept[1]+i]==1:
                action="right"
                moves=i
              
            if log[percept[0]][percept[1]-i]==1:
                action="left"    
                moves=i
              
        return action   

    def perception(action):
        print(action)
        if action=="down":
            percept[0]=percept[1]+1
        if action=="up":
            percept[0]=percept[1]-1
        if action=="left":
            percept[1]=percept[2]-1
        if action=="right":
            percept[1]=percept[2]+1
            
        if action=="suck":
           percept[2]=0
           
        log[percept[0]][percept[1]]=EnvMap[percept[0]][percept[1]]
        percept[2]=EnvMap[percept[0]][percept[1]]
        return percept

    def checker():

        for row in log:
            for elem in row:
                if elem==1:
                    return False
        else:
            return True            

    act=discusion(percept)
    checker()        
    perception(act)
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
action=""
def discusion(percept):

        action=random.choice(["left","right","up","down"])
        log[percept[0]][percept[1]]=percept[2]
        
        print("Env Map:")
        for row in log:
            print(row)


        print("\n")
        if percept[2]==1:
            action="suck"
        else:
            i=1
            if  percept[0]<len(EnvMap)-1:
                if log[percept[0]+i][percept[1]]==0:  
                   action="down"
                   moves=i
                if log[percept[0]+i][percept[1]]==-1:
                   action="down"    
                   moves=i
                   return action   
                if log[percept[0]+i][percept[1]]==1:
                   action="down"
                   moves=i
                   return action   

            if  percept[0]>0:
                if log[percept[0]-i][percept[1]]==0:
                   action="up"
                   moves=i 
                if log[percept[0]-i][percept[1]]==-1:   
                   action="up"
                   moves=i
                   return action   
                if log[percept[0]-i][percept[1]]==1:   
                   action="up"
                   moves=i
                   return action   

            if percept[1]<len(EnvMap[0])-1:
                if log[percept[0]][percept[1]+i]==0:
                   action="right"
                   moves=i   
                if log[percept[0]][percept[1]+i]==-1 :
                   action="right"
                   moves=i
                   return action   
                if log[percept[0]][percept[1]+i]==1:
                   action="right"
                   moves=i
                   return action   

            if percept[1]>0:
               if log[percept[0]][percept[1]-i]==0:
                  action="left"    
                  moves=i
               if log[percept[0]][percept[1]-i]==-1:
                  action="left"    
                  moves=i
                  return action   
               if log[percept[0]][percept[1]-i]==1:
                  action="left"    
                  moves=i
                  return action   
 
        
        return action   

def perception(action):
        print(action)
        if action=="down":
            percept[0]=percept[0]+1
        if action=="up":
            percept[0]=percept[0]-1
        if action=="left":
            percept[1]=percept[1]-1
        if action=="right":
            percept[1]=percept[1]+1    
        if action=="suck":
           percept[2]=0
           EnvMap[percept[0]][percept[1]]=0
        
        log[percept[0]][percept[1]]=EnvMap[percept[0]][percept[1]]

        percept[2]=EnvMap[percept[0]][percept[1]]

        return percept

def checker():

        for row in log:
            for elem in row:
                
                if elem==-1 or elem==1:
                    return False
        else:
            return True            




while flag !=1:
    
    action=discusion(percept)
    if checker():
        print("all clear!")
        exit()
    else:    
        percept=perception(action)
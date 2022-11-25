import random
while(True):
    x=random.randint(10,900)
    y=random.randint(10,900)
    if(x>250 and y>60):
        print("High temperature and humidity of:",x,y,"%","alaram is on")
        print("*********************************************************")
    elif(x==250 and y==60):
        print("mid temperature and humidity of:",x,y,"%","alarm is on")
        print("*********************************************************")
    elif(x<250 and y<800):
        print("Normal temperature and humidity of:",x,y,"%","alarm is off")
        
        break


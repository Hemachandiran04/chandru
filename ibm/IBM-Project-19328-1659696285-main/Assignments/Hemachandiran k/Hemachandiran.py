import random
while(True):
    x=random.randint(10,1000)
    y=random.randint(10,1000)
    if(x>400 and y>900):
        print("high temperature and humidity of:",x,y,"%","alarm is on")
    elif(x==400 and y==900):
        print("mid temperature and humidity of:",x,y,"%","alarm is on")
    elif(x<400 and y<900):
        print("Normal temperature and humidity of:",x,y,"%","alarm is off")
        break

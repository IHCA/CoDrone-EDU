from codrone_edu.drone import *
from random import randint
drone = Drone()
drone.pair()
drone.takeoff() 

drone.set_throttle(50)
drone.move(2)
drone.hover(1)

for x in range(0, 3, 1):
    powerRand = randint(10,15)
    timeRand = randint(1,2)
    drone.set_throttle(-powerRand)
    drone.move(timeRand)
    drone.hover(1)
    powerRand = randint(10,15)
    timeRand = randint(1,2)
    drone.set_throttle(powerRand)
    drone.move(timeRand)
    drone.hover(1)
  
drone.land()
drone.close()
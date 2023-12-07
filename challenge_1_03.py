'''from codrone_edu.drone import *

drone = Drone()
drone.pair()
print("Paired!")
drone.takeoff()
print("In the air!")
drone.set_pitch(40) # set pitch value to +30
drone.move(3)       # move with the set parameters for 1 second
print("Landing")
drone.land()
drone.close()
print("Program complete")
'''
from codrone_edu.drone import *
drone = Drone()
drone.pair()

drone.takeoff()

drone.set_pitch(20)  # setting forward pitch

drone.move(2)  # moving forward!

drone.set_pitch(0)  # resetting pitch to 0

drone.set_roll(20)  # setting roll to the right

drone.move(2)  # moving right!

drone.set_roll(0)  # resetting roll to 0

drone.set_pitch(-20)  # setting backwards pitch

drone.move(2)  # moving backwards!

drone.set_pitch(0)  # resetting pitch to 0

drone.set_roll(-20)  # setting roll to the left

drone.move(2)  # moving left!

drone.land()

drone.close()

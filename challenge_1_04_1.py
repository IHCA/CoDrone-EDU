from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()

drone.set_yaw(-20)
#drone.set_pitch(20)
drone.move(2)

drone.land()
drone.close()
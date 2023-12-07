from codrone_edu.drone import *
drone = Drone()
drone.pair()
power = 25
turn = 50
#duration = 3
duration = 1
drone.takeoff()

drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
drone.set_yaw(turn)
drone.move(duration)
drone.set_yaw(0)
power = power + 5
drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
drone.set_yaw(turn)
drone.move(duration)
'''
drone.set_yaw(0)
power = power + 5
drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
drone.set_yaw(turn)
drone.move(duration)
drone.set_yaw(0)
power = power + 5
drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
drone.set_yaw(turn)
drone.move(duration)
drone.set_yaw(0)
power = power + 5
drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
drone.set_yaw(turn)
drone.move(duration)
'''

drone.land()
drone.close()
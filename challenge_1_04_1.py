from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()

drone.set_yaw(-20)
#drone.set_pitch(20)
drone.move(2)

drone.land()
drone.close()


'''
我覺得繞圓圈應該是同時設定yaw跟pitch，讓無人機可以一邊轉彎一邊前進，只
設定yaw並給予足夠時間的話無人機確實會在原地繞圈，但是設定pitch之後轉彎
的幅度開始變得很奇怪，前進的方式也很不順暢，不管是讓無人機一邊轉彎一邊前
進，或是讓無人機轉彎，停止，再往前，再繼續旋轉，都無法達到預期的成果。
'''

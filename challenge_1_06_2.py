#算角度

from codrone_edu.drone import * #引入CoDrone EDU的函式庫
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
power = 25 #變數power的值設為25
turn = 50 #變數turn的值設為50
#duration = 3
duration = 1 #變數duration的值設為1
drone.takeoff() #讓無人機起飛並停在空中

drone.set_pitch(power) #往前移動的功率設為power，也就是25
drone.move(duration) #往前移動duration秒，也就是1秒
drone.set_pitch(0) #往前移動的功率設為0
drone.set_yaw(turn) #逆時針用turn的功率旋轉，也就是50的功率旋轉
drone.move(duration) #往前移動duration秒，也就是1秒
drone.set_yaw(0) #旋轉的功率設為0
power = power + 5 #power從25變成30
drone.set_pitch(power) #往前移動的功率設為power，也就是30
drone.move(duration) #往前移動duration秒，也就是1秒
drone.set_pitch(0) #往前移動的功率設為0
drone.set_yaw(turn) #逆時針用turn的功率旋轉，也就是50的功率旋轉
drone.move(duration) #往前移動duration秒，也就是1秒
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
drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線

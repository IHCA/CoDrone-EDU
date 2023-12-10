from codrone_edu.drone import * #引入CoDrone EDU的函式庫
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
power = 20 #變數power的值設為20
duration = 1 #變數duration的值設為1
side = 0 #變數side的值設為0
drone.takeoff() #讓無人機起飛並停在空中

drone.set_pitch(power) #往前移動的功率設為power，也就是20
drone.move(duration) #往前移動duration秒，也就是1秒
drone.set_pitch(side) #往前移動的功率設為side，也就是0
power = power / 2 #power變成power/2，也就是10
drone.set_roll(power) #往右移動的功率設為power，也就是10
drone.move(duration) #往前移動duration秒，也就是1秒
drone.set_roll(side) #往右移動的功率設為side，也就是0
power = power + 10 #power變成power+10，也就是20
drone.set_pitch(-power) #往後移動的功率設為power，也就是20
drone.move(duration) #往後移動duration秒，也就是1秒
drone.set_pitch(side) #往後移動的功率設為side，也就是0
power = 30 - power #power變成30-power，也就是10
drone.set_roll(-power) #往左移動的功率設為power，也就是10
drone.move(duration) #往左移動duration秒，也就是1秒

drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線

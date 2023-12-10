from codrone_edu.drone import * #引入CoDrone EDU的函式庫
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
x = 20 #變數x的值設為20
y = 30 #變數y的值設為30
drone.takeoff() #讓無人機起飛並停在空中

drone.set_pitch(y) #往前移動的值設為y，也就是30
drone.move(1) #無人機移動1秒
drone.set_pitch(0) #往前移動的值設為0
drone.set_roll(x) #往右移動的值設為x，也就是20
drone.move(1) #無人機移動1秒
drone.set_roll(0) #往右移動的值設為0
drone.set_pitch(y) #往前移動的值設為y，也就是30
drone.move(1) #無人機移動1秒
drone.set_pitch(0) #往前移動的值設為0
drone.set_roll(-x) #往左移動的值設為x，也就是20
drone.move(1) #無人機移動1秒
drone.set_roll(0) #往左移動的值設為0
drone.set_pitch(y) #往前移動的值設為y，也就是30
drone.move(1) #無人機移動1秒
drone.set_pitch(0) #往前移動的值設為0
drone.set_roll(x) #往右移動的值設為x，也就是20
drone.move(1) #無人機移動1秒
drone.set_roll(0) #往右移動的值設為0
drone.set_pitch(y) #往前移動的值設為y，也就是30
drone.move(1) #無人機移動1秒

drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線

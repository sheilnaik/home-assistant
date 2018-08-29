from roku import Roku
import time

r = Roku('192.168.1.103')

r.home()
time.sleep(2)
ps_vue = r[93374]
ps_vue.launch()
time.sleep(7)
r.down()
r.select()
time.sleep(8)
r.down()
r.down()
r.down()
r.down()
time.sleep(4)
r.select()
time.sleep(3)
r.select()

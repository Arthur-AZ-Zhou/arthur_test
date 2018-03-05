#stout object
import sys
sys.stdout.write("What does a fish say when it swims into a wall? Dam")
#py version
import sys
print(sys.version)
#time
import time
print(time.time())
def num_print(max):
    t1 = time.time()
    for x in range(0,max):
        print(x)
    t2 = time.time()
    print("It took %s seconds" % (t2-t1))
#Asctime
import time
print(time.asctime())
#Localtime
import time
print(time.localtime())
t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)
#Time off w/ sleep
for x in range(1,61):
    print(x)
    time.sleep(1)

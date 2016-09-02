import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print struct_time

time2 = "04:52"
real_time = time.strptime(time2, "%H:%M")  
print real_time
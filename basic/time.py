import time
from time import perf_counter as my_timer # > time.time()
from time import process_time as my_timer # measured time in cpu

# get time since epoch (passing in seconds)
print(time.gmtime(0))
# local time to device
print(time.localtime())
# epoch in UTC
print(time.time())
# UTC
print(time.gmtime())

time_here = time.localtime()
print(time_here[0])
# time.struct_time(tm_year=2020, tm_mon=11, tm_mday=29, tm_hour=3,
# tm_min=50, tm_sec=37, tm_wday=6, tm_yday=334, tm_isdst=0)
# can access either by property: tm_year, or by index time_here[0]
print(f"Year: {time_here.tm_year}")
print(f"Month: {time_here.tm_mon}")
print(f"Day: {time_here.tm_mday}")

# how to measure time
# from time import time as my_timer
print("*" * 40)
start_time = time.time()
_start = time.strftime("%X", time.localtime(start_time))
print(f"Started at: {_start}")
time.sleep(2)
end_time = time.time()
_end = time.strftime("%X", time.localtime(end_time))
print(f"Ended at: {_end}")
print(f"Total elapsed time  {end_time - start_time} seconds")
print("*" * 40)
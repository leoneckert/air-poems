import subprocess
#            _  __  __      _                   
#           (_)/ _|/ _|    | |                  
#  ___ _ __  _| |_| |_     | | ___   ___  _ __  
# / __| '_ \| |  _|  _|    | |/ _ \ / _ \| '_ \ 
# \__ \ | | | | | | |      | | (_) | (_) | |_) |
# |___/_| |_|_|_| |_|      |_|\___/ \___/| .__/ 
#                                        | |    
#                                        |_|

# adapted from here: http://stackoverflow.com/a/4417735
def run(command):    
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    return iter(popen.stdout.readline, b"")


#GLOBAL variables:
current_channel = 1
def channel_controller(c, c_hop_interval):
    global current_channel
    if c > c_hop_interval:
            idx = channel_range.index(current_channel)
            idx = idx + 1
            if idx >= len(channel_range):
                idx = 0;
            current_channel = channel_range[idx]

            subprocess.call("airport -c" + str(current_channel), shell=True)
            # print "///////////////////////////////////////////// Switched to channel: " + str(current_channel)
            c = 0   
    else:
        c = c + 1 
    return c


# def sniffloop(handle_function):
#     global current_channel
#     count = 10
#     alreadyInspected = set()
#     current_channel = channel_range[-1]

#     #next line makes all the difference, making sure the hoping works by disassociating fro any network before start:
#     # subprocess.call("airport -z", shell=True)     # DEactivate for TESTING

#     # for line in run("./bps_v1"):      # DEactivate for TESTING
#     for line in open("lot_to_test.log", "r"):  # activate for TESTING
#         #next line for channel hoping:
#         # count = channel_controller(count, channel_hop_interval)       # DEactivate for TESTING
#         line = line.strip()

#         handle_function(line)

# FOR TESTNG:
import time
from pprint import pprint
startTime = 1463353999
testdata = dict()
deltaStart = 0
timeschecked = set()
# ---

def sniffloop(handle_function):
    global current_channel
    count = 10
    alreadyInspected = set()
    current_channel = channel_range[-1]


    # FOR TESTNG:

    for line in open("lot_to_test.log", "r"):
        line = line.strip()
        ts = int(line.split(',')[0])
        if ts not in testdata:
            testdata[ts] = list()
        testdata[ts].append(line)   
    print "[+] done preparing test data"
    first = True
    while True:
        if first is True:
           deltaStart = int(time.time())
           first = False

        currentFakeTime = startTime + (int(time.time()) - deltaStart)
        if currentFakeTime in testdata and currentFakeTime not in timeschecked:
            for line in testdata[currentFakeTime]:
                handle_function(line)
            timeschecked.add(currentFakeTime)




  #   #next line makes all the difference, making sure the hoping works by disassociating fro any network before start:
  #   subprocess.call("airport -z", shell=True)		# DEactivate for TESTING

  #   for line in run("./bps_v1"):		# DEactivate for TESTING
		# #next line for channel hoping:
		# count = channel_controller(count, channel_hop_interval)		# DEactivate for TESTING
		# line = line.strip()

		# handle_function(line)


# GLOBAL variables:
channel_range = [1,6,11,36,40,44,48]
channel_hop_interval = 50







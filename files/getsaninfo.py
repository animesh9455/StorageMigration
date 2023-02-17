# get number of servers
# run linux command saninfo (ls)
# get output (json) in variable
# parse json file using frame number and get count of each app_name with size
import subprocess
import os
import json
#tmp.py file contains sanindo o/p in json format
import tmp

frame_number = "000197802751"
#frame_number. is given by the user
saninfo_otpt = tmp.saninfo_output 
#print(saninfo_otpt)
dict_app = {}
# dict_app is a dictionary within a dictionary - outer dictionary will have app_name as key while inner will have size and their occurances as key and value
for frame in saninfo_otpt.values():
    if(frame.get("frame") == frame_number) and frame.get("app"):
        app_name = frame.get("app")
        # initalize empty dict
        if app_name not in dict_app:
            dict_app[app_name] = {}
        frame_size = frame.get("size")
        if dict_app[app_name].get(frame_size):
            frame_val = dict_app[app_name].get(frame_size)
            dict_app[app_name][frame_size] +=1 
        else:
            dict_app[app_name][frame_size] =1 
print(dict_app)



# get number of servers
# subprocessmodule :
# run linux command saninfo (ls)
# get output (json) in variable
import subprocess
import os
import json
import tmp

#saninfo_out = subprocess.check_output('/auto/hosting/bin/saninfo -j', shell = True) 
#saninfo_out = subprocess.check_output('echo "{\'key1\': \'val1\', \'key2\': \'val2\'}"', shell = True) 
#print(type(saninfo_out))

# saninfo_json = saninfo_out.decode('utf8').replace("'", '"')

# data = json.loads(saninfo_json)
#print(type(data))
# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)
frame_number = "000197802751"
saninfo_otpt = tmp.saninfo_output 
#print(saninfo_otpt)
dict_app = {}

for frame in saninfo_otpt.values():
    #print(frame)
    if(frame.get("frame") == frame_number):
        app_name = frame.get("app")
        #print(app_name)

        if app_name != "None" and app_name not in dict_app:
            dict_app[app_name] = {}
        
        #dict_app[app_name] = {frame.get("size") : int(frame.get("size"), 0) + 1}
        #print(dict_app[app_name].get(frame.get("size"), 0))
        dict_app[app_name] = {frame.get("size") : int(dict_app[app_name].get(frame.get("size"), 0)) + 1}
        #dict_app[frame.get(app)] = dict_app.get(frame.get(app  )) +1 
        #map.put(frame.getOrDeafult(app, 0) +1);
print(dict_app)
# for x in dict_app:
#     print()
# s = json.dumps(dict_app, indent=4, sort_keys=True)
# print(s)
#list_disk_in_frame = saninfo_otpt[






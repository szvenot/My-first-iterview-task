import json
import os
from collections import OrderedDict

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        seconds = float(f.readline().split()[0])
	minutes = seconds // 60
	hours = minutes // 60
	uptime = "%iH%iM%iS" % (hours, minutes % 60, seconds % 60)
    return uptime

text = os.popen('ps').read()
list_of_text = text.split() 

process = {}

def get_pid_n_name(lista):
	for i,word in enumerate(lista):
		try:
			if float(word) > 0: 
				process[word] = (lista[i+3])
		except:
			continue
	return process

final_dicti = OrderedDict()
final_dicti['uptime'] = get_uptime()
final_dicti['processes'] = get_pid_n_name(list_of_text)


with open('solution.json','w') as json_dict:
	json.dump(final_dicti, json_dict)

print(final_dicti)



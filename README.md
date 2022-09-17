Without using the library psutil, create a python program that generates a JSON file containing the system up-time and a dictionary containing the active processes' PIDs as key and the invocation command as value. It should follow the exemplified format:

 

{"uptime": "04H23M23S", "processes": {"2414": "ls", "4341": "bash"}}

 

The solution should be compatible with Ubuntu 18.04+.

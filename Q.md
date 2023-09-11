From Tamir Arieli to Everyone 01:03 PM
Consider the following input file which contains JSONS of the following structure:

[{"process_name":"a.exe", "pid":420, "parent_pid":428}
{"process_name":"c.exe", "pid":428, "parent_pid":None}
{"process_name":"d.exe", "pid":551, "parent_pid": 420}
{"process_name":"e.exe", "pid":552, "parent_pid":428}
{"process_name":"f.exe", "pid":553, "parent_pid":None}
{"process_name":"g.exe", "pid":4, "parent_pid":553}
{"process_name":"b.exe", "pid":7, "parent_pid":4}
{"process_name":"h.exe", "pid":11, "parent_pid":7}]

The program should output the following:

c.exe
----a.exe
--------d.exe
----e.exe
f.exe
----g.exe
--------b.exe
------------h.exe


pl = [{"process_name":"a.exe", "pid":420, "parent_pid":428},
{"process_name":"c.exe", "pid":428, "parent_pid":None},
{"process_name":"d.exe", "pid":551, "parent_pid": 420},
{"process_name":"e.exe", "pid":552, "parent_pid":428},
{"process_name":"f.exe", "pid":553, "parent_pid":None},
{"process_name":"g.exe", "pid":4, "parent_pid":553},
{"process_name":"b.exe", "pid":7, "parent_pid":4},
{"process_name":"h.exe", "pid":11, "parent_pid":7}]

from collections import defaultdict
from typing import Dict

def events_to_dict(process_events: list) -> Dict:
    ppid = defaultdict(list)
    for event in process_events:
        parent_pid = event["parent_pid"] or 0
        ppid[parent_pid].append(event)

    return ppid



def print_events(ppid: Dict, pid: int, name: str = "", depth: int = -1) -> None:
    if name:
        print("----" * depth + name)
    for event in ppid[pid]:
        print_events(ppid, event["pid"], event["process_name"], depth + 1)

def main():
    ppid = events_to_dict(pl)
    print_events(ppid, 0)

    
if __name__ == "__main__":
    main()




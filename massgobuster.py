#!/usr/bin/python
import os, sys, operator, subprocess, threading

def bash_fg(cmd):
    cmd = str(cmd).strip().rstrip()
    print "Running command\r\n{}".format(str(cmd))
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return
def runGobuster(host,port):
    wordlist = "/usr/share/wordlists/dirbuster/allpaths.txt"
    output = "gobuster-{}-{}.txt".format(
        str(host),
        str(port)
    )
    cmd = "gobuster dir -u http://{}:{} -w {} -o {}".format(
        str(host),
        str(port),
        str(wordlist),
        str(output)
    )
    bash_fg(cmd)
    return cmd
def readInputFile(inputFile):
    # reads a input file separated as HOST,PORT
    r = open(inputFile,'r+')
    lines = r.readlines()
    for l in lines:
        line = l.split(',')
        host = str(line[0]).strip().rstrip()
        port = str(line[1]).strip().rstrip()
        runGobuster(host,port)
    return

def main():
    if len(sys.argv) < 2:
        print "Usage:\r\npython massgobuster.py <list of hosts and ports separated by commas>"
        exit(0)
    else:
        inputFile = sys.argv[1]
        readInputFile(inputFile)
    return
main()
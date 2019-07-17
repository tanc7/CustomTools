#!/usr/bin/python
import os, sys, operator, subprocess, threading

def bash_fg(cmd):
    cmd = str(cmd).strip().rstrip()
    print "Running command\r\n{}".format(str(cmd))
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return
def runGobuster(host,port):
    wordlist = sys.argv[2]

    # wordlist = "/usr/share/wordlists/dirbuster/allpaths.txt"
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
    print "MassGoBuster. Automatically run gobuster against a wordlist of host,port.\r\nComing soon: Threading by running 5 gobuster processes at a time."
    if len(sys.argv) < 3:
        print "Usage:\r\npython massgobuster.py <wordlist host,port> <wordlist of /paths>"
        exit(0)
    else:
        inputFile = sys.argv[1]
        readInputFile(inputFile)
    return
main()
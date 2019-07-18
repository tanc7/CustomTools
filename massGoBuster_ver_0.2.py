#!/usr/bin/python
import os, sys, operator, subprocess, threading, toolkits



# WARNING: Do not run mass-go-buster unless you have MORE than 16GB of RAM on your host operating system and allocated AT LEAST 8GB to your guest. Gobuster itself is VERY memory hungry. 
# Run gobuster 5 at a time using threading and asyncio (Python3 only)
# Work on this later, get the scanners back up

# Reasons.
# Gobustering one IP at a time is too slow
# Half-assing multiple processes by appending & creates too many processes, potentially crashing your NIC.
# Each gobuster thread needs to be throttled, up to 5 at a time.
# Meanwhile each gobuster process can have their threads throttled or increased. By default its 10 threads.

def threadPacker(thread):
    return threadList

# Create 5 threads into a list. And then have asyncio run those 5 threads. The threads are joined together, once they are completed, pack 5 more threads and gobuster them.
def asyncManager(threadList):
    threadList = threadPacker(thread)

    return

def bash_fg(cmd):
    cmd = str(cmd).strip().rstrip()
    print "Running command\r\n{}".format(str(cmd))
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return
def runGobuster(host,port):
    wordlist = sys.argv[2]
    if len(sys.argv) < 4:
        threads = 10
    else:
        threads = sys.argv[3]
    output = "gobuster-{}-{}.txt".format(
        str(host),
        str(port)
    )
    cmd = "gobuster dir -u http://{}:{} -w {} -t {} -o {}".format(
        str(host),
        str(port),
        str(wordlist),
        str(threads),
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
    if len(sys.argv) < 2:
        print toolkits.yellow("Usage:\r\npython massgobuster.py <wordlist of host,ports> <wordlist of paths> <OPTIONAL: threads, default=10>")
        print toolkits.cyan("\r\nEXAMPLE: python massGoBuster.py targetHostPort.txt /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt 50\r\nEXAMPLE EFFECT: Runs GoBuster at a rate of 50 threads against each target,port combo found in the list of targets using the wordlist")
        exit(0)
    else:
        inputFile = sys.argv[1]
        readInputFile(inputFile)
    return
main()
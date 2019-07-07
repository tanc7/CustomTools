#!/usr/bin/python
import os, sys, subprocess, operator, socket, threading,time, toolkits
# Mass scans a wordlist of IP\sport with the following tools and generates output as host-tool-scanned.txt
# nikto, wapiti, uniscan, arachni

red = toolkits.red
green = toolkits.green
yellow = toolkits.yellow
cyan = toolkits.cyan

def bash_cmd_fg(cmd,IP,PORT,TOOL):
    cmd = str(cmd).strip().rstrip()
    cmd += " 2>&1 | tee {}-{}-scanned.txt &".format(
        str(IP),
        str(TOOL)
    )
    print cyan("DEBUG: Running command {} in 5 seconds".format(str(cmd)))
    time.sleep(5)
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return cmd

def writeOutput(IP,PORT,TOOL,line):
    outfile = "{}-{}-{}.txt".format(
        str(IP),
        str(PORT),
        str(TOOL)
    )
    w = open(outfile, 'ab+')
    w.write(line)
    w.close()
    return

def bash_cmd_bg(cmd,IP,PORT,TOOL):
    cmd = str(cmd).strip().rstrip()
    # cmd += " | tee {}-{}-scanned.txt".format(
    #     str(IP),
    #     str(TOOL)
    # )
    print "DEBUG: Running command {} in 5 seconds".format(str(cmd))
    time.sleep(5)
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    verbose =  out + err
    # verbose = str(verbose.encode('utf-8')).strip().rstrip()
    lines = verbose.splitlines()
    for line in lines:
        print line
        writeOutput(IP,PORT,TOOL,line)
    return cmd

def retHTTP(PORT):
    if PORT == "443" or "8443":
        httpProto = "https"
    if PORT == "80" or "8080" or "81" or "8081":
        httpProto = "http"
    return httpProto

# additional modules that need to be implemented
def changeme():
	return
def grabber():
	return
def joomscan():
	return
def vuls():
	return
def wpscan():
	return

# implemented automated modules
def nikto(IP,PORT):
    TOOL = "nikto"
    cmd = "nikto -host {} -port {}".format(str(IP),str(PORT))
    bash_cmd_fg(cmd,IP,PORT,TOOL)
    return cmd, TOOL
def wapiti(IP,PORT):
    TOOL = "wapiti"
    httpProto = retHTTP(PORT)
    cmd = "wapiti -u {0}://{1}:{2}/\r\n".format(
        str(httpProto),
        str(IP),
        str(PORT)
    ).strip().rstrip()
    bash_cmd_bg(cmd,IP,PORT,TOOL)
    #bash_cmd_fg(cmd,IP,PORT,TOOL)
    return cmd, TOOL
def uniscan(IP,PORT):
#uniscan -u http://target:80 -qwedsiogj
    TOOL = "uniscan"
    httpProto = retHTTP(PORT)
    cmd = "uniscan -u {}://{}:{} -qwedsiogj".format(
        str(httpProto),
        str(IP),
        str(PORT)
    )
    bash_cmd_bg(cmd,IP,PORT,TOOL)
    # bash_cmd_fg(cmd,IP,PORT,TOOL)
    return cmd, TOOL
def arachni(IP,PORT):
    TOOL = "arachni"
    httpProto = retHTTP(PORT)
    cmd = "arachni {}://{}:{}".format(
        str(httpProto),
        str(IP),
        str(PORT)
    )
    bash_cmd_fg(cmd,IP,PORT,TOOL)
    return cmd, TOOL

def threadPacker():
    return
def readTargets(targets="/root/Documents/OffSec2019/offsec-subnet-webservers.log"):
    r = open(targets,'r')
    lines = r.readlines()
    for line in lines:
        s = line.split(" ")
        IP = s[0]
        PORT = s[1]
        nikto(IP,PORT)
        wapiti(IP,PORT)
        uniscan(IP,PORT)
        arachni(IP,PORT)
    print "Completed scans"
    exit(0)
    return
def main():
    os.chdir('/root/Documents/OffSec2019/')
    readTargets()
    return
main()

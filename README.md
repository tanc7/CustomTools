# To be added to (pulled) Arms-Commander repo in OSCP exam update

Arms-Commander has been pulled. Instead, this repo serves as the public repository of custom tools I made to make the exam and labs less ardous.

Arms-Commander will be re-released with these tools. To better pave the path to newcoming students of the Penetration Testing with Kali Linux Course


# Added MassGoBuster

Automatically run gobuster against a wordlist of ip,port on each line, useful for offsec labs. After my Exam on Sunday, I will introduce a multi-threaded version, right now that version is not completed.

Syntax:

`python massgobuster.py <wordlist>`

Where each line in wordlist looks like:

10.1.1.1,80
10.11.1.230,80
10.11.1.227,8080

# Added Pass-the-Hash Bruter

Automatically runs pth-winexe against a list of collected hashes, commonly from Metasploit's hashdump (meterpreter) hashdump command. It auto parses out the LM:NTLM hashes and attempts to execute cmd.exe via SMB. 

Coming soon after exam attempt

1. Automatic add Administrative User and Enabling Remote Desktop Protocol
2. Automatic dropping of rpivot into C:\Windows\System32 and then running rpivot.exe client to connect back to rpivot.py servver
3. Automatic fgdump.exe and homebrew Python SimpleHTTPServer to download additional stages

Syntax:

`python pth-bruter.py <ip> <hashlist> <domain:optional>`

# Added RPivot Documentation

# Added Examples of both Windows and Linux Buffer Overflow Exercises

These are meant to serve as notes for current PwK students.

Chang Tan Lister
Lister Unlimited
changtan@listerunlimited.com

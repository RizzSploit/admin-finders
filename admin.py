import os
import requests

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

os.system('clear')
f = open('asci')
print merah+f.read()
f.close
print '---------------------------------------------------'
print cyan+' Author  : '+green+'RizzSploit '
print cyan+' Github  : '+green+'http://github.com/RizzSploit '
print cyan+' Youtube : '+green+'RizzSploit '
print putih+'---------------------------------------------------'
print ''
#input
web = raw_input(merah+'Website: ')

#buka wordlist
f = open('wordlist.txt','r')
kontent = f.read()
x = kontent.split('\n')

for i in x:
    url = web+'/'+i
    code = requests.get(str(url)).status_code
    if code == 200:
           print green+"[+] Berhasil url: "+url
           exit()
    else:
           print merah+"[-] Gagal url: "+url

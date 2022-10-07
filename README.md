# Jeff's OSCP Notes
> OSCP Pass Plsssssss!!!!!!!!!!!!!!

Start virtual env before using python3
```bash
virtualenv -p python3 venv
. venv/bin/activate
# now you are in a nice python3 world, completely isolated from system python
# remember to say . venv/bin/python every time you do anything
# or you can even add it to your .bashrc
```

Chisel Cheatsheet
```bash
#Server
./chisel server -p 8000 --reverse

#Client
./chisel client 192.168.10.11:8000 R:socks

#Server
proxychains command
```

SSH with old algo
```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-dss,ssh-rsa <Username>@<IP>
```

## Contents & Resources

### OSCP Review and Guides
- [2021::OSCP::回顧與分享](http://blog.terrynini.tw/tw/2021-OSCP-%E5%9B%9E%E9%A1%A7%E8%88%87%E5%88%86%E4%BA%AB/#Lab-%E7%9A%84%E5%BE%A1%E4%B8%89%E5%AE%B6)
- [Hattrick Commands](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/juicypotato)

### Cheatsheet
- [Reverse Shell Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp)
- [NSE Library](https://nmap.org/nsedoc/lib/)
- [Nmap Cheatsheet](https://www.stationx.net/nmap-cheat-sheet/)
- [WebShell Cheatsheet](https://github.com/danielmiessler/SecLists/tree/master/Web-Shells/FuzzDB)
- [Linux Privilege Escalation](https://gtfobins.github.io/gtfobins/chown/)
- [Web Encoding](https://www.w3schools.com/tags/ref_urlencode.asp)
- [Crackmapexec](https://cheatsheet.haax.fr/windows-systems/exploitation/crackmapexec/)
- [Mona Cheat Sheet for finding bad chars](https://x3tb3t.github.io/2018/03/29/mona/#useful-mona-commands)
- [Spwan TTY](https://sushant747.gitbooks.io/total-oscp-guide/content/spawning_shells.html)
- [RevShell - Generator](https://www.revshells.com/) 

### Active Directory
- [Command Checklist](https://wadcoms.github.io/)
- [AD Cheatsheet 1](https://gist.github.com/ssstonebraker/a1964b2f20acc8edb239409b6c4906ce)
- [AD Cheatsheet 2](https://github.com/brianlam38/OSCP-2022/blob/main/cheatsheet-active-directory.md)
- [PasstheHash](https://ares-x.com/2020/03/21/%E5%9F%9F%E6%B8%97%E9%80%8F%E5%AD%A6%E4%B9%A0%EF%BC%88%E5%85%AD%EF%BC%89PTH-%E5%93%88%E5%B8%8C%E4%BC%A0%E9%80%92%E6%94%BB%E5%87%BB/)
### External Tools
- [Hash Crack](https://crackstation.net/)

### Script

#### Privilege Escalation
- [Windows Priv Check](https://github.com/pentestmonkey/windows-privesc-check)
- [Linux Priv Check](https://github.com/HappyTreeFriend/linux-exploit-suggester)


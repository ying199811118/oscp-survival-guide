# Intercepting LDAP & SMB

## Hosting Rogue LDAP Server
```
#TCP DUMP
sudo tcpdump -SX -i breachad tcp port 389
```

## Intercepting NetNTLM Challenge (SMB)
```
#Responder
sudo responder -I tun0
```

# Enumerating Active Directory

## Check Runas.exe
```
runas.exe /netonly /user:<domain>\<username> cmd.exe
```


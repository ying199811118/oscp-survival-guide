## Intercepting LDAP & SMB

### Hosting Rogue LDAP Server
```
sudo tcpdump -SX -i breachad tcp port 389
```

### Intercepting NetNTLM Challenge (SMB)
```
sudo responder -I tun0
```

## Enumerating Active Directory

### Check Runas.exe
```
runas.exe /netonly /user:<domain>\<username> cmd.exe
```
### Bloodhound & Sharphound
```
Sharphound.exe --CollectionMethods <Methods> --Domain za.tryhackme.com --ExcludeDCs
neo4j console start


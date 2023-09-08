# CTF gathered resources 

## PrivEsc

```
https://gtfobins.github.io/
```
## Commands

- `sudo -l`
- `puttygen keeper.ppk -O private-openssh -o keeper.pem` PPK to PEM
- `ansible2john ansible.vaul >> hashes`

## Resources


## Samba

```
smbclient -L \\\\authority.htb\\
smbclient  \\\\authority.htb\\Development
```

## Windows

- `evil-winrm -i 10.10.11.222 -u svc_ldap -p 'lDaP_1n_th3_cle4r!'` SSH for windows
-  `sudo responder -I tun0` Start some service

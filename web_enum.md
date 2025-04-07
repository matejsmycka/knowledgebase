# Web enum

```bash
wget https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt
ffuf  -u https://<PAGE>/FUZZ -w common.txt -o paths.txt
cat paths.txt | jq .results[].redirectlocation | tr -d "\"" > paths2.txt 
```

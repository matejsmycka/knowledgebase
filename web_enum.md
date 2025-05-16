# Web enum

## Paths

```bash
wget https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt
ffuf  -u https://<PAGE>/FUZZ -w common.txt -o paths.txt
cat paths.txt | jq .results[].redirectlocation | tr -d "\"" > paths2.txt 
```
## FFUF

```bash
ffuf -w common -u <URL>/FUZZ
ffuf -w common -u <url>  -H "Host: FUZZ.<url>" -fs 101
```

# Wordpress pentest guide

Start with Nuclei to catch low-hanging fruit.

## Plugin/Path Enumeration

### Generic

```bash
wget https://raw.githubusercontent.com/satyasai1460/wp-Fuzzing-list/refs/heads/main/wp-fuzz.txt
ffuf  -u https://quietsustainability.geogr.muni.cz:443/FUZZ -w wp-fuzz.txt  -mc 200 -s
```
## Plugins
```
wp-wordlist()
{
    option="$1"
    if [[ "$option" == *"plugin"* ]]; then
        curl -s https://plugins.svn.wordpress.org/ | tail -n +5 | sed -e 's/<[^>]*>//g' -e 's/\///' -e 's/ \+//gp' | grep -v "Powered by Apache" | sort -u
    elif [[ "$option" == *"theme"* ]]; then
     curl -s https://themes.svn.wordpress.org/ | tail -n +5 | sed -e 's/<[^>]*>//g' -e 's/\///' -e 's/ \+//gp' | grep -v "Powered by Apache" | sort -u
    fi
}

wp-wordlist "$1"
chmod +x wp-wordlist.sh
./wp-wordlist.sh  plugin > plugins.txt
./wp-wordlist.sh theme > theme.txt
ffuf  -u https://<SITE>/wp-content/plugins/FUZZ/readme.txt -w plugins.txt -mc 200
ffuf  -u https://<SITE>/wp-content/themes/FUZZ/readme.txt -w theme.txt -mc 200
```

## Vulnerability Scan

### Nuclei
```bash
git clone https://github.com/topscoder/nuclei-wordfence-cve.git
nuclei -t nuclei-wordfence-cve -severity critical,high -u https://<SITE>
```

### WPScan

```bash
wpscan --url  https://<SITE>
```

# Bug Bounty

## Cloud

Needed packages
```bash
tmux
go
jq
nuclei
httpx
naabu
ffuf
nginx
```

Nginx notice
```bash
sudo systemctl stop nginx 2>/dev/null; sudo bash -lc '
DIR=/srv/bugbounty
MAIL=""
HTML="<!doctype html><meta charset=\"utf-8\"><title>Notice</title><h1>Automated security assessment tool.</h1><p>For opt-out requests or inquiries, please reach out to <a href=\"mailto:$MAIL\">$MAIL</a></p>"
mkdir -p $DIR/htdocs
printf "%s\n" $HTML > "$DIR/htdocs/index.html"
printf "%s\n" "user root;" "events {}" "http {" \
"  server {" \
"    listen 80;" \
"    server_name _;" \
"    root $DIR/htdocs;" \
"    location / { try_files \$uri \$uri/ =404; }" \
"  }" \
"}" > "$DIR/nginx.conf"
nginx -c "$DIR/nginx.conf" -p "$DIR"
'
```

## Nuclei

```bash
tmux new-session -t nuclei-1
cat scope.txt | httpx -j -sc -bp -o scope_httpx.json
cat scope_httpx.json | jq -r .url | katana -j -o scope_katana.json 
cat scope_httpx.json | jq -r .url | nuclei -jsonl -o findings.jsonl -H "User-Agent: Automated security assessment tool. For opt-out requests or inquiries, please reach out to: $MAIL" -retries 2 
```

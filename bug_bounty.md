# Bug Bounty

## Cloud

Needed packages
```bash
tmux
nuclei
ffuf
nginx
```

Nginx notice
```bash
sudo systemctl stop nginx 2>/dev/null; sudo bash -lc '
DIR=/srv/bugbounty
mkdir -p $DIR/htdocs
printf "%s\n" "<!doctype html><meta charset=\"utf-8\"><title>Notice</title><h1>User-Agent: Bug bounty scanner</h1><p>To opt out of scanning, email: <a href=\"mailto:22qsvkmnf@mozmail.com\">22qsvkmnf@mozmail.com</a></p>" > "$DIR/htdocs/index.html"
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
cat scope.txt | nuclei -jsonl -o findings.jsonl -H "User-Agent: Automated security assessment tool. For opt-out requests or inquiries, please reach out to: 22qsvkmnf@mozmail.com" -retries 2 
```

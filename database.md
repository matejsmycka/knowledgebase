# Databases

## Mysql or MariaDB

### Dump all
`[mariadb-dump|mysqldump] -u <USER> -P 3306 -h <HOSTNAME> --all-databases -p --single-transaction --ssl | gzip > db_dump.sql.gz`
```
#!/bin/bash


databases="asdasd adasdasd dsaddasds dasasd asasddas"

for db in $databases; do
echo "Dumping database: $db"
    mariadb-dump -u <USER> -P 3306 -h <HOST> -p<PASSWD>--single-transaction --ssl $db | gzip > ${db}_dump.sql.gz
done
```

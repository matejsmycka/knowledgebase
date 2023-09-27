# Databases

## Mysql or MariaDB

### Dump all
`[mariadb-dump|mysqldump] -u <USER> -P 3306 -h <HOSTNAME> --all-databases -p --single-transaction --ssl | gzip > db_dump.sql.gz

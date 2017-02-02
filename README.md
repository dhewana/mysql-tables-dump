# mysql-tables-dump
Dump a MySQL database per table, and then will delete the mysql backup folder older than 7 days.

## Config example
```
DB_OPT = '--tz-utc=false --single-transaction=true'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_USER = 'dbuser'
DB_USER_PASSWORD = 'dbpassword'
DB_NAME = 'dbname'
BACKUP_PATH = '/home/user/dbname/'
```
Note : The `/` at the end of `BACKUP_PATH` is **important**.

You can choose the mysql backup command by modifying the `dump_cmd` variable, the default is with `DB_OPT` :
```
dump_cmd = "mysqldump " + DB_OPT + " -h " + DB_HOST + " -P " + DB_PORT + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " " + tables + " | gzip > " + TODAYBACKUPPATH + "/" + DB_NAME + "." + tables + "." + DATETIME + ".sql.gz"
```

or without `DB_OPT` :
```
dump_cmd = "mysqldump -h " + DB_HOST + " -P " + DB_PORT + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " " + tables + " | gzip > " + TODAYBACKUPPATH + "/" + DB_NAME + "." + tables + "." + DATETIME + ".sql.gz"
```

## Cron job daily example
```
20 0 * * * /usr/bin/python3 /home/user/mysql_tables_dump.py > /home/user/mysql_tables_dump.log
```

# mysql-tables-dump
Dump a MySQL database per table, and delete backup folder older than 7 days.

### Config example
```
DB_OPT = '--tz-utc=false --single-transaction=true'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_USER = 'dbuser'
DB_USER_PASSWORD = 'dbpassword'
DB_NAME = 'dbname'
BACKUP_PATH = '/backup/dbname/'
```
The `/` at the end of BACKUP_PATH is **important**.

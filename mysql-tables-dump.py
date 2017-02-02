#!/usr/bin/python3

import os
import time
import datetime

DB_OPT = ''
DB_HOST = ''
DB_PORT = ''
DB_USER = ''
DB_USER_PASSWORD = ''
DB_NAME = ''
BACKUP_PATH = ''

DATETIME = time.strftime('%Y%m%d-%H%M%S')
print ("DATETIME: " + DATETIME + "\n")

TODAYBACKUPPATH = BACKUP_PATH + DATETIME
print (time.strftime('%Y%m%d-%H%M%S') + " - Creating TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' ...")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
print (time.strftime('%Y%m%d-%H%M%S') + " - TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' created.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Listing tables ...")
tables_cmd = "mysql -u " + DB_USER + " -p" + DB_USER_PASSWORD + " -h " + DB_HOST + " -P " + DB_PORT + " -D " + DB_NAME + " -e 'SHOW TABLES'"
tables_data_raw = os.popen(tables_cmd).read()
tables_data = tables_data_raw.split('\n')
tables_data.pop(0)
tables_data.pop()
tables_data_new = ''
print (time.strftime('%Y%m%d-%H%M%S') + " - Listing tables done.\n")
for tables in tables_data:
    tables_data_new += tables +'\n'
    print (time.strftime('%Y%m%d-%H%M%S') + " - Starting to backup table '" + tables + "' ...")
    dump_cmd = "mysqldump " + DB_OPT + " -h " + DB_HOST + " -P " + DB_PORT + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " " + tables + " | gzip > " + TODAYBACKUPPATH + "/" + DB_NAME + "." + tables + "." + DATETIME + ".sql.gz"
    os.system(dump_cmd)
    print (time.strftime('%Y%m%d-%H%M%S') + " - Backup of table '" + tables + "' completed.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Backup script completed, your backup has been created in '" + TODAYBACKUPPATH + "' directory.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Deleting backup files older than 7 days...")
rmgz = "find " + BACKUP_PATH + "* -type d -ctime +7 -exec rm -rf {} \;"
os.system(rmgz)
print (time.strftime('%Y%m%d-%H%M%S') + " - Backup files older than 7 days deleted.\n")

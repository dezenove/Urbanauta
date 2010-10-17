# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.getcwd())

import psycopg2
import settings

dbconf = settings.DATABASES['default']

# default superuser configuration
conn_params = {
    'database': 'postgres',
    'user' : 'postgres',
    'password' : raw_input('Digite a senha root do postegresql: '),
    'host' : 'localhost'
}

conn = psycopg2.connect(**conn_params)
conn.set_client_encoding('UTF8')
conn.set_isolation_level(0)

try:
    cursor = conn.cursor()
    print "Drop database (if exists) .."
    cursor.execute('DROP DATABASE IF EXISTS ' + dbconf['NAME'])
    print ".. OK"
    print "Create database .."
    cursor.execute("CREATE DATABASE " + dbconf['NAME'] + " WITH OWNER = " + dbconf['USER'] + " TEMPLATE = template_postgis ENCODING = 'UTF8'")
    conn.commit()
    print ".. OK"
except psycopg2.OperationalError, e:
    print str(e).decode('utf-8')

cursor.close()
conn.close()

print "Running syncdb .."
os.system('python manage.py syncdb')
print ".. OK"
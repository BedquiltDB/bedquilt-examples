#! /usr/bin/env python

import os
import subprocess
import pipes
import json


BEDQUILT_EXAMPLE = 'bedquilt_example'


def psql(sql, db='postgres'):
    return subprocess.check_output([
        'psql', '-qAt', '-d', db,
        '-c', sql
    ])

    return result


def sql_escape(st):
    return st.replace("'", "''")


def main():

    print ">> Seeding {}...".format(BEDQUILT_EXAMPLE)

    # Get list of existing databases
    databases = psql(
        "select datname from pg_catalog.pg_database"
    ).splitlines()
    databases = map(lambda s: s.strip(), databases)

    # Check if the example database exists already
    if BEDQUILT_EXAMPLE in databases:
        print ">> Database {} already exists".format(BEDQUILT_EXAMPLE)
        print ">> Dropping {}".format(BEDQUILT_EXAMPLE)
        # TODO: handle client connections to database
        psql("drop database {}".format(BEDQUILT_EXAMPLE))

    # Create the bedquilt_example database
    print ">> Creating the {} database".format(BEDQUILT_EXAMPLE)
    psql("create database {}".format(BEDQUILT_EXAMPLE))

    # Enable extensions on db
    print ">> Enabling bedquilt extension on {}".format(BEDQUILT_EXAMPLE)
    psql(
        """
        create extension if not exists pgcrypto;
        drop extension if exists bedquilt;
        create extension bedquilt;
        """,
        db=BEDQUILT_EXAMPLE)

    # loop over data:
    #   - insert into bedquilt_example
    print ">> Adding data to database"
    data = json.load(open('seed/data.json'))
    for k, v in data.iteritems():
        for item in v:
            psql("""select bq_insert('{}', '{}'::json)""".
                 format(
                     k,
                     sql_escape(json.dumps(item))),
                 db=BEDQUILT_EXAMPLE)

    print ">> Done"

if __name__ == '__main__':
    main()

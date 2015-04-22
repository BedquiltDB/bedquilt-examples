# BedquiltDB Webapp Example

## Requirements

- PostgreSQL >=9.4, with a database called `bedquilt_example`
- Python 2.7
- pybedquilt, flask

## Setting up the database

Create a database:
```
CREATE DATABASE bedquilt_example;
```

Then connect to the database and enable the extension:
```
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION bedquilt;
```

See the getting-started guide here: http://bedquiltdb.readthedocs.org


## Running The Server

```
$ python server.py
```
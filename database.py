from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text, URL
from db_auth import load_db_auth

db_user, db_pass = load_db_auth()
drivername = 'mysql+pymysql'
host = 'aws.connect.psdb.cloud'
port = '3306'
database = 'joviancareers'

db_connection_string = "{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8mb4".format(drivername, db_user, db_pass, host, port, database)


# sqlalchemy connect to mysql
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": ".dbcert.pem"
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id=:val"),
            {'val':id}
        )

        for row in result.all():
            if row is not None:
                return row
            else:
                return None
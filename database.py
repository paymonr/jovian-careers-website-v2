from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://tw9lruclmicne8zqfur1:pscale_pw_qHba2MMYxcB0X4YPT0w8Thtq2alvvBA0wTGQcb4CKmy@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4'

# sqlalchemy connect to mysql
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        
        return jobs
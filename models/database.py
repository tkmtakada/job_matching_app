# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import socket

if 'ec2' in socket.gethostname():  # EC2, USE MySQL
    engine = create_engine('mysql://admin:cteam_pass@db-instance.ciaelricvhfz.us-east-1.rds.amazonaws.com/matching', convert_unicode=True)
else:  # LOCAL USE SQLite  
    db_path =os.path.join(os.path.abspath(os.path.dirname(__file__)), 'matching.db')
    engine = create_engine('sqlite:///' + db_path, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# ==========================
#  EXCUTE THE COMMAND BELOW
# from models.database import init_db
# init_db()
# ==========================

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)

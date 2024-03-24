from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://dbuser:ldxrJfmAE68oYsMKqKhcQwSeXh4Kevgc@dpg-cnv1g4ljm4es73dpa26g-a.oregon-postgres.render.com/dbname_3s0u"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
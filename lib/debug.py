#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

# Create engine
engine = create_engine('sqlite:///seed_db.db')

# Bind Base metadata (makes sure tables exist)
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

#!/usr/bin/env python3

from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()


c1 = Company(name="Google", founding_year=1998)
c2 = Company(name="Amazon", founding_year=1994)

d1 = Dev(name="Alice")
d2 = Dev(name="Bob")

f1 = Freebie(item_name="Sticker Pack", value=5, dev=d1, company=c1)
f2 = Freebie(item_name="T-Shirt", value=20, dev=d2, company=c2)
f3 = Freebie(item_name="Mug", value=15, dev=d1, company=c2)

session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()
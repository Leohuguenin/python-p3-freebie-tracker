from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    
    # A company has many freebies
    freebies = relationship("Freebie", backref="company")

    # Company has many devs THROUGH freebies
    devs = relationship("Dev",
                        secondary="freebies",
                        viewonly=True)

    def __repr__(self):
        return f'<Company {self.name}>'
    
     # Give a freebie to a dev
    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()
        return new_freebie

    # Class method to find the oldest company
    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    
     # A dev has many freebies
    freebies = relationship("Freebie", backref="dev")

    # Dev has many companies THROUGH freebies
    companies = relationship("Company",
                             secondary="freebies",
                             viewonly=True)

    def __repr__(self):
        return f'<Dev {self.name}>'
    
      # Check if dev has received a specific item
    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

    # Give away a freebie to another dev
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()
            return True
        return False
    
class Freebie(Base):
    __tablename__= 'freebies'
    
    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    
    dev_id = Column(Integer, ForeignKey("devs.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    
    
    def __repr__(self):
        return f'<Freebie {self.name}>'
    
      # Aggregate method
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."

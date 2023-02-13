#!/usr/bin/python3
""" this is declaretie_base"""

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

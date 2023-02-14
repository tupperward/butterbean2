from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WelcomeMessages(Base):
    __tablename__ = "welcome_messages"
    
    id = Column(Integer, primary_key = True),
    serverDescription = Column(String, CheckConstraint("channelId==None"),CheckConstraint("channelMessage==None"),CheckConstraint("emoji==None")),
    channelId = Column(Integer, CheckConstraint('serverDescription==None')),
    channelMessage = Column(String, CheckConstraint('serverDescription==None')),
    emoji = Column(String, CheckConstraint('serverDescription==None'))

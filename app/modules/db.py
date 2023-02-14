from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint, create_engine, select
from sqlalchemy.orm import declarative_base, Session, selectinload

Base = declarative_base()
engine = create_engine("sqlite+pysqlite:///memory")

class WelcomeMessages(Base):
    __tablename__ = "welcome_messages"
    
    id = Column(Integer, primary_key=True)
    serverDescription = Column(String, CheckConstraint("channelId IS NULL"), CheckConstraint("channelMessage IS NULL"), CheckConstraint("emoji IS NULL"))
    channelId = Column(Integer, CheckConstraint('serverDescription IS NULL'))
    channelMessage = Column(String, CheckConstraint('serverDescription IS NULL'))
    emoji = Column(String, CheckConstraint('serverDescription IS NULL'))

async def getWelcomeDataByChannelId(channelId):
    async with Session(engine) as session:
        channelData = await session.query(WelcomeMessages).filter_by(channelId=channelId).first()
    return channelData

async def upsertWelcomeMessage(channelId, serverDescription=None, channelMessage=None, emoji=None):
    async with Session(engine) as session:
        message = await session.execute(select(WelcomeMessages).filter_by(channelId=channelId))

        if message:
            # update the existing row
            message.serverDescription = serverDescription
            message.channelMessage = channelMessage
            message.emoji = emoji
        else:
            # insert a new row
            message = WelcomeMessages(channelId=channelId, serverDescription=serverDescription, channelMessage=channelMessage, emoji=emoji)
            session.add(message)

        await session.commit()
        await session.refresh(message)

        return message
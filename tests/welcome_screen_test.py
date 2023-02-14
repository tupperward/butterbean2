import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.modules.db import WelcomeMessages, Base
from app.modules.db import getAllChannels, getWelcomeDataByChannelId, upsertWelcomeMessage, getServerDescription, upsertServerDescription

# create an engine and a sessionmaker for a test database
engine = create_engine('sqlite:///db/test_database.db')
Session = sessionmaker(bind=engine)

class TestORMFunctions(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)

    async def test_upsert_welcome_message(self):
        channelId = 1234
        channelMessage = 'Test channel message'
        emoji = 'Test emoji'

        # insert a new row
        message = await upsertWelcomeMessage(channelId, channelMessage, emoji)
        self.assertEqual(message.channelId, channelId)
        self.assertEqual(message.channelMessage, channelMessage)
        self.assertEqual(message.emoji, emoji)

        # update the existing row
        channelMessage = 'Updated channel message'
        emoji = 'Updated emoji'
        message = upsertWelcomeMessage(channelId, channelMessage, emoji)
        self.assertEqual(message.channelId, channelId)
        self.assertEqual(message.channelMessage, channelMessage)
        self.assertEqual(message.emoji, emoji)

    async def test_getWelcomeDataByChannelId(self):
        channelId = 1234
        channelMessage = 'Test channel message'
        emoji = 'Test emoji'

        # insert a new row
        message = WelcomeMessages(channelId=channelId, channelMessage=channelMessage, emoji=emoji)
        with Session(engine) as session:
            session.add(message)
            session.commit()

        # retrieve the row
        message = await getWelcomeDataByChannelId(channelId)
        self.assertIsNotNone(message)
        self.assertEqual(message.channelId, channelId)
        self.assertEqual(message.channelMessage, channelMessage)
        self.assertEqual(message.emoji, emoji)
    
    async def test_serverDescription(self):
        serverDescription = 'Test Server Description'
        message = upsertServerDescription(serverDescription)
        sd = getServerDescription()
        self.assertEqual(message.serverDescription, serverDescription)
        self.assertEqual(sd, serverDescription)
            

if __name__ == '__main__':
    unittest.main()

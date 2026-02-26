from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
bot = ChatBot(
    'SimpleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot with English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
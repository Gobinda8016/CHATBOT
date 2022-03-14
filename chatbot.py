from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Creating ChatBot Instance
chatbot = ChatBot('EDOC')

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("data/data.yml")
trainer.train("data/symptoms.yml")
trainer.train("data/illness.yml")

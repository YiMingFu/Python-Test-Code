# -*- coding: utf-8 -*-
from chatterbot import ChatBot
# 构建ChatBot并指定
bot = ChatBot(
   'Default Response Example Bot',
   logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'},{'import_path': 'chatterbot.logic.LowConfidenceAdapter','threshold': 0.65,'default_response': '很抱歉，我还在学习中，还不'}],
   trainer='chatterbot.trainers.ListTrainer')

# 手动给定一点语料用于训练
bot.train([
  'How can I help you?',
  'I want to create a chat bot',
  'Have you read the documentation?',
  'No, I have not',
  'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'])
#给定问题并取回结果
question = 'How do I make an omelette?'
print(question)
response = bot.get_response(question)
print(response)
print("\n")
question = 'how to make a chat bot?'
print(question)
response = bot.get_response(question)
print(response)

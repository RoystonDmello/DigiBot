import os 
from keras.models import load_model
import cv2 
import numpy as np
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

TOKEN = 'Insert token given by BotFather here'

logging.basicConfig(format = '%(asctime)s - %(name)s -%(levelname)s -%(message)s)', level =logging.INFO)

model = load_model('mnist_model.h5')

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def process(bot, update):
	chat_id = update.message.chat_id

	bot.sendMessage(chat_id,'Processing...')

	pic = '%d.jpg' % (chat_id)

	file_id = update.message.photo[-1].file_id
	fileobj = bot.getFile(file_id)
	fileobj.download(pic)

	img = cv2.imread(pic,0)
	img = cv2.resize(img,(28,28), interpolation = cv2.INTER_AREA)
	img = cv2.adaptiveThreshold(img,255.0,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
	img = img/255.0
	img = img.reshape(1,1,28,28)
	pred = model.predict_classes(img) 

	os.remove(pic)

	bot.sendMessage(chat_id,'The digit is %d yo !' %(pred))

start_handler = CommandHandler('start', lambda bot, update: bot.sendMessage(update.message.chat_id,
	'Hi, I\'m DigiBot. Send me images of digits and I\'ll tell you which digit it is' ))

message_handler = MessageHandler(Filters.photo, process)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
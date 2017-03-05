# DigiBot
Simple telegram bot for digit recognition made for fun. 

This is my first bot so any kind of criticism will be appreciated.
It uses a pretrained keras LeNet-5 model trained on the MNIST dataset.

Since it's a digit recognition bot, it will fail for characters and even numbers.

It's not trained on natural scenes so it fails whenever the background overwhelms the digit.

Obtain a bot token from the BotFather and add it's value to the TOKEN variable, afterwhich running the file will activate the bot and it can be used on Telegram. 

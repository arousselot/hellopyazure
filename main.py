
from microsoftbotframework import MsBot
from tasks import *

bot=MsBot()
bot.add_process(echo_response)


if __name__=='__main__':
    bot.run()

#from flask import Flask

#app=Flask(__name__)

#@app.route("/")
#def hello():
#	return "Hello, World!"

#if __name__=="__main__":
#	app.run()
from microsoftbotframework import ReplyToActivity
# import aibot as ai
# import dbLoad as dbload

# db_crf = dbload.load_db('crf')
# db_wwmd = dbload.load_db('wwmd')
# dbs = [db_crf, db_wwmd]


def echo_response(message):
    if message["type"]=="message":
        # answer=ai.get_response(message["text"], message["from"]["name"],dbs)
        ReplyToActivity(fill=message,text="hello world!").send()
        


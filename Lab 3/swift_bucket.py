from celery import Celery

app = Celery('celeryApp',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')

@app.task
def count_pronouns(jsonfile, ):	
	
    

for line in sys.stdin:
    if len(line) != 1:
        try:
            each_tweet = json.loads(line)
        except:
            continue
        word_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
        word_count = {}
        if not each_tweet['retweeted']:
            text = each_tweet['text'].lower()
            for eachword in word_list:
                if eachword in text:
                    print('%s\t%s' % (eachword, 1))
            print('%s\t%s' % ('unique',1))
                
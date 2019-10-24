from celery import Celery
import json
import time

app = Celery('celeryApp', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def count_pronouns(tweets_file, word_list):
	with open(tweets_file,'r') as my_file:
		total_lines = (line.rstrip() for line in my_file) # All lines read
		total_lines = (line for line in total_lines if line) #Non blank lines that have tweets
		for line in total_lines:
			each_line = json.loads(line)
			if not each_line['retweeted']: #check that tweet is not a retweet
				word_list['TOTAL_UNIQUE_TWEETS'] +=1
				tweet_content = each_line['text'].upper()
				for eachPronoun in word_list.keys():
					word_list[eachPronoun] += tweet_content.count(eachPronoun)
		time.sleep(1) #to make asynchronous calls of celery workers to be synchronous
		return word_list

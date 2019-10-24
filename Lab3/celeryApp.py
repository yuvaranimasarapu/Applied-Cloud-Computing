from celery import Celery
import json

app = Celery('celeryApp', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def count_pronouns(tweets_file, word_list):
	with open(tweets_file,'r') as my_file:
		total_lines = my_file.readlines()
		for line in total_lines:
			try:
				each_line = json.loads(line)
				if not each_line['retweeted'] and each_line['text']: 
					#check that tweet is not a retweet
					word_list['total'] +=1
					tweet_content = each_line['text'].upper()
					for eachPronoun in word_list.keys():
						word_list[eachPronoun] += tweet_content.count(eachPronoun)
			except:
				continue
		return word_list

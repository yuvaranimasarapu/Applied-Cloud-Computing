from celery import Celery
import json

app = Celery('celeryApp', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def count_pronouns(tweets_file, word_list):
	with open(tweets_file,'r') as my_file:
		total_lines = my_file.readlines()
		for line in total_lines:
			try:
				total_lines = total_lines.rstrip() 
				#removing blank lines between consecutive tweets in our file
				each_line = json.loads(line)
				if not each_line['retweeted']: 
				#check that tweet is not a retweet
					word_list['total'] +=1
					tweet_content = each_line['text'].upper()
					for pronoun in word_list.keys():
						word_list[pronoun] += tweet_content.count(pronoun)
			except:
				continue
		return word_list
from flask import Flask,jsonify
from tasks import count_pronouns
import os
import time
from functools import reduce

app = Flask(__name__)

word_list = {'HAN':0 , 'HON':0 , 'DEN':0 , 'DET':0 , 'DENNA':0 , 'DENNE':0 , 'HEN':0, 'total':0}

@app.route ('/pronounsCount/', methods =['GET'])
def get_wordList():
	temp = []
	for eachfile in os.listdir('Lab3'):
		temp.append(count_pronouns(('/home/ubuntu/Applied-Cloud-Computing/Lab3/data' + eachfile), word_list))
	time.sleep(10)
	return jsonify(appendWords(temp))

def appendWords(temp):
	def map_words_count(final_list_words, temp_list):
		for pronoun,count_p in temp_list.items():
			final_list_words[pronoun] = final_list_words.get(pronoun,0) + count_p
		return final_list_words

	return reduce(map_words_count,temp,{})

if __name__ == '__main__':
	app.run(host ='0.0.0.0', debug = True )
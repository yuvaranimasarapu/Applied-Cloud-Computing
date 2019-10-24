from flask import Flask,jsonify
from celeryApp import count_pronouns
import os
import time
from functools import reduce

app = Flask(__name__)

word_list = {'HAN':0 , 'HON':0 , 'DEN':0 , 'DET':0 , 'DENNA':0 , 'DENNE':0 , 'HEN':0, 'total':0}

@app.route ('/pronounsCount/', methods =['GET'])
def get_wordList():
	temp = []
	for every_file in os.listdir('/home/ubuntu/data/'):
		temp.append(count_pronouns(('/home/ubuntu/data/' + every_file), word_list))
	time.sleep(10)
	return jsonify(appendWords(temp))

def appendWords(temp):
	def reducer(accumulator, element):
		for key, value in element.items():
			accumulator[key] = accumulator.get(key,0) + value
		return accumulator

	return reduce(reducer, temp, {})

if __name__ == '__main__':
	app.run(host ='0.0.0.0', debug = True )

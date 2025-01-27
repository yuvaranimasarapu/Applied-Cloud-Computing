from flask import Flask,jsonify
from celeryApp import count_pronouns
import os
from functools import reduce

app = Flask(__name__)

word_list = {'HAN':0 , 'HON':0 , 'DEN':0 , 'DET':0 , 'DENNA':0 , 'DENNE':0 , 'HEN':0, 'TOTAL_UNIQUE_TWEETS':0}

@app.route('/pronounsCount/', methods =['GET'])
def get_wordList():
	temp = []
	for every_file in os.listdir('data'):
		temp.append(count_pronouns(('/home/ubuntu/Applied-Cloud-Computing/Lab3/data/' + every_file), word_list))
	return jsonify(appendWords(temp))

def appendWords(temp):
	def func_reduct(accumulator, element):
		for key, value in element.items():
			accumulator[key] = accumulator.get(key,0) + value
		return accumulator

	return reduce(func_reduct, temp, {})

if __name__ == '__main__':
	app.run(host ='0.0.0.0', debug = True )

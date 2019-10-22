from flask import Flask,jsonify
from tasks import count_pronouns
import os
import time
from functools import reduce

app = Flask(__name__)

pronounCount = {'HAN':0 , 'HON':0 , 'DEN':0 , 'DET':0 , 'DENNA':0 , 'DENNE':0 , 'HEN':0, 'total':0}

@app.route (’/ getResult /’, methods =[ ’GET ’])
def getPronouns () :
queueResults = []
for eachfile in os . listdir (’data ’) :
queueResults . append ( countTweets (( ’/ home / ubuntu / data /’+ eachfile ) ,
pronounCount ))
time . sleep (10)
return jsonify ( combineLists ( queueResults ))

def combineLists ( queueList ):
def reducer ( accumulator , element ):

for key , value in element . items () :
accumulator [ key ] = accumulator . get ( key , 0) + value
return accumulator

return reduce ( reducer , queueList , {})

if __name__ == ’__main__ ’:
app . run ( host =’0.0.0.0 ’, debug = True )

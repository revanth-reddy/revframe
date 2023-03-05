import os
from time import sleep

import requests
from flask import Flask, request, abort, jsonify, send_from_directory, flash, redirect, url_for
from flask_cors import CORS
from model.model import textmodel

api = Flask(__name__)
CORS(api)


"""
import threading

# Sample Multi threading Concept:

def targetMethod(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
    return

@api.route('/multithreadroute/')
def multithreadmethod():
    # start threads
    commands_thread = threading.Thread(target=targetMethod, name="execute commands", args=[arg1, arg2, arg3])
    commands_thread.start()
    # return something even before completion of the above targetMethod
    return "some response"
"""

@api.route('/model/<input_text>', methods=['GET'])
def model(input_text):
    # running some python command to run the model
    # os.system('python3 model/model.py --test_arg=himodel')
    
    output = textmodel(input_text)
    return output

    # prints response of model in terminal
    return "Ok from model. see reponse in terminal"

@api.route('/test/', methods=['GET'])
def test():
    return "hi"

if __name__ == "__main__":
    api.run(debug=True)
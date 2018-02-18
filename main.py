# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import random

from flask import Flask
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

hamster_ask = Ask(app, "/hamster")

logging.getLogger("flask_ask").setLevel(logging.INFO)

greetings = open("greetings.txt").readlines()
sentences = open("sentences.txt").readlines()

sentences = open("hamster_sentences.txt").readlines()



@app.route('/')
def hello():
    return 'Hello World!'

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

@ask.launch
def random_tricky_word_sentence():

    random_sentence = random.choice(sentences)
    msg = "<speak>"
    msg += "<s>%s!</s>" % random.choice(greetings)
    msg += "<s>Please write down the following sentence: %s.</s>" % random_sentence
    msg += "<s>I repeat: <emphasis level='strong'>%s.</emphasis></s>" % random_sentence
    msg += "</speak>"

    return statement(msg)

@ask.intent("YesIntent")
def sentence():
    return statement("""
    <speak>
        ok, one more time: <emphasis level='strong'>The circulating air turbines were full of muffins</emphasis>
    </speak>
    """)

@ask.intent("NoIntent")
def sentence():
    return statement("ok.")

@hamster_ask.launch
def random_hamster_sentence():

    random_sentence = random.choice(hamster_sentences)
    msg = "<speak>"
    msg += "<s>%s!</s>" % random.choice(greetings)
    msg += "<s>Please write down the following sentence: %s.</s>" % random_sentence
    msg += "<s>I repeat: <emphasis level='strong'>%s.</emphasis></s>" % random_sentence
    msg += "</speak>"

    return statement(msg)


if __name__ == '__main__':
    app.run(debug=True)


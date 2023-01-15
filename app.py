from flask import Flask, render_template, request


app = Flask(__name__)
from picture import chatgpt

@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
@app.route('/story',methods = ['post'])
def insert():
    if request.method == 'POST':
        prompt = request.form['prompt']
        #var = []
        print(prompt)
        story_response = chatgpt(prompt)
        final_story = story_response[0]
        print(final_story)
        url_list = story_response[1]
        title = story_response[2]
        print(url_list)
        return render_template('result.html', story = final_story, url1 = url_list[0], url2 = url_list[1],url3 = url_list[2], title_name = title) 
        
        
    
"""
@app.route('/home',methods = ['post','get'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Coming Soon to Theaters':
            pass # do something
        elif request.form['submit_button'] == 'Top movies':
            pass # do something else
        elif request.form['submit_button'] == 'Popular Streaming movies':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('movies_get.html')"""


if __name__ == "__main__":
    
    app.run(debug=True)
    
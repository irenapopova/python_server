from flask import Flask, render_template, url_for

app = Flask(__name__)
#print(__name__)

#print (url_for('static', filename='favicon.ico'))
@app.route('/') #anytime the browser requests
def my_home():
    print (url_for('static', filename='favicon.ico'))
    return render_template('./index.html')

@app.route('/about.html') #
def about():
    return render_template('about.html')

@app.route('/work.html') #
def work():
    return render_template('work.html')


@app.route('/favicon.ico') #
def blog():
    return ""

@app.route('/blog') #s
def blog3():
    return "These are my thoughts on my blog"

@app.route("/blog/2023/dogs") #
def blog2():
    return "This is my dog  "
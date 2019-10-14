from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "<h1> Vamos Kannan! </h1>"

@app.route('/about')
def about():
	return "<h1> This is the web app created by Kannan. Lots to come. </h1>"

@app.route('/user/<name>')
def user(name):
	return f"<h1> Hola! Mi amor {name}!!!"

if __name__ == '__main__':
    app.run(debug=True)

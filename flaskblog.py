from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h4>Hello Bay Ridge World!</h4>"

#@app.route("/about")
#def about():
#    return "<h2>This is about your mom</h2>"
## Test Language ##

if __name__ == '__main__':
	app.run(debug=True)

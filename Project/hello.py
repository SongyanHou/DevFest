from flask import Flask, jsonify, render_template, request 
#Flask always wants for string
import requests

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/name111') #URL, static route
def newname():
	return "Name: Songyan Hou"

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url="https://api.github.com/search/repositories?q=" + request.form["user_search"]
		#url = "https://api.github.com/search/repositories?q=" + search_query
		response_dict=requests.get(url).json()#python dictionary
		return jsonify(response_dict)#return a string
	else:
		return render_template("search.html")

@app.route("/add/<x>/<y>")
def add(x,y):
  return str(int(x)+int(y))

@app.errorhandler(404)
def page_not_found(error):
	return "Songyan: Sorry, page is not found"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
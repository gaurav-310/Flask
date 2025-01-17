from flask import Flask


app = Flask(__name__)



@app.get('/')
def index():
	return {"hello" : "this is the root folder"




}

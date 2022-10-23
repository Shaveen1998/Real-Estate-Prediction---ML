from flask import Flask
app = Flask(__name__)

#routes
@app.route('/')
def get_location_names():
    return('Hello')

if __name__== "__main__" :
    app.run( debug=True )
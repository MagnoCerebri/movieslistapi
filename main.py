from flask import Flask, jsonify,send_file
app = Flask(__name__)

@app.route('/')
def startpage():
    return 'API for my movie streaming application'

@app.route('/movie')
def movielist():         
    return send_file('movies.json')

if __name__ == "__main__":
    app.run()

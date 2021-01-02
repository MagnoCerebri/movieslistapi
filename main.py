from flask import Flask, jsonify,send_file
app = Flask(__name__)
@app.route('/')
def movielist():         
    return send_file('movies.json')

if __name__ == "__main__":
    app.run()

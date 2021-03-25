from flask import Flask, jsonify,send_file
app = Flask(__name__)
@app.route('/')
def start():
    return "Home page for my movie streaming app api"
@app.route('/isaac')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "/TechnoJoJo.jpg"
    return send_file(path, as_attachment=True)
@app.route('/tec')
def download():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "/Isaac.jpg"
    return send_file(path, as_attachment=True)

@app.route('/movies')
def movielist():         
    return send_file('movies.json')

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify,send_file
import json
app = Flask(__name__)

@app.route('/')
def movielist():         
    return send_file('movies.json')



@app.route('/search/<string:query>')
def query(query):
    with open("movies.json") as jsondata:
        items = json.load(jsondata)
        def search_name (name):
            for keyval in items["movies"]:
                if name.lower() in keyval['name'].lower():
                    return keyval
        if (search_name(query) != None):
            result={"movies":[
                search_name(query)
                 ]
                }
            return jsonify(result)
        else:
            return jsonify("Movie is not found")

    
    




if __name__ == "__main__":
    app.run()

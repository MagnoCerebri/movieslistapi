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
        initial={"movies":[]}
        
        def search_name (name):
            for keyval in items["movies"]:
                if name.lower() in keyval['name'].lower():
                    initial["movies"].append(keyval)
                    
            

   
    search_name(query)
    return initial
                    
       

    
    




if __name__ == "__main__":
    app.run()

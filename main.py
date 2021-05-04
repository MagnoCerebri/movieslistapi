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
        num=1
        initial={}
        initial[num]=[]
        
        
        for keyval in items["movies"]:
                if query.lower() in keyval['name'].lower():
                    if len(initial[num])==11:
                        num=num+1
                        initial[num]=[]
                        initial[num].append(keyval)
                    else:
                        initial[num].append(keyval)
                    
            

   
    
    return initial
                    
       

    
    




if __name__ == "__main__":
    app.run()

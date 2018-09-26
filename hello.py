from flask import Flask, Response, jsonify
import datastructure

app = Flask(__name__)

@app.route("/<id>", methods=['GET', 'POST'])
def hello(id):
    #user = datastructure.get_user_by(id)

    #conver user object to json
    #return json

    return jsonify({
        "name": "brian",
        "age": 12
    })
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
     return jsonify({'name':'Jimit',
                    'address':'India'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
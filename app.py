#!flask/bin/python
from watson_developer_cloud import ToneAnalyzerV3
from flask import Flask, jsonify

app = Flask(__name__)

try :
    tone_analyzer = ToneAnalyzerV3(
    username='5b55cac9-1576-4669-ac69-c1d8358c0015',
    password='ec0wKSjOyZb1',
    version='2016-09-20')
except:
    print('Tone analyzer credentials failed.')
    logging.exception(time.strftime("%c")+ ". " + 'Tone analyzer credentials failed. Traceback:')

@app.route('/sku/api/v1.0/retrieve', methods=['GET'])
def update_sku():
    print("SKU number is:" + " " + payload['name'])
    response = tone_analyzer.tone(text=payload['comment'])
    print("Comment analyzed and saved sucessfully!")
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
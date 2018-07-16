from flask import Flask, request, send_from_directory, jsonify, render_template, send_file
from model import process
import glob, os

app = Flask(__name__, static_url_path='')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def root():
  print 'test'
  print glob.glob(os.path.join('dist','*'))
  return send_file('dist/index.html')

@app.route('/run', methods=['POST'])
def run_model():
  data = request.get_json()
  filepath = data.get('path', 'test.txt')
  params = data.get('params', {})
  return jsonify(process.run(filepath,**params))

@app.route('/listfiles', methods=['GET'])
def listfiles():
  files = [os.path.basename(fl) for fl in glob.glob('data/*')]
  return jsonify(files)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=1101)

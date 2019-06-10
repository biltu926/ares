import json
from flask import Flask, render_template

import config
from web.resolver import resolver

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload_data():
    ''' Upload the CSV file to the storage'''

@app.route("/download", methods=['POST'])
def download_result():
    ''' Download the REQ data'''

@app.route("/req", methods=['GET'])
def compute_replenishment_order():
    ''' Compute the REQ'''
    #return render_template('home.html', resolver=resolver.ares_resolver.resolver_replenishment_order())
    return resolver.ares_resolver.resolver_replenishment_order()

if __name__ == '__main__':
    app.run(debug=True)
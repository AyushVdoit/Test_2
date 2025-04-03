from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)


@app.route('/scrape', methods=['GET'])
def index():
    print("REACHED")
    try:
        urls = request.args.get('url')
        # if not urls:
        #     return jsonify({"error": "Missing URL parameter"}), 400
        
        resp = requests.get(urls)
        html_doc =  BeautifulSoup(resp.content,'html.parser')

        data = {}
        count = 0
        for link in html_doc.find_all('a'):
            href = link.get('href')
            if "http" in href:
                count += 1
                data[f"link:{count}"] = href

        if len(data) == 0:
            return jsonify({"message":"No link found in the website","link_data":data}), 200

        return jsonify({"link_data":data}), 200
    except Exception as e:
        return jsonify({"error":f"something went wrong: {e}"}),500


    # resp = requests.get("https://www.tutorialspoint.com/")
    # return "Task Master"




if __name__ == "__main__":
    app.run(debug=True)
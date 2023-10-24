import uuid
import threading
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
# Dictionary to store crawled data (for simplicity, we use an in-memory dictionary)
crawled_data = {}
# Lock to ensure thread safety when accessing crawled_data
crawled_data_lock = threading.Lock()

# Function to crawl a URL and extract data
def crawl_url(url, identifier):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        # Extract the date if available on the website
        date_element = soup.find("time", {"data-testid": "timestamp"})
        date = date_element["datetime"] if date_element else None
        content = str(soup)
        result = {
            "title": title,
            "date": date,
            "url": url,
            "content": content
        }
        with crawled_data_lock:
            crawled_data[identifier] = result
    else:
        return {}

# Endpoint to schedule URLs for crawling
@app.route("/schedule", methods=["POST"])
def schedule_url():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Generate a unique identifier for this crawl job
    identifier = str(uuid.uuid4())
    # Start a new thread for crawling the URL
    thread = threading.Thread(target=crawl_url, args=(url, identifier))
    thread.start()
  
    return jsonify({"identifier": identifier})

# Endpoint to retrieve results for a scheduled URL
@app.route("/results/<identifier>", methods=["GET"])
def get_results(identifier):
    with crawled_data_lock:
        result = crawled_data.get(identifier)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Result not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

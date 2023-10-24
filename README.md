# Web Crawler with Flask

This is a web crawler application implemented with Python and Flask. It allows users to schedule URLs for crawling and retrieve the results, including the title, date, URL, and content of the crawled web pages.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Scheduling URLs for Crawling](#scheduling-urls-for-crawling)
  - [Retrieving Crawl Results](#retrieving-crawl-results)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Schedule multiple URLs for crawling without blocking incoming requests.
- Retrieve crawl results, including title, date, URL, and content.
- Handles concurrent crawling with multithreading.

## Getting Started

### Prerequisites

- Python 3
- Flask
- BeautifulSoup
- requests

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kartikeynick/web-crawler.git

2. Change into the project directory:
    ```bash
   cd src

3. Install the required Python packages:
    ```bash
    pip install Flask BeautifulSoup4 requests


### Usage

## Scheduling URLs for Crawling

- To schedule a URL for crawling, make a POST request to the /schedule endpoint with the URL you want to crawl. The API will return a unique identifier for the crawl job.

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"url": "http://"your-website"}' http://127.0.0.1:5000/schedule

- This command schedules the crawling of "your-website" and returns a JSON response with an identifier, like this:

  ```json
  {"identifier": "your-identifier"}
  ```

## Retrieving Crawl Results

- To retrieve the results of a scheduled crawl, make a GET request to the /results/<identifier> endpoint, where <identifier> is the unique identifier provided when scheduling the URL.

  ```bash
  curl http://127.0.0.1:5000/results/your-identifier

### Examples 

Here are some Examples of the websites you can use:

- [bbc news] (https://www.bbc.com/news)
- [The New York Times](https://www.nytimes.com/)
- [CNN] (https://www.nytimes.com/)
  
### Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or additional features.

### License

License under [MIT-License](https://www.mit.edu/~amini/LICENSE.md)

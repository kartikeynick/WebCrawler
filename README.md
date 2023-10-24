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
  curl -X POST -H "Content-Type: application/json" -d '{"url": "http://"<your website's name>"}' http://127.0.0.1:5000/schedule

- This command schedules the crawling of "<your website>" and returns a JSON response with an identifier, like this:

  ```bash
  {"identifier": "your-identifire"}


  ```bash
  curl http://127.0.0.1:5000/results/d042aaf5-9ecb-4e64-9927-72c3b2a53f84


  



``` bash

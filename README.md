# Welcome to My Imdb Api
***

## Task
Create a backend app with a light web framework. (For python we recommand to use flask.)
It will listen on port 8080.

All your routes will answer in JSON format!

You don't need to create a database, just parse the provided CSV.

Your backend will serve six routes:

GET on / This route will parse the GET parameter genre, to be able to filter by movie genre.

## Description
You will create a backend API to allow a user to search for a movie search by genre.
What is a backend? and what is an API?
These two questions might require some googling to grasp the concepts before starting the project. :-)

We will provide you with a CSV file.
This file contains more than one thousand movie titles. One of the columns marks the genre for each movie.

Your backend will receive a requested genre and will only serve movies with the corresponding genre.
Example:
The client requests all Action movies.
Your backend should parse the CSV, filter by the genre `Action and reply with a list of Action movies, while also respecting the HTTP protocol.

For this project you will be able to use a framework to take care of the HTTP communication protocol.

## Installation
pip install flask

## Usage
python app.py 
```
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:8080/ (Press CTRL+C to quit)
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar Silicon Valley</a></i></span>
<span><img alt='Qwasar Silicon Valley Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>

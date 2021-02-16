from flask import Flask, make_response
from waitress import serve
import os 

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = make_response("{\"language\": \"python\", \"content\": \"Hello, World!\"}")
    response.headers["Content-Type"] = "application/json" 
    return response

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  serve(app, port=port)
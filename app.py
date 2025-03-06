from flask import Flask, render_template
import random

app = Flask(__name__)

jokes = [
    "🚀 Why do DevOps engineers prefer Kubernetes? Because it orchestrates their life!",
    "🔥 Why did the server break up with the database? Too many connections!",
    "🤖 Why don’t programmers like nature? It has too many bugs!",
    "💻 Why do DevOps engineers love automation? Because manual work is a failure pipeline!"
]

@app.route('/')
def home():
    joke = random.choice(jokes)
    return f"<h1>Welcome to DevOps Fun!</h1><p>{joke}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


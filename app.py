import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "⚠️ High CPU or Memory usage detected! Please scale up your resources."
    return jsonify(cpu=cpu_percent, memory=mem_percent, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

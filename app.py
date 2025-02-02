from flask import Flask, request, jsonify
from ziwei_calculator import calculate_ziwei  # 引入算法

app = Flask(__name__)

@app.route('/ziwei', methods=['POST'])
def ziwei_api():
    data = request.json
    name = data.get("name")
    birthdate = data.get("birthdate")
    hour = int(data.get("hour"))

    result = calculate_ziwei(name, birthdate, hour)
    return jsonify(result)

@app.route("/")
def home():
    return "Hello, this is your improved Ziwei API running on Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


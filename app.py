from flask import Flask, request, jsonify
from flask_cors import CORS  # ⭐ 新增這一行，允許 CORS

app = Flask(__name__)
CORS(app)  # ⭐ 這行讓 WebSim 可以存取 API

@app.route('/ziwei', methods=['POST'])
def ziwei_api():
    try:
        data = request.json
        name = data.get("name")
        birthdate = data.get("birthdate")
        hour = int(data.get("hour"))

        result = {
            "name": name,
            "mingGong": f"第 {hour} 宮",
            "mainStar": "紫微",
            "liuNian": f"流年運勢：{hour} 宮",
            "fortune": "大吉",
            "loveLuck": "順遂",
            "lifeExpectancy": "85 歲"
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return "Hello, this is your Flask API running on Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

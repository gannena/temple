from flask import Flask, request, jsonify
from flask_cors import CORS  # 新增 CORS 支援
from ziwei_calculator import calculate_ziwei
from ziwei_database import save_ziwei_result, get_all_results

app = Flask(__name__)
CORS(app)  # 允許跨域請求

@app.route('/ziwei', methods=['POST'])
def ziwei_api():
    data = request.json
    name = data.get("name")
    birthdate = data.get("birthdate")
    hour = int(data.get("hour"))

    result = calculate_ziwei(name, birthdate, hour)
    result["birthdate"] = birthdate  # 儲存生日資訊
    result["hour"] = hour  # 儲存時辰資訊

    # 儲存到數據庫
    save_ziwei_result(result)

    return jsonify(result)

@app.route('/history', methods=['GET'])
def history():
    results = get_all_results()
    return jsonify(results)

@app.route("/")
def home():
    return "Hello, this is your improved Ziwei API running on Render with a Database!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

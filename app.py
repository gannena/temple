from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# 紫微斗數排盤 - 簡易邏輯
stars = ["紫微", "天機", "太陽", "武曲", "天同", "廉貞", "天府", "太陰", "貪狼", "巨門", "天相", "天梁"]
si_hua = ["化祿", "化權", "化科", "化忌"]

@app.route('/ziwei', methods=['POST'])
def calculate_ziwei():
    data = request.json
    name = data.get("name")
    birthdate = data.get("birthdate")
    hour = int(data.get("hour"))

    # 計算命宮（簡化版）
    birth_year = datetime.strptime(birthdate, "%Y-%m-%d").year
    ming_gong = (birth_year + hour) % 12
    main_star = stars[ming_gong]

    # 四化星影響
    hua = random.choice(si_hua)

    # 隨機運勢
    fortune = random.choice(["大吉", "吉", "平", "凶", "大凶"])
    loveLuck = random.choice(["順遂", "波折", "桃花旺", "爛桃花", "穩定"])
    lifeExpectancy = f"{random.randint(70, 100)} 歲"

    result = {
        "name": name,
        "mingGong": f"第 {ming_gong} 宮",
        "mainStar": main_star,
        "liuNian": f"流年運勢：{random.randint(1, 12)} 宮",
        "fortune": fortune,
        "loveLuck": loveLuck,
        "lifeExpectancy": lifeExpectancy
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

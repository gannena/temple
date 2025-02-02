import random
from datetime import datetime

# 定義紫微斗數的 14 顆主星
stars = ["紫微", "天機", "太陽", "武曲", "天同", "廉貞", "天府", "太陰", "貪狼", "巨門", "天相", "天梁", "七殺", "破軍"]
si_hua = ["化祿", "化權", "化科", "化忌"]

def calculate_ziwei(name, birthdate, hour):
    """
    計算紫微命盤（簡化版）
    """
    birth_year = datetime.strptime(birthdate, "%Y-%m-%d").year

    # 計算命宮（更精準版本應該根據農曆年份）
    ming_gong = (birth_year + hour) % 12  

    # 命宮的主星
    main_star = stars[ming_gong % len(stars)]

    # 決定四化星
    hua = random.choice(si_hua)

    # 生成運勢結果
    result = {
        "name": name,
        "mingGong": f"第 {ming_gong} 宮",
        "mainStar": main_star,
        "liuNian": f"流年運勢：{random.randint(1, 12)} 宮",
        "fortune": random.choice(["大吉", "吉", "平", "凶", "大凶"]),
        "loveLuck": random.choice(["順遂", "波折", "桃花旺", "爛桃花", "穩定"]),
        "lifeExpectancy": f"{random.randint(70, 100)} 歲"
    }

    return result

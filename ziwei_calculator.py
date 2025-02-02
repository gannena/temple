import random
from datetime import datetime

# 紫微斗數 14 顆主星
stars = ["紫微", "天機", "太陽", "武曲", "天同", "廉貞", "天府", "太陰", "貪狼", "巨門", "天相", "天梁", "七殺", "破軍"]

# 四化星
si_hua = ["化祿", "化權", "化科", "化忌"]

# 五行屬性
five_elements = ["金", "木", "水", "火", "土"]

# 根據農曆年的天干對應五行
def get_five_element(year):
    tiangan = "甲乙丙丁戊己庚辛壬癸"
    index = (year - 4) % 10  # 從甲子年開始對應
    element_map = {
        "甲": "木", "乙": "木",
        "丙": "火", "丁": "火",
        "戊": "土", "己": "土",
        "庚": "金", "辛": "金",
        "壬": "水", "癸": "水"
    }
    return element_map[tiangan[index]]

# 計算紫微命盤
def calculate_ziwei(name, birthdate, hour):
    birth_year = datetime.strptime(birthdate, "%Y-%m-%d").year
    ming_gong = (birth_year + hour) % 12  # 命宮
    main_star = stars[ming_gong % len(stars)]
    
    # 決定四化星
    hua = random.choice(si_hua)

    # 根據五行與命宮來決定運勢（降低隨機性）
    five_element = get_five_element(birth_year)
    fortune_map = {
        "金": ["吉", "平", "凶"],
        "木": ["大吉", "吉", "平"],
        "水": ["吉", "平", "大凶"],
        "火": ["大吉", "大凶", "吉"],
        "土": ["吉", "平", "吉"]
    }
    fortune = random.choice(fortune_map[five_element])  # 運勢影響

    # 感情運勢：根據天干五行來影響
    loveLuck_map = {
        "金": ["穩定", "爛桃花", "順遂"],
        "木": ["桃花旺", "波折", "穩定"],
        "水": ["爛桃花", "波折", "順遂"],
        "火": ["桃花旺", "波折", "穩定"],
        "土": ["穩定", "順遂", "桃花旺"]
    }
    loveLuck = random.choice(loveLuck_map[five_element])

    # 依據五行相剋影響壽命
    base_life = random.randint(75, 90)
    life_bonus = 5 if five_element in ["金", "木"] else -5  # 土水火略短
    lifeExpectancy = f"{base_life + life_bonus} 歲"

    result = {
        "name": name,
        "mingGong": f"第 {ming_gong} 宮",
        "mainStar": main_star,
        "liuNian": f"流年運勢：{random.randint(1, 12)} 宮",
        "fortune": fortune,
        "loveLuck": loveLuck,
        "lifeExpectancy": lifeExpectancy
    }

    return result

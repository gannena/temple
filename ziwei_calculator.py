import sqlite3

DB_NAME = "ziwei_data.db"

# 建立數據庫表格
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ziwei_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birthdate TEXT,
            hour INTEGER,
            mingGong TEXT,
            mainStar TEXT,
            fortune TEXT,
            loveLuck TEXT,
            lifeExpectancy TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 儲存命盤結果
def save_ziwei_result(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ziwei_results (name, birthdate, hour, mingGong, mainStar, fortune, loveLuck, lifeExpectancy)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["name"], data["birthdate"], data["hour"], 
        data["mingGong"], data["mainStar"], 
        data["fortune"], data["loveLuck"], data["lifeExpectancy"]
    ))
    conn.commit()
    conn.close()

# 查詢所有紀錄
def get_all_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ziwei_results")
    rows = cursor.fetchall()
    conn.close()
    return rows

# 初始化數據庫
init_db()

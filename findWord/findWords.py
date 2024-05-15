import os
import time
import pyodbc
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数から接続情報を取得
server = os.getenv('DB_SERVER')
port = os.getenv('DB_PORT')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DB_DRIVER')

############################################################################################################

print('------------------------------------------------------------')
print()

# 計測開始
print('Job Start!')
print('Start Time:', time.strftime('%Y/%m/%d %H:%M:%S'))
start_time = time.time()

print()
print('------------------------------------------------------------')
print()

############################################################################################################

print()
print('------------------------------------------------------------')
print()

print('DB Connect start!')

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT={port}'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

print('DB Connect finish!')

print()
print('------------------------------------------------------------')
print()
############################################################################################################

print()
print('------------------------------------------------------------')
print()

print('Query start!')

query = 'SELECT * FROM [患者詳細]'
cursor.execute(query)

unencodable_strings = []
for row in cursor.fetchall():
    string = row[0]
    try:
        string.encode('utf-8')
    except Exception as e:
        unencodable_strings.append((string, e))

for string, error in unencodable_strings:
    print(f'{string} cannot be encoded: {error}')

print('Query finish!')

print('------------------------------------------------------------')
print()

cursor.close()
conn.close()

# 計測終了
end_time = time.time()
execution_time = end_time - start_time
print("Script execution time: {:.2f} seconds".format(execution_time))
print('End Time:', time.strftime('%Y/%m/%d %H:%M:%S'))
print('Good job!')

print()
print('------------------------------------------------------------')

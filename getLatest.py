import sqlite3
import json
import base64
import zlib
from urllib.parse import quote
from datetime import date
conn = sqlite3.connect('solves.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(single_solves)")
columns = cursor.fetchall()
column_names = [column[1] for column in columns]
cursor.execute("SELECT * FROM single_solves ORDER BY id DESC LIMIT 1")
highest_single_solve_row = cursor.fetchone()
row_map = dict(zip(column_names, highest_single_solve_row))
starting_point = row_map['move_times_start_id']
cursor.execute(f"SELECT time FROM move_times WHERE id >= {starting_point}")
sequence = [row[0] for row in cursor.fetchall()]
width = row_map['width']
height = row_map['height']
time = row_map['time'] / 1000
moves = int(row_map['moves'] / 1000)
tps = row_map['tps'] / 1000
scramble = row_map['scramble']
solution = row_map['solution']
short_info = f"{width}x{height} sliding puzzle solved in {time:.3f}s with {moves} moves {tps:.3f} tps\n{scramble}\n{solution}"
print(short_info)
print(str(sequence).replace("[","").replace("]",""))
conn.close()
today = date.today()
print("Today's date:", today)

def encodeURIComponent(string):
    return ''.join(c if c.isalnum() or c in ['-', '_', '.', '~'] else f"%{ord(c):02X}" for c in string)

def compress_array_to_string(input_array):
    json_string = json.dumps(input_array)
    compressed_data = zlib.compress(json_string.encode(), level=9)
    base64_encoded_string = base64.b64encode(compressed_data).decode()
    return encodeURIComponent(base64_encoded_string)
    
print("Short link (no moveTiems, use that if link is too large): https://dphdmn.github.io/betterLeaderboard/?r=" +compress_array_to_string([solution,row_map['tps'],scramble, -1]))
print("MoveTimes accurate: https://dphdmn.github.io/betterLeaderboard/?r=" +compress_array_to_string([solution,row_map['tps'],scramble, sequence]))

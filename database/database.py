import sqlite3
import os
import csv
def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        name TEXT,
                        date TEXT,
                        time TEXT
                    )''')
    conn.commit()
    conn.close()

def mark_attendance(name, date, time):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance WHERE name=? AND date=?", (name, date))
    result = cursor.fetchone()
    if result:
        conn.close()
        return False  
    cursor.execute("INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)", (name, date, time))
    conn.commit()
    conn.close()
    export_to_csv(date);
    return True

def export_to_csv(date):
    filename = f"Attendance/Attendance_{date}.csv"
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance WHERE date = ?", (date,))
    data = cursor.fetchall()
    conn.close()

    os.makedirs("Attendance", exist_ok=True)
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])
        writer.writerows(data)
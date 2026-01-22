import sqlite3
import csv

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS breaches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_name TEXT,
    individuals_affected INTEGER,
    breach_type TEXT,
    breached_info TEXT,
    breach_start TEXT,
    breach_end TEXT,
    state TEXT,
    country TEXT
)
""")

# Open CSV file
with open("breaches.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT INTO breaches (
            entity_name,
            individuals_affected,
            breach_type,
            breached_info,
            breach_start,
            breach_end,
            state,
            country
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row.get("Name_of_Covered_Entity"),
            row.get("Individuals_Affected", 0),
            row.get("Type_of_Breach"),
            row.get("Location_of_Breached_Information"),
            row.get("Breach_Start"),
            row.get("Breach_End"),
            row.get("State"),
            row.get("Country")
        ))

conn.commit()
conn.close()

print("✅ Dataset imported successfully")
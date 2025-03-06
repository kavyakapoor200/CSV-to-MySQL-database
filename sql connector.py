import mysql.connector

# Connect to MySQL using correct settings
db = mysql.connector.connect(
    host="localhost", 
    port=3306,  # MySQL is running on port 3306
    user="Kavya",  # MY MySQL username
    password="Kavya@123",  # MY MySQL password
    database="twitter_data",  # Database I created there
    auth_plugin="mysql_native_password"  #  Explicitly specifying the auth plugin
)

cursor = db.cursor()
print("Connected to MySQL successfully!")

import pandas as pd

# Load CSV file
csv_file_path = r"C:\Users\pc\Documents\SQL Connector\scraped_twitter_data.csv"
df = pd.read_csv(csv_file_path)

#  Rename columns to match MySQL table
df.rename(columns={
    "Username": "username",
    "Bio": "bio",
    "Following Count": "following_count",
    "Followers Count": "followers_count",
    "Location": "location",
    "Website": "website"
}, inplace=True)

# Convert "Not Available" to 0 and Remove Commas as I was having those values in my scrapped data
df["following_count"] = df["following_count"].replace("Not Available", "0").str.replace(",", "").astype(int)
df["followers_count"] = df["followers_count"].replace("Not Available", "0").str.replace(",", "").astype(int)

# Insert data into MySQL
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO profiles (username, bio, following_count, followers_count, location, website) VALUES (%s, %s, %s, %s, %s, %s)",
        (row["username"], row["bio"], row["following_count"], row["followers_count"], row["location"], row["website"])
    )

db.commit()
print(" Data inserted successfully!")

#  Verify the inserted data
cursor.execute("SELECT * FROM profiles LIMIT 12")
for row in cursor.fetchall():
    print(row)

#Close the database connection
cursor.close()
db.close()
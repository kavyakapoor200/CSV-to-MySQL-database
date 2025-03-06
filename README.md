# CSV-to-MySQL-database
# **Twitter Scraper Data Storage in MySQL**  

This project **stores scraped Twitter profile data** into a **MySQL database** using **Python and Pandas**.  

## **🔹 Features**  
✅ Reads scraped **Twitter profile data** from a CSV file.  
✅ Cleans missing values and converts number formats.  
✅ Connects to **MySQL** and inserts the data into a structured table.  
✅ Fetches and displays stored data for verification.  

## **🔹 Setup & Installation**  
1️⃣ Install required Python packages:  
   ```sh
   pip install mysql-connector-python pandas
   ```  
2️⃣ Ensure **MySQL is running** and create a database:  
   ```sql
   CREATE DATABASE twitter_data;
   ```  
3️⃣ Run the script in **VS Code or any Python environment**:  
   ```sh
   python sql_connector.py
   ```  

## **🔹 MySQL Table Structure**  
```sql
CREATE TABLE profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    bio TEXT,
    following_count INT,
    followers_count INT,
    location VARCHAR(255),
    website VARCHAR(500)
);
```

## **🔹 Author**  
👤 **Kavya**  

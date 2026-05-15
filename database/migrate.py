import os
import mysql.connector

def run_migration():
    try:
        config = {'host': os.getenv('DB_HOST'), 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASSWORD'),
                'database': os.getenv('DB_NAME')}
        conn = mysql.connector.connect(**config)
        curse = conn.cursor()
    except Exception as e:
        print("connection failed: ",e)
        return

    curse.execute("CREATE TABLE IF NOT EXISTS _migrations (id INT AUTO_INCREMENT PRIMARY KEY,file_name VARCHAR(255) NOT NULL UNIQUE,executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")

    curse.execute("SELECT file_name FROM _migrations")

    executed_files = {row[0] for row in curse.fetchall()}

    migration_dir = os.path.join(os.path.dirname(__file__),'migration')
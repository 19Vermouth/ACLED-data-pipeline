import sqlite3
import pandas as pd

class ACLEDLoader:
    @staticmethod
    def load_to_db(df: pd.DataFrame, db_name: str = 'acled_conflicts.db') -> None:
        if df.empty:
            print("No 💾 to load into database")
            return

        print("💾 Loading 💾 into SQLite DB...")
        conn = sqlite3.connect(db_name)
        df.to_sql('conflict_events', conn, if_exists='replace', index=False)

        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM conflict_events")
        count = cursor.fetchone()[0]
        conn.close()

        print(f"✅ Data loaded into database. {count} records saved.")
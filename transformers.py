import pandas as pd

class ACLEDTransformer:
    @staticmethod
    def transform_data(df: pd.DataFrame) -> pd.DataFrame:
        print("🔧 Transforming data...")
        if df.empty:
            print("No 💾 to transform")
            return df

        print(f"Data shape: {df.shape}")
        print(f"Available columns: {list(df.columns)}")

        if 'event_date' not in df.columns:
            print("❌ Missing 'event_date' column")
            return df

        df = df.copy()
        df['event_date'] = pd.to_datetime(df['event_date'])

        if 'fatalities' in df.columns:
            df['fatalities'] = pd.to_numeric(df['fatalities'], errors='coerce').fillna(0)
            initial_count = len(df)
            df = df[df['fatalities'] > 0]
            print(f"Filtered to {len(df)} events with fatalities (from {initial_count} total)")
        else:
            print("⚠️ No 'fatalities' column found - keeping all events")

        df['year'] = df['event_date'].dt.year
        print("✅ Data transformation complete.")
        return df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

class ACLEDVisualizer:
    @staticmethod
    def visualize_data(df: pd.DataFrame) -> None:
        if df.empty:
            print("No 💾 to visualize")
            return

        print("📊 Creating visualizations...")
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))

        sns.countplot(data=df, x='year', ax=axes[0])
        axes[0].set_title("Conflict Events by Year")
        axes[0].set_xlabel("Year")
        axes[0].set_ylabel("Number of Events")

        if 'event_type' in df.columns:
            event_counts = df['event_type'].value_counts().head(10)
            event_counts.plot(kind='bar', ax=axes[1])
            axes[1].set_title("Top 10 Event Types")
            axes[1].set_xlabel("Event Type")
            axes[1].set_ylabel("Number of Events")
            axes[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig("acled_analysis.png", dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Visualizations saved as acled_analysis.png")

    @staticmethod
    def map_conflicts(df: pd.DataFrame) -> None:
        if df.empty:
            print("No 💾 to map")
            return

        if 'latitude' not in df.columns or 'longitude' not in df.columns:
            print("❌ Missing latitude/longitude columns for mapping")
            print(f"Available columns: {list(df.columns)}")
            return

        print("🗺️ Generating interactive map...")
        m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
        added_markers = 0

        for _, row in df.iterrows():
            try:
                lat, lon = float(row['latitude']), float(row['longitude'])
                popup_text = f"""
                Date: {row.get('event_date', 'Unknown')}
                Type: {row.get('event_type', 'Unknown')}
                Location: {row.get('location', 'Unknown')}
                Fatalities: {row.get('fatalities', 'Unknown')}
                """
                folium.CircleMarker(
                    location=[lat, lon],
                    radius=max(3, min(row.get('fatalities', 1) / 2, 15)),
                    popup=folium.Popup(popup_text, max_width=300),
                    color='red',
                    fill=True,
                    fillOpacity=0.7
                ).add_to(m)
                added_markers += 1
            except (ValueError, TypeError):
                continue

        m.save("acled_conflicts_map.html")
        print(f"✅ Interactive map saved as acled_conflicts_map.html ({added_markers} markers added)")
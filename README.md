# ACLED Data Pipeline

A modular Python pipeline for **extracting**, **transforming**, **loading**, and **visualizing** conflict data from the [ACLED (Armed Conflict Location & Event Data Project)](https://acleddata.com/) API.  
This project fetches conflict event data for a specified country and time period, processes it, stores it in a **SQLite** database, and generates visualizations, including an **interactive map**.
**Data source: Armed Conflict Location & Event Data Project (ACLED); www.acleddata.com.**

---

## 📚 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#5--usage)
- [Customize Parameters](#-customize-parameters)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features

- **Data Extraction**: Fetches conflict data from the ACLED API for a specified country (default: *India*) and date range (default: *2023*).
- **Data Transformation**: Parses dates and filters events (e.g., only with fatalities).
- **Data Storage**: Loads processed data into a local SQLite database (`acled_conflicts.db`).
- **Visualization**: 
  - Bar charts for conflict events by year and event type using *Matplotlib* and *Seaborn*.
  - Interactive map using *Folium*.
- **Modular Design**: Clean separation of configuration, ETL logic, and visualizations.
- **Error Handling**: Robust handling for API failures and data processing exceptions.

---

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/acled-data-pipeline.git
cd acled-data-pipeline
```
### 2.Set Up a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
``` 
pip install -r requirements.txt
```
If requirements.txt is missing, manually install:
```
pip install requests pandas python-dotenv matplotlib seaborn folium
```
### 4. Configure Environment Variables
1. Copy the example environment file:
```aiignore
cp .env.example .env
```

2.Edit .env and add your ACLED API key and email:
```
ACLED_API_KEY=your_api_key_here
ACLED_EMAIL=your_email@example.com
```
***📝 You can obtain your API key from the ACLED Data Portal.***
### 5. ▶️ Usage
**Run the Full ETL Pipeline**
```
python main.py
```
This will:

1. Test ACLED API connectivity
2. Extract 2023 conflict data for India
3. Transform the data (add year, filter fatalities, etc.)
4. Load it into acled_conflicts.db

Generate:
* acled_analysis.png (bar charts)
* acled_conflicts_map.html (interactive map)
### 🔧 Customize Parameters
* Modify the extract_data method in extractors.py to change the country, date range, or API limit.
* Example: To extract data for Nigeria in 2022, update the call in pipeline.py:
```aiignore
response = self.extractor.extract_data(country="Nigeria", start="2022-01-01", end="2022-12-31")
```
View Outputs:
* Check acled_analysis.png for bar charts.
* Open acled_conflicts_map.html in a browser for the interactive map.
* Query the SQLite database (acled_conflicts.db) using any SQLite client.

### Project Structure
```
acled-data-pipeline/
├── config.py           # Configuration management (API key, email)
├── models.py           # Data models for API response handling
├── extractors.py       # Data extraction from ACLED API
├── transformers.py     # Data transformation pipeline
├── loaders.py          # Data loading to SQLite
├── visualizers.py      # Visualization and mapping components
├── pipeline.py         # Main pipeline orchestrator
├── main.py             # Entry point for running the pipeline
├── .env.example        # Template for environment variables
├── .gitignore          # Git ignore file for sensitive data and outputs
└── README.md           # Project documentation
```
###  Configuration

* Environment Variables: Store your ACLED API key and email in .env. Do not commit .env to Git (it’s ignored by .gitignore).
* Database: The pipeline uses an SQLite database (acled_conflicts.db) by default. Modify db_name in loaders.py to change the database name.
* API Parameters: Adjust country, start, end, and limit in extractors.py for custom data extraction.

###  Dependencies:
1. [x] Python 3.8+
2. [x] requests
3. [x] pandas
4. [x] python-dotenv
5. [x] sqlite3 (included with Python)
6. [x] matplotlib
7. [x] seaborn
8. [x] folium

Install via:
```
pip install requests pandas python-dotenv matplotlib seaborn folium
```
### Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m "Add your feature").
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request on GitHub.
6. Please include tests and update documentation as needed.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

# Hockey Team Stats Scraping 🏒

A Python web scraper that extracts NHL (National Hockey League) team statistics from Hockey Reference website and saves the data in Excel format.

## 📋 Description

This project scrapes real-time NHL team standings and statistics from [Hockey-Reference.com](https://www.hockey-reference.com/) and exports the data to an Excel file for easy analysis.

## 🔧 Technologies Used

- **Python 3.x**
- **Requests** - For making HTTP requests to fetch web pages
- **BeautifulSoup4** - For parsing HTML content
- **Pandas** - For data manipulation and Excel export
- **OpenPyXL** - For writing Excel files
- **html5lib/lxml** - HTML parsers

## 📊 Data Collected

The scraper collects the following NHL statistics:

| Column | Description |
|--------|-------------|
| GP | Games Played |
| W | Wins |
| L | Losses |
| OL | Overtime Losses |
| PTS | Points |
| PTS% | Points Percentage |
| GF | Goals For |
| GA | Goals Against |
| SRS | Simple Rating System |
| SOS | Strength of Schedule |
| RW | Regulation Wins |

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/ShafiqUllah2233/hockey_team_stats_scraping.git
cd hockey_team_stats_scraping
```

2. Install required packages:
```bash
pip install requests beautifulsoup4 pandas openpyxl html5lib lxml
```

## 💻 Usage

Run the scraper:
```bash
python scrape_hockey_stats.py
```

The script will:
1. Fetch data from Hockey Reference website
2. Parse all available tables (Division standings, team stats)
3. Save the data to `hockey_teams_stats.xlsx`

## 📁 Output

The Excel file contains multiple sheets:
- **Table_1**: Atlantic & Metropolitan Division standings
- **Table_2**: Central & Pacific Division standings
- **Table_3**: Detailed team statistics
- **Table_4**: Additional statistics

## 🔍 How It Works

```
1. HTTP Request → Fetch webpage using requests library
2. HTML Parsing → Parse HTML content with BeautifulSoup & html5lib
3. Table Extraction → Extract tables using pandas.read_html()
4. Data Processing → Clean and organize the data
5. Excel Export → Save to .xlsx file using openpyxl engine
```

## 📝 Code Explanation

Here's what the code does step by step:

1. **Imports**: First, all required libraries are imported (requests, BeautifulSoup, pandas)
2. **URL Set**: The Hockey Reference website URL is defined as the data source
3. **HTTP Request**: Using `requests.get()`, the webpage content is fetched from the server
4. **HTML Parsing**: BeautifulSoup parses the raw HTML into a structured format
5. **Table Extract**: `pd.read_html()` extracts all HTML tables from the page
6. **Excel Save**: `pd.ExcelWriter()` saves the extracted data into an Excel file

## 👤 Author

**Shafiq Ullah**

## 📄 License

This project is open source and available for educational purposes.

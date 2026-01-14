import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# URL for NHL standings/stats from Hockey Reference
url = "https://www.hockey-reference.com/leagues/NHL_2025.html"

print("Fetching hockey teams stats...")

try:
    # Send request to the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the standings table
    tables = pd.read_html(StringIO(response.text), flavor='html5lib')
    
    if tables:
        # Get the first few tables (typically standings)
        all_data = []
        
        for i, table in enumerate(tables[:4]):  # Get first 4 tables
            print(f"\nTable {i+1} found with {len(table)} rows")
            all_data.append(table)
        
        # Combine Eastern and Western conference standings if available
        if len(all_data) >= 2:
            # Save each conference separately and combined
            with pd.ExcelWriter('hockey_teams_stats.xlsx', engine='openpyxl') as writer:
                for i, df in enumerate(all_data):
                    sheet_name = f'Table_{i+1}'
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    print(f"Saved {sheet_name} to Excel")
        else:
            # Save single table
            all_data[0].to_excel('hockey_teams_stats.xlsx', index=False, engine='openpyxl')
        
        print("\n✓ Data successfully saved to 'hockey_teams_stats.xlsx'")
        print(f"Location: c:\\Users\\TECHNIFI\\Desktop\\hockey_teams_stats_scraping\\hockey_teams_stats.xlsx")
        
        # Display preview
        print("\n--- Preview of scraped data ---")
        for i, df in enumerate(all_data[:2]):
            print(f"\nTable {i+1}:")
            print(df.head(10).to_string())
    else:
        print("No tables found on the page")
        
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"Error: {e}")

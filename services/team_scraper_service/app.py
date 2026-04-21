from bs4 import BeautifulSoup
import requests

def get_premier_league_clubs():
    """
    Scrapes club names from the Premier League page on Transfermarkt.
    Returns a list of club names.
    """
    url = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1/saison_id/2025'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table with class 'items'
    table = soup.find('table', class_='items')
    
    if not table:
        print("Could not find table with class 'items'")
        return []
    
    # Find all links in cells with class 'hauptlink no-border-links'
    # These cells contain the club names
    club_names = []
    tbody = table.find('tbody')
    if tbody:
        for row in tbody.find_all('tr'):
            # Find the cell with club name (class 'hauptlink no-border-links')
            name_cell = row.find('td', class_='hauptlink')
            if name_cell:
                link = name_cell.find('a')
                if link:
                    club_name = link.get_text(strip=True)
                    club_names.append(club_name)
    
    return club_names


if __name__ == '__main__':
    clubs = get_premier_league_clubs()
    print("Premier League Clubs (2025/26 Season):")
    for club in clubs:
        print(f"{club}")


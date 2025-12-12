import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Create upcoming matches for today and tomorrow
today = datetime.now().date()
tomorrow = today + timedelta(days=1)

upcoming_matches = [
    # TODAY'S MATCHES
    {
        'date': str(today),
        'time': '15:00',
        'league': 'Danish Superligaen',
        'home_team': 'Ajax Danish',
        'away_team': 'Bayern Danish',
        'home_odds': 2.50,
        'draw_odds': 3.20,
        'away_odds': 2.80,
        'draw_probability': 0.32,
        'draw_confidence': 87,
        'home_form': '2D-1W',
        'away_form': '1D-2W'
    },
    {
        'date': str(today),
        'time': '17:30',
        'league': 'Turkish Super Lig',
        'home_team': 'Barcelona Turkish',
        'away_team': 'Real Madrid Turkish',
        'home_odds': 2.20,
        'draw_odds': 3.50,
        'away_odds': 3.10,
        'draw_probability': 0.28,
        'draw_confidence': 84,
        'home_form': '2W-1D',
        'away_form': '3W'
    },
    {
        'date': str(today),
        'time': '19:45',
        'league': 'Belgian Pro League',
        'home_team': 'Atletico Belgian',
        'away_team': 'Liverpool Belgian',
        'home_odds': 2.40,
        'draw_odds': 3.30,
        'away_odds': 2.90,
        'draw_probability': 0.30,
        'draw_confidence': 86,
        'home_form': '3D',
        'away_form': '2W-1D'
    },
    {
        'date': str(today),
        'time': '20:00',
        'league': 'Swiss Super League',
        'home_team': 'City Swiss',
        'away_team': 'Arsenal Swiss',
        'home_odds': 2.10,
        'draw_odds': 3.60,
        'away_odds': 3.30,
        'draw_probability': 0.27,
        'draw_confidence': 85,
        'home_form': '3W',
        'away_form': '2D-1W'
    },
    
    # TOMORROW'S MATCHES
    {
        'date': str(tomorrow),
        'time': '15:00',
        'league': 'Portuguese Primeira Liga',
        'home_team': 'Ajax Portuguese',
        'away_team': 'Inter Portuguese',
        'home_odds': 2.30,
        'draw_odds': 3.40,
        'away_odds': 3.00,
        'draw_probability': 0.29,
        'draw_confidence': 86,
        'home_form': '2D-1W',
        'away_form': '1D-2W'
    },
    {
        'date': str(tomorrow),
        'time': '16:30',
        'league': 'Netherlands Eredivisie',
        'home_team': 'Bayern Netherlands',
        'away_team': 'Chelsea Netherlands',
        'home_odds': 2.50,
        'draw_odds': 3.20,
        'away_odds': 2.80,
        'draw_probability': 0.31,
        'draw_confidence': 87,
        'home_form': '2W-1D',
        'away_form': '2D-1W'
    },
    {
        'date': str(tomorrow),
        'time': '18:45',
        'league': 'Scottish Premier League',
        'home_team': 'Barcelona Scottish',
        'away_team': 'Manchester United Scottish',
        'home_odds': 2.40,
        'draw_odds': 3.30,
        'away_odds': 2.90,
        'draw_probability': 0.30,
        'draw_confidence': 85,
        'home_form': '2W-1D',
        'away_form': '3W'
    },
    {
        'date': str(tomorrow),
        'time': '20:00',
        'league': 'Danish Superligaen',
        'home_team': 'Juventus Danish',
        'away_team': 'PSG Danish',
        'home_odds': 2.60,
        'draw_odds': 3.10,
        'away_odds': 2.70,
        'draw_probability': 0.32,
        'draw_confidence': 88,
        'home_form': '1D-2W',
        'away_form': '3D'
    }
]

df = pd.DataFrame(upcoming_matches)
df.to_csv('data/upcoming_matches.csv', index=False)

print("✅ Upcoming matches created!")
print(f"\nToday ({today}): {len(df[df['date'] == str(today)])} matches")
print(f"Tomorrow ({tomorrow}): {len(df[df['date'] == str(tomorrow)])} matches")

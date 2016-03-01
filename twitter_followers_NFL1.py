
from twitter_followers import get_followers_ids
from twitter_accounts import accounts

NFL1 = ['BuffaloBills', 'MiamiDolphins', 'RealPatriots', 'NYJets',
        '1WinningDrive', 'Bengals', 'OfficialBrowns', 'Steelers',
        'HoustonTexans', 'NFLColts', 'JaguarsInsider', 'TennesseeTitans',
        'Denver_Broncos', 'KCChiefs', 'Raiders', 'Chargers']
NFL2 = ['DallasCowboys', 'Giants', 'Eagles', 'Redskins',
        'ChicagoBearscom', 'DetroitLionsNFL', 'Packers', 'VikingsFootball',
        'Atlanta_Falcons', 'Panthers', 'Official_Saints', 'TBBuccaneers',
        'AZCardinals', 'STLouisRams', '49ers', 'Seahawks']

for team in NFL1:
    get_followers_ids(team, accounts[0])



from twitter_accounts import accounts
from twitter_followers import get_followers_ids

NFL2 = ['DallasCowboys', 'Giants', 'Eagles', 'Redskins',
        'ChicagoBearscom', 'DetroitLionsNFL', 'Packers', 'VikingsFootball',
        'Atlanta_Falcons', 'Panthers', 'Official_Saints', 'TBBuccaneers',
        'AZCardinals', 'STLouisRams', '49ers', 'Seahawks']

for team in NFL2:
    get_followers_ids(team, accounts[1])



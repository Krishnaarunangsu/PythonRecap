import pandas as pd

venue_dict = [{'year': 1998, 'host': 'France', 'winner': 'France'},
              {'year': 2002, 'host': 'South Korea', 'winner': 'Brazil'},
              {'year': 2006, 'host': 'Germany', 'winner': 'Italy'},
              {'year': 2010, 'host': 'South Af4rica', 'winner': 'Spain'},
              {'year': 2006, 'host': 'Brazil', 'winner': 'Germany'}, ]

venues = pd.DataFrame(venue_dict)
# print(venues)
print(venues['winner'])
print(venues[['winner']])

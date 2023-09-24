import pandas as pd

df = pd.read_json('listUsers.json')
user_ids = df['id'].tolist()
print(user_ids)
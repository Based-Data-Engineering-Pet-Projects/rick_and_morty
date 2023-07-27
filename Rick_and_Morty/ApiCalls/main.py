import pandas as pd
import requests




def create_df(results) -> pd.DataFrame:
    df_array = [pd.DataFrame(pd.json_normalize(x)) for x in results]
    return pd.concat(df_array)

character_url = "https://rickandmortyapi.com/api/character/?page=1"

response = requests.get(character_url).json()

character_details = response["results"]

first_page_data = create_df(character_details)


other_pages_data = []
while response["info"]["next"]:
    response = requests.get(response["info"]["next"]).json()
    other_pages_data.extend(response["results"])

all_other_date = create_df(other_pages_data)

frames = [first_page_data, all_other_date]

character_df = pd.concat(frames)

pd.set_option('display.max_columns', None)
print(character_df)
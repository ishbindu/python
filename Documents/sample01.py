a=["1","6","2","7"]
sample_dict = {'key1': 1, 'key2':  2, 'key3': 3}
import pandas as pd
df = pd.DataFrame(list(sample_dict.items()),columns = ['column1','column2']) 
print(df)
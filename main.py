# import pandas as pd
#
# df = pd.read_csv("data.csv", error_bad_lines=False, index_col=0)
# df_clean = df.drop_duplicates()
# df_clean.to_csv('clean_data.csv')

import pandas as pd
import glob

path = r'/Users/prakhar/Workspace/stats_dataset'  # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
df_clean = frame.drop_duplicates()
df_clean.to_csv('clean_data.csv')

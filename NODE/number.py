import pandas as pd
import numpy as np


dfs = pd.read_excel('NODE/box.xlsx',keep_default_na=False, sheet_name=[0], index_col=None)
print(dfs)
dfs.to_excel('1.xlsx', index=False)

# df = pd.concat(dfs)
# # print(df)
# df_data = np.array(df)
# df_data_list = df_data.tolist()
# finall_data = np.array(df_data_list)
# print(finall_data)
# date_frame = pd.DataFrame(finall_data)
# writer = pd.ExcelWriter('1.xlsx', engine='xlsxwriter')
# date_frame.to_excel(writer, sheet_name='1', index=False)
# writer.save()
# df.to_excel('1.xlsx', index=False)
# train_data = np.array(df)
# train_data_list = train_data.tolist()
# print(np.array(train_data_list))

# dateframe = pd.DataFrame(np.array(train_data_list))
# writer = pd.ExcelWriter('1.xlsx', engine='xlsxwriter')
# dateframe.to_excel(writer, sheet_name='1', index=False)
# writer.save()
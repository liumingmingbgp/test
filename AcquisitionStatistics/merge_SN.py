import pandas as pd
import os

folder_path = os.getcwd()
csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
final_sorted_data = pd.DataFrame(data=None)
# for file in csv_files:
for file in csv_files:
    SN = pd.read_csv(file, index_col='SerialNumber')    
   
    final_sorted_data = pd.concat([final_sorted_data, SN])

final_sorted_data.to_excel('./final_sorted.xlsx')
import pandas as pd
import os

folder_path = "C:/Users/liumi/Desktop/Python/Practice/AcquisitionStatistics"
csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
final_sorted_data = pd.DataFrame(data=None)
for file in csv_files:
    battery_status = pd.read_csv(file, index_col='SerialNumber')
    battery_status.sort_values(by='BatteryChargeLevelFinal', inplace=True, ascending=True)
    number = len(battery_status['BatteryChargeLevelFinal'])
    threshold = int((number-1) * 0.05)
    sorted_data = battery_status.head(threshold)
   
    final_sorted_data = pd.concat([final_sorted_data, sorted_data])

final_sorted_data.to_excel('final_sorted.xlsx')
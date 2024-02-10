import pandas as pd
import os

folder_path = r'#PATH_TO_YOUR_FOLDER_WITH_FILES_TO_COMBINE'
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

print(f'Found {len(all_files)} CSV files:')
print(all_files)

data_frames = []

for file in all_files:
    file_path = os.path.join(folder_path, file)
    data = pd.read_csv(file_path)
    data_frames.append(data)
    print(f'Processed {file}')

combined_data = pd.concat(data_frames, ignore_index=True)

output_file_path = os.path.join(folder_path, 'combined_csv.csv')
combined_data.to_csv(output_file_path, index=False)
print(f'Saved combined data to {output_file_path}')

# Ein Modul von Kapitel 7
# K7_data_processing.py

def read_data(file_path):
  with open(file_path, "r") as f:
    data = f.readlines()
  return data

def process_data(data):
  processed = [line.strip() for line in data if line.strip()]
  return processed

def output_results(processed_data, output_file):
  with open(output_file, "w") as f:
    for item in processed_data:
      f.write(f'{item}\n')
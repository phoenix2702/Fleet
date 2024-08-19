import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate synthetic data
def generate_synthetic_data(num_records):
    data = {
        'Engine RPM': [random.uniform(2500, 3500) for _ in range(num_records)],
        'Lub Oil pressure': [random.uniform(2.0, 6.0) for _ in range(num_records)],
        'Fuel pressure': [random.uniform(2.0, 6.0) for _ in range(num_records)],
        'Coolant pressure': [random.uniform(0.5, 1.5) for _ in range(num_records)],
        'Coolant temp': [random.uniform(70, 90) for _ in range(num_records)],
        'Lub oil temp': [random.uniform(70, 90) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Generate synthetic data
num_records = 100  # Adjust the number of records as needed
df = generate_synthetic_data(num_records)

# Save to Excel
excel_file_path = 'InsuranceFrontend/synthetic_engine_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Excel file '{excel_file_path}' created successfully with {num_records} records.")

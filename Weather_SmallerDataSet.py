# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MHFoqWJlyXIu9AyNjb3-mXx8WBi1eAtx
"""

import pandas as pd
import random
from datetime import datetime, timedelta

# Generate random dates for 6 days
start_date = datetime(2024, 3, 1)
dates = [start_date + timedelta(days=i) for i in range(6)]

# Generate random temperature and windspeed data
temperature = [round(random.uniform(30, 80), 1) for _ in range(6)]
windspeed = [round(random.uniform(5, 15), 1) for _ in range(6)]

# Generate random event data
events = ['Rain', 'Sunny', 'Snow']
event = [random.choice(events) for _ in range(6)]

# Create DataFrame
data = {
    'Day': dates,
    'Temperature': temperature,
    'Windspeed': windspeed,
    'Event': event
}

smaller_table = pd.DataFrame(data)

# Save DataFrame to CSV file
smaller_table.to_csv('smaller_table.csv', index=False)

# print("CSV file 'smaller_table.csv' has been created.")


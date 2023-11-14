from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import csv

# Set up Chrome driver
service = ChromeService(executable_path='/Users/sahibk/Documents/3401/ML/archive/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=service)

# Set the URL
url = 'https://www.fifa.com/fifa-world-ranking/men?dateId=id14177'

# Open the URL
driver.get(url)

# Find the table
table = driver.find_element(By.CLASS_NAME, 'table_rankingTable__7gmVl')

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, 'tr')

# List to store country names
countries = []

# Iterate through rows and extract data
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        text = cell.text.strip()  # Remove any extra whitespace
        # Check if the cell has alphabetic characters, assuming country names only have letters and spaces
        if any(char.isalpha() for char in text):
            countries.append(text)
            break  # Once the country name is found in a row, move to the next row

# Close the browser
driver.quit()

# Save to CSV
with open('countries.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country'])  # header
    for country in countries:
        writer.writerow([country])

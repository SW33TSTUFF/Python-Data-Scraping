# PERSONAL PROJECT
import requests
from bs4 import BeautifulSoup
import csv

# Login credentials
login_url = "https://abc/login/index.php"
username = "user"
password = "admin"

# Create a session
session = requests.Session()

# Send a GET request to the login page to retrieve the necessary information
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

# Extract the login form and its input fields
login_form = soup.find('form', id='login')
login_data = {
    "username": username,
    "password": password,
    "logintoken": login_form.find('input', {'name': 'logintoken'})['value']
}

# Send a POST request to the login endpoint with the credentials
session.post(login_url, data=login_data)

# Data for CSV
data = []

# Iterate through the range of IDs
for id in range(344):
    url = f"https://abc/user/profile.php?id={id + 1490}"

    try:
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title_text = soup.title.string.split(':')[0].strip()
        index_number = soup.find('dt', text='Index Number').find_next('dd').get_text()
        registration_number = soup.find('dt', text='Registration Number').find_next('dd').get_text()
        email_address = soup.find('dt', text='Email address').find_next('dd').get_text()


        id_data = url.split('=')[1]

        data.append([id_data, index_number, title_text, registration_number, email_address])
        print(f"Printing ID {id + 1487}: {title_text}")
    except Exception as e:
        print(f"Skipping ID {id + 1487}: {str(e)}")
        data.append([id_data, "User Not Available"])
        continue


with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id Number", "Index Number", "Name", "Registration Number", "Email address"])
    writer.writerows(data)

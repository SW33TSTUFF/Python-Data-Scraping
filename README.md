👋 Welcome to the User Data Scraper!


📝 Description:
This script allows you to scrape user data from a moodle website and save it to a CSV file. It requires an existing account, making the data extraction process smooth and hassle-free.


🔧 Installation:


Clone the repository to your local machine.
Make sure you have Python installed (version 3.6 or above).
Install the required dependencies by running the command pip install -r requirements.txt.

🚀 Usage:


Open the script (dataCollectionTemp.py) in your preferred Python editor.
Enter your login credentials (username and password) in the respective variables: username and password.
Customize the range of IDs to scrape data from by modifying the range function in the for loop.
Run the script by executing the command python scraper.py.
Sit back and relax while the script scrapes user data from the UGVLE website.
Once the scraping process is complete, the extracted data will be saved in a CSV file named output.csv.

📄 CSV Format:
The extracted data will be saved in the following format:


Id Number
Index Number
Name
Registration Number
Email Address

🔒 Privacy and Security:
Please ensure that you have the necessary permissions and adhere to the privacy policies when using this script. Avoid sharing or misusing any scraped data obtained through this tool.


🙏 Acknowledgements:
This script relies on the following libraries:

requests for making HTTP requests
beautifulsoup4 for parsing HTML content
csv for reading and writing CSV files

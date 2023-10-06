from bs4 import BeautifulSoup
import requests

html_txt = requests.get('https://moodlegurukul.nie.ac.in/login/index.php')
print(html_txt)
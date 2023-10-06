import webbrowser

url = 'https://www.google.com/search?q=www.google.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(using='chrome', executable_path=chrome_path).open(url)

history = webbrowser.get(using='chrome', executable_path=chrome_path).history
for i, item in enumerate(history):
    print(f'{i+1}. {item["url"]}')


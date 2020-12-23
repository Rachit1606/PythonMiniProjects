import webbrowser as wb

def webauto():
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    URL = ("stackoverflow.com", "gmail.com","google.com","youtube.com")
    
    for url in URL:
        print("opening : ",url)
        wb.get(chrome_path).open(url)
    

webauto()

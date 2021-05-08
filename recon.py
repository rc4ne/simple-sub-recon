import requests,time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--log-level=3")
options.headless = True
fname = input("Enter the file path(or drag and drop): ")
f = input("Enter the output file name: ")
path = os.getcwd()+"\\"+f
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory {} failed..!".format(path))
else:
    print("Successfully created the output directory..".format(path))
fp = open(fname)
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
for line in fp:
    if line == '\n':
        continue
    else:
        print("\n--------------------------------------------------------------")
        try:
            url = "https://"+line.strip('\n')
            print("Checking with https: ",url)
            x = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception Encountered with https...")
        try:
            url = "http://"+line.strip('\n')
            print("Checking with http: ",url)
            x = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception Encountered with http as well...Moving on to next")
            continue
        print("Status: ",x.status_code)
        driver.get(url)
        print("Capturing screenshot...")
        driver.get_screenshot_as_file("{}\{}_{}.png".format(path,line.strip('\n'),x.status_code))
        print("Saved successfully!")
        driver.quit()
fp.close()

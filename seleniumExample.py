from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME, "q")
# arama kismina yazilacak yazi:
input.send_keys("kodlama.io")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(1)
# arama sonucu cikan ilk websiteye tikliyor
firstResult = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
# firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
cources = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlama.io sitesinde su anda {len(cources)} adet kurs var")
# chrome'un hemen kapanmamasi icin yaziyoruz: input() veya:
# sleep(10) #veya:
while True:
    continue

# full xpath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

# xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

# sitelerden veri kazima gibi islemlere we scraping veya data scraping diyebiliriz

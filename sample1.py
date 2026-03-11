from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

'''Calendar 1'''
calendar = driver.find_element("id","datepicker")
driver.execute_script("arguments[0].scrollIntoView(true);", calendar)
sleep(3)
calendar.click()
sleep(3)

target_date = datetime.strptime("28-March-2027","%d-%B-%Y")

while True:
    month = driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
    year = driver.find_element("xpath","//span[@class='ui-datepicker-year']").text

    current_date = datetime.strptime(f"{month} {year}","%B %Y")

    if current_date.month == target_date.month and current_date.year == target_date.year:
        break

    elif target_date > current_date:
        driver.find_element("xpath","//a[@title='Next']").click()
        sleep(1)

    elif target_date < current_date:
        driver.find_element("xpath","//a[@title='Prev']").click()
        sleep(3)

days = driver.find_elements("xpath","//table[@class='ui-datepicker-calendar']//a")
print(type(target_date.day))

for day in days:
    if day.text == str(target_date.day):
        day.click()
        sleep(3)



'''Calendar 2'''
calendar2 = driver.find_element("id","txtDate")
driver.execute_script("arguments[0].scrollIntoView(true);", calendar2)
sleep(3)
calendar2.click()

month = driver.find_element("xpath","//select[@class='ui-datepicker-month']")
month.click()
sleep(3)
month_options = Select(month)
month_options.select_by_index(2)
sleep(3)

year = driver.find_element("xpath","//select[@class='ui-datepicker-year']")
year.click()
sleep(2)
year_options = Select(year)
year_options.select_by_value("2030")
sleep(2)

driver.find_element("xpath","//a[text()='16']").click()
sleep(3)


'''Calendar 3'''
calendar3 = driver.find_element("id","start-date")
driver.execute_script("arguments[0].scrollIntoView(true);", calendar3)
sleep(3)
calendar3.send_keys("14-02-2026")
sleep(3)



driver.quit()
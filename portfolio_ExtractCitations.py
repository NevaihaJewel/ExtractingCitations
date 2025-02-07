import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# path to chrome driver
chrome_driver = "chrome_driver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver))

# the function to get citation info in the most recent year
def get_citation_data(facility_name):
    # open website
    driver.get("website.com")

    # WEBPAGE 1
    # find search field and input facility name
    search_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_TextBoxPvName") # name input field
    search_field.send_keys(facility_name)
    search_field.send_keys(Keys.RETURN)

    time.sleep(0.1)

    # WEBPAGE 2
    # click select button
    try:
        select_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'DgFacils') and contains(@href, 'Select$0') and text()='Select']"))
        )
        select_button.click()
    except Exception as e:
        print(f"Error selecting facility {facility_name}: {e}")
        return None, 0

    time.sleep(0.1)

    # WEBPAGE 3
    # get the most recent date, extract the year, and click select button
    try:
        survey_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvInspections"))
        )
    except Exception as e:
        print(f"Error finding survey table for {facility_name}: {e}")
        return None, 0

    rows = survey_table.find_elements(By.TAG_NAME, "tr")

    # Select the last row (most recent year)
    if len(rows) > 1:  # Ensure there are rows to select from
        last_row = rows[-1]  # Get the last row
        cells = last_row.find_elements(By.TAG_NAME, "td")
        citation_year = cells[1].text.split('/')[-1] 
        last_row.find_element(By.TAG_NAME, "a").click()  # Click the button in the last row
        time.sleep(0.1)

        # WEBPAGE 4
        # count the number of citations if there are any
        try:
            citation_table = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvDetails"))
            )
            citation_rows = citation_table.find_elements(By.TAG_NAME, "tr")

            total_citations = 0
            if len(citation_rows) > 1:  # Check if there are citation rows
                for citation_row in citation_rows[1:]:  # skip the header row
                    cells = citation_row.find_elements(By.TAG_NAME, "td")
                    if len(cells) > 1:
                        total_citations += 1

            print(f"{total_citations} citations in {citation_year} for {facility_name}") # to verify the right info is being collected
            return citation_year, total_citations
        except TimeoutException:
            print(f"No citations found for {facility_name}.") # when no citations with the facility
            return datetime.now().year, 0
        except Exception as e:
            print(f"Error finding citation table for {facility_name}: {e}")
            return datetime.now().year, 0
    else:
        print(f"No survey results found for {facility_name}.")
        return None, 0

# the function to store the collected info into a new excel sheet
def citations_from_excel(file_path):
    df = pd.read_excel(file_path)
    facility_names = df['FACILITY_NAME'].tolist()
    phone_numbers = df['TELEPHONE'].tolist()
    addresses = df['ADDRESS'].tolist()

    all_data = []
    for i, facility in enumerate(facility_names):
        most_recent_year, total_citations = get_citation_data(facility)
        if most_recent_year:
            all_data.append((facility, addresses[i], phone_numbers[i], total_citations, most_recent_year))
        else:
            all_data.append((facility, addresses[i], phone_numbers[i], 0, None))

    # create dataframe with new data
    new_df = pd.DataFrame(all_data, columns=['Send SMS', 'First Name', 'Address', 'Phone Number', 'Notes', 
                                             'CONTRACT ->', 'CONTRACT <-', 'ALTCS', 'Citations', 'Year', 'Civil Penalty'])
    new_df.to_excel("updated_file.xlsx")

citations_from_excel("source_file.xlsx")

# close browser
driver.quit()
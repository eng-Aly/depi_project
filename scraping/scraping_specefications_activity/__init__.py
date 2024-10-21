# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main(param) :
    def scrape_product_details(url, output_file):
        # Initialize WebDriver
        driver = webdriver.Chrome()
        
        # Open the main product list page
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        
        # Find all "wishlist" buttons to extract product IDs
        wishlist_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.label-wishlist')
        
        # Dictionary to store product IDs and URLs
        product_dict = {}
        
        # Loop through each button to extract product ID and build product URL
        for button in wishlist_buttons:
            onclick_attr = button.get_attribute('onclick')
            product_id = onclick_attr.split('(')[1].split(',')[0]  # Extract the product ID
            product_url = f"https://elshennawy.com/ProductsList/Show?productId={product_id}"
            product_dict[product_id] = product_url
        
        print(product_dict)
        
        # Close the WebDriver after extracting the necessary data
        driver.quit()
        
        # Initialize an empty DataFrame to hold all product data
        all_products_df = pd.DataFrame()
        
        # Loop through each product URL
        for product_id, product_url in product_dict.items():
            response = requests.get(product_url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find the main container with product specifications
                holder = soup.find('div', class_='holder')
                
                if holder:
                    # Find all specification tables
                    tables = holder.find_all('table', class_='table')
                    
                    product_data = []  # Temporary list to store product specs
                    
                    # Loop through each table and extract section headers and key-value pairs
                    for table in tables:
                        section_headers = table.find_all('thead')
                        for section_header in section_headers:
                            section_title = section_header.get_text(strip=True)
                            
                            # Find all rows and extract key-value pairs
                            rows = table.find_all('tr')
                            for row in rows:
                                columns = row.find_all('td')
                                if len(columns) == 2:  # Ensure we have key-value pairs
                                    key = columns[0].get_text(strip=True)
                                    value = columns[1].get_text(strip=True)
                                    product_data.append([product_id, section_title, key, value])
                    
                    # Convert product data into a DataFrame
                    product_df = pd.DataFrame(product_data, columns=['Product ID', 'Section', 'Specification', 'Details'])
                    
                    # Concatenate the product DataFrame with the overall DataFrame
                    all_products_df = pd.concat([all_products_df, product_df], ignore_index=True)
            else:
                print(f"Failed to retrieve the webpage for product ID {product_id}. Status code: {response.status_code}")
        
        # Save all the scraped product data into a CSV file
        all_products_df.to_csv(output_file, index=False)
        return all_products_df
        



    return scrape_product_details("https://www.elshennawy.com/ProductsList?categoryId=1&brandId=2","elshnawy_apple_specs")
    
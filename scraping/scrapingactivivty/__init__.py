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
    
    def scrape_elshennawy_products(url, output_file='elshnawy_apple.csv'):
        # Initialize WebDriver

        
        # Open the webpage using Selenium
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        
        # Send a GET request to the webpage
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all product information containers
            products = soup.find_all('div', class_='prd-info')
            
            # Initialize lists to store product details
            product_names = []
            product_brands = []
            product_storage = []
            product_colors = []
            product_prices_new = []
            product_prices_old = []
            product_savings = []
            product_ids = []
            
            # Iterate through each product
            for product in products:
                # Product name
                name = product.find('h2', class_='prd-title').get_text(strip=True)
                product_names.append(name)
                
                # Brand
                brand = product.find('div', class_='prd-tag').get_text(strip=True)
                product_brands.append(brand)
                
                # Storage
                storage = product.find_all('div', class_='d-block')[0].get_text(strip=True).replace("Storage ", "")
                product_storage.append(storage)
                
                # Color
                blocks = product.find_all('div', class_='d-block')
                color = blocks[1].get_text(strip=True).replace("Color ", "") if len(blocks) > 1 else "N/A"
                product_colors.append(color)
                
                # New Price
                price_new = product.find('div', class_='price-new').get_text(strip=True)
                product_prices_new.append(price_new)
                
                # Old Price
                price_old = product.find('div', class_='price-old').get_text(strip=True) if product.find('div', class_='price-old') else None
                product_prices_old.append(price_old)
                
                # Savings
                savings = product.find('div', class_='price-comment').get_text(strip=True) if product.find('div', class_='price-comment') else None
                product_savings.append(savings)
            
            # Get product IDs using Selenium
            wishlist_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.label-wishlist')
            for button in wishlist_buttons:
                onclick_attr = button.get_attribute('onclick')
                product_id = onclick_attr.split('(')[1].split(',')[0]
                product_ids.append(product_id)
            
            # Create a DataFrame with the collected product data
            df = pd.DataFrame({
                'Product Name': product_names,
                'Brand': product_brands,
                'Storage': product_storage,
                'Color': product_colors,
                'New Price': product_prices_new,
                'Old Price': product_prices_old,
                'Savings': product_savings,
                'ID': product_ids
            })
            
            # Save the DataFrame to a CSV file
            df.to_csv(output_file, index=False)
            print(f"Data saved to {output_file}")
            
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        
        # Close the Selenium driver
        driver.quit()

    return  scrape_elshennawy_products("https://www.elshennawy.com/ProductsList?categoryId=1&brandId=2", output_file='elshnawy_apple.csv')  
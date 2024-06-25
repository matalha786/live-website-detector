import requests
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return url, 'good'
        else:
            return url, 'bad'
    except requests.exceptions.RequestException:
        return url, 'bad'

def check_websites(file_name):
    # Open the input file and read the list of websites
    with open(file_name, 'r') as file:
        websites = file.readlines()

    total_websites = len(websites)
    processed_websites = 0
    start_time = time.time()
    update_interval = 11  # seconds

    # Using ThreadPoolExecutor for concurrent requests
    with ThreadPoolExecutor(max_workers=64) as executor:
        futures = {executor.submit(check_website, website.strip()): website.strip() for website in websites}

        for future in as_completed(futures):
            website_url, result = future.result()
            if result == 'good':
                with open('good.txt', 'a') as good_file:
                    good_file.write(website_url + '\n')
            else:
                with open('bad.txt', 'a') as bad_file:
                    bad_file.write(website_url + '\n')
            
            # Update progress
            processed_websites += 1
            if time.time() - start_time >= update_interval:
                progress_percentage = (processed_websites / total_websites) * 100
                print(f"Progress: {progress_percentage:.2f}%")
                start_time = time.time()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter the name of the file with the list of websites: ")
    
    check_websites(input_file)

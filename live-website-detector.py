import requests
import time
import sys

def check_websites(file_name):
    # Open the input file and read the list of websites
    with open(file_name, 'r') as file:
        websites = file.readlines()

    total_websites = len(websites)
    processed_websites = 0
    start_time = time.time()
    update_interval = 11  # seconds

    # Check each website
    for website in websites:
        website = website.strip()
        try:
            response = requests.get(website)
            if response.status_code == 200:
                with open('good.txt', 'a') as good_file:
                    good_file.write(website + '\n')
            else:
                with open('bad.txt', 'a') as bad_file:
                    bad_file.write(website + '\n')
        except requests.exceptions.RequestException:
            with open('bad.txt', 'a') as bad_file:
                bad_file.write(website + '\n')
        
        # Update the progress
        processed_websites += 1

        # Check if 11 seconds have passed since the last update
        if time.time() - start_time >= update_interval:
            progress_percentage = (processed_websites / total_websites) * 100
            print(f"Progress: {progress_percentage:.2f}%")
            start_time = time.time()  # Reset the timer

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter the name of the file with the list of websites: ")
    
    check_websites(input_file)

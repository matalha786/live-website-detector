# live-website-detector

```
# Website Checker

This Python script checks a list of websites for their availability and logs the results into `good.txt` and `bad.txt` files based on their HTTP response status.

## Features

- Checks each website in the list for HTTP status code 200 (OK).
- Logs working websites into `good.txt`.
- Logs non-working websites or those with other status codes into `bad.txt`.
- Displays progress every 11 seconds while processing.

## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)

## Usage

1. Create a text file (`website_list.txt`) containing the list of websites, with each URL on a new line.
2. Run the script:
   ```
   python check_websites.py website_list.txt
   ```
   If you omit `website_list.txt`, it will prompt you to enter the file name.
3. Monitor progress updates printed to the console every 11 seconds.
4. After execution, check the following files:
   - `good.txt`: Contains URLs of websites responding with HTTP status code 200.
   - `bad.txt`: Contains URLs of websites with non-200 status codes or errors.

## Example

Assume `website_list.txt` contains:
```
https://example.com
https://example.org
https://nonexistent.example
```

Running `python check_websites.py website_list.txt` will produce:
- `good.txt` with `https://example.com` and `https://example.org` (assuming they return 200 OK).
- `bad.txt` with `https://nonexistent.example` (assuming it doesn't exist or returns a non-200 status code).

## Notes

- Make sure `website_list.txt` is accessible and contains valid URLs.
- Depending on the number of websites and their response times, execution may take some time.

## License

This project is licensed under the GLP License - see the [LICENSE](LICENSE) file for details.
```


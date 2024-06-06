# FilesDownloader
A file downloader with options like downloading all files from a webpage or only files with specific extensions

This script uses the `requests` library to fetch web pages and the `BeautifulSoup` library to parse HTML. Additionally, it uses the `urlparse` library to handle URL parsing and constructing.
To use this script, you'll need to install the required libraries if you haven't already:

```bash
pip install requests beautifulsoup4
```

### How to Use the Script
1. Run the script.
2. Enter the URL of the webpage from which you want to download files.
3. Enter the destination folder where you want the files to be saved.
4. Optionally, enter the file extensions you want to download (e.g., `.jpg, .png`). Leave blank to download all files.
5. The script will download the specified files to the destination folder.

This script supports downloading files with specific extensions or all files from a webpage, depending on the user's input

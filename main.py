import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    response = requests.get(url, stream=True)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

def download_files_from_webpage(url, dest_folder, extensions=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    
    files_downloaded = []

    for link in links:
        file_url = urljoin(url, link['href'])
        parsed_url = urlparse(file_url)
        if parsed_url.scheme not in ['http', 'https']:
            continue
        if extensions:
            if any(file_url.endswith(ext) for ext in extensions):
                print(f"Downloading {file_url}...")
                local_filename = download_file(file_url, dest_folder)
                files_downloaded.append(local_filename)
        else:
            print(f"Downloading {file_url}...")
            local_filename = download_file(file_url, dest_folder)
            files_downloaded.append(local_filename)
    
    return files_downloaded

def main():
    url = input("Enter the URL of the webpage: ")
    dest_folder = input("Enter the destination folder: ")
    extensions_input = input("Enter file extensions to download (comma separated, leave blank to download all files): ")
    extensions = [ext.strip() for ext in extensions_input.split(',')] if extensions_input else None
    
    files_downloaded = download_files_from_webpage(url, dest_folder, extensions)
    
    print("Downloaded files:")
    for file in files_downloaded:
        print(file)

if __name__ == "__main__":
    main()

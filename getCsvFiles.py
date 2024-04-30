import os
import boto3
import requests
from bs4 import BeautifulSoup 
DOWNLOAD_URL = os.environ['download_url']
BUCKET_NAME = os.environ['bucket_name']
                  

def get_files_lambda():
    session = boto3.Session(profile_name = 'stockai')
    s3 = session.client('s3')
 
    s3response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='csvfiles/')
    existing_files = [obj['Key'] for obj in s3response.get('Contents', [])]
    #print(existing_files)

    webresponse = requests.get(DOWNLOAD_URL)
    soup = BeautifulSoup(webresponse.text, 'html.parser')
    links = soup.find_all('a')

    files = [link.get('href') for link in links]
    csv_files = list(filter(lambda file: file.endswith('.csv'), files))

    for file in csv_files:
        if f'csvfiles/{file}' not in existing_files:
            download_file = requests.get(f'{DOWNLOAD_URL}/{file}')
            with open(file, 'wb') as f:
                f.write(download_file.content)
            s3.upload_file(file, BUCKET_NAME, f'csvfiles/{file}')
            print(f'Uploaded {file}')
            os.remove(file)

if __name__ == '__main__':
    get_files_lambda()

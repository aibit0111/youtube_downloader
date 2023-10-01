

# import csv
# import os
# from pytube import YouTube

# def download_all_streams(url, directory):
#     youtube = YouTube(url)
#     video_dir = os.path.join(directory, sanitize_filename(youtube.title))
#     os.makedirs(video_dir, exist_ok=True)
    
#     for i, stream in enumerate(youtube.streams.filter(file_extension='mp4').order_by('resolution')):
#         filename = f"{i}_{stream.resolution}.mp4"
#         stream.download(output_path=video_dir, filename=filename)

# def sanitize_filename(filename):
#     return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()

# def read_urls_from_csv(file_path, base_directory):
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
#         for i, row in enumerate(reader):
#             url = row[0]  # Assumes URLs are in the first column
#             video_directory = os.path.join(base_directory, str(i))
#             download_all_streams(url, video_directory)

# read_urls_from_csv(r'D:\Code\youtube_downloader\video_link.csv', r'D:\Code\youtube_downloader\download')  # replace with your CSV file path and base directory
             

import csv
import os
from pytube import YouTube

def download_all_streams(url, directory):
    youtube = YouTube(url)
    os.makedirs(directory, exist_ok=True)
    
    
    for i, stream in enumerate(youtube.streams.filter(file_extension='mp4').order_by('resolution')):
        filename = f"{i}_{stream.resolution}.mp4"
        stream.download(output_path=directory, filename=filename)

def read_urls_from_csv(file_path, base_directory):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for i, row in enumerate(reader):
            url = row[0]  # Assumes URLs are in the first column
            video_directory = os.path.join(base_directory, str(i))
            download_all_streams(url, video_directory)

read_urls_from_csv(r'D:\Code\youtube_downloader\video_link.csv', r'D:\Code\youtube_downloader\download')  # replace with your CSV file path and base directory

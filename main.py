import streamlit as st
from pytube import YouTube


def Downloader(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        asset = youtubeObject.download()
    except:
        print('error')
    print('succesfull')
    with open(asset, 'rb') as file:
        btn = st.download_button(label='Download',
                                 data=file,
                                 file_name='video.mp4',
                                 mime='video/mp4')


link = st.text_input('Place the URL here')
if len(link) > 0:
    Downloader(link)

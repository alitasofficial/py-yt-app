import streamlit as st
import pytube
import os

st.set_page_config(page_title="Video Downloader",
                   page_icon=":film_projector:",
                   layout="wide"
                   )

st.title("Video Downloader")

video_url = st.text_input("Enter the video URL")

if video_url:
    yt = pytube.YouTube(video_url)
    highest_resolution = yt.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    file_name = highest_resolution.default_filename

    try:
        video = highest_resolution.download()
        with open(video, 'rb') as file:
            st.download_button(
                label='Download the video',
                data=file,
                file_name=file_name,
                mime='video/mp4'
            )
            st.write("Downloading...")
            st.success("Video downloaded!")
            os.remove(file_name)
            st.success("Video removed from server!")
    except:
        st.write('error')

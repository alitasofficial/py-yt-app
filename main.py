import streamlit as st
import pytube
import os

st.set_page_config(page_title="Video Downloader",
                   page_icon="🌏",
                   layout="centered")

st.title("Video Downloader")

form = st.form(key='my-form', clear_on_submit=True)
url = form.text_input("Enter the video URL")
submit = form.form_submit_button('Get the video')

if submit:
    yt = pytube.YouTube(url)
    highest_resolution = yt.streams.filter(
        progressive=True,
        file_extension='mp4').order_by('resolution').desc().first()
    file_name = highest_resolution.default_filename
    try:
        video = highest_resolution.download()
        with open(video, 'rb') as file:
            st.success("Video is ready!")
            st.download_button(label='Download the video',
                               data=file,
                               file_name=file_name,
                               mime='video/mp4')
            os.remove(file_name)
    except:
        st.write('error')

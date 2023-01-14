import streamlit as st
import pytube
import os

st.set_page_config(page_title="Video Downloader",
                   page_icon=":film_projector:",
                   layout="wide")

st.title("Video Downloader")

with st.form('my_form'):
    url = st.text_input("Enter the video URL")
    submitted = st.form_submit_button("Submit")
    if submitted:
        yt = pytube.YouTube(url)
        highest_resolution = yt.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').desc().first()
        file_name = highest_resolution.default_filename
        try:
            video = highest_resolution.download()
            with open(video, 'rb') as file:
                st.download_button(label='Download the video',
                                   data=file,
                                   file_name=file_name,
                                   mime='video/mp4')
                st.success("Video is ready!")
                os.remove(file_name)
        except:
            st.write('error')

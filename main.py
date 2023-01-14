import streamlit as st
import pytube

st.set_page_config(page_title="Video Downloader",
                   page_icon=":film_projector:", layout="wide")

st.title("Video Downloader")

video_url = st.text_input("Enter the video URL")

if video_url:
    yt = pytube.YouTube(video_url)
    available_qualities = yt.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().all()
    video_quality = st.selectbox("Select video quality", [
                                 i.resolution for i in available_qualities])
    selected_video = next(
        x for x in available_qualities if x.resolution == video_quality)
    st.write("Downloading...")
    selected_video.download()
    st.success("Video downloaded!")
else:
    st.write("Please enter a video URL")

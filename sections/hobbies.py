import streamlit as st
import os

# Define your genre folders
GENRE_FOLDERS = {
    "Hawk Photography": "photos/Hawk Photography",
    "Paintings": "photos/Paintings",
    "Surfing": "photos/Surfing",
    "Hiking": "photos/Hiking",
    "Wildlife Photography": "photos/Wildlife Photography"
}

def run():
    st.title("🎨 Hobbies")

    # Select genre
    genre = st.selectbox("Choose a Genre", list(GENRE_FOLDERS.keys()))
    folder_path = GENRE_FOLDERS[genre]

    if os.path.exists(folder_path):
        # Collect valid media files
        media_files = sorted([
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov'))
        ])

        index_key = f"{genre}_index"
        if index_key not in st.session_state:
            st.session_state[index_key] = 0

        total_files = len(media_files)
        current_index = st.session_state[index_key]

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 6, 1])
        with col1:
            if st.button("⬅️", key=f"{genre}_prev"):
                if current_index > 0:
                    st.session_state[index_key] -= 1
        with col3:
            if st.button("➡️", key=f"{genre}_next"):
                if current_index < total_files - 1:
                    st.session_state[index_key] += 1

        # Display current media
        selected_file = media_files[st.session_state[index_key]]
        media_path = os.path.join(folder_path, selected_file)

        st.markdown(f"#### {genre} ({st.session_state[index_key]+1} of {total_files})")

        if selected_file.lower().endswith(('.mp4', '.mov')):
            st.video(media_path, start_time=0, width=850)
        else:
            st.image(media_path, width=850)

    else:
        st.warning("This genre folder does not exist.")

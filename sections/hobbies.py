import streamlit as st
import os

# Define genre folders relative to the main repo
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
        media_files = sorted([
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov'))
        ])

        # Create a session state key per genre to maintain separate indexes
        index_key = f"{genre}_index"
        if index_key not in st.session_state:
            st.session_state[index_key] = 0

        total_files = len(media_files)
        current_index = st.session_state[index_key]

        # Navigation arrows
        col1, col2, col3 = st.columns([1, 6, 1])
        with col1:
            if st.button("⬅️"):
                if current_index > 0:
                    st.session_state[index_key] -= 1
        with col3:
            if st.button("➡️"):
                if current_index < total_files - 1:
                    st.session_state[index_key] += 1

        # Display image or video
        selected_file = media_files[st.session_state[index_key]]
        media_path = os.path.join(folder_path, selected_file)

        st.markdown(f"#### {genre} ({st.session_state[index_key]+1} of {total_files})")

        if selected_file.lower().endswith(('.mp4', '.mov')):
            st.video(media_path)
        else:
            st.image(media_path, use_column_width=True)
    else:
        st.warning("This genre folder does not exist.")

import streamlit as st
import os

def run():
    st.markdown("## 📷 Hobbies")

    genre_folders = {
        "Hawk Photography": "photos/Hawk Photography",
        "Paintings": "photos/Paintings",
        "Surfing": "photos/Surfing",
        "Hiking": "photos/Hiking",
        "Wildlife Photography": "photos/Wildlife Photography"
    }

    genre = st.selectbox("Choose Genre", list(genre_folders.keys()))

    if genre:
        folder = genre_folders[genre]
        files = sorted([
            f for f in os.listdir(folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".mp4", ".mov"))
        ])

        if files:
            index = st.session_state.get(f"{genre}_index", 0)

            col1, col2, col3 = st.columns([1, 6, 1])
            with col1:
                if st.button("⬅️ Prev", key=f"{genre}_prev") and index > 0:
                    index -= 1
            with col3:
                if st.button("Next ➡️", key=f"{genre}_next") and index < len(files) - 1:
                    index += 1

            st.session_state[f"{genre}_index"] = index
            file_path = os.path.join(folder, files[index])

            if file_path.lower().endswith((".mp4", ".mov")):
                st.video(file_path)
            else:
                st.image(file_path, use_column_width=True, caption=files[index])

import streamlit as st

def run_hobbies():
    st.title("📸 Hobbies")

    genres = {
        "Hawk Photography": "photos/Hawk Photography",
        "Wildlife Photography": "photos/Wildlife Photography",
        "Surfing": "photos/Surfing",
        "Hiking": "photos/Hiking",
        "Paintings": "photos/Paintings"
    }

    selected_genre = st.selectbox("Choose a Category", list(genres.keys()))

    image_folder = genres[selected_genre]

    # List of valid media files (images + videos)
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.mp4')

    # Hardcoded filenames from your original list, can also use GitHub API for dynamic
    files = [
        f for f in [
            "1.JPG01.mp4", "2.JPG02.mp4", "3.JPG03.mp4", "4.JPG04.mp4", "5.JPG05.mp4"
        ] if f.lower().endswith(valid_extensions)
    ] if "Hawk" in selected_genre else \
    [
        "1.jpg", "01.jpg", "6.jpg", "7.jpg", "15.jpg", "18.jpg", "21.jpg", "22.jpg",
        "23.jpg", "24.jpg", "29.jpg", "30.mp4", "112.JPG", "113.JPG", "114.JPG",
        "115.JPG", "116.JPG", "117.JPG", "118.jpeg"
    ] if "Wildlife" in selected_genre else \
    [
        "1 DSC_0055.JPG", "2 DSC_0059.JPG", "3 bDSC_0277.JPG", "4 DSC_0426.JPG",
        "5 DSC_0780.JPG", "6 DSC_0944.JPG", "7 DSC_0183.JPG", "8 DSC_0423.JPG",
        "8 DSC_0423~2.JPG", "9 DSC_0708.JPG", "10 DSC_0805.JPG", "10 DSC_0805~2.JPG"
    ] if "Surfing" in selected_genre else \
    [
        "1.JPG", "01.JPG", "1.MOV", "2.JPG", "4.JPG", "5.JPG", "6.JPG", "7.jpg", "8.png",
        "9.jpeg", "10.JPG", "11.JPG", "P1010768.JPG", "P1010774.JPG", "P1010800.JPG",
        "P1010825.JPG", "P1010826.JPG", "P1280412.JPG", "P1280426.JPG", "P1280437.JPG"
    ] if "Hiking" in selected_genre else \
    [
        "1.mp4", "2.jpg", "4.jpg", "5.jpg", "11.mp4"
    ]

    # Slideshow HTML
    slides = ""
    for file in files:
        file = file.strip()
        url = f"https://raw.githubusercontent.com/ashz1/ProfilePage/main/{image_folder}/{file.replace(' ', '%20')}"
        if file.lower().endswith(".mp4"):
            slides += f"""
            <div class="mySlides fade">
                <video width="100%" autoplay muted loop controls>
                    <source src="{url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            """
        else:
            slides += f"""
            <div class="mySlides fade">
                <img src="{url}" style="width:100%">
            </div>
            """

    # Embed slideshow
    st.markdown(f"""
    <style>
    .slideshow-container {{
        max-width: 1000px;
        position: relative;
        margin: auto;
    }}
    .mySlides {{
        display: none;
    }}
    .fade {{
        animation: fadeEffect 1.5s;
    }}
    @keyframes fadeEffect {{
        from {{opacity: .4}} 
        to {{opacity: 1}}
    }}
    .prev, .next {{
        cursor: pointer;
        position: absolute;
        top: 50%;
        width: auto;
        margin-top: -22px;
        padding: 16px;
        color: white;
        font-weight: bold;
        font-size: 18px;
        transition: 0.6s ease;
        border-radius: 0 3px 3px 0;
        user-select: none;
        background-color: rgba(0,0,0,0.5);
    }}
    .next {{
        right: 0;
        border-radius: 3px 0 0 3px;
    }}
    </style>

    <div class="slideshow-container">
        {slides}
        <a class="prev" onclick="plusSlides(-1)">❮</a>
        <a class="next" onclick="plusSlides(1)">❯</a>
    </div>

    <script>
    let slideIndex = 0;
    showSlides();

    function plusSlides(n) {{
        showSlides(slideIndex += n);
    }}

    function showSlides(n) {{
        let i;
        let slides = document.getElementsByClassName("mySlides");
        if (!n) {{ slideIndex++; }}
        else {{ slideIndex = n; }}
        if (slideIndex >= slides.length) {{ slideIndex = 0 }}
        if (slideIndex < 0) {{ slideIndex = slides.length - 1 }}
        for (i = 0; i < slides.length; i++) {{
            slides[i].style.display = "none";  
        }}
        slides[slideIndex].style.display = "block";  
        setTimeout(showSlides, 5000);
    }}
    </script>
    """, unsafe_allow_html=True)

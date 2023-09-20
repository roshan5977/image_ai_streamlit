import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="Feuji AI App", page_icon="🤖")

st.image("https://static.wixstatic.com/media/81c9d4_1824e1c1f77a433c8929407f1240f1b2~mv2.png", width=150)
st.title("Compare the images")

logo_html = """

            <div style="display: flex; align-items: center;">

                <img src="https://static.wixstatic.com/media/81c9d4_1824e1c1f77a433c8929407f1240f1b2~mv2.png" alt="Logo" width="200" height="100">

            </div>

            """

# st.markdown(logo_html, unsafe_allow_html=True)

# File upload widgets
st.header("Upload base of Images")
images = st.file_uploader("", type=["jpg", "png"], accept_multiple_files=True)

st.header("Upload image to compare")
single_image = st.file_uploader("", type=["jpg", "png"])

if st.button("Find Matching Images"):
    if not images or not single_image:
        st.warning("Please upload both a base images and a image to compare.")
        # pass
    else:
        # Send images to FastAPI backend for processing
        backend_url = "http://localhost:8000/upload/"  # Replace with your FastAPI server URL
        files = [("images", image) for image in images] + [("single_image", single_image)]
        response = requests.post(backend_url, files=files)

        if response.status_code == 200:
            matching_images = response.json().get("matching_images", [])
            if matching_images:
                st.success("Matching Images Found:")
                for img_url in matching_images:
                    st.image(img_url, use_column_width=True)
            else:
                st.warning("No matching images found.")
        else:
            st.error("An error occurred while processing images.")

    # col1, col2 = st.columns(2)

    # with st.form("my_form"):

    #     with col1:

    #         st.header("Upload List of Images")

    #         uploaders = []

    #         images = st.file_uploader("Upload multiple images", type=["jpg", "png"], accept_multiple_files=True)

    #     with col2:

    #         st.header("Upload List of Images")

    #         single_images = st.file_uploader("Upload multiple images", type=["jpg", "png"], accept_multiple_files=True)

 

 

 

 

# if __name__ == '__main__':

#     main()




    
# def fetch(session, url):

#     try:

#         result = session.get(url)

#         return result.json()

#     except Exception:

#         return {}

 

 

# def main():

#     session = requests.Session()
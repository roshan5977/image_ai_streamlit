import streamlit as st
from PIL import Image
import io
import numpy as np
from streamlit_image_comparison import image_comparison

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
uploaded_images = []

tab1, tab2 = st.tabs(["Base Image", "Upload Image"])

with tab1:
    st.header("Multi-image comparison")
    upload_multiple_images = st.file_uploader("Upload multiple images", type=["jpg", "png"], accept_multiple_files=True)

with tab2:
    st.header("Single-image comparison")
    upload_single_image = st.file_uploader("Upload a single image", type=["jpg", "png"], accept_multiple_files=False)

if st.button("Find Matching Images"):
    if upload_single_image is not None:
        img2_binary = upload_single_image.read()
        for uploaded_file in upload_multiple_images:
            img1_binary = uploaded_file.read()
            if img1_binary == img2_binary:
                st.write("Images Matched");
                st.image(Image.open(io.BytesIO(img1_binary)), caption="Matched Image", use_column_width=True)
                
# tab1, tab2 = st.tabs(["Base Image", "Upload Image"])

# with tab1:
#     st.header("Multi image comparision")
#     upload_multiple_images = st.file_uploader("", type=["jpg", "png"], accept_multiple_files=True)

# uploaded_compare_image = []
# with tab2:
#     st.header("Side by side comparision")
#     upload_single_image = st.file_uploader("", type=["jpg", "png"], accept_multiple_files=False);

# if st.button("Find Matching Images"):
#     for i in range(len(uploaded_images)):
#         img1 = np.array(uploaded_images[i])
#         img2 = np.array(upload_single_image)
#         if image_comparison(img1, img2):
#             st.caption("Images Matched")
                



# if st.button("Find Matching Images"):
#     if not images or not single_image:
#         st.warning("Please upload both a base images and a image to compare.")
#         # pass
#     else:
#         for img in images:
#             image_comparison(img, single_image)
        # Send images to FastAPI backend for processing
        # backend_url = "http://localhost:8000/upload/"  # Replace with your FastAPI server URL
        # files = [("images", image) for image in images] + [("single_image", single_image)]
        # response = requests.post(backend_url, files=files)

        # if response.status_code == 200:
        #     matching_images = response.json().get("matching_images", [])
        #     if matching_images:
        #         st.success("Matching Images Found:")
        #         for img_url in matching_images:
        #             st.image(img_url, use_column_width=True)
        #             image_comparison(img_url, matching_images)
        #     else:
        #         st.warning("No matching images found.")
        # else:
        #     st.error("An error occurred while processing images.")

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
import streamlit as st
import requests
from streamlit_image_comparison import image_comparison
from PIL import Image
from io import BytesIO
import base64

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
# adding tabs
# tab1, tab2 = st.tabs(["Multi image comparision", "Dual image comparision"])
# with tab1:
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
        
        backend_url = "http://localhost:8000/compare/"  # Replace with your FastAPI server URL
        files = [("images", image) for image in images] + [("single_image", single_image)]
        response = requests.post(backend_url, files=files)

        if response.status_code == 200:
            matching_images = response.json().get("matching_images", [])
            if matching_images:
                st.success("Matching Images Found:")
            
                for img_data in matching_images:
                    
                    
                    image_bytes = img_data.get("image_base64",{})
            
                    if image_bytes:
                        image_data = base64.b64decode(image_bytes)

                # Create a PIL Image from the binary data
                    # image = Image.open(BytesIO(image_data))
                
                # Display the image using st.image
                        st.image(image_data, use_column_width=True, caption=img_data["filename"])
                    # print(img_data["filename"],"Image")

            else:
                st.warning("No matching images found.")
        else:
            st.error("An error occurred while processing images.")
# with tab2:
#     image1 = st.file_uploader("", type=["jpg", "png"],key="someName1")
#     image2 = st.file_uploader("", type=["jpg", "png"],key="someName2")
#     if st.button("Compare images"):
#         if image1 is not None and image2 is not None:
#             image_comparison(
#             image1.name,
#             image2.name
#             )
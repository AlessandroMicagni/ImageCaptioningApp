import streamlit as st
from premai import Prem
from PIL import Image

# Set up Prem client with API key
API_KEY = "wnvmT1VFtmCnvnbSTFB7z9F9DN6MmID3i1"  # Replace with your actual API key
PROJECT_ID = "7482"  # Replace with your Project ID

client = Prem(api_key=API_KEY)

# App title
st.title("Image Captioning Assistant with Prem SDK")

# Sidebar: Upload Image
st.sidebar.header("Upload an Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert the image to bytes for Prem SDK
    image_bytes = uploaded_file.read()

    # Generate caption using Prem SDK
    st.write("### Generating Caption...")
    system_prompt = "Describe the image content in one sentence."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Here's an image."},
    ]

    response = client.chat.completions.create(
        project_id=PROJECT_ID,
        system_prompt=system_prompt,
        messages=messages,
        repositories=None,  # Optional: Use RAG repositories for contextual responses
    )

    caption = response.choices[0].message.content
    st.write(f"**Caption:** {caption}")

    # Improvement suggestions
    st.write("### Suggestions for Improvement")
    suggestions = [
        "Make the caption more descriptive.",
        "Ensure all objects in the image are mentioned.",
        "Use captions tailored for specific tasks, like e-commerce."
    ]
    for i, suggestion in enumerate(suggestions, 1):
        st.write(f"{i}. {suggestion}")

import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import os
import traceback
import time

# --- Configuration ---
st.set_page_config(page_title="Image Background Remover", layout="wide")

# --- Constants ---
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_IMAGE_SIZE = 2000  # pixels

# --- Title & Description ---
st.title("Image Background Remover")
st.markdown("""
🐶 **Try uploading an image** to watch the background magically removed.Full quality images can be downloaded from the **sidebar**.This project is [open source on GitHub](https://github.com/Nishanthini09/BackGround_Removal-Using-rembg).Powered by the [rembg library](https://github.com/danielgatis/rembg).  
""")

st.sidebar.header("Upload or Choose a Sample")

# --- Functions ---
def convert_image(img: Image.Image) -> bytes:
    """Convert an image to bytes."""
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    """Resize the image to stay within max dimensions."""
    width, height = image.size
    if width <= max_size and height <= max_size:
        return image
    scale = min(max_size / width, max_size / height)
    return image.resize((int(width * scale), int(height * scale)), Image.LANCZOS)

@st.cache_data
def process_image(image_bytes: bytes):
    """Open, resize, and remove background from the image."""
    try:
        image = Image.open(BytesIO(image_bytes))
        resized = resize_image(image, MAX_IMAGE_SIZE)
        result = remove(resized)
        return image, result
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        return None, None

def display_image_results(original: Image.Image, result: Image.Image, processing_time: float):
    """Show the original and processed images."""
    col1, col2 = st.columns(2)
    col1.subheader("Original")
    col1.image(original, use_column_width=True)

    col2.subheader("Background Removed")
    col2.image(result, use_column_width=True)

    st.sidebar.download_button(
        "⬇️ Download PNG",
        data=convert_image(result),
        file_name="no-background.png",
        mime="image/png"
    )
    st.sidebar.success(f"Done in {processing_time:.2f} seconds ✅")

def fix_image(image_bytes: bytes):
    """Main image processing with progress bar."""
    try:
        start = time.time()
        progress = st.sidebar.progress(10)
        status = st.sidebar.empty()
        status.text("⏳ Processing...")

        original, processed = process_image(image_bytes)
        if original and processed:
            progress.progress(80)
            display_image_results(original, processed, time.time() - start)
            progress.progress(100)
        else:
            st.error("🚫 Failed to process image.")
    except Exception as e:
        st.error("An error occurred during image processing.")
        st.sidebar.error("Check traceback in logs.")
        st.sidebar.code(traceback.format_exc())

# --- Image Upload ---
upload = st.sidebar.file_uploader("Upload PNG, JPG, or JPEG", type=["png", "jpg", "jpeg"])

# --- Optional Samples ---
samples = {
    "🐼 Panda": "panda.jpeg",
    "🦓 Zebra": "zebra.jpeg",
    "🦘 Wallaby": "panda.jpeg"
}

selected_sample = None
if not upload:
    choice = st.sidebar.selectbox("Or choose a sample image", ["None"] + list(samples.keys()))
    if choice != "None":
        selected_sample = samples[choice]

# --- Image Guidelines ---
with st.sidebar.expander("ℹ️ Image Guidelines"):
    st.markdown("""
- Maximum file size: **10MB**  
- Large images will be resized  
- Supported formats: **PNG**, **JPG**, **JPEG**  
- Processing time may vary  
""")

# --- Image Processing Execution ---
if upload:
    if upload.size > MAX_FILE_SIZE:
        st.error("🚫 The uploaded image is too large. Please choose one under 10MB.")
    else:
        fix_image(upload.read())
elif selected_sample and os.path.exists(selected_sample):
    with open(selected_sample, "rb") as f:
        fix_image(f.read())
else:
    st.info("👈 Upload an image or choose a sample to begin.")

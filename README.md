
# Image Background Remover

A simple and effective tool to remove backgrounds from images using [rembg](https://github.com/danielgatis/rembg). Built with Streamlit for a smooth web interface experience.

![demo](![alt text](Output.png))) 

## Features

- 📤 Upload JPG, PNG, or JPEG images
- 🧠 Automatic background removal using AI (rembg)
- 📥 Download high-quality PNGs with transparent backgrounds
- ⚡ Fast processing with image size optimization
- 🐼 Comes with sample images to test

---

## Installation

Clone this repo and set up a virtual environment:

```bash
git clone https://github.com/Nishanthini09/BackGround_Removal-Using-rembg.git
cd BackGround_Removal-Using-rembg
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

---

## Run the App

After installation, start the app using:

```bash
streamlit run app.py
```

It will open a local server in your browser: [http://localhost:8501](http://localhost:8501)

---

## Folder Structure

```bash
.
├── app.py               # Main Streamlit app
├── panda.jpeg            # sample images 
├── zebra.jpeg 
├── Wallaby.jpeg           
├── requirements.txt     # Dependencies
└── README.md            # You're here!
```

---

## Requirements

- Python 3.7+
- rembg
- streamlit
- pillow

Install them using:

```bash
pip install -r requirements.txt
```

---

## Contributing

Pull requests are welcome! If you find a bug or want a feature, feel free to open an issue or submit a PR.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- [rembg](https://github.com/danielgatis/rembg) - for the core background removal magic.
- [Streamlit](https://streamlit.io) - for the interactive UI framework.


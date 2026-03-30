# 🌙 UrduOCR: Advanced Text Extraction & Evaluation Pipeline
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-blueviolet)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A robust, computer-vision-powered Python application for extracting, preprocessing, and evaluating Urdu text from PDFs and images. Built with OpenCV, Tesseract OCR, and advanced error-rate analytics.

## 📋 Overview

UrduOCR tackles the unique complexities of extracting the right-to-left, cursive-style Urdu script from digital documents. It utilizes a custom OpenCV preprocessing pipeline to clean noisy images, leverages Tesseract for text extraction, and automatically calculates Word Error Rate (WER) and Character Error Rate (CER) to grade the model's accuracy against ground-truth data.



## ✨ Key Features

### 👁️ Advanced Image Preprocessing
* **Grayscale Conversion** - Automatically normalizes image color channels.
* **Noise Reduction** - Uses `fastNlMeansDenoising` to clean up low-quality scans or grainy document photos.
* **Contrast Enhancement (CLAHE)** - Applies Contrast Limited Adaptive Histogram Equalization to make faded text pop.
* **Adaptive Thresholding** - Uses Gaussian adaptive thresholding to perfectly separate dark Urdu script from light backgrounds.

### 📝 Intelligent Text Extraction
* **Multi-Format Support** - Seamlessly processes standard images (`.png`, `.jpg`) and multi-page documents (`.pdf`).
* **Specialized Language Parsing** - Configured specifically for Urdu using Tesseract's `urd` language pack with optimized Page Segmentation Modes (PSM 6).
* **Automated Export** - Automatically formats, saves, and downloads the extracted text as a clean `.txt` file.

### 📊 Performance Analytics
* **Word Error Rate (WER)** - Calculates exactly how many words the AI missed or misinterpreted compared to a perfect human translation.
* **Character Error Rate (CER)** - Provides hyper-granular accuracy metrics at the individual character/letter level using the `jiwer` library.

## 🚀 Technology Stack

* **Language:** Python 3
* **Computer Vision:** OpenCV (`cv2`), Pillow (`PIL`)
* **OCR Engine:** Tesseract OCR (`pytesseract`)
* **PDF Processing:** `pdf2image`, `poppler-utils`
* **Evaluation Metrics:** `jiwer`
* **Environment:** Designed for Google Colab / Jupyter Notebooks

## 📦 Installation & Setup

Because this project requires system-level Linux dependencies (like Tesseract language packs and Poppler), it is highly recommended to run this in **Google Colab**.

### Local Setup (Ubuntu/Linux)
If you wish to run this on your local machine, clone the repository first:
```bash
git clone [https://github.com/HamadAliRaza/UrduOCR.git](https://github.com/HamadAliRaza/UrduOCR.git)
cd UrduOCR
```
Install the system dependencies:

```Bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-urd poppler-utils -y
```
Then, install the Python requirements:

```Bash
pip install opencv-python pillow pdf2image pytesseract jiwer
```
## 📖 Usage
1. Prepare Your Files
Have your target Urdu document ready (e.g., Urdu.pdf).

Create a ground_truth.txt file containing the exact, correct Urdu text that should be in the document (this is used to grade the AI).

2. Run the Pipeline
Execute the script. The program will pause and prompt you to upload files via your browser.

Upload your Urdu.pdf when prompted.

The script will preprocess the image, extract the text, and automatically download extracted_urdu_text.txt to your computer.

Keep ground_truth.txt in the same directory (or upload it if running in Colab) so the script can calculate the WER and CER scores.

## 📁 Project Structure
Below is the organized directory layout for the UrduOCR application.

```Plaintext
UrduOCR/
├── UrduOCR_Pipeline.ipynb      # Main Google Colab execution notebook
├── requirements.txt            # Python pip dependencies
├── README.md                   # Project documentation
├── sample_data/                 
│   ├── Urdu.pdf                # Sample input document
│   └── ground_truth.txt        # Sample text for accuracy evaluation
└── output/                      
    └── extracted_urdu_text.txt # Auto-generated OCR result (Example)
```
## 🎓 Learning Outcomes
This project demonstrates proficiency in:

Computer Vision Pipeline Design - Chaining OpenCV filters to optimize images for machine reading.

Natural Language Processing (NLP) Prep - Extracting and structuring non-Latin script data.

System Integration - Combining Python code with Linux-level binaries (poppler, tesseract).

Model Evaluation - Using industry-standard metrics (WER/CER) to quantify system accuracy.

## 🔮 Future Enhancements
Integrate a spell-checker specifically designed for Urdu syntax to correct post-OCR errors.

Build a Streamlit web interface to allow users to upload files and view side-by-side comparisons of the image and extracted text.

Add bounding-box visualization to highlight exactly where the text was found on the original image.

## 👨‍💻 Author
Hamad Ali Raza

GitHub: [@HamadAliRaza](https://github.com/SyedHamadAliRaza714)

Project Link: [UrduOCR Repository](https://github.com/SyedHamadAliRaza714/Urdu-OCR-System)

## 📄 License
This project is open source and available under the MIT License.

## 🙏 Acknowledgments
Built to demonstrate advanced computer vision and data extraction techniques.

Designed to support the digitization and accessibility of the Urdu language.

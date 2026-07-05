# VisionCraft AI

VisionCraft AI is a simple multimodal AI web application that transforms text prompts and rough sketches into high-quality AI-generated images using OpenAI's API.


# Features

-  Generate images from text prompts
-  Upload a rough sketch and generate an improved AI version
-  AI-powered sketch analysis using Vision
-  Download generated images
-  Simple and user-friendly web interface


# Tech Stack

- Python
- Streamlit
- OpenAI API
- Pillow
- python-dotenv


# Project Structure

```
VisionCraftAI/
│
├── app.py
├── config.py
├── image_generator.py
├── vision.py
├── prompt_builder.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── assets/
├── input/
```


#  Installation

### Clone the repository

```bash
git clone https://github.com//VisionCraftAI.git](https://github.com/Shruti-0920/VisionCraftAI.git
```

### Move into the project folder

```bash
cd VisionCraftAI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```


# API Key Setup

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```


# Run the Application

```bash
streamlit run app.py
```


# How It Works

## Text to Image

1. Enter a text prompt.
2. Click **Generate Image**.
3. AI generates a high-quality image.
4. Download the generated image.

## Sketch to Image

1. Upload a rough sketch.
2. AI analyzes the sketch using Vision.
3. The application builds an enhanced prompt.
4. AI generates a polished version of the sketch.
5. Download the generated image.


#  Sample Workflow

```
Text Prompt
      │
      ▼
OpenAI Image Model
      │
      ▼
Generated Image


OR


Upload Sketch
      │
      ▼
Vision Analysis
      │
      ▼
Prompt Enhancement
      │
      ▼
OpenAI Image Model
      │
      ▼
Generated Image
```


# Screenshots


<img width="1124" height="625" alt="image" src="https://github.com/user-attachments/assets/56561248-bb47-45cf-8e1d-b278a119e6b8" />

<img width="1131" height="627" alt="image" src="https://github.com/user-attachments/assets/29ff8a72-3102-4d26-a81c-96a97d51ee0a" />



# Requirements

- Python 3.10+
- OpenAI API Key

---




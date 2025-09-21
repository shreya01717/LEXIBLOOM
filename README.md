# LexiBloom

LexiBloom is a web application designed to assist students with **Dyslexia, ADHD, and Low Vision**. It provides a personalized reading experience and an eye-controlled virtual keyboard to make studying and typing easier and more accessible.

---

## Features

- **Dyslexia-Friendly Reader:** Adjusts text display for easier reading.
- **ADHD Mode:** Helps students focus with interactive tools.
- **Low Vision Mode:** Enhances contrast and font sizes for readability.
- **Eye-Controlled Virtual Keyboard:** Allows hands-free typing using eye movement.
- **Multi-Mode Support:** Switch between Dyslexia, ADHD, and Low Vision modes seamlessly.

---

## How to Run Locally

# 1. Clone the repository
git clone https://github.com/shreya01717/LexiBloom.git
cd lexi


# 2. Set up the backend
cd backend

# Create virtual environment (optional)
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install backend dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py

# 3. Set up and run the frontend
cd ../fronthead1
npm install
npm start



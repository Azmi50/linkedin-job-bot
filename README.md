# 🔄 LinkedIn Job Application Bot

A Python automation bot that applies to LinkedIn jobs using Selenium.

This bot logs into your LinkedIn account, clicks 'Easy Apply' on job listings, fills in your phone number, and skips complex multi-step applications — saving you hours of manual job hunting.

---

## 🚀 Features

- ✅ Automatically logs in to your LinkedIn account
- ✅ Fills in phone number during job applications
- ✅ Skips complex/multi-step application forms
- ✅ Handles cookie rejection automatically
- ✅ Easy-to-edit configuration using `.env` file

---

## 🛠 Tech Stack

- Python 3
- Selenium
- WebDriver Manager
- dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

 ```bash
 git clone https://github.com/yourusername/linkedin-job-bot.git
 cd linkedin-job-bot
 ```
 ### 2. Install Dependencies
bash

pip install -r requirements.txt

### 3. Add Your Credentials
Create a file named .env in the root directory and add your LinkedIn details:

env
LINKEDIN_EMAIL=your_email_here
LINKEDIN_PASSWORD=your_password_here
PHONE_NUMBER=your_phone_number_here
⚠️ Important: Do not share your .env file. It contains sensitive information.

### 4. Run the Bot
python main.py

When prompted with a CAPTCHA on LinkedIn, solve it manually, then press Enter in the terminal to continue.

### ⚠️ Disclaimer
This project is for educational purposes only.
Using automated tools on LinkedIn may violate their Terms of Service, and may lead to account restrictions or bans.
Use at your own risk.

 📬 Author
Khan Adnan
GitHub: Azmi50










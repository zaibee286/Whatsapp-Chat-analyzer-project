# 📊 WhatsApp Chat Analyzer

A simple and powerful **WhatsApp Chat Analyzer** built with Python and Streamlit that lets you extract meaningful insights from your exported WhatsApp chat history.

👉 Export your `.txt` WhatsApp chat and upload it to analyze message trends, statistics, emojis, links and more — all in one place!

---

## 🔍 About The Project

This tool processes WhatsApp chat exports (without media) and gives you useful statistics and visualizations to understand your messaging habits, most active users, word usage and trends over time.

💡 It’s ideal for both **1‑on‑1 chats** and **group chats**.

---

## 🛠 Features

✔️ Count total messages, words, media and links  
✔️ Identify most active users in a group  
✔️ Message timeline (daily/monthly trends)  
✔️ Word frequency and common words  
✔️ Emoji usage statistics  
✔️ Clean and interactive UI using Streamlit

---

## 🚀 Demo

> ⚠️ Live demo not hosted yet — run locally or deploy on Streamlit/Heroku!

---

## 📦 Installation

Make sure you have Python 3.7+ installed.

1. Clone the repository  
```bash
git clone https://github.com/zaibee286/Whatsapp-Chat-analyzer-project.git
```
## ▶️ Usage

- 1 Export your WhatsApp chat as a .txt file:

  WhatsApp → Open a chat → ⋮ menu → More → Export chat → Without Media

- 2 Run the Streamlit app:
  ```bash
  streamlit run app.py
   ```
- 3 Upload your .txt file in the UI and explore the analytics!

## 🧠 How It Works

- The chat file is parsed and cleaned in preprocess.py

- Messages and user data are extracted in helper.py

- The main analytics and UI logic are in app.py
##🧾 Requirements

- See all dependencies in requirements.txt. Major libraries include:

- Streamlit

- Pandas

- Emoji processing

- Visualizations (Matplotlib/Seaborn/Plotly — if used)
## 📁 Project Structure
 ```bash
  Whatsapp-Chat-analyzer-project/
├── app.py
├── helper.py
├── preprocess.py
├── stop_hinglish.txt
├── requirements.txt
├── README.md

 ```
## 📜 License

This project is open‑source and available under the MIT License.


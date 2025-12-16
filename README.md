# 📧 AI Email Generator

Welcome to **AI Email Generator** – your smart assistant to create professional, engaging, and context-aware emails in seconds! Built with Streamlit and OpenAI, this tool helps you generate emails ranging from job applications to quotations, follow-ups, leave requests, and cold emails, all tailored to your preferred tone and length.

---

## 🌟 Key Features

* **AI-Powered Email Generation**: Automatically create polished emails with a clear subject line and well-structured body.
* **Multiple Email Types**: Choose from Job Application, Quotation, Follow-up, Leave Request, or Cold Email.
* **Customizable Tone**: Select Professional, Friendly, or Formal style.
* **Flexible Length**: Generate Short, Medium, or Detailed emails.
* **User-Friendly Interface**: Easily edit, download, or copy generated emails.
* **Instant Productivity**: Save time and maintain consistency across all your professional communications.

---

## 🛠 Technology Stack

* **Python** – core programming language.
* **Streamlit** – interactive and responsive web UI.
* **OpenAI API** – AI engine for generating email content.
* **pyperclip** – seamless copy-to-clipboard functionality.
* **python-dotenv** – manage environment variables securely.

---

## ⚡ Quick Start Guide

Follow these simple steps to get your AI Email Generator up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/Ajuu1801/ai-email-generator.git
cd ai-email-generator
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your OpenAI API Key

* Duplicate `.env.example` to `.env`:

```bash
cp .env.example .env   # Windows: copy .env.example .env
```

* Open `.env` and insert your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Launch the App

```bash
streamlit run app.py
```

> The app interface will open in your default browser, ready to generate emails.

---

## 📦 Dependencies

Ensure the following packages are installed (listed in `requirements.txt`):

```
streamlit
openai
python-dotenv
pyperclip
```

---

## 🖥 How to Use

1. **Select Email Type & Tone**: Choose the type and tone for your email.
2. **Select Length**: Decide if your email should be Short, Medium, or Detailed.
3. **Provide Email Details**: Enter the key points or instructions for your email.
4. **Generate Email**: Click **✨ Generate Email** to create a draft.
5. **Edit & Refine**: Make adjustments in the interface as needed.
6. **Download or Copy**: Download as `.txt` or copy directly to clipboard.

---

## ⚠️ Important Notes

* Make sure your **OpenAI API key** is valid and has sufficient usage quota.
* **Clipboard functionality** relies on `pyperclip` and works across most OS platforms.
* Customize the AI prompt in `app.py` for specialized email styles or formats.

---

## 🌐 Example Use Case

**Input Details:**

```
Write a professional email informing the client that their quotation is ready and include the price list.
```

**Generated Email:**

```
Subject: Quotation Ready for Your Review

Dear [Client Name],

I hope this message finds you well. Your requested quotation is ready for review. Please find the attached price list for your reference.

Feel free to reach out with any questions.

Best regards,
[Your Name]
```

---

## 📚 License

This project is **MIT licensed**, giving you full freedom to use, modify, and distribute it.

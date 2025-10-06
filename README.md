# 💌 SmartMail Automator

> **Automate Gmail emails with a beautiful Python GUI, secure app password authentication, and ready-to-edit templates!**

---

## 🚀 Features

- 🎨 **Modern GUI:** Tkinter interface with dropdowns, color themes, and responsive layout.
- 📋 **Ready-Made Templates:** Meeting Reminders, Thank You Notes, Offer Letters, Follow-Ups, and Custom Messages.
- 🖊️ **Easy Customization:** Edit template placeholders instantly.
- 🔒 **Secure Sending:** Uses Gmail App Passwords stored in `.env` (never raw passwords).
- ⚡ **One-Click Email:** Send emails in seconds, with instant feedback popups.
- ⏩ **Keyboard Shortcuts:**  
  - `Ctrl+Enter` — Send  
  - `Ctrl+L` — Clear

- 🧃 **Bonus-Ready:** Attachments, AI body generation, email scheduling (see [Enhancements](#-bonus-features))!

---

## 🛠️ Setup

### 1️⃣ Clone and Enter Project

```sh
git clone https://github.com/yourusername/smartmail_automator.git
cd smartmail_automator
```

### 2️⃣ Install Dependencies

```sh
pip install python-dotenv
```

### 3️⃣ Configure Gmail App Password

- Go to your [Google Account Security](https://myaccount.google.com/security).
- Enable 2-Step Verification.
- Create an **App Password** for "Mail" and "Windows Computer".
- Add to `.env` file:

```env
GMAIL_ADDRESS=your_gmail_address@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
```

### 4️⃣ Customize Templates

Edit `templates.json` to suit your needs:
```json
{
  "Meeting Reminder": "Hi {name}, ...",
  "Thank You Note": "Dear {name}, ...",
  "Offer Letter": "Dear {name}, ...",
  ...
}
```

### 5️⃣ Run the App

```sh
python main.py
```

---

## 🧑‍💻 Usage

1. 👤 Enter recipient email and subject.
2. 📑 Select a template from the dropdown.
3. 📝 Edit the message body as needed (replace placeholders!).
4. ✅ Click **Send Email** or use `Ctrl+Enter`.
5. 🧹 Use **Clear All** (`Ctrl+L`) to reset fields.
6. ❌ Click **Exit** to close.

---

## 🏆 Why SmartMail Automator?

- 🕒 **Save Time:** No more copying and pasting from old emails.
- 💁 **Professional:** Always send well-formatted, error-free messages.
- 🛡️ **Safe:** Your Gmail credentials are protected.

---

## ⚙️ File Structure

```shell
smartmail_automator/
│
├── main.py               # Main GUI and application logic
├── email_sender.py       # Handles SMTP email composition and delivery
├── templates.json        # Predefined email templates
├── .env                  # Securely stores Gmail credentials
└── README.md             # Documentation
```

---

## 🏅 Bonus Features

- 📎 **Attachment Support:** Send files (see `email_sender.py` for extension).
- ⏰ **Email Scheduling:** Set send times with `apscheduler`.
- 📜 **Send Log:** Track sent emails in `sent_log.csv`.
- 🤖 **AI Smart Templates:** Integrate OpenAI or other APIs for auto-generated email bodies.
- ✨ Simple animations (fade-in success labels).

---

## 🧑‍🤝‍🧑 Contributing

1. Fork the repo 🍴
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request!

---

## 🩺 Troubleshooting

- ❌ **SMTP/auth errors:** Double-check App Password and `.env`.
- ⚡ **No internet:** App needs connectivity for Gmail SMTP.
- ⚠️ **Gmail blocks sign-in:** Make sure 2FA and App Password are set up.
- 💡 **Still stuck?** Check [Google App Password Help](https://support.google.com/accounts/answer/185833).

---

## 📚 Resources

- [Google App Passwords](https://support.google.com/accounts/answer/185833)
- [Python SMTP docs](https://docs.python.org/3/library/smtplib.html)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 💬 Feedback

Questions or suggestions?  
Open an [issue](https://github.com/yourusername/smartmail_automator/issues) or email me at:  
📧 your_gmail_address@gmail.com

---

**Happy Automating!** 🚀  
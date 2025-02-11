# 🚀 Automated Email Sender for HR Applications  

Easily automate job applications by sending personalized emails to recruiters with your resume attached.  

---

## ✨ Features  

- 💼 **Personalized Emails:** Generate customized emails for each recruiter  
- 📎 **Resume Attachment:** Automatically attach your resume to emails  
- 📊 **Excel Integration:** Load recruiter data directly from Excel  
- 🔐 **Secure Credentials:** Keep email credentials safe using `.env`  

---

## ⚙️ Setup  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-repo-url.git
   cd Automated_Email_Sender
   ```  

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Create `.env` File:**  
   Add your credentials securely in a `.env` file:  

   ```env
   SMTP_SERVER=smtp.gmail.com  
   SMTP_PORT=587  
   YOUR_EMAIL=your_email@gmail.com  
   YOUR_PASSWORD=your_app_password  
   ```  

4. **Run the Script:**  
   ```bash
   python main.py
   ```  

---

## 📦 Dependencies  

- `python-dotenv` for environment variable management  
- `pandas` for Excel data handling  
- Built-in `smtplib` for sending emails  

---

## 🚀 Usage  

1. Ensure your Gmail account allows **App Passwords** or less secure app access.  
2. Replace recruiter information in the Excel sheet (`recruiters.xlsx`).  
3. Run the script and watch your applications get delivered effortlessly!  

---

## 🔒 Security Tip  
Always store sensitive information (like email passwords) in the `.env` file and never push it to GitHub. Add `.env` to `.gitignore`.  

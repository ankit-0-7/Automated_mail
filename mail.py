import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")

# Default job title
DEFAULT_JOB_TITLE = "Software Developer"

# Load recruiter data from Excel
def load_recruiter_data(file_path):
    """
    Load recruiter details from an Excel file.
    Expected columns: SNo, Name, Email, Title, Company
    """
    try:
        df = pd.read_excel("recuriter.xlsx")
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Send email to a recruiter with an attachment
def send_email(to_email, subject, body, attachment_path):
    """
    Send an email with an attachment using Gmail's SMTP server.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = YOUR_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Attach the resume file
        with open("FinalRes.pdf", "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_path}",
        )
        msg.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_email} successfully!")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Generate email body from a template
def generate_email_body(name, company_name):
    """
    Generate a personalized email body with a referral request.
    """
    body = f"""
Dear {name},

I hope this message finds you well. My name is Ankit, and I am a final-year student at RNS Institute Of Technology,Bengaluru pursuing Bachelor of Engineering in Artificial Intelligence and Machine Learning. I came across your profile and am excited about the opportunity to connect with you regarding the {DEFAULT_JOB_TITLE} role at {company_name}.

With a strong foundation in software development, I have developed expertise in Python, Java, C++, and system design. I am particularly passionate about solving complex problems and delivering innovative solutions. I believe my skills and experiences align well with the requirements of the {DEFAULT_JOB_TITLE} role at {company_name}.

I have attached my resume for your reference and would love to discuss how I can contribute to your team. If you believe I would be a good fit for this role, I would greatly appreciate a referral from you. Please let me know if there’s any additional information I can provide to facilitate this process.

Thank you for your time and consideration.

Best regards,
Ankit Kumar Sharma
+91 7318560**
linkedin.com/in/ankit***
"""
    return body.strip()

# Main function
def main():
    # Load recruiter data
    file_path = "recruiters.xlsx"  # Replace with your Excel file path
    recruiters_df = load_recruiter_data(file_path)

    # Path to the resume file
    resume_path = "FinalRes.pdf"  # Replace with your resume file path

    if recruiters_df is not None:
        email_count = 0  # Counter to track emails sent
        for index, row in recruiters_df.iterrows():
            name = row["Name"]
            email = row["Email"]
            company_name = row["Company"]  # Use the company name directly from the Excel sheet

            # Generate email subject and body
            subject = f"Application for {DEFAULT_JOB_TITLE} Role "
            body = generate_email_body(name, company_name)

            # Send the email with the attached resume
            send_email(email, subject, body, resume_path)
            email_count += 1

            # Pause after sending 100 emails
            if email_count % 100 == 0:
                print("Pausing for 24 hours to respect Gmail's daily sending limit...")
                time.sleep(86400)  # 24-hour delay

if __name__ == "__main__":
    main()
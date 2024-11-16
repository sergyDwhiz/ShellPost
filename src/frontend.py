import streamlit as st
import requests

st.title("Email Classification and Management")

# Email Classification
st.header("Classify Email")
email_content = st.text_area("Enter email content:")
if st.button("Classify"):
    response = requests.post("http://localhost:5000/emails", json={"content": email_content})
    if response.status_code == 201:
        result = response.json()
        st.write(f"Classification: {result['classification']}")
    else:
        st.write("Error classifying email")

# Send Email
st.header("Send Email")
recipient = st.text_input("Recipient Email")
subject = st.text_input("Subject")
body = st.text_area("Email Body")
attachment_path = st.text_input("Attachment Path (optional)")
if st.button("Send Email"):
    response = requests.post("http://localhost:5000/send-email", json={
        "recipient": recipient,
        "subject": subject,
        "body": body,
        "attachment_path": attachment_path
    })
    if response.status_code == 200:
        st.write("Email sent successfully")
    else:
        st.write("Error sending email")

# Receive Emails
st.header("Receive Emails")
if st.button("Receive Emails"):
    response = requests.get("http://localhost:5000/receive-emails")
    if response.status_code == 200:
        emails = response.json()
        for email in emails:
            st.write(f"From: {email['from']}")
            st.write(f"Subject: {email['subject']}")
            st.write(f"Body: {email['body']}")
            st.write("---")
    else:
        st.write("Error receiving emails")
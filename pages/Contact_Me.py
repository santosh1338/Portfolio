import streamlit as st
from send_email import Send_email

st.header("Contact Me!")

with st.form("form1"):
    user_email = st.text_input("Enter your email address:", placeholder="Your email address")
    old_message = st.text_area("Enter your message:", placeholder="Your message")
    message = f'''\
Subject: New email from {user_email}

From: {user_email}
{old_message}
'''
    button = st.form_submit_button("Submit")
    if button:
        Send_email(message, user_email)
        st.info("Your email was sent successfully!")
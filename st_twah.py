import streamlit as st

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("Transition with a heart")

with st.form("email"):
  sender = "twah.nz.441@gmail.com"
  sender_password = "vnldlgpemvhmfmli "
  subject = "Your Transition With a Heart Request"

  receiver_email = st.text_input("email:")
  receiver_name = st.text_input("name:")
  st.header("I want to talk about:")
  row1 = st.pills("row_1", ["My heart disease", "Operations", "Medication", "Care (skin, teeth...)"], selection_mode="multi", label_visibility='hidden')
  row2 = st.pills("row_2", ["Education", "Leisure and sports", "Relationships", "Something else..."], selection_mode="multi", label_visibility='hidden')
  st.header("I want to talk about this with:")
  row3 = st.pills("row_3", ["My cardiologist", "A psychologist", "My nurse", "Somebody else..."], selection_mode="multi", label_visibility='hidden')

  discuss_topic = row1 + row2
  discuss_with = row3

  submit_button = st.form_submit_button("Send Email")

if submit_button:
  if not receiver_email or not receiver_name:
    st.error("Please add your email and name")
  else:
    body = f"Kia ora {receiver_name}:\n\nYou have chosen to discuss {discuss_topic} with {discuss_with}\n\nSee you at your next appointment!\n\nNgā mihi,\nYour Cardio team"
    print(body)

    try:
      # Set up the MIME message headers
      msg = MIMEMultipart()
      msg['From'] = sender
      msg['To'] = receiver_email
      msg['Subject'] = subject
            
      # Attach the body text
      msg.attach(MIMEText(body, 'plain'))
            
      # Connect to Gmail's SMTP server
      with smtplib.SMTP('smtp.gmail.com', 587) as server:
          server.starttls()  # Secure the connection
          server.login(sender, sender_password)
          server.sendmail(sender, receiver_email, msg.as_string())
                
      st.success("Email sent successfully!")
            
    except Exception as e:
      st.error(f"Failed to send email. Error: {e}")

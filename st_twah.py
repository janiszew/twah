import streamlit as st

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def format_yn(answer):
  mapping = {"yes": "Yes, please spam me", "no": "No, please keep my response confidential"}
  return mapping.get(answer)

st.title("Transition with a heart")

with st.form("email"):
  sender = "twah.nz.441@gmail.com"
  sender_password = "vnldlgpemvhmfmli "
  subject = "Your Transition With a Heart Request"

  receiver_email = st.text_input("email:")
  receiver_name = st.text_input("name:")

  condition = st.selectbox("My condition of interest:",
                           ["Atrial Septal Defect (ASD)",
                            "Ventricular Septal Defect (VSD)",
                            "Patent Ductus Arteriosis (PDA)",
                            "Transposition of the Great Arteries (TGA)",
                            "Coarctation of the Aorta (CoA)",
                            "Hypoplastic Left Heart Syndrome (HLHS)",
                            "Tricuspid Atresia",
                            "Tetralogy of Fallot (ToF)",
                            "Ebstein Anomaly",
                            "I Don't Know (IDK)"])

  verbose = st.radio("Would you like detailed information in your confirmation email?",
                     ["yes",
                      "no"],
                     format_func=format_yn)

  st.header("I want to talk about:")
  discuss_topic = st.pills("topic_row", 
                           ["My heart disorder", 
                            "Operations", 
                            "Mental Health",
                            "Personal care",
                            "Caring for myself as an adult", 
                            "Contraception and pregnancy",
                            "Leisure and sports", 
                            "Relationships", 
                            "Something else..."], 
                           selection_mode="multi",
                           label_visibility='hidden')
  st.header("I want to talk about this with:")
  discuss_with = st.pills("discuss_row", ["My cardiologist", "A psychologist", "My nurse", "Somebody else..."], 
                          selection_mode="multi", label_visibility='hidden')

  submit_button = st.form_submit_button("Send Email")

if submit_button:
  if not receiver_email or not receiver_name:
    st.error("Please add your email and name")
  else:
    if verbose == "yes":
      body = f"Kia ora {receiver_name}:\n\nHere's a summary of what you've requested we cover in your next appointment."
      if "My heart disorder" in discuss_topic:
        body += "\n\nMy Heart:\n\nWe will plan on giving you as much information on your condition as you want, to the best of our abilities!"
        match condition:
          case "Atrial Septal Defect (ASD)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/11622-atrial-septal-defect-asd"
          case "Ventricular Septal Defect (VSD)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/17615-ventricular-septal-defects-vsd"
          case "Patent Ductus Arteriosis (PDA)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/17325-patent-ductus-arteriosus-pda"
          case "Transposition of the Great Arteries (TGA)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/23387-transposition-of-the-great-arteries"
          case "Coarctation of the Aorta (CoA)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/16876-aortic-coarctation"
          case "Hypoplastic Left Heart Syndrome (HLHS)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/12214-hypoplastic-left-heart-syndrome-hlhs"
          case "Tricuspid Atresia":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/14789-tricuspid-atresia"
          case "Tetralogy of Fallot (ToF)":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/22343-tetralogy-of-fallot"
          case "Ebstein Anomaly":
            body += "\n\nThis hospital is top tier, and can be trusted: "
            body += "https://my.clevelandclinic.org/health/diseases/16946-ebsteins-anomaly-for-adults"
      if "Operations" in discuss_topic:
        body += "\n\nOperations:\n\nWe have your back when it comes to any procedures. We can talk about what you need to know, but if you want a checklist to start thinking "
        body += "about what you can do to be ready, here's a great one: https://www.heartkids.org.au/factsheets/hospital-checklist-young-people/"
      if "Mental Health" in discuss_topic:
        body += "\n\nMental Health:\n\nMental health is an important component of managing a condition like this - thanks for letting us know you're interested in learning more. "
        body += "There are counselling resources available, and we will help connect you!"
        body += "\n\nThis podcast may be of interest - it gets into some of the issues faced by young people around medical procedures and mental health: https://www.heartkids.org.au/podcast/carlye-crank/"
      if "Personal care" in discuss_topic:
        body += "\n\nPersonal Care:\n\nEvery case is different, but you are likely not completely and permanently excused from going to the dentist. Just ask the trusted dentists at 'saycheez': "
        body += "https://saycheezdental.com/blog/congenital-heart-disease-and-dental-visits/"
        body += "\n\nIf you're feeling ambitious, here's a very readable technical paper on tattoos and piercings for CHD patients: https://pmc.ncbi.nlm.nih.gov/articles/PMC8748479/"
      if "Caring for myself as an adult" in discuss_topic:
        body += "\n\nCaring for myself as an adult:\n\nStarship, a clinic in Auckland, has a great checklist for taking care of your health as an adult: "
        body += "https://media.starship.org.nz/own-health/own_health.pdf"
      if "Contraception and pregnancy" in discuss_topic:
        body += "\n\nContraception and pregnancy:\n\nThanks for trusting us with this, it's a big topic. We have resources and people able to help with these issues. For now, if you're interested "
        body += "in contraception, here's something from Starship (https://media.starship.org.nz/contraception/contraception.pdf) and for pregnancy, they have the "
        body += "info as well (https://media.starship.org.nz/pregnancy/pregnancy.pdf). Your cardio team is here to support you the whole way."
      if "Leisure and sports" in discuss_topic:
        body += "\n\nLeisure and sports:\n\nIt would be patronising to say \"people with serious congenital heart issues have gone on to win Olympic gold!\", but just know that we "
        body += "will meet you where you are and support you wherever you want to go. Here's a useful site with info on how to responsibly exercise your heart: "
        body += "https://www.aboutkidshealth.ca/playing-sports-with-congenital-heart-disease\n\n(And look up Shaun White, he's amazing.)"
      if "Relationships" in discuss_topic:
        body += "\n\nRelationships:\n\nThis is a complex topic and we can hear you out when you show up at the clinic. If you're intersted in a challenging read, here's a paper on the subject from some of the world's leading researchers: "
        body += "https://pubmed.ncbi.nlm.nih.gov/25296699/"
      body += "\n\nSee you at your next appointment!"
    else:
      body = f"Kia ora {receiver_name}:\n\nThanks for your response, see you at your next appointment!"

    body += "\n\nNgā mihi,\nYour Cardio team"
    try:
      msg = MIMEMultipart()
      msg['From'] = sender
      msg['To'] = receiver_email + ", twah.nz.441@gmail.com"
      msg['Subject'] = subject
            
      msg.attach(MIMEText(body, 'plain'))
            
      with smtplib.SMTP('smtp.gmail.com', 587) as server:
          server.starttls()  # Secure the connection
          server.login(sender, sender_password)
          server.sendmail(sender, receiver_email, msg.as_string())
                
      st.success("Email sent successfully!")

    except Exception as e:
      st.error(f"Failed to send email. Error: {e}")

    internal_body = f"{receiver_name} {receiver_email} has chosen to discuss {discuss_topic} with {discuss_with}"

    try:
      int_msg = MIMEMultipart()
      int_msg['From'] = sender
      int_msg['To'] = "twah.nz.441@gmail.com"
      int_msg['Subject'] = receiver_name
      
      int_msg.attach(MIMEText(internal_body, 'plain'))

      with smtplib.SMTP('smtp.gmail.com', 587) as server:
          server.starttls()  # Secure the connection
          server.login(sender, sender_password)
          server.sendmail(sender, sender, int_msg.as_string())

    except Exception as e:
      st.error(f"Failed to send email. Error: {e}")

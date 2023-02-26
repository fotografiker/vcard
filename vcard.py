import streamlit as st
import qrcode
from unidecode import unidecode
from PIL import Image

#import base64



# Create the vCard text as a string
vcard_template = """BEGIN:VCARD;CHARSET=iso-8859-1
VERSION:4.0
N:{last_name};{name}
FN:{name} {last_name}
ORG:{organisation}
TITLE: {title}
EMAIL;PREF=1;TYPE=INTERNET:{email}
EMAIL:{email2}
TEL;TYPE#work,voice;VALUE#uri:tel:{tel}
TEL;TYPE#mobile,voice;VALUE#uri:tel:{mobile}
ADR;TYPE#WORK;PREF#1: {work_address}
ADR;TYPE#HOME: {home_address}
URL:{website}
END:VCARD"""


#inputs
name = st.text_input("Ad", key="name")
last_name = st.text_input("Soyad", key="last_name")
title = st.text_input("Ünvan", key="title")
e_mail = st.text_input("E-posta adresi", key="email")
e_mail2 = st.text_input("E-posta adresi2", key="email2")
tel = st.text_input("Telefon", key="tel")
mobile = st.text_input("Mobil Telefon", key="mobile")
home_address = st.text_input("Ev adresi", key="home_address")
work_address = st.text_input("İş adresi", key="work_address")
organisation = st.text_input("İşyeri Adı", key="organisation")
website = st.text_input("Websitesi", key="website")

# Define a function to generate the QR code image
def generate_qr_code(data):
    # Format the vCard text with the variables from the data dictionary
    vcard_text = vcard_template.format(**data)
    # Create the QR code image
    img = qrcode.make(vcard_text, box_size=10)
    # Return the QR code image
    return img

# Add a "Generate QR Code" button
if st.button("Generate QR Code"):
    # Create the data dictionary
    data = {
        "name": name,
        "last_name": last_name,
        "email": e_mail,
        "email2": e_mail2,
        "tel": tel,
        "mobile": mobile,
        "home_address": home_address,
        "work_address": work_address,
        "organisation": organisation,
        "website": website,
        "title": title
    }
    # Generate the QR code image
    img = generate_qr_code(data)
    # Display the QR code image
    st.image(img)
# Convert the name to Latin characters using the unidecode function
file_name = unidecode(name)

# Make the file name all lowercase
file_name = file_name.lower()

# Replace any spaces with underscores
file_name = file_name.replace(' ', '_')

# Add the .png extension to the file name
file_name = f'{file_name}_vcard.png'

# Save the QR code image to a file
#with open(file_name, 'wb') as f:
    #img.save(f)

import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64


#QR GENERATION FUNCTION

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="White")
    return img

#STREAMLIT UI
 
st.title("Metro Ticket Booking System with QR + Auto voice")

stations = ["Ameerpet","Erragadda","Bharath nagar","Moosapet"]
name = st.text_input("Passenger Name")
source=st.selectbox("Source Station", stations)
destination=st.selectbox("Destination station",stations)
no_tickets=st.number_input("Number of Tickets",min_value=1, value=1)
price_per_ticket = 30
total_amount =  no_tickets * price_per_ticket
st.info(f" Total Amount: (total_amount)")

#BOOKING BUTTON

if st.button("Book Ticket"):

    if name.strip() == "":
        st.error("Please enter passenger name.")

    elif source==destination:
        st.error("Source and Destination cannot be the same. Please select different stations ")

    else:
        booking_id=str(uuid.uuid4())[:8]

        qr_data =(
            f"BookingID: {booking_id}\n"
            f"Name: {name}\nFrom: {source}\nTo: {destination}\n Tickets:{no_tickets}"
            )
        qr_img = generate_qr(qr_data)

        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes = buf.getvalue()

        st.success("Ticket Booked Successfully!")

        st.write("### Ticket details")
        st.write(f"**Booking ID:** {booking_id}")
        st.write(f"**Passenger:** {name}")
        st.write(f"**From:** {source}")
        st.write(f"**To :** {destination}")
        st.write(f"**Tickets:** {no_tickets}")
        st.write(f"**Amount Paid:** {total_amount}")
        st.image(qr_bytes, width=250)

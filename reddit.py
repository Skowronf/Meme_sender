import praw
import requests
import re
import smtplib
from email.message import EmailMessage
import imghdr

# feel free to use this account or gmail account

reddit = praw.Reddit(client_id='nxTGFOSqQCezNA',
                     client_secret='oxphRtgib4s4DnnrRKpBsPwXW-I',
                     username='PrawProject',
                     password='gY6CaVsm7qR87k2',
                     user_agent='WhatDoYouMean')

subreddit = reddit.subreddit('memes')

top_memes = subreddit.top(limit=10, time_filter='day')

msg = EmailMessage()
msg['Subject'] = 'Wanna some memes?'
msg['From'] = 'memessender@gmail.com'
# below email of person u wanna send mails
msg['To'] = ''
msg.set_content('Here you go!')

for post in top_memes:
    url = post.url
    file_name = url.split('/')
    file_name = file_name[-1]

    r = requests.get(url)
    with open(file_name + '.jpg', 'wb') as f:
        f.write(r.content)
        f.close()

    with open(file_name + '.jpg', 'rb') as h:
        file_data = h.read()
        file_type = imghdr.what(h.name)
        file_name = h.name
        h.close()

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login('memessender@gmail.com', 'gY6CaVsm7qR87k2')

        smtp.send_message(msg)

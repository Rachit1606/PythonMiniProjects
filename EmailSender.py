# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 02:18:30 2020

@author: HP
"""


import smtplib

to = input("Enter the email of the recipitant :- ")
content = input("Enter the  content for the mail :- ")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', '1234')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

sendEmail(to,content)
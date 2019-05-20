#!/usr/bin/python3
import smtplib
import sys
import urllib.request
from pathlib import Path

import config


def main():
    config.init()
    ip_file_exists = Path('external_ip.txt')

    if ip_file_exists.is_file():
        f = open("external_ip.txt", "r")
        prev_ip = f.read()
        f.close()
        if prev_ip != get_ip():
            send_ip()
            update_ip()
        else:
            print("no changes to external ip")
            sys.exit(2)
    else:
        update_ip()
        send_ip()


def update_ip():
    f = open("external_ip.txt", "w")
    f.write(get_ip())
    f.close()


def get_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip


def send_ip():
    send_email("CURRENT IP:", get_ip())


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("email sent")
    except:
        print("error")


if __name__ == "__main__":
    main()

# ISS Location Notifinder
Monitor the International Space Station's position and receive email notifications when it's passing overhead at night.

## Project Overview
The ISS Location Notifinder is a Python application that utilizes external APIs to track the International Space Station (ISS). It checks the ISS's current location against the user's position and sends an automated email notification when the ISS is overhead during nighttime.

## Features
1. ISS Tracking: Leverages real-time ISS location data from the ISS Now API.
2. Location Matching: Compares ISS coordinates with the user's coordinates.
3. Time Check: Determines whether it's nighttime at the user's location.
4. Email Notifications: Sends an email alert when conditions are met.


## Technologies
1. Python: Primary programming language.
2. Requests: HTTP library for making API requests.
3. smtplib: Python's built-in library for sending emails.
4. datetime: Standard library for manipulating dates and times.


## Setup
1. Ensure Python is installed on your system.
2. Install the Requests library using pip install requests if not already installed.
3. Update the MY_LAT and MY_LONG constants with your actual latitude and longitude.
4. Enter your email credentials in MY_EMAIL and MY_PASSWORD. Note: Use an app password if 2FA is enabled on your email account.
5. Run the script with python main.py.

## How It Works
The script runs in an infinite loop, checking every 60 seconds if the ISS is overhead and it's nighttime.
If both conditions are met, an email is sent to the specified address with a notification.
To avoid sending too many emails, consider implementing additional logic to notify once per ISS pass or when you haven't been notified in a certain period.


## Email Alert Example
The email sent will have the following subject and body:

1. Subject: Look Up, ISS is here

2. Body:
The ISS is above you in the sky.

## Important Notes
This script will keep running until it is manually stopped.
Customize the waiting time between checks as necessary.
Make sure to handle your email credentials securely and not expose them in public repositories.
Enjoy tracking the ISS and catching it in your night sky!

# SMS App

## Author
Hossein Kargar

## Date
January 5, 2025

## Description
The **SMS App** is a desktop application built with Python and Tkinter, allowing users to send SMS messages using the Twilio API. It provides a simple graphical interface for entering the recipient's phone number, typing the message, and sending it with a single click.

---

## Features
- **Send SMS Messages**: Use your Twilio account credentials to send SMS messages to any valid 10-digit phone number.
- **User-Friendly GUI**: Built with Tkinter, the app offers a minimal and simple interface.
- **Phone Number Validation**: The app checks if the number entered is valid (10 digits) before sending the message.
- **Feedback Messages**: Get visual confirmation of success or errors during the SMS sending process.

---

## Requirements
Before running the application, make sure you have the following installed:
1. **Python 3.7 or higher**: Download from [https://www.python.org/](https://www.python.org/)
2. **Twilio API Key and Credentials**:
   - Sign up for a Twilio account at [https://www.twilio.com/](https://www.twilio.com/).
   - Get your `ACCOUNT_SID`, `AUTH_TOKEN`, and a `FROM_PHONE_NUMBER` from the Twilio Console.
3. **Required Python Libraries**:
   - The app uses the `twilio` library for interacting with the Twilio API.
   - If not already installed, run the following command:
     ```bash
     pip install twilio
     ```

---

## Installation and Setup

### 1. Clone the Repository
Download or clone the repository using:
```bash
git clone https://github.com/<your-username>/sms-app.git
cd sms-app
```

### 2. Update Twilio Credentials
Open the `sms_app.py` file and modify the following placeholders with your Twilio credentials:
```python
ACCOUNT_SID = "your_sid_here"
AUTH_TOKEN = "your_token_here"
FROM_PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
```
Replace them with:
- `ACCOUNT_SID`: Your Twilio Account SID.
- `AUTH_TOKEN`: Your Twilio Authentication Token.
- `FROM_PHONE_NUMBER`: Your registered Twilio phone number (in the format "+1234567890").

### 3. Run the Application
Run the Python script to start the application:
```bash
python sms_app.py
```

---

## How to Use
1. Launch the application by running the script as instructed above.
2. Enter the recipient's **10-digit phone number** (do not include the country code, as the app prefixes it with `+1` automatically).
3. Write your message in the "Write your message here" box.
4. Click the **"Send SMS"** button.
5. A confirmation message will appear, indicating success or any errors (e.g., invalid phone number).

---

## Example Screenshot
(Not provided in the current repository. Add a screenshot here if desired, showing the UI of the running application.)

---

## Notes
- This app only works with phone numbers in regions supported by Twilio.
- Make sure **your Twilio phone number is verified** if you're using a trial account.
- Ensure an active internet connection when using the application, as Twilio requires access to its API.

---

## License
MIT License. You are free to use, modify, and distribute this application with proper attribution to the author.

---

## Troubleshooting
1. **Invalid Phone Number**:
   - Check that the phone number is exactly 10 digits and numeric (e.g., `1234567890`).
   - Do not include the `+1` part; the app appends it automatically.

2. **Twilio Credential Errors**:
   - Ensure your `ACCOUNT_SID`, `AUTH_TOKEN`, and `FROM_PHONE_NUMBER` are correct.
   - If the error persists, verify them directly in your Twilio account dashboard.

3. **Dependency Issues**:
   - Confirm the `twilio` library is installed:
     ```bash
     pip install twilio
     ```

4. **Application Not Starting**:
   - Ensure your Python version is 3.7 or above by running:
     ```bash
     python --version
     ```

---

## Acknowledgements
Special thanks to the Twilio API team for making SMS integration streamlined and simple.
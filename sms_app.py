"""
SMS App
Author: Hossein Kargar
Date: January 5, 2025
Description: A desktop application for sending SMS messages using the Twilio API.
"""

# Import Modules
from tkinter import *
from twilio.rest import Client

# Constants for Twilio API
ACCOUNT_SID = "your_sid_here"
AUTH_TOKEN = "your_token_here"
FROM_PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# Helper function to send an SMS
def send_sms(account, message_body, phone_number):
    """
    Sends an SMS message to a specified phone number using the given account.

    This function utilizes the `account` object to send an SMS to a recipient
    phone number. It makes use of the Twilio API to create and dispatch the
    message, and prints the SID of the sent message for tracking purposes.

    :param account: The account object used to send SMS messages. Typically,
        this would be a Twilio client instance with the required
        authentication credentials.
    :param message_body: The content of the SMS message to be sent.
    :param phone_number: The recipient's phone number (excluding the country
        code). It will be prefixed with `+1` during the message creation.
    :return: None
    """
    message = account.messages.create(
        from_=FROM_PHONE_NUMBER, body=message_body, to=f"+1{phone_number}"
    )
    print(f"Message SID: {message.sid}")


# Helper function to center the window
def center_window(window, width, height):
    """
    Centers a window on the screen by calculating appropriate x and y coordinates
    based on the window's required width and height and the screen dimensions.
    Updates the window geometry accordingly and returns the modified window object.

    :param window: The tkinter window object that needs to be centered.
    :param width: The width of the window in pixels.
    :param height: The height of the window in pixels.
    :return: The tkinter window object after it has been centered.
    """
    window.update_idletasks()
    x = int((window.winfo_screenwidth() - window.winfo_reqwidth()) / 2)
    y = int((window.winfo_screenheight() - window.winfo_reqheight()) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    return window


# Helper function to create labels
def create_label(parent, text, xpos, ypos, anchor=CENTER):
    """
    Creates and places a Label widget within a given parent widget.

    This function initializes a tkinter Label widget with the specified text,
    positions it relative to the parent widget using the given x and y
    coordinates, and sets the anchor to define the positioning behavior. The
    Label widget is then returned to the caller for further customization or
    use.

    :param parent: The parent tkinter widget to which the Label belongs.
    :type parent: tkinter.Widget
    :param text: The text content to be displayed within the Label.
    :type text: str
    :param xpos: The relative horizontal position (0.0 to 1.0) within the parent
        widget.
    :type xpos: float
    :param ypos: The relative vertical position (0.0 to 1.0) within the parent
        widget.
    :type ypos: float
    :param anchor: The alignment anchor for positioning the Label. Defaults to
        CENTER.
    :type anchor: str
    :return: The created tkinter Label widget.
    :rtype: tkinter.Label
    """
    label = Label(parent, text=text)
    label.place(relx=xpos, rely=ypos, anchor=anchor)
    return label


# Main application
root = Tk()
root.minsize(320, 320)
root.title("SMS App")
root = center_window(root, 450, 350)


# Bind the `Tab` key to move focus to the next widget
def focus_next_widget(event):
    """
    Provides functionality to move focus to the next widget in a Tkinter interface.

    This function attempts to change focus to the next widget in the user
    interface by using the `tk_focusNext` method of the current widget.
    If successful, it breaks the event loop for the event that triggered
    the function. Typically used in environments where keyboard navigation
    is supported.

    :param event: The Tkinter event that triggered the focus change.
    :type event: tkinter.Event

    :return: A string indicating that the event loop should break.
    :rtype: str
    """
    event.widget.tk_focusNext().focus()
    return "break"


# UI elements
create_label(root, "Write the phone number here", 0.5, 0.1)
phone_number_input = Text(root, width=35, height=1)
phone_number_input.place(relx=0.5, rely=0.2, anchor=CENTER)
phone_number_input.bind("<Tab>", focus_next_widget)


create_label(root, "Write your message here", 0.5, 0.3)
confirmation_message = Label(root, text="", state="normal", fg="green")
confirmation_message.place(relx=0.5, rely=0.8, anchor=CENTER)

message_input = Text(root, width=35, height=5)
message_input.place(relx=0.5, rely=0.48, anchor=CENTER)
message_input.bind("<Tab>", focus_next_widget)


# Event handler for SMS sending
def on_send_sms():
    """
    Handles the logic for sending an SMS message based on provided input values.
    Ensures that the phone number is valid and the message body is not empty.
    Validates the phone number to ensure it contains exactly 10 digits.
    Displays appropriate messages in the GUI indicating the success
    or failure of the operation.

    :raises ValueError: If the provided phone number is not 10 digits long
        or contains non-numeric characters.
    :return: None
    """
    phone_number = phone_number_input.get("1.0", "end-1c").strip()
    message_body = message_input.get("1.0", "end-1c").strip()

    if not phone_number.isdigit() or len(phone_number) != 10:
        confirmation_message.configure(
            text="Phone number must be exactly 10 digits", fg="red"
        )
        return

    if not message_body:
        confirmation_message.configure(text="Please enter a message to send", fg="red")
        return

    send_sms(client, message_body, phone_number)
    confirmation_message.configure(text="The message has been sent", fg="green")


# Button for sending SMS
send_sms_button = Button(root, text="Send SMS", fg="red", command=on_send_sms)
send_sms_button.place(relx=0.5, rely=0.9, anchor=CENTER)

# Run the Tkinter GUI
root.mainloop()

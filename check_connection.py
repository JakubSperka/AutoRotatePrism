import requests
import tkinter as tk


def check_connection(token, entry_field):
    """
       Check the connection status of an ARP device using an API request.

       Parameters:
       - token (str): The ARP token used for authentication in the API request.
       - entry_field (tk.Entry): The Tkinter Entry widget where the connection status
                                 will be displayed and updated.

       This function sends an API request to check the connection status of an ARP device
       using the provided token. It updates the specified Tkinter Entry widget (`entry_field`)
       based on the response received:
       - If the device is connected (response is True), it displays "Online" in green text.
       - If the device is not connected (response is False), it displays "Offline" in red text.
       - If there's an error during the API request, it displays an appropriate error message
         in the Entry widget (`entry_field`) and prints the error to the console.

       The `entry_field` should be a Tkinter Entry widget configured to show read-only text,
       which will be updated by this function based on the ARP device's connection status.

       Example usage:
       check_connection("your_arp_token_here", status_entry)
       """

    # Construct the URL with the provided token
    url = f"https://blynk.cloud/external/api/isHardwareConnected?token={token}"
    print(url)

    try:
        # Send GET request to the constructed URL
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the response data in JSON format
            print(response.json())

            # Enable the entry field for editing
            entry_field.config(state="normal")
            # Clear any existing text in the entry field
            entry_field.delete(0, tk.END)
            # Set the text based on connection status
            entry_field.insert(0, "Online" if response.json() is True
                               else "Offline")
            # Set the text color based on connection status
            entry_field.config(state="readonly", foreground="green" if response.json() is True
                               else "red")

        # Handle unsuccessful response (display error message)
        else:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)
            entry_field.insert(0, f"Error, check ARP Token. Status code: {response.status_code}")
            print(f"Failed to retrieve status. Status code: {response.status_code}")
            entry_field.config(state="readonly", foreground="orange")

    # Handle any exceptions that occur during the API request
    except Exception as e:
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")
        print(f"An error occurred: {e}")
        entry_field.config(state="readonly", foreground="orange")

"""
   Check if hardware is connected by making an API request and update the Tkinter Entry field.
"""

import requests
import tkinter as tk


def check_connection(token, entry_field):

    url = f"https://blynk.cloud/external/api/isHardwareConnected?token={token}"
    print(url)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Online" if response.json() is True
                               else "Offline")
            entry_field.config(state="readonly", foreground="green" if response.json() is True
                               else "red")
        else:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)
            entry_field.insert(0, f"Error, check ARP Token. Status code: {response.status_code}")
            print(f"Failed to retrieve status. Status code: {response.status_code}")
            entry_field.config(state="readonly", foreground="orange")
    except Exception as e:
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")
        print(f"An error occurred: {e}")
        entry_field.config(state="readonly", foreground="orange")

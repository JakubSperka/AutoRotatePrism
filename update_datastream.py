from select_item import *


def update_angle(angle_value):

    token = selected_arp_token
    pin = "V0"
    value = str(angle_value)
    print(f"Importing value: {value}")

    url = f"https://blynk.cloud/external/api/update?token={token}&{pin}={value}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating Blynk pin: {e}")
        return False

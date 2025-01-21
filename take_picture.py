"""
Date: 21/01/2025
Author: Andree Renteria
Description: Main file to store functions to take and manage camera operations 

Revision History:
    - Rev 1.0 (21/01/2025): Initial version, including basic functionality.
"""

# Import Libraries
import subprocess
import datetime

def take_picture():

    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    #output_filename = "/mnt/Kasia/MendixTemp/Pic-" + timestamp + ".jpg"
    output_filename = timestamp + ".jpg"

    # Trigger camera to take a picture
    print("Taking picture...")
    import subprocess
    subprocess.run(['rpicam-still', '--output', output_filename, '--immediate'])
    return "Picture taken!"


import os
import requests

def fetch_image():
    # Prompting user for an image URL
    url = input("Enter the image URL: ").strip()

    # Creating a directory for fetched images if it doesn't exist
    folder_name = "Fetched_Images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        # Attempting to download the image
        response = requests.get(url, timeout=10)

        # Checking if request was successful
        response.raise_for_status()

        # Extracting filename from URL
        filename = url.split("/")[-1]
        if not filename:  # if URL ends with /
            filename = "downloaded_image.jpg"

        # Saving path
        filepath = os.path.join(folder_name, filename)

        # Saving image content
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Image downloaded successfully and saved as {filepath}")

    except requests.exceptions.RequestException as e:
        print(f" Failed to fetch image. Error: {e}")

if __name__ == "__main__":
    fetch_image()

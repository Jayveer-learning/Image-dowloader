import os
import requests

# create folder()
def create_folder(folder_name: str = "Leslis burke Gallery") -> None:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"{folder_name} already exists.")


def image_download(url: str, file_name: str = "Leslie_burke_photo1", folder_name: str = "Leslis burke Gallery") -> None:
    
    # Call the create_folder function
    create_folder(folder_name)

    # Ensure the URL is not empty
    if not url:
        print("Error: No URL provided.")
        return
    
    # Send a GET request to the server for the photo
    response = requests.get(url)

    file_name_data = file_name + ".jpg"
   
    # Create the file path using join
    file_full_path = os.path.join(folder_name, file_name_data)

    if os.path.exists(file_full_path):
        print(f"Image '{file_name_data}' is already in folder '{folder_name}'.")
        return  # Exit the function if the file already exists

    elif response.status_code == 200 and "image" in response.headers['Content-Type']:
        # Open the file in binary mode to write image content
        with open(file_full_path, "wb") as download_image:
            download_image.write(response.content)
            print(f"File '{file_name}' added to '{folder_name}' successfully.")
    else:
        print(f"Failed to download the image. Status code: {response.status_code}")

# Test cases
image_download("https://i.pinimg.com/550x/a6/22/7e/a6227e7c995c773e422943078904f832.jpg")
image_download("https://tinyurl.com/276tksag", "Leslie_burke_photo2")


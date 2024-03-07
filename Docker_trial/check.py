import zipfile
import pickle
import os

# Specify the path to the ZIP file
zip_file_path = "Model/Naive_Bayes_Model_Returns.zip"

# Extract the ZIP file
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    # Extract all contents to a temporary directory
    zip_ref.extractall("temp_extracted")

# Path to the extracted directory
extracted_dir = r"temp_extracted"

# Path to the content directory inside the extracted directory
content_dir = os.path.join(extracted_dir, "content")

# List the contents of the content directory
content_files = os.listdir(content_dir)
print("Contents of 'content' directory:", content_files)

# Assuming there's only one file in the 'content' directory
if len(content_files) == 1:
    # Get the filename of the pickled file
    pickled_filename = content_files[0]

    # Path to the pickled file
    pickled_file_path = os.path.join(content_dir, pickled_filename)

    # Load the pickled object from the extracted file
    with open(pickled_file_path, "rb") as file:
        try:
            obj = pickle.load(file)
            print("File loaded successfully!")
        except Exception as e:
            print("An error occurred while loading the file:", e)
else:
    print("Error: Multiple files found in 'content' directory.")

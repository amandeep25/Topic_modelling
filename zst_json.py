import os
import pyzstd

def uncompress_zst_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Check if the file has a ZST extension
        if file.endswith(".zst"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file[:-4]+ ".json")  # Remove ".zst" from the output file name

            # Read the compressed content
            with open(input_path, "rb") as compressed_file:
                compressed_content = compressed_file.read()

            # Decompress the content
            decompressed_content = pyzstd.decompress(compressed_content)

            if decompressed_content:
                print(f'Success!')
            else:
                print(f':(((')

            # Write the decompressed content to the output file
            # Write the decompressed content to the output file
            with open(output_path, "wb") as output_file:
                output_file.write(decompressed_content)

uncompress_zst_folder('/Users/a3kaur/Downloads/supplements/files/', '/Users/a3kaur/Downloads/supplements/files/')

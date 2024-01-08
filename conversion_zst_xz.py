import subprocess

def convert_zst_to_xz(input_file, output_file):
    # Run zstd to decompress from ZST to temporary file
    subprocess.run(["zstd", "-d", "--stdout", input_file], stdout=subprocess.PIPE, check=True)

    # Run xz to compress from temporary file to XZ format
    subprocess.run(["xz", '--stdout', input_file[:-4]], stdout=subprocess.PIPE, check=True)


    # Rename the temporary file to the desired output file
    subprocess.run(["mv", f"{input_file[:-4]}.xz", output_file], check=True)

# Example usage:
input_zst_file = "/Users/a3kaur/Downloads/supplements/stopdrinking_comments.zst"
output_xz_file = "/Users/a3kaur/Downloads/supplements/stopdrinking_comments.xz"

convert_zst_to_xz(input_zst_file, output_xz_file)

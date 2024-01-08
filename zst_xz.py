import zstandard
import lzma

def convert_zst_to_xz(input_zst_file, output_xz_file):
    # Decompress ZST file
    with open(input_zst_file, 'rb') as zst_file:
        decompressor = zstandard.ZstdDecompressor()
        with decompressor.stream_reader(zst_file) as reader:
            decompressed_data = reader.read()

    # Compress and write to XZ file
    with lzma.open(output_xz_file, 'wb') as xz_file:
        xz_file.write(decompressed_data)

# Example usage
input_zst_file = '/Users/a3kaur/Downloads/supplements/files/stopdrinking_comments.zst'
output_xz_file = '/Users/a3kaur/Downloads/supplements/files/stopdrinking_comments.xz'

convert_zst_to_xz(input_zst_file, output_xz_file)


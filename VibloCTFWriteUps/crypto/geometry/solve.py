import zlib

with open("geometry.png", "rb") as file:
    file.seek(91)  # Di chuyển con trỏ đọc đến offset 91
    compressed_data = file.read()


with open("compressed_data.zlib", "rb") as file:
    compressed_data = file.read()

try:
    uncompressed_data = zlib.decompress(compressed_data)
    with open("uncompressed_data", "wb") as output_file:
        output_file.write(uncompressed_data)
        print(uncompressed_data)
except zlib.error as e:
    print(f"Error decompressing data: {e}")

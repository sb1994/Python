f = open(
    "core_python_getting_started/11_io_file_managment/open_files.txt",
    mode="rt",
    encoding="utf-8",
)

# Will read a specific number of bytes
print(f.read(31))

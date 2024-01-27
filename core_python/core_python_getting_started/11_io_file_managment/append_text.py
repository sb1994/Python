f = open(
    "core_python_getting_started/11_io_file_managment/open_files.txt",
    mode="at",
    encoding="utf-8",
)

f.writelines(
    [
        "Son of man\n",
        "You cannot say, or guess",
        "for you know only,\n",
        "A heap of broken images, ",
        "where the sun beats\n",
    ]
)
print(f)

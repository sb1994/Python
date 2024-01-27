f = open(
    "core_python_getting_started/11_io_file_managment/open_files.txt",
    mode="wt",
    encoding="utf-8",
)

print(f)


f.write("What are the roots that clutch\n")
f.write("What branches grow\n")
f.write("Out of this stony rubbish\n")

# close the file when finished with the file
f.close()

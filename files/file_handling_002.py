# create a file called "countries.txt" and write
# some names of the countries
# then close the file handle
file_handle = open("countries.txt", "w")
file_handle.write("India\n")
file_handle.write("USA\n")
file_handle.write("Russia\n")
file_handle.close()

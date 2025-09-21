file_read = open('Codingal.txt', 'r')
print("File in Read Mode - ")
print(file_read.read)
file_read.close()

file_write = open('Codingal.txt', 'r')
print("File in Write Mode...")
print(file_write.write)
print("I can't wait for my birthday!")
file_write.close

file_append = open('Codingal.txt', 'r')
print("File in Append Mode: ")
print(file_append.write)
print("I'm gonna go bowling!")
file_append.close
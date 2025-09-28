file_read = open('Homework2.txt', 'r')
print(file_read.read)
file_read.close()

file_write = open('Homework3.txt', 'r')
print(file_write.write)
print("My birthday was yesterday!")
file_write.close

file_append = open('Homework4.txt', 'r')
print(file_append.write)
print("I'm officially 12 now!")
file_append.close
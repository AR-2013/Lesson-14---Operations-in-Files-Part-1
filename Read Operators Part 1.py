file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in Parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'w')
print("Hi! My name is Anaira and I am turning 12 in 6 days.")
file.close()
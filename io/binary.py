with open("../data/binary", "bw") as binary_file:
    for i in range(17):
        binary_file.write(bytes([i]))

with open("../data/binary", "br") as bin_file:
    for b in bin_file:
        print(b)

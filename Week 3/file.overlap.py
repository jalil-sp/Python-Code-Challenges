

def read_file(file_path):
    num_list = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            number = int(line)
            if number not in num_list:
                num_list.append(number)
    return num_list

file_path1 = r'C:\Users\14046\Desktop\Python Code Challenges\Week 3\primenumbers.txt'
file_path2 = r'C:\Users\14046\Desktop\Python Code Challenges\Week 3\happynumbers.txt'

prime_num = read_file(file_path1)
happy_num = read_file(file_path2)

overlap = [i for i in prime_num if i in happy_num]
print(f'The common numbers between both files are: \n{overlap}')
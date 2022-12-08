import os

with open('./input.txt') as file:
    lines = file.readlines()

for line in lines:
    if line[-2] == '/':
        os.chdir('/home/ubuntu')
    elif line[0] == '$' and line[2] == 'c':
        os.chdir(line.split(' ')[2].replace('\n', ''))
    elif line[0:3] == 'dir':
        os.mkdir(line.split(' ')[1].replace('\n', ''))
    elif line[0].isdigit():
        with open("./{}".format(line.split(' ')[1].replace('\n', '')), 'w') as temp:
            temp.write('0' * int(line.split(' ')[0].replace('\n', '')))


files = []
for file in os.listdir('/home/ubuntu'):
    if not file.startswith('.') and os.path.isdir(f"/home/ubuntu/{file}"):
        files.append(file)

os.chdir('/home/ubuntu')
def filesize(path):
    size = 0
    for p, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(p, f)
            size += os.path.getsize(fp)
    return size
total = 0

total_space = 70_000_000
unused_space = 70_000_000

for file in os.listdir('/home/ubuntu'):
    if os.path.isdir('/home/ubuntu/' + file) and ('.' not in file):
        unused_space -= filesize('/home/ubuntu/' + file)

print(unused_space)

subdirs = [x[0] for x in os.walk('/home/ubuntu')]
for subdir in subdirs:
    if not '.' in subdir and filesize(subdir) >= (30_000_000 - unused_space):
        print(filesize(subdir), subdir)
        total += filesize(subdir)

print(total)
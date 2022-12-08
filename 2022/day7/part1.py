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

subdirs = [x[0] for x in os.walk('/home/ubuntu')]
for subdir in subdirs:
    if not subdir.startswith('.') and filesize(subdir) <= 100000:
        print(filesize(subdir), subdir)
        total += filesize(subdir)

print(total)
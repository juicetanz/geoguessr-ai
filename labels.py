import os

file = open('data/labels.txt', 'w')

for country in sorted(os.listdir('data/train')):
    file.writelines(str(country) + '\n')

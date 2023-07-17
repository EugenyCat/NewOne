"""
'r' - open for READ
'w' - open for WRITE. Old data are deleted!!!
'a' - open for ADD. Data is added in end.
'wb' - open for WRITE_BITES.
'rb' - open for READ_BITES.
"""
f = open('files/visit_log.csv', 'r', encoding='utf-8')


"""Print some information about file and from file"""
print(f)
print(f.readline())
#print(f.readlines())


"""Read data by line"""
#for line in f:
#    print(line)

"""Use method enumerate for autonumber each line"""
for i, line in enumerate(f):
    print(i, line)

    if i > 5:
        break


"""Read in RAM"""
content = f.readlines()

"""Close file"""
f.close()


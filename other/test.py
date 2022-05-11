romeo_append = []
romeo_open = open('romeo.txt')

for romeo_list in romeo_open:
    romeo_split = romeo_list.split()
    if romeo_split in romeo_append:
       continue
    #romeo_append.append(romeo_split)
    romeo_append.extend(romeo_split)
    romeo_append.sort()

print(romeo_append)
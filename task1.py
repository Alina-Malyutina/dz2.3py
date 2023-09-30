start_list = input("Enter list of dublicate numbers: ")

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

print(find_duplicates(start_list))
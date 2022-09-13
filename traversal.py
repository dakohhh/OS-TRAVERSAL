import os



# Using Recurssion
def traverse(path):
    hash = {}
    hash1 = {}
    for dir, folders, files in os.walk(path):
        folders.extend(files)
        for i in folders:
            if os.path.isfile(os.path.join(dir, i)):
                hash1[i] = 0
            else:
                hash1[i] = traverse(os.path.join(dir, i))
        wis = hash[os.path.basename(dir)] = hash1

        return wis


# Using Recurssion
def create_traversal(hash, destination_dir):

    for i in hash:
        if os.path.splitext(os.path.join(destination_dir, i))[1] != "" or type(hash[i]) == int:
            f = open(os.path.join(destination_dir, i), "w")
            f.close()
        else:
            true_path = os.path.join(destination_dir , i)
            os.makedirs(true_path)
            create_traversal(hash[i], true_path)
            



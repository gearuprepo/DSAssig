# File Recursion
import os
base_path = os.path.dirname(os.path.realpath(__file__))
path = base_path+"/testdir"

def loopdir( path):
    ls_files = []
    for f in os.listdir(path):
        localpath = path + "/" + f
        if os.path.isdir(localpath):
            ls_files.append(localpath)
            ret_ls = loopdir(localpath)
            if ret_ls.__len__() ==0:
                ls_files.remove(localpath)
            else:
                for r in ret_ls:
                    ls_files.append(r)
        else:
            if str(path +"/"+f).endswith(".c"):
                ls_files.append(path +"/"+f)
    return ls_files

for p in loopdir(path):
    print(str(p).replace(base_path,"."))



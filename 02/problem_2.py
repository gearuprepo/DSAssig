# File Recursion
import os
base_path = os.path.dirname(os.path.realpath(__file__))
path = base_path+"/testdir"
#Fix 3: Do not hard code suffix.
suff = ".c"
def loopdir( path,suffix):
    ls_files = []
    #Fix 1: Check for dir
    if os.path.isdir(path):
        for f in os.listdir(path):
            #Fix 2: For cross platform compatibility
            localpath = os.path.join(path,f)
            if os.path.isdir(localpath):
                ls_files.append(localpath)
                ret_ls = loopdir(localpath,suffix)
                if ret_ls.__len__() ==0:
                    ls_files.remove(localpath)
                else:
                    for r in ret_ls:
                        ls_files.append(r)
            else:
                if str(path +"/"+f).endswith(suffix):
                    ls_files.append(path +"/"+f)
    return ls_files

for p in loopdir(path,suff):
    print(str(p).replace(base_path,"."))



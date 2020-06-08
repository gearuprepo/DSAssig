# File Recursion

The code uses recursion to loop through the folders and sub folders and lists down the files. 

n is the number of folders and sub folders

> * Time O(n)  = nlogn [traversal through all the folders and sub folders using recursion.]
> * Space O(n) = n [file names are stored to ls_files variable]

Call Stack:
Below is a example of how the call stack will work with the code.
- loopdir(Folder 1)
-- loopdir(Folder 1.1)
--- loopdir (Folder 1.1.1)
-- loopdir(Folder 1.2)


Fixed review comments
----------------------
1. validation for os.listdir(path)
2. For cross-platform compatibility, you should be making use of the os.path.join() method to concatenate string paths. 
3. The suffix should be passed directly into the function and not hard coded as you have done.
4. Review 2 - Add time and space complexity in md file.
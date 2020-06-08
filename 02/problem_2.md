# File Recursion

The code uses recursion to loop through the folders and sub folders and lists down the files. The time complexity will be in the range of n to nlogn

Fixed review comments
----------------------
1. validation for os.listdir(path)
2. For cross-platform compatibility, you should be making use of the os.path.join() method to concatenate string paths. 
3. The suffix should be passed directly into the function and not hard coded as you have done.
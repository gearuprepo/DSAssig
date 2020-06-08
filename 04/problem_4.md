# Active Directory

The active directory implementation uses recursion for iterating and finding out the user.

n is the number of groups and subgroups

> * Time O(n)  = nlogn [traversal through all the folders and sub folders using recursion.]
> * Space O(n) = n [file names are stored to ls_files variable]

Call Stack:
Below is a example of how the call stack will work with the code aassuming the user is in group 1.1.1
- is_user_in_group(Group 1)
-- is_user_in_group(Group 1.1)
--- is_user_in_group (Group 1.1.1)


Review comments fixed
---------------------
Review 1 - No comments
Review 2 - Updated the md file with additional information.
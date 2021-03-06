# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
# We can construct this hierarchy as such.
# Where User is represented by str representing their ids.
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        #self.users.append(user)
        self.users[user] = user

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

#O(n) = nlogn
def is_user_in_group(user, group):
    """
        Return True if user is in the group, False otherwise.

        Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    chi = group.users.get(user)
    if chi != None:
        return chi
    else:
        for gitem in group.groups:
            return is_user_in_group(user,gitem)


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group("sub_child_user",parent))

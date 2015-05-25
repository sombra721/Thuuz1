'''
This function loads the string as a file path then returns a normalized path. 

The rules of normalization:
• all single dot components of the path must be removed.  
  For example, "foo/./bar" should be normalized to "foo/bar".
• all double dots components of the path must be removed, 
  along with their parent directory.  For example, "foo/bar/../baz" should be normalized to "foo/baz".
• all multiple slashes will remain the same, which means this function does not normalize the multiple slashes.

Usage:
print normalize_path(string)

'''

def normalize_path(string):
    if string == "":
        return
    result = ""
    stack = []
    index = string.find("/")
    while index != -1:    
        if string[:index] == "..":
            del stack[-1]
        elif string[:index] ==  ".":
            pass
        else:
            stack.append(string[:index])
        string = string[index+1:]
        index = string.find("/")
    stack.append(string)
    if stack:
        result += stack.pop(0)
    while stack:
        result += "/" + stack.pop(0)
    return result

string = "foo/bar/../baz" 
print normalize_path(string)
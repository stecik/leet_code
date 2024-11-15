# slow
# def simplifyPath(path: str) -> str:
#     path = [part for part in path.strip().split("/") if part != "" and part != "."]
#     i = 0
#     while i < len(path):
#         if i + 1 < len(path) and path[i + 1] == "..":
#             path.pop(i)
#             path.pop(i)
#             i -= 1 if i > 0 else 0
#         else:
#             i += 1
#     if len(path) and path[0] == "..":
#         path.pop(0)
#     path = "/" + "/".join(path)
#     return path


# optimized
def simplifyPath(path: str) -> str:
    path = [part for part in path.strip().split("/") if part != "" and part != "."]
    result = ""
    count = 0
    while path:
        part = path.pop(-1)
        if part == "..":
            count += 1
        elif count > 0:
            count -= 1
        elif count == 0:
            result = "/" + part + result
    return result if result else "/"


path = "/home/"
print(simplifyPath(path))
path = "/home//foo/"
print(simplifyPath(path))
path = "/home/user/Documents/../Pictures"
print(simplifyPath(path))
path = "/../"
print(simplifyPath(path))
path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))
path = "/a/./b/../../c/"
print(simplifyPath(path))
path = "/a/../../b/../c//.//"
print(simplifyPath(path))
path = "/home/of/foo/../../bar/../../is/./here/."
print(simplifyPath(path))

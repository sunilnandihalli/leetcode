# Design an in-memory file system to simulate the following functions: 
# 
#  ls: Given a path in string format. If it is a file path, return a list that o
# nly contains this file's name. If it is a directory path, return the list of fil
# e and directory names in this directory. Your output (file and directory names t
# ogether) should in lexicographic order. 
# 
#  mkdir: Given a directory path that does not exist, you should make a new dire
# ctory according to the path. If the middle directories in the path don't exist e
# ither, you should create them as well. This function has void return type. 
# 
#  addContentToFile: Given a file path and file content in string format. If the
#  file doesn't exist, you need to create that file containing given content. If t
# he file already exists, you need to append given content to original content. Th
# is function has void return type. 
# 
#  readContentFromFile: Given a file path, return its content in string format. 
# 
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# 
# Output:
# [null,[],null,null,["a"],"hello"]
# 
# Explanation:
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  You can assume all file or directory paths are absolute paths which begin wit
# h / and do not end with / except that the path is just "/". 
#  You can assume that all operations will be passed valid parameters and users 
# will not attempt to retrieve file content or list a directory or file that does 
# not exist. 
#  You can assume that all directory names and file names only contain lower-cas
# e letters, and same names won't exist in the same directory. 
#  
#  Related Topics Design


# leetcode submit region begin(Prohibit modification and deletion)
class FileSystem:

    def __init__(self):
        

    def ls(self, path: str) -> List[str]:
        

    def mkdir(self, path: str) -> None:
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        

    def readContentFromFile(self, filePath: str) -> str:
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
# leetcode submit region end(Prohibit modification and deletion)

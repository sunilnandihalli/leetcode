# An abbreviation of a word follows the form <first letter><number><last letter>
# . Below are some examples of word abbreviations: 
# 
#  
# a) it                      --> it    (no abbreviation)
# 
#      1
#      ↓
# b) d|o|g                   --> d1g
# 
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
#  
# 
#  Assume you have a dictionary and given a word, find whether its abbreviation 
# is unique in the dictionary. A word's abbreviation is unique if no other word fr
# om the dictionary has the same abbreviation. 
# 
#  Example: 
# 
#  
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
#  
#  Related Topics Hash Table Design


# leetcode submit region begin(Prohibit modification and deletion)
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        

    def isUnique(self, word: str) -> bool:
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# leetcode submit region end(Prohibit modification and deletion)

""" 
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = false.
"""

def solution(strings, patterns):
    str_pat_map = {}
    for i in range(len(strings)): 
        if not str_pat_map[patterns[i]]: 
            str_pat_map[patterns[i]] = strings[i]
        elif str_pat_map[patterns[i]] != strings[i]: 
            return False
            break
        elif i == len(strings): 
            return True
        else: 
            return "?"
            
            
strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

solution(strings,patterns)

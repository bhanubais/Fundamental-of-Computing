'''
"Pig Latin" is a language game that involves altering words via a simple set of rules. Write a Python function pig_latin that takes a string word and applies the following rules to generate a new word in "Pig Latin". If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word. For example, pig_latin("pig") would return "igpay". If the first letter in word is a vowel, append "way" to the end of the word. For example, pig_latin("owl") returns "owlway". You can assume that word is in lower case. The provided template includes code to extract the first letter and the rest of word in Python. Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. However, we don't know enough Python to implement full Pig Latin just yet.
'''
# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter in 'aeiou':
        return rest_of_word + first_letter + 'ay'
    else:
        return rest_of_word + 'way'

    # Student should complete function on the next lines.



###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""

    print(pig_latin(word))

test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay

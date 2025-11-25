"""
re Module
"""

a = "My Mobile Number is 9999999999."
print(a.find("9999999999"))
print(a.index("9999999999"))

print(a.find("888888"))
# print(a.index("888888"))

"""
Pattern Matching
"""
import re


"""
\d = Digit
\s = Space Character
\S = Not a Space
\w = Word
\W = Not a Word
. => Any character
* => Zero or more Occurences
+ => One or more Occurences
? => Zero or one occurence
[] => Characters set
{} => Group
^ => Start
$ => end
"""


text = """
ksjdcnskldjvcn 
jshd jkshd s
jhsdjsd 
]shdhjskds
8928329832
skdjnsnkds'
skdjskds
2837283728
''sd''
eksjek@skjd.cin
ksjdcskjd'
skdjs@jksjd.cin'
skjdksjefdds'
skejskf@.cim
23-10-2025
skdjskjds
skdjskdjskd
sdkjskdsjs
31-10-2025
skdjslkjclsdjcs
s
dsskjdskdjs
01-10-2025
ksjdksjcsk
sdkjcsksdj
31-12-2025
skdjcsnnkcjsd
skjdcksdjcn
25-12-2025
ksjdkscd
skdjcskds
01-01-2026
xkdjccskcjskcjsd
sjkhdcksdchsk
jksdhncksddch
kjxxdkx
"""


mobile_number_pattern = "\\d{10}"
mobile_numbers = re.findall(mobile_number_pattern, text)
print(mobile_numbers)


email_pattern = r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+"
emails = re.findall(email_pattern, text)
print(emails)

date_pattern = r"\d{2}-\d{2}-\d{4}"
dates = re.findall(date_pattern, text)
print(dates)

"""
1. match - Searches for the string only at the beginning. If the string is not at the beginning, it will return a None.
2. <match_object>.span - returns a tuple with string starting and ending indices of the match object.
4. compile - Used for performance optimization.
5. search - Searches for the entire string and returns the first occurence if there is a match. Else, None
6. findall() - returns all the matching strings in a list.
7. finditer() - returns an iterator with all the match objects.
8. sub() - replaces the pattern with a new string
"""


text = """
slkejs
cat
skdjs
bat
ksjdsk
rat
ksjds
catch
skjdsk
batch
skdjs
match
skatch
btatch
atch
"""

at_text_pattern = ".at.*"
at_words = re.findall(at_text_pattern, text)
print(at_words)


text = """
ksjsd
cat
slkjdsl
hat
lsdkjsl
bat
klsjdls
mat
ksjsk
eat
haat!!
baat!!

ksjdskdjeat
sldjsldkbat
sljsldcat
sldksledkdat
lskdsldeat
at
at
at
at
at
"""
at_words_pattern = ".at"
at_words = re.findall(at_words_pattern, text)
print(at_words)

at_words_pattern = ".*at"
at_words = re.findall(at_words_pattern, text)
print(at_words)


at_words_pattern = ".+at"
at_words = re.findall(at_words_pattern, text)
print(at_words)

at_words_pattern = ".?at"
at_words = re.findall(at_words_pattern, text)
print(at_words)


at_words_pattern = "[cbm]at"
at_words = re.findall(at_words_pattern, text)
print(at_words)

at_words_pattern = "[cbm]at"
at_words = re.finditer(at_words_pattern, text)
print(at_words)
for matching_word in at_words:
    print(matching_word)
    print(matching_word.span())
    print(type(matching_word.span()))

text = "Hello World!!!"
pattern = ".*llo"
match_object = re.match(pattern, text)
print(match_object)
pattern = "World"
match_object = re.match(pattern, text)
print(match_object)

pattern = "World"
match_object = re.search(pattern, text)
print(match_object)


text = """
cat
dlfkjd
bat
slkdjsld
mat
skdjsd
hat
sdkjsdsk
"""
pattern = ".at"
match = re.search(pattern, text)
print(match)

pattern = ".ab"
match = re.search(pattern, text)
print(match)

pattern = ".at"
replaced_string = re.sub(pattern, "re", text)
print("Replaced String: ")
print(replaced_string)
replaced_string = re.sub(pattern, "re", text, 2)
print("Replaced String: ")
print(replaced_string)
print("Original Text")
print(text)


pattern = ".at"
compiled_pattern = re.compile(pattern)
print(compiled_pattern)
matching_words = compiled_pattern.findall(text)
print(matching_words)
matching_words = compiled_pattern.finditer(text)
print(matching_words)
matching_words = compiled_pattern.search(text)
print(matching_words)
matching_words = compiled_pattern.match(text)
print(matching_words)


split_words = re.split(pattern, text)
print(split_words)


text = """
matching
ksdjcskfejw 
catching
lwejn a;we 
eating
lzijn ;AWE
sleeping
akejdckzder
drinking
"""
pattern = "(.*)(ing)"
matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(type(match.groups()))
    print(match.groups())


# my_str = "Hello\nWorld"
# my_str = "Hello\\nWorld"
my_str = r"Hello\nWorld"
print(my_str)


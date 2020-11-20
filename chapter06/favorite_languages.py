# favorite_languages.py

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# } 
# print(favorite_languages)
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())    

# for name in favorite_languages:
#     print(name.title())        

# friends = ['phil', 'sarah']
# # for name in favorite_languages.keys():
# for name in favorite_languages:
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# print(favorite_languages)
# print(favorite_languages.keys())
# keys = favorite_languages.keys()
# print(type(keys))
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print(favorite_languages.values())
# values = favorite_languages.values()
# print(type(values))
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# setofvalues = set(favorite_languages.values())
# print(setofvalues)
# print(type(setofvalues))
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title()) 

favorite_languages = {
                    'jen': ['python', 'ruby'],
                    'sarah': ['c'],
                    'edward': ['ruby', 'go'],
                    'phil': ['python', 'haskell'],
                    }
for name, languages in favorite_languages.items():
    # print(f"\n{name.title()}'s favorite languages are:")
    mesg = f"\n{name.title()}'s favorite language"
    if len(languages) > 1:
        mesg += 's are:'
    else:
        mesg += ' is:'
    print(mesg)
    for language in languages:
        print(f"\t{language.title()}") 




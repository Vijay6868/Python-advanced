
# demonstrate template string functions

from string import Template
# Usual string formatting with f-strings
str1 = "Advanced Python: Language Features"
str2 = "Vijay Kumar"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# TODO: create a template with placeholders
templ = Template("you are watching ${title} by ${author}")
# TODO: use the substitute method with keyword arguments
str2 = templ.substitute(title="advanced python programming language", author="AJ")
#str2 = templ.substitute(title="advanced python language feature", author="vijay kumar")
print(str2)
# TODO: use the substitute method with a dictionary
data = {
    "author":"vijay kumar",
    "title":"Advanced python programming language"
}
str3=templ.substitute(data)
print(str3)
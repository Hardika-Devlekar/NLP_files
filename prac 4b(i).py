import re

text = """Hardika is smart and she rocks. Riddhi is great"""
tokens = re.findall("[\w']+", text)
print(tokens)

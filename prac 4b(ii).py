import re

text = """Hardika is great and she rocks?. Riddhi is great"""
sentences = re.compile('[.!?]').split(text)
print(sentences)

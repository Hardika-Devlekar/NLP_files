from spacy.lang.en import English

nlp = English()
text = """This tool is an a beta stage. Alexa developers can use Get Metrics API to
seamlessly analyse metric. It also supports custom skill model, prebuilt Flash Briefing
model, and the Smart Home Skill API. You can use this tool for creation of monitors,
alarms, and dashboards that spotlight changes. The release of these three tools will
enable developers to create visual rich skills for Alexa devices with screens. Amazon
describes these tools as the collection of tech and tools for creating visually rich and
interactive voice experiences."""

my_doc = nlp(text)

token_list = []
for token in my_doc:
  token_list.append(token.text)
  token_list
print(token_list)

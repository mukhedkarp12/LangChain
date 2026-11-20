# This code is a manual simulation of semantic search process.
# Here we are 

documents = {
"remote_work": "Employees can work remotely.",
"online_training": "Students can attend online classes.",
"library_hours": "The library closes at 6 PM."
}

concepts = {
"remote_work": ["work remotely", "work from home"],
"online_training": ["online classes", "learn from home"],
"library_hours": ["library closes", "closing time"]
}

question = "Can I work from home?"
matched = None

for concept, phrases in concepts.items(): # .items() returns both key and value from dict
    if any(phrase in question.lower() for phrase in phrases): #if anythng matches any returns true
       matched = documents[concept]
       break
print("Question:", question)
if matched:
    print("Related Document:", matched)
else:
    print("No related document found")
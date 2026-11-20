# """ This progarm is for Jaccard Similarity where we are finding out the similarity between the 2 
# sentences. We are splitting the text based on spaces by deafult and then typecasting it to
# set. Jaccard similarity performs following algo :  (A intersection B) / (A union B)



def jaccard_similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    union = words1.union(words2)
    if not union:
        return 1.0
    common = words1.intersection(words2)
    return len(common)/ len(union)


s1 = "I love to learn Python" # here s1 and s2 are opposite still jaccrd says its similar because it counts the similar words"""
s2 = "I hate to learn Python" #and only 1 word (love and hate) are not similar , else every word is same, which results into similar texts for s1 ans s2. but acutally they are not
s3 = "The weather is very hot"

print(round(jaccard_similarity(s1,s2),2))
print(round(jaccard_similarity(s2,s3),2))
print(round(jaccard_similarity(s1,s3),2))

import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

from sentence_transformers import SentenceTransformer
import numpy as np
import json
import logging

# Initilizing model and loading Question embeddings and QA database
model = SentenceTransformer('all-MiniLM-L6-v2')
question_embeddings = np.array(json.load(open('data/DB_embeddings.txt')))
knowledge_db = json.load(open('data/scienceQ.json'))


############################################################
# Callback function called on update config
############################################################


def config(configuration: ConfigClass):
    pass

############################################################
# Callback function called on each execution pass
############################################################


def execute(request: SimpleText, ray: OpenfabricExecutionRay):
    output = []
    query = request.text[0].strip()   # remove leading and trailing spaces
    # case 1: no input
    if not query:
        response = "Please enter a question."
        logging.warning("  No input given.")
        output.append(response)
        return SimpleText(dict(text=output))

    # case 2: input is given
    query_embedding = model.encode(query)  # encode the input question
    query_norm = np.linalg.norm(query_embedding)
    question_norm = np.linalg.norm(question_embeddings, axis=1)
    cosine_similarities = np.inner(
        question_embeddings, query_embedding) / (query_norm * question_norm)  # calculate cosine similarity
    # get the index of the most similar question
    most_similar_index = np.argmax(cosine_similarities)

    # case 3: no similar question found
    if cosine_similarities[most_similar_index] < 0.5:
        response = "Sorry, I don't know the answer to that question."
        logging.warning("  No answer found for input question.\t Possible Answer: {} \t Confidence: {}".format(knowledge_db[most_similar_index]["correct_answer"],
                                                                                                               cosine_similarities[most_similar_index]))
    # case 4: similar question found
    else:
        response = knowledge_db[most_similar_index]["correct_answer"]
        confidence = cosine_similarities[most_similar_index]
        logging.info("  Answer found for input question.\tAnswer: {} \t Confidence: {} \n Base: {}".format(
            response, confidence, knowledge_db[most_similar_index]["support"]))

    output.append(response)
    return SimpleText(dict(text=output))

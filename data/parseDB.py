import json
from sentence_transformers import SentenceTransformer

knowledge_db = json.load(open('data/scienceQ.json'))

model = SentenceTransformer('all-MiniLM-L6-v2')
questions = [db_question["question"] for db_question in knowledge_db]
question_embeddings = model.encode(questions)

# store the embeddings in a file
with open('data/DB_embeddings.txt', 'w') as f:
    json.dump(question_embeddings.tolist(), f)

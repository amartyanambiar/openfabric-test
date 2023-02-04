#openfabric-test

## Getting Started

1. Clone the repository to your local machine using
   //display in code block
   `git clone https://github.com/amartyanambiar/openfabric-test.git`
2. Change into the project directory
   `cd openfabric-test`
3. Install the required packages using pip
   `pip install -r requirements.txt`
4. Run the data parsing script(create embeddings). This step may take 3-5 minutes.
   `python parse_data.py`
5. Start the program using
   `./start.sh`

## Usage

Open the swagger-ui at http://127.0.0.1:5020/swagger-ui/ to test the API.
In the swagger-ui, you can provide sample questions for testing. For example:

- "What is H2O?"
- "What is the largest bone?"
- "What are the smallest arteries called?"

After passing a question in the terminal, you can see the confidence level of the answer and the support base for it in the console.

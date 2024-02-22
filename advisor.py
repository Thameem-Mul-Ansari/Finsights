from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "Your OpenAI API Key"


@app.route("/get_answer", methods=["POST"])
def get_answer():
    question = request.json["question"]

    # Call the answer_question function
    answer = answer_question(question)

    return jsonify({"answer": answer})


context = "At interest rates so low, should I instead take a loan, finance the house and invest my capital in the stock market? So last but not least, I'm in my 30s and can now afford to buy a house full cash without taking any debt. However, with interest rates so low and they wrote this one a while back, but should I take a loan anyway and finance the house and invest my capital in the stock market? I think this is interesting that rates could change the story. Going from a 3% mortgage rate to a 5% that hurdle changes. So nine months ago, I would have said you'd be nuts to pay full cash now. Maybe it kind of makes sense, but first of all, who does this person for having that amount of money? I don't really live to be able to buy and cash, but that's great. But so Matt, you're thinking through this type of decision with a client. And this is the kind of thing where there really is no right or wrong answer, right? A lot of this is personality driven and depending on what the person wants to get"


def answer_question(question):
    prompt = f"""Answer the following question using only the context below. Answer in the style of Ben Carlson, a financial advisor, and podcaster.

Context:
{context}

Q: {question}
A:"""

    # Specify the GPT-3.5-turbo model when making the API request
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Specify the GPT-3.5-turbo engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )["choices"][0]["text"].strip(" \n")

    return response


def main():
    st.title("Financial Advisor Q&A")

    # Input for user question
    question = st.text_area("Ask a question:")

    if st.button("Get Answer"):
        if question:
            # Call the answer_question function
            answer = answer_question(question)
            # Display the answer
            st.text_area("Answer:", answer)
        else:
            st.warning("Please enter a question.")


if __name__ == "__main__":
    app.run(debug=True)

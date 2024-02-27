from openai import OpenAI
import prompt 
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

question = "For school children, their teachers have more influence on their intelligence and social development than their parents. To what extent do you agree or disagree?"
answer = '''It is true that school children are at an impressionable age, and two strong influences on their intelligence and social development are teachers and parents. While I accept that teachers may have more influence on their pupils’ intelligence, I would argue that parents probably exert a greater influence on the social development of their children.

In terms of encouraging the intellectual development and stimulating the intelligence of school children, I believe that teachers play the major role. While not all teachers can inspire their students, they are trained to impart their knowledge of their subject areas in challenging and imaginative ways. For example, some students owe their lifelong love of a subject to dedicated teachers who taught this discipline in secondary school. Of course, at home, parents may also reinforce this passion by encouraging study habits during the formative years of their children. Such support is vital for academic achievement.

From the perspective of social development, I think that parents are mainly responsible for guiding their children. Firstly, they spend far more time with their children than any individual teacher is able to do. They can therefore monitor the activities of children outside school hours, at weekends and during holidays. Secondly, parents are able to provide role models in a whole range of situations. These might include showing respect towards elders, choice of friends, or proper behaviour in public when eating out in restaurants.
'''

def essay_assessment(question, answer, testing=True):
    if not testing:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"{prompt.WritingTask1}"},
                {"role": "user", "content": f"The question is: {question}.\n My answer is: \n{answer}"}
            ],
            temperature=0,
            seed=14024
        )
        json_response = json.loads(response.choices[0].message.content)
        json_object = json.dumps(json_response, indent=4)
        with open("response.json", "w") as f:
            f.write(json_object)
        return json_response  
    else:
        with open("response.json", "r") as f:
            json_response = json.load(f)
        print(testing)
        return json_response 
# essay_assessment(question, answer)
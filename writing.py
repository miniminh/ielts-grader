import relevant
import openAI
import grammar_vocab

question = "For school children, their teachers have more influence on their intelligence and social development than their parents. To what extent do you agree or disagree?"
answer = '''It is true that school children are at an impressionable age, and two strong influences on their intelligence and social development are teachers and parents. While I accept that teachers may have more influence on their pupils’ intelligence, I would argue that parents probably exert a greater influence on the social development of their children.

In terms of encouraging the intellectual development and stimulating the intelligence of school children, I believe that teachers play the major role. While not all teachers can inspire their students, they are trained to impart their knowledge of their subject areas in challenging and imaginative ways. For example, some students owe their lifelong love of a subject to dedicated teachers who taught this discipline in secondary school. Of course, at home, parents may also reinforce this passion by encouraging study habits during the formative years of their children. Such support is vital for academic achievement.

From the perspective of social development, I think that parents are mainly responsible for guiding their children. Firstly, they spend far more time with their children than any individual teacher is able to do. They can therefore monitor the activities of children outside school hours, at weekends and during holidays. Secondly, parents are able to provide role models in a whole range of situations. These might include showing respect towards elders, choice of friends, or proper behaviour in public when eating out in restaurants.
'''

def evaluation_scores(question, answer):
    grammar_errors, grammar_score = grammar_vocab.get_grammar_errors_and_grammar_scores(answer)

    print(f"Grammar Errors: {grammar_errors}")
    print(f"Vocabulary Score: {grammar_score:.2f}%")
    relevancy_score = relevant.relevant(question, answer)
    print('Relevancy Score: ', relevancy_score)

    response = openAI.essay_assessment(question, answer)
    band_score = response['band_score']
    feedback = response['feedback']
    print('Band score: ', band_score)
    band_score = (relevancy_score * 9 + grammar_score * 9 + band_score) / 3 - (grammar_errors * 0.25)

    print('Band score: ', band_score)

evaluation_scores(question, answer)
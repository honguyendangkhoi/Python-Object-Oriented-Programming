import requests

parameters={
    "amount":50,
    "catergory":24,
    "type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data=response.json()
question_data=data["results"]

# question_data = [
#     "results":{
#         {
#         "type":"boolean",
#         "difficulty":"medium",
#         "category":"History",
#         "question":"The Hundred Years; War was fought for more than a hundred years.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"],
#     },
#     {
#         "type":"boolean",
#         "difficulty":"easy",
#         "category":"History",
#         "question":"United States President John F. Kennedy was assassinated during his presidential motorcade in Atlanta, Georgia on November 22nd, 1963.",
#         "correct_answer":"False",
#         "incorrect_answers":["True"]},
#     },
#     {
#         "type":"boolean",
#         "difficulty":"easy",
#         "category":"History",
#         "question":"Vikings were the first Europeans to discover North America.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"],
#     },
#     {
#         "type":"boolean",
#         "difficulty":"easy",
#         "category":"History",
#         "question":"The United States of America declared their independence from the British Empire on July 4th, 1776.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"],
#     },
#     {
#         "type":"boolean",
#         "difficulty":"medium",
#         "category":"History",
#         "question":"The M41 Walker Bulldog remains in service in some countries to this day.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"]
#     },
#     {
#         "type":"boolean",
#         "difficulty":"medium",
#         "category":"History",
#         "question":"Ottoman Empire was created in 1299.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"]
#     },
#     {
#         "type":"boolean",
#         "difficulty":"easy",
#         "category":"History",
#         "question":"The Spitfire originated from a racing plane.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"]
#     },
#     {
#         "type":"boolean",
#         "difficulty":"medium",
#         "category":"History",
#         "question":"Augustus was the cousin of Julius Caesar. ",
#         "correct_answer":"False",
#         "incorrect_answers":["True"]
#     },
#     {
#         "type":"boolean",
#         "difficulty":"medium","category":"History",
#         "question":"Brezhnev was the 5th leader of the USSR.",
#         "correct_answer":"True",
#         "incorrect_answers":["False"]
#     },
#     {
#         "type":"boolean",
#         "difficulty":"hard",
#         "category":"History",
#         "question":"During the Winter War, the amount of Soviet Union soliders that died or went missing was five times more than Finland",
#         "correct_answer":"True",
#         "incorrect_answers":["False"]
#     }
#     "type":bool,
#     }
# ]
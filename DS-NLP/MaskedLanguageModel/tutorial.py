from transformers import (
    AutoModelForQuestionAnswering,
    AutoTokenizer,
    pipeline
)

nlp = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2"
)


# Contextual text or corpus
wikipedia_text = """
    Spider-Man is a superhero appearing in American comic books published by Marvel Comics. 
    Created by writer-editor Stan Lee and artist Steve Ditko, he first appeared in the anthology comic book Amazing Fantasy #15 (August 1962) in the Silver Age of Comic Books. 
    He has since been featured in movies, television shows, video games, and plays. 
    Spider-Man is the alias of Peter Parker, an orphan raised by his Aunt May and Uncle Ben in New York City after his parents Richard and Mary Parker died in a plane crash. 
    Lee and Ditko had the character deal with the struggles of adolescence and financial issues and gave him many supporting characters, such as Flash Thompson, J. Jonah Jameson and Harry Osborn, romantic interests Gwen Stacy, Mary Jane Watson and the Black Cat, and foes such as Doctor Octopus, the Green Goblin and Venom. 
    In his origin story, he gets spider-related abilities from a bite from a radioactive spider; these include clinging to surfaces, superhuman strength and agility, and detecting danger with his "spider-sense." 
    He also builds wrist-mounted "web-shooter" devices that shoot artificial spider webs of his own design.
    
    When Spider-Man first appeared in the early 1960s, teenagers in superhero comic books were usually relegated to the role of sidekick to the protagonist. 
    The Spider-Man series broke ground by featuring Peter Parker, a high school student from Queens behind Spider-Man's secret identity and with whose "self-obsessions with rejection, inadequacy, and loneliness" young readers could relate.[9] 
    While Spider-Man had all the makings of a sidekick, unlike previous teen heroes such as Bucky and Robin, Spider-Man had no superhero mentor like Captain America and Batman; he thus had to learn for himself that "with great power there must also come great responsibility"—a line included in a text box in the final panel of the first Spider-Man story but later retroactively attributed to his guardian, his late Uncle Ben Parker.
"""

# Define questions
questions = [
    {
        'question':'Who is Spiderman\'s enemy?',
        'context':wikipedia_text
    },
    {
        "question": "Who is Spiderman's romantic interest?",
        "context": wikipedia_text
    },
    {
        "question": "How did Spiderman relate to younger readers?",
        "context": wikipedia_text
    },
    {
        "question": "What were Spiderman's abilities?",
        "context": wikipedia_text
    }
]

for question in questions:
    print(f"Question: {question['question']}")
    result = nlp(question)
    print(f"Answer: {result['answer']}")
    print(f"Score: {result['score']}")
    print()

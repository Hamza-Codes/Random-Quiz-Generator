#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

# Step 1: Store the Quiz Data in a Dictionary - The first step is to create a skeleton script and fill it with your quiz data.

import random

# the quiz data - Keys are stats. Values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Step 2: Create the Quiz File and Shuffle the Question Order - 

# generate 35 random quiz files

for quizNum in range(35):
    # create the quiz file and answer key files.
    
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') # The filenames for the quizzes will be capitalsquiz<N>.txt, 
    # where <N> is a unique number for the quiz that comes from quizNum's for loop.
    
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')  # The answer key for capitalsquiz<N>.txt will 
    # be stored in a text file named capitalsquiz_answers<N>.txt.

    # Each time through the loop, the %s placeholder in 'capitalsquiz%s.txt' and 'capitalsquiz_answers%s.txt' will be 
    # replaced by (quizNum + 1),sothefirstquizandanswerkeycreatedwillbecapitalsquiz1.txt and capitalsquiz_answers1.txt. 


    # write the header for the quiz

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')  # creates a quiz header for the student to fill out. 
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1)) 
    quizFile.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states) # a randomized list of US states is created with the help of the random.shuffle() function


    # Step 3: Create the Answer Options - Generate the answer options for each question, which will be multiple choice from A to D.

    # loop through all the 50 states, making a question for each. 


    # This loop will loop through the states in the shuffled states list, from states[0] to states[49], find each state in 
    # capitals, and store that state’s corresponding capital in correctAnswer.
    
    
    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]] # The correct answer is easy to get—it’s stored as a value in the capitals dictionary

        wrongAnswers = list(capitals.values()) # The list of possible wrong answers is trickier. You can get it by duplicating all 
        # the values in the capitals dictionary
        
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # delete the correct answer
        
        wrongAnswers = random.sample(wrongAnswers, 3) # selecting three random values from the list. The random.sample makes this easy
        
        answerOptions = wrongAnswers + [correctAnswer] # The full list of answer options is the combination of these three wrong answers 
        # with the correct answers
        
        random.shuffle(answerOptions) # the answers need to be randomizedzso that the correct response isn’t always choice D.



# Step 4: Write Content to the Quiz and Answer Key Files - All that is left is to write the question to the quiz file and the 
# answer to the answer key file.

# Write the question and the answer options to the quiz file.

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

# Write the answer key to a file.

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))


    quizFile.close()
    answerKeyFile.close()
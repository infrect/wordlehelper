import pandas as pd

class WordleSolver:
    def __init__(self, word_lists):
        """
        Initialize the WordleSolver with a list of valid words.
        
        Args:
            word_list (list): A list of valid words.
        """
        self.word_list = word_lists.copy()
#        self.valid_words = valid_words
        self.answer = ['_'] * 5
        
    def apply_guess(self, guess, feedback):

        for i in range(0,5):
            print(f"Processing letter {i}: {guess[i]} with feedback {feedback[i]}")
            self.updatewordlist(guess[i], feedback[i], i)

        return self.word_list
    
    def updatewordlist(self, letter, feedback, index):

        new_word_list = []

        for word in self.word_list:
            if feedback == 'G':
                self.answer[index] = letter
                if word[index] == letter:
                    new_word_list.append(word)
            elif feedback == 'Y':
                if letter in word and word[index] != letter:
                    new_word_list.append(word)
            elif feedback == 'X':
                if letter not in word:
                    new_word_list.append(word)
#        print (new_word_list)
        self.word_list = new_word_list
    
#    def guess_information(self, guess, feedback):

    
    def get_word_list(self):
        """
        Get the current list of valid words.
        
        Returns:
            list: The current list of valid words.
        """
        return self.word_list

    def __str__(self):
        """
        Get a string representation of the current word list.
        
        Returns:
            str: A string representation of the current word list.
        """
        return ''.join(self.answer)
          
def main():
    df = pd.read_csv("valid_solutions.csv")
    words = [word.lower() for word in df['word'].tolist()]
    df = pd.read_csv("valid_guesses.csv")
    allvalidguesses = [word.lower() for word in df['word'].tolist()]
    df = pd.read_csv("past_answers.csv")
    past_answers = [word.lower() for word in df['word'].tolist()]
    for word in past_answers:
        if word in words:
            words.remove(word)
    solver = WordleSolver(list(set(words)))
    foundAnswer = False

    while foundAnswer == False:
        print("Enter your guess:")
        guess = input().strip().lower()
        print("Enter feedback:")
        feedback = input().strip().upper()

        print("Filtered words based on your guess and feedback:")
        valid_answers = solver.apply_guess(guess, feedback)
        if len(valid_answers) == 1:
            foundAnswer = True
            print(F"Answer is: {valid_answers}")
        else:
#            for word in df['word'].tolist():
            print(valid_answers)
            print("Current answer state:", solver)
      
   

if __name__ == "__main__":
    main()

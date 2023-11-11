from back.words_manager import load_pickle_list_of_words
import random as rd

def get_random_word_in_list_of_words_and_pop(list_of_words: list[str]) -> str:
    random_index = rd.randint(0, len(list_of_words)-1)
    chosen_word = list_of_words[random_index]
    list_of_words.remove(chosen_word)
    return chosen_word


def ask_if_already_seen() -> bool:
    answer = input("Already seen ? YN : ")
    while answer not in ["Y", "y", "N", "n"]:
        print("I do not understood you.")
        answer = input("Already seen ? YN : ")
    if answer in ["Y", "y"]:
        return True
    return False


class Word:
    def __init__(self, word, difficulty):
        self.word: str = word
        self.difficulty: int = difficulty
    def __repr__(self):
        return f"{self.word}, {self.difficulty}"


class Experiment:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.turn: int = 0
        self.pool_of_seen_words: list[Word] = []
        self.pool_of_unseen_words: list[str] = load_pickle_list_of_words()

    def update_pool_of_seen_words_difficulty(self, difficulty_modifier: int) -> None:
        for word in self.pool_of_seen_words:
            word.difficulty += difficulty_modifier
            if word.difficulty < 0:
                word.difficulty = 0
    
    def choose_next_word(self) -> Word:
        for word in self.pool_of_seen_words:
            if word.difficulty == 0:
                self.pool_of_seen_words.remove(word)
                return word
        next_word = get_random_word_in_list_of_words_and_pop(self.pool_of_unseen_words)
        self.pool_of_seen_words.append(Word(next_word, self.difficulty))
        return Word(next_word, self.difficulty)
        

    def next_turn(self):
        print(f"Tour num {self.turn}. Difficultee: {self.difficulty}")
        self.update_pool_of_seen_words_difficulty(-1)
        chosen_word = self.choose_next_word()
        print("###############################################")
        print("##")
        print(f"##########: {chosen_word.word}")
        print("##")        
        print("###############################################")
        answer = ask_if_already_seen()
        if chosen_word.difficulty == 0:
            self.update_pool_of_seen_words_difficulty(1)
            if answer:
                self.difficulty+=1
            else:
                self.difficulty -= 1
        self.turn += 1
    
    def play(self, n_turn: int):
        for i in range(0, n_turn):
            self.next_turn()


if __name__ == "__main__":
    experiment = Experiment(3)
    experiment.play(200)
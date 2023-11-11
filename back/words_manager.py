import pickle

RAW_WORDS = "data/list_fr_words.txt"
PICKLE_FILE = "back/dump_data/pickle_words.pkl"

def get_list_word_from_raw_txt() -> list[str]:
    all_words = open(RAW_WORDS)
    list_of_words = []
    for word in all_words:
        list_of_words.append(word.strip())
    return list_of_words


def create_pickle_of_list_of_words() -> None:
    list_of_words = get_list_word_from_raw_txt()
    with open(PICKLE_FILE, "wb") as output_file:
        pickle.dump(list_of_words, output_file)


def load_pickle_list_of_words() -> list[str]:
    with open(PICKLE_FILE, "rb") as input_file:
        list_of_words = pickle.load(input_file)
    return list_of_words


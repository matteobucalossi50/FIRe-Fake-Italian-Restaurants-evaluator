def read_file(filename):
    input_file_text = open(filename, encoding='utf-8').read()
    return input_file_text


def read_directory_files(directory):
    file_texts = []
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    for f in files:
        file_text = read_file(join(directory, f))
        file_texts.append(file_text)
    return file_texts


# creating a function menu_cleaner to clean the menus

def menu_cleaner(menu):
    menu = menu.replace('\n', ' ')
    menu = menu.replace('"', '')
    menu = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', menu)
    menu = menu.lower()

    return menu


# appending all the cleaned menus to a new list tabula_corpus_cleaned
def corpus_builder(Tabula_Corpus):
    Tabula_Corpus_Cleaned = []

    for m in Tabula_Corpus:
        m = menu_cleaner(m)
        Tabula_Corpus_Cleaned.append(m)
    return Tabula_Corpus_Cleaned


# Upload the retrieved menus from the directory
# dir_base = r"C:\Users\andre\Tabula Menus"
# Tabula_Corpus = read_directory_files(dir_base)

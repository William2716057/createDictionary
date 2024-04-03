import re

def extractWords(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        #Tokenize words and remove punctuation allowing characters '!' and '*'
        words = re.findall(r'\b[\w!*]+\b', content.lower())
        return set(words)
    #Save to dictionary.txt
def writeToDictionary(sorted_words):
    with open('dictionary.txt', 'w') as dictionary_file:
        for word in sorted_words:
            dictionary_file.write(word + '\n')

def main():
    file_path = input("Enter the path to the file: ")
    words = extractWords(file_path)
    sorted_words = sorted(words)
    writeToDictionary(sorted_words)
    print("Dictionary created successfully.")

if __name__ == "__main__":
    main()

"""Word Frequency Counter."""


# In this program we will read a text file and and write code to output
# the frequency of words in the file. We will be able to see which words 
# appear most in a given piece of text. Feel free to use any text file
# or you can use the 'Zen Of Python' text file.

# To improve this code:
# - Could you rewrite the code to read multiple text files?
# - Could you write the frequency dictionary back to a text file?


def read_text_file(filename: str) -> str:
    """Read text file and return contents.

     Args:
        filename: This is the name of the file to be read.

    Returns:
       A string of characters.
    
    """
    with open(filename, mode="r") as text_file:
        return text_file.read()


def file_content_parser(text: str) -> list:
    """Parse raw file contents to leave only alphanumeric chars and spaces.
    
    This function parses the contents of the file by iterating over all
    characters in the file, and when an alphanumeric character or space
    is detected, it is concatenated to a new string. This new string
    is then split and returned as a list of lower-case words.


    Args:
        text: This is the raw string which comes from the text file.

    Returns:
       A parsed list of words.
    """
    desired_characters = ""

    for char in text:
        if char.isalnum() or char.isspace():
            desired_characters += char.lower()


    return desired_characters.split()


def frequency_dict_builder(parsed_words: list) -> dict:
    """Build dict. where keys are words with frequency as the value.
    
    This function accepts the list of parsed words, and iterates over them.
    If the word does not appear in the dict. it is added with a value of 1,
    if the word already appears then its value is incremented. The dictionary
    is then passed to the sorted function where it is sorted by value and returned.


    Args:
        parsed_words: This is the parsed list of words.

    Returns:
       A sorted dictionary.
    """
    word_dict = {}
    for word in parsed_words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))


# Define the filename here
filename = "zen_of_python.txt"

# This filename is passed to read_text_file which returns the contents to 'raw_contents' as a string.
raw_contents = read_text_file(filename)

# The string is then passed to 'file_content_parser' which cleans the string, and returns a list of parsed words.
parsed_words = file_content_parser(raw_contents)

# The parsed word list is sent to 'frequency_dict_builder' to return the frequency dictionary.
word_dict = frequency_dict_builder(parsed_words)


# Then we can use that dictionary to print the summary of the words in the text file!
for word, freq in word_dict.items():
    out_string = f"The Word '{word}' appears {freq} times" if freq > 1 else f"The Word '{word}' appears once."
    print(out_string)



    
        
        

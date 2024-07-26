import html

def html_entity_encode(string):
    """
    Encode a given string using HTML entity encoding.
    
    :param string: The input string to be HTML entity encoded.
    :return: The HTML entity encoded string.
    """
    encoded_string = ''.join(f'&#{ord(char)};' for char in string)
    return encoded_string

# Prompt the user to input the string they wish to HTML entity encode
user_input = input("Enter the string to be HTML entity encoded: ")

# Encode the string
encoded_string = html_entity_encode(user_input)

print(f"HTML entity encoded string: {encoded_string}")

def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    return text.find(word)

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)


text_processing_operations = {
    'word_count': word_count,
    'character_count': character_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    if operation not in text_processing_operations:
        raise ValueError("Invalid operation")
    
    text_func = text_processing_operations[operation]
    
    if operation in ['find_word', 'replace_word']:
        return text_func(text, **kwargs)
    else:
        return text_func(text)


text = "Hello world! This is a test text."

print(process_text(text, 'word_count'))
print(process_text(text, 'character_count'))
print(process_text(text, 'find_word', word='test'))
print(process_text(text, 'replace_word', old_word='test', new_word='sample'))

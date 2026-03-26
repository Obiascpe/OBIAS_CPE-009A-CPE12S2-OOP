def censor_sentence(sentence, bad_words):
    words = sentence.split()
    censored_words = []

    for word in words:
        clean_word = word.strip(".,!?;:").lower()
        
        if clean_word in bad_words:
            censored_word = "*" * len(word)
        else:
            censored_word = word
        
        censored_words.append(censored_word)

    return " ".join(censored_words)


# Example usage
sentence = "This is a bad example with ugly words."
bad_words = ["bad", "ugly"]

result = censor_sentence(sentence, bad_words)
print(result)
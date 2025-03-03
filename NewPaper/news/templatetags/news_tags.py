from django import template

register = template.Library()


@register.filter
def censor(value):
    # Список нежелательных слов (пример)
    bad_words = ['плохо', 'ужасно', 'негатив']

    words = value.split()
    censored_words = []

    for word in words:
        if word.lower() in bad_words:
            # Заменяем все буквы слова, кроме первой и последней, на *
            if len(word) > 2:
                censored_word = word[0] + '*' * (len(word) - 2) + word[-1]
            else:
                censored_word = word  # Если слово слишком короткое, оставляем как есть
        else:
            censored_word = word
        censored_words.append(censored_word)

    return ' '.join(censored_words)
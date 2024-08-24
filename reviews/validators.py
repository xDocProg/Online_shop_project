from django.core.exceptions import ValidationError


def validate_profanity(value):
    """ Проверка на наличие нецензурной лексики в тексте """

    try:
        with open('profanity_words.txt', 'r', encoding='utf-8') as file:
            profanity_words = [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        raise ValidationError("Файл с нецензурными словами не найден.")

    words = value.lower().split()

    for word in words:
        if word in profanity_words:
            raise ValidationError("Ваш отзыв содержит нецензурные слова.")
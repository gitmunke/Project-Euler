# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (
# one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.


def integer_to_words(number):    #from my good friend Bobby
    def digit_to_word(digit):
        if digit == 0:
            return ""
        if digit == 1:
            return "one"
        if digit == 2:
            return "two"
        if digit == 3:
            return "three"
        if digit == 4:
            return "four"
        if digit == 5:
            return "five"
        if digit == 6:
            return "six"
        if digit == 7:
            return "seven"
        if digit == 8:
            return "eight"
        if digit == 9:
            return "nine"

    if number == 1000:
        return "one thousand"
    if number >= 100:
        partial_answer = digit_to_word(number // 100) + ' hundred '
        if number % 100 != 0:
            partial_answer += 'and '
            return partial_answer + integer_to_words(number % 100)

    if number >= 20:
        if number <= 29:
            partial_answer = "twenty"
        elif number <= 39:
            partial_answer = "thirty"
        elif number <= 49:
            partial_answer = "forty"
        elif number <= 59:
            partial_answer = "fifty"
        elif number <= 69:
            partial_answer = "sixty"
        elif number <= 79:
            partial_answer = "seventy"
        elif number <= 89:
            partial_answer = "eighty"
        elif number <= 99:
            partial_answer = "ninety"

        if number % 10 != 0:
            partial_answer += '-' + digit_to_word(number % 10)

        return partial_answer

    if number < 10:
        return digit_to_word(number)

    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 14:
        return "fourteen"
    if number == 15:
        return "fifteen"
    if number == 16:
        return "sixteen"
    if number == 17:
        return "seventeen"
    if number == 18:
        return "eighteen"
    if number == 19:
        return "nineteen"

c = 0
char_total = 0
for i in range(1001):
    word = integer_to_words(i)
    word = word.replace(' ', '')
    word = word.replace('-', '')
    char_total += len(word)
    print(integer_to_words(i), char_total)
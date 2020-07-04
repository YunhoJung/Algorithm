# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution1(phone_book):
    answer = True

    phone_book.sort(key=len)
    pattern = phone_book[0]
    h = hash(pattern)
    to_be_checked = phone_book[1:]

    for phone in to_be_checked:
        if hash(phone[:len(pattern)]) == h:
            answer = False

    return answer

def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

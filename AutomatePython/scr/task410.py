def test410(lists):
    lists.insert(-1, ', and')
    for l in lists:
        print(l, end=' ')

spam = ['apples', 'bananas', 'tofu', 'cats']

test410(spam)
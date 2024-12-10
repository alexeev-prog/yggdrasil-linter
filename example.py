print('hello world')


s = {1, 2}
l = [1, 2,3 , 1, 3, 4]

def test2():
    for item in l:
        methods = {
            "GET", "PUT", "POST", 'POST'
        }
        if item in methods:
            print(item)


def main():
    for item in l:
        methods = {
            "GET", "PUT", "POST", 'PUT'
        }
        if item in methods:
            print(item)

main()

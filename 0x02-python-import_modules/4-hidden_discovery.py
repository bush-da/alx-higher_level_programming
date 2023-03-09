#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    avoid = "__"
    for i in dir(hidden_4):
        if avoid not in i:
            print("{}".format(i), end='\n')

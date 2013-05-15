"""
hello.py

this script takes no arguments (for now).
"""

def main():
    """
    main

    this does stuff all the time anytime any place
    """
    say_hello()
    say_hello('Cream Cheez')

def say_hello(name="World"):
    """
    say_hello

    this function will print out a nice hello world message
    """
    print('Hello, ' + name + '!')

def pig_sound():
    """
    pig_sound

    this function will return the sound of a pig
    """
    return 'oink!'

if __name__ == "__main__":
    main()

#!python3

#* 1: Implement a fibonacci series generator
#* I implemented it using classes


class Fibonacci:
    # Initialize the object with variables
    def __init__(self):
        self.__a = 1
        self.__b = 1
        # Initialize counter to track position in the series
        self.__counter = 0
        self.__bridge = 0

    # get next number in the fibonacci series
    def gen(self):
        while True:
            if self.__b == 1 and self.__counter < 2:
                # Logic to account for first two numbers in the series
                self.__counter += 1
                yield (self.__a)
            elif self.__counter >= 2:
                self.__bridge = self.__a + self.__b
                self.__a = self.__b
                self.__b = self.__bridge
                self.__counter += 1
                yield self.__b

    @property
    def index(self):
        return self.__counter

    @property
    def position(self):
        return self.__b

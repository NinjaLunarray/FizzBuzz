'''The starting files are unrelated to the exercise.

They show examples of writing and testing
  o) a global function
  o) an instance method
Pick the style most suitable to your exercise.
'''


class FizzBuzz:
    
    def isFizz(self, n):
        return n % 3 == 0
    
    def isFizzBuzz(self, n):
        return n % 15 == 0

    def isBuzz(self, n):
        return n % 5 == 0

    def answer(self, n):
        if self.isFizzBuzz(n):
            return 'FizzBuzz'
        elif self.isFizz(n):
            return 'Fizz'
        elif self.isBuzz(n):
            return 'Buzz'
        return n

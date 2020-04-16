#Lab 3.1
#Davydenko Ilya
#IV-73

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def is_square(x):

    ''' The function of a square number '''

    return (int(x ** 0.5)) ** 2 == x


def prime_number(n):

    ''' Function of prime number '''

    a = 2
    while n % a != 0:
        a += 1
    return a == n


def ferma_factorize(n, counter=100):

    ''' The Farm factorization function and processing of all cases when numbers are enteredа '''

    if prime_number(n):
        return 1, n, 'It's a prime number'

    if n <= 1:
        return None, None, 'Error: Number must be greater than 0'

    if n % 2 == 0:
        return None, None, 'Error: The number must be odd'

    if is_square(n):
        return int(n ** 0.5), int(n ** 0.5), 'The operation was successful!'

    x = int(n ** 0.5) + 1
    c = 0
    while not is_square(x * x - n):
        x += 1
        c += 1
        if c > counter:
            return None, None, 'Error! \ nTask not counted'
    y = int((x * x - n) ** 0.5)
    a, b = x - y, x + y
    return a, b, 'The operation was successful!'


class Container(GridLayout):

   
    def calculation(self):

        try:

            inp_number = int(self.text_input.text)
            a, b, c = ferma_factorize(inp_number, int(self.count_input.text))
            self.first_number.text, self.second_number.text, self.state_factorization.text = str(a), str(b), c

        except:
            self.state_factorization.text = 'ncorrect input'


class Lab3_1App(App):


    def build(self):


        return Container()


if __name__ == "__main__":

    '''Running the program'''

    Lab_3.1App().run()
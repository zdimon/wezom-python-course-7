class Animal():
    color = 'red'
    size = 20

    def jump(self):
        print('jump jump')

    def say_your_color(self):
        print('my color is %s' % self.color)


class CanJump():
    def jump(self):
        print('I can jump')

class CanNotJump():
    def jump(self):
        print('I can NOT jump')

class Dog(Animal):
    def sound(self):
        print(f'gav gav {self.color}')

class Cat(Animal):
    def sound(self):
        print(f'mau {self.color}')

class WoodenCat(Animal):
    jump = CanNotJump()
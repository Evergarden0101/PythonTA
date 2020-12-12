class Dad:
    age = 0

    def __init__(self, a):
        self.age = a

    def talk(self):
        print('Dad')


class Mom:
    def talk(self):
        print('Mom')


class Baby(Mom, Dad):
    pass


baby = Baby(2)  # 继承上上层父类的属性
baby.talk()  # 可使用上上层父类的方法
baby.talk(super().talk)

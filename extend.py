class People:
    # 基本属性
    name = ''
    # 私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, n, w):
        self.name = n
        self.__weight = w

    def speak(self):
        print(self.name)


class Student(People):
    school = ''

    def __init__(self, n, w, s):
        # 调用父类的构函
        People.__init__(self, n, w)
        self.school = s

    # 覆写父类的方法
    def speak(self):
        print("%s,%s" % (self.school, self.name))
        super().speak()


s = Student('天山新泰罗', 100, '东京佛佛立第一中学')
s.speak()
super(Student, s).speak()
print(isinstance(s, People))

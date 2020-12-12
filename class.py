class People:
    # 定义基本属性
    name = '张三'
    age = 24
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 200

    def talk(self):
        print("%s: %d 岁，%d 斤" % (self.name, self.age, self.__weight))


# 实例化类
p = People()
p.talk()
print("%s: %d 岁" % (p.name, p.age))  # 无法访问__weight

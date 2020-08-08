#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'oo_work1'
__author__ = 'creamk'
__time__ = '2020/8/8 21:44'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def run(self):
        print("我是人，我会跑步")


class Man(Person):
    def __init__(self, name, gender, high, weight):
        super().__init__(name, gender)
        self.high = high
        self.weight = weight

    def introduce(self):
        print(f"我是{self.name}, 身高{self.high}, 体重{self.weight}")

    def run(self):
        print("我是男人，我跑的飞")


class Woman(Person):
    def __init__(self, name, gender, dress_cloth):
        super().__init__(name, gender)
        self.dress_cloth = dress_cloth

    def run(self):
        print(f"我叫{self.name}")
        print(f"我是女人，我穿{self.dress_cloth}慢慢跑")


person1 = Person("AD", "女")
person1.run()
man1 = Man("zhangwei", "男", "174cm", "80kg")
man1.introduce()
man1.run()
woman1 = Woman("heling", "女", "连衣裙")
woman1.run()

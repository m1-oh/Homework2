class introduce:
    def __init__(self, name, sex, height, weight):
        self.name = name
        self.sex = sex
        self.height = height
        self.weight = weight

    def info(self):
        print(f'이름:{self.name}')
        print(f'성별:{self.sex}')
        print(f'키:{self.height}')
        print(f'몸무게:{self.weight}')

name1 = input('무슨 이름? : ')
sex1 = input('성별이 뭐야? : ')
height1 = input('키는 몇이야? : ')
weight1 = input('몸무게는 몇이야? : ')

introduce1 = introduce(name1, sex1, height1, weight1)

introduce1.info()
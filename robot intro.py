class robot:

    species ="robot"
    def  __init__(self,name):
       self.name = name

tom = robot("tom")
jerry = robot("jerry")

print('tom:I am {}'.format(tom.name))
print('jerry: I am {}'.format(jerry.name))
       
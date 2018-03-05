#The Giraffe Shuffle
class Things:
    pass

class Animate(Things):
	pass
    
class Inanimate(Things):
	pass

class Sidewalks(Inanimate):
	pass

class Animals(Animate):
	pass

class Mammals(Animals):
	pass

class Giraffes(Mammals):
	pass

class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')

class Mammals(Animals):
	def feed_young_with_milk(self):
		print('feeding young')

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('eating leaves')

class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
class Giraffes(Mammals):
    def leftfootforward(self):
        print('left foot forward')
    def leftfootback(self):
        print('left foot back')
    def rightfootforward(self):
        print('right foot forward')
    def rightfootback(self):
        print('right foot back')
    def leftfootback(self):
        print('left foot back')
    def dance(self):
        self.leftfootforward()
        self.leftfootback()
        self.rightfootforward()
        self.rightfootback()
        self.leftfootback()
reginald = Giraffes()
reginald.dance()

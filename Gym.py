# Calculator for diets
class Human:
    def __init__(self,gender,weight,train):
        self.gender=gender
        self.weight=weight
        self.train=train
    def cpf_calculate(self,gender,weight,train):
        if (gender=="Man" and train<=4):
            cal=25*weight
            protein=2.3*weight
            carbohydrates=2.3*weight
            fats=0.7*weight
            print("You should consume: ",cal,"calories ",protein,"grams of protein ",carbohydrates,"grams of carbohydrates ",fats,"grams of fats ")
        elif ((gender=="Man" and train>=4)):
            cal = 32 * weight
            protein = 2.3 * weight
            carbohydrates = 3 * weight
            fats = 1.2 * weight
            print("You should consume: ", cal, "calories ", protein, "grams of protein ", carbohydrates,
                  "grams of carbohydrates ", fats, "grams of fats ")
        elif ((gender == "woman" and train <= 4)):
            cal = 22 * weight
            protein = 2.3 * weight
            carbohydrates = 1.8 * weight
            fats = 0.6 * weight
            print("You should consume: ", cal, "calories ", protein, "grams of protein ", carbohydrates,
                  "grams of carbohydrates ", fats, "grams of fats ")
        elif ((gender == "woman" and train >= 4)):
            cal = 29 * weight
            protein = 2.3 * weight
            carbohydrates = 3 * weight
            fats = 1.2 * weight
            print("You should consume: ", cal, "calories ", protein, "grams of protein ", carbohydrates,
                  "grams of carbohydrates ", fats, "grams of fats ")
g=str(input("Enter your gender: "))
w=int(input("Enter your weight: "))
k=int(input("Enter your number of workouts per week: "))

hum=Human(g,w,k)
hum.cpf_calculate(g,w,k)


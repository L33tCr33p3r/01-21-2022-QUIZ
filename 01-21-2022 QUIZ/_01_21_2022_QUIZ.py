#Segment 3 class
class Cheese:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.isMelted = False
    def melt(self):
        self.isMelted = True
    def printInfo(self):
        print(self.xPos)
        print(self.yPos)
        print(self.isMelted)

#Beginning of "Main"

#Segment 1
print("Enter your score")
tempVar = int(input())

if tempVar > 9000:
    print("IT'S OVER 9000!!!!!")
    print("That's amazing. Vegeeta(?) would be proud.")
    print()
elif tempVar < 100:
    print("Haha, get gud scrub-")
    print()
else:
    print("Keep practicing!")
    print()

#Segment 2
for i in range(10, 100, 5):
    print(i)

tempVar = 0
while i < 12:
    print("CHEESE")
    tempVar += 1
print()

#Segment 3

cheese1 = Cheese(10, 500)
cheese2 = Cheese(400, 300)
cheese3 = Cheese(600, 700)

cheese1.printInfo()
cheese2.printInfo()
cheese3.printInfo()

cheese1.melt()
cheese2.melt()
cheese3.melt()

cheese1.printInfo()
cheese2.printInfo()
cheese3.printInfo()
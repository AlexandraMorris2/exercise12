cheese = ['cheddar', "stilton", "cornish yarg"]
cheese += "oke"
print(cheese)

#in this case the oke is added as 3 seperate letters
#it should be like this:

cheese.append("oke")
print(cheese)

#to add more than one item with one command we do this:
cheese [:0] = ["brie", "edam"]
print(cheese)

#or to add the items to the end of the list:
cheese.extend(["gouda","wenslydale"])
print(cheese)
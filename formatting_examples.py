Name = "Horus"
Age = 25
Rank = 10

print("My Name is: " + Name)
# print("My Name is: " + Name + " and My Age is: " + Age)    int مع str تجمع عاوز علشان  Error هنا هيقولي 

               # " float أو int مع str لكن في طرق ممكن من خلالها تدمج الـ "

# %s => String
# %d => Number
# %f => Float

print("My Name is: %s and My Age is: %d" % (Name, Age))
print("My Name is: %s and My Age is: %d and My Rank is: %d" % (Name, Age, Rank))

print("________________________________________________\n")

# {  }                  .format()
# {:s} => String        .format()
# {:d} => Number        .format()
# {:f} => Float         .format()

n ="Mohammed"
l = "Python"
y = 3

print("My Name is {} Iam {} Developer With {} Years Exp".format(n, l, y))

# Or........

print("My Name is {:s} Iam {:s} Developer With {:d} Years Exp".format(n, l, y))

print("________________________________________________\n")

Name = "Mohammed"
Age = 25

print(f"My Name is: {Name} and My Age is: {Age}")

print("________________________________________________\n")

a, b, c = 10, 20, 30

print("Numbers is: {}, {}, {}".format(a, b, c))
print("Numbers is: {:d}, {:d}, {:d}".format(a, b, c))




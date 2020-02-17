#An Introduction to Lists

topics = ["Physics", "Computer Science", "Algebra", "Art"]
print(topics)
print(type(topics))

topics_2 = ["Algebra", "Physics", "Art", "Computer Science"]
print(topics_2)

print(topics + topics_2)
print(topics[0])

topics.append("biology")
print(topics)

color = []
color.append("red")
color.append("green")
color.append("blue")
print(color)
color.insert(1, "brown")
print(color[1])
print(color)
color[3] = "new_blue"
print(color)

print("\n")
new_topics = topics
print(new_topics)
new_topics.remove("Algebra")
print(new_topics)
bad_color = topics.pop(0)
print(bad_color)
del topics[2]
print(topics)

#fruits = []
#fruits.append(input("Enter:"))
#fruits.append(input("Enter:"))
#fruits.append(input("Enter:"))
#print(fruits)

print("\n")
print(topics_2)
print(sorted(topics_2))
print(sorted(topics_2, reverse=True))

print("\n")
print(topics_2)
length = len(topics_2)
print(length)
print(type(length))
topics_2.sort()
print(topics_2)
topics_2.reverse()
print(topics_2)











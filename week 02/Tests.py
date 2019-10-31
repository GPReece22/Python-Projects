scores = []

for result in range(4):
    scores.append((float(input("Please enter score " + str(result+1)))))

print("the highest score was ", max(scores))
print("the lowest score was ", min(scores))
print("the average score was ", sum(scores)/len(scores))
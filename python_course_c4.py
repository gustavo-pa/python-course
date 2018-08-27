edges=[]
for line in open("data/twitter.txt"):
    name_a, name_b=line.strip().split(";")
    edges.append((name_a,name_b))
# print(edges[:10])

def following(user,edges):
    followees=[]
    for follower, followee in edges:
        if follower == user:
            followees.append(followee)
    return followees
print(following("@Fox",edges))

%timeit following("@Fox", edges)
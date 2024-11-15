size=int(input("No. of favourite movies in the list: "))
movies=[]
for i in range(size):
    movies.append(input("Enter the movie: "))
print("The movie list is\n",movies)
from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)

  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 


print("The total number of different flower available in the dataset:", len(X))

y = iris.data.targets

print("The names of all different flowers in the dataset:")

for flower in iris.data.targets["class"].unique():
    print(flower)
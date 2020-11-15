bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) 

print(bicycles[0])

print(bicycles[0].title()) 

print(bicycles[1])
print(bicycles[3]) 

print(bicycles[-1])

print(bicycles[-1].lower())

print(bicycles[3].lower())

print(bicycles[-1] == bicycles[3]) 

print(bicycles[-4].lower() == bicycles[0].lower()) 

message = f"My first bicycle was a {bicycles[0].title()}."
print(message) 

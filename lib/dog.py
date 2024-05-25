class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Create an instance of the Dog class with only the name argument
fido = Dog("fido")
print(f"fido's breed: {fido.breed}")  

# Create another instance of the Dog class with both name and breed arguments
snoopy = Dog("snoopy", "Beagle")
print(f"snoopy's breed: {snoopy.breed}")  

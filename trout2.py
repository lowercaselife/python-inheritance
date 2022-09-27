from fish import Fish

class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)


terry = Trout()

# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
print(terry.water)

# Use parent swim() method
terry.swim()

print(terry.first_name)
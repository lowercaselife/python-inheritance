from fish import Fish


class Trout(Fish):
    pass

terry = Trout("Terry")



print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

terry.live_with_anemone()

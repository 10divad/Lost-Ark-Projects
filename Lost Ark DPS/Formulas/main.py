# test formula and dictionaries for skills
# important variables: atkinput, atkpower

atkinput=input("whats your atk power?")

try:
    atkpower=int(atkinput)

except ValueError:
    print("please input a proper value")

skill_level=input("whats your skill level")

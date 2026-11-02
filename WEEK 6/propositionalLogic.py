from itertools import product

print("P Q R | Q->P | P->~Q | QvR | KB")
print("-" * 39)

models = []

for P, Q, R in product([True, False], repeat=3):
    sentence1 = (not Q) or P       # Q -> P
    sentence2 = (not P) or (not Q) # P -> ~Q
    sentence3 = Q or R             # Q v R

    KB = sentence1 and sentence2 and sentence3

    print(
        f"{int(P)} {int(Q)} {int(R)} |"
        f"   {int(sentence1)}  |"
        f"   {int(sentence2)}   |"
        f"  {int(sentence3)}  |"
        f"  {int(KB)}"
    )

    if KB:
        models.append((P, Q, R))

print("\nModels of KB:")
for model in models:
    print(f"P={int(model[0])}, Q={int(model[1])}, R={int(model[2])}")

# Check entailment: KB entails X if X is true in every model of KB
entails_R = all(R for P, Q, R in models)
entails_R_implies_P = all((not R) or P for P, Q, R in models)
entails_Q_implies_R = all((not Q) or R for P, Q, R in models)

print("\nAnswers:")
print("ii) Does KB entail R?", entails_R)
print("iii) Does KB entail R -> P?", entails_R_implies_P)
print("iv) Does KB entail Q -> R?", entails_Q_implies_R)

import re

# ---------------------------------------
# FIRST ORDER LOGIC - FORWARD CHAINING
# ---------------------------------------
print("Ayush R Kallingal\n1WN24CS057")

def parse_atom(text):
    match = re.fullmatch(
        r"\s*([A-Za-z_]\w*)\s*\((.*?)\)\s*",
        text
    )

    if not match:
        raise ValueError(f"Invalid statement: {text}")

    predicate = match.group(1)
    args = tuple(x.strip() for x in match.group(2).split(","))

    if args == ("",):
        args = ()

    return predicate, args


def is_variable(value):
    return value[0].islower()


def unify(pattern, fact, bindings):
    if pattern[0] != fact[0] or len(pattern[1]) != len(fact[1]):
        return None

    result = bindings.copy()

    for p, f in zip(pattern[1], fact[1]):

        if is_variable(p):
            if p in result:
                if result[p] != f:
                    return None
            else:
                result[p] = f

        elif p != f:
            return None

    return result


def substitute(atom, bindings):
    predicate, args = atom

    new_args = tuple(bindings.get(x, x) for x in args)

    # Only infer fully instantiated facts
    if any(is_variable(x) for x in new_args):
        return None

    return predicate, new_args


def find_matches(premises, facts):
    if not premises:
        yield {}
        return

    def search(index, bindings):
        if index == len(premises):
            yield bindings
            return

        premise = premises[index]

        for fact in list(facts):
            matched = unify(premise, fact, bindings)

            if matched is not None:
                yield from search(index + 1, matched)

    yield from search(0, {})


def forward_chaining(kb):
    facts = set()
    rules = []

    # Read facts and rules
    for line in kb.splitlines():
        line = line.strip()

        if not line:
            continue

        if "->" in line:
            left, right = line.split("->", 1)

            premises = [
                parse_atom(x)
                for x in left.split("&")
            ]

            conclusion = parse_atom(right)

            rules.append((premises, conclusion))

        else:
            facts.add(parse_atom(line))

    print("\nInitial Facts:")
    for fact in sorted(facts):
        print(fact)

    # Forward chaining until no new facts are generated
    changed = True

    while changed:
        changed = False
        new_facts = set()

        for premises, conclusion in rules:

            for bindings in find_matches(premises, facts):

                inferred = substitute(conclusion, bindings)

                if inferred is not None and inferred not in facts:
                    new_facts.add(inferred)

        if new_facts:
            print("\nNewly Inferred Facts:")

            for fact in sorted(new_facts):
                print(fact)

            facts.update(new_facts)
            changed = True

    return facts


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

print("=" * 50)
print(" FIRST ORDER LOGIC - FORWARD CHAINING")
print("=" * 50)

print("\nEnter Knowledge Base.")
print("Enter one fact or rule per line.")
print("Type END when the knowledge base is complete.\n")

kb_lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    if line.strip():
        kb_lines.append(line)

kb = "\n".join(kb_lines)

# Generate all possible inferences
knowledge = forward_chaining(kb)

print("\n" + "=" * 50)
print(" KNOWLEDGE BASE READY")
print("=" * 50)

# Continuously accept queries
while True:

    query = input("\nEnter statement to prove (or EXIT): ").strip()

    if query.upper() == "EXIT":
        print("\nExiting Forward Chaining Program.")
        break

    try:
        statement = parse_atom(query)

        if any(is_variable(x) for x in statement[1]):
            print("Please enter a ground statement (no variables).")
            continue

        print("\nQuery:", query)

        if statement in knowledge:
            print("RESULT: TRUE")
            print("PROOF: The statement is supported by the Knowledge Base.")
        else:
            print("RESULT: FALSE")
            print("PROOF: The statement cannot be inferred from the Knowledge Base.")

    except ValueError as error:
        print("Invalid input:", error)

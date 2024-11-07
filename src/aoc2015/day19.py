from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_19(DayBase):
    YEAR = "2015"
    DAY = "19"


def matchall(theList, value):
    for i, x in enumerate(theList):
        if x == value:
            yield i


def replacement(atoms, transitions):
    outputs = set()
    for (t0, t1) in transitions:
        length = len(t0)
        for pos in matchall(atoms, t0):
            new_atoms = atoms[:pos] + t1 + atoms[pos + 1 :]
            outputs.add("".join(new_atoms))
    return len(outputs)


def stringToAtoms(string):
    atoms = []
    while string:
        if len(string) > 1 and string[1].islower():
            count = 2
        else:
            count = 1
        atoms.append(string[:count])
        string = string[count:]
    print(atoms, list(reversed(atoms)))
    return list(reversed(atoms))


class TransitionCandidate:
    def __init__(self, start, end, sub, length):
        self.start = start
        self.end = end
        self.sub = sub
        self.length = length

    def __repr__(self):
        return "{} {} {}".format(self.start, self.end, self.sub)


class AtomList:
    def __init__(self, atoms, transitions, raw=True):

        if raw:
            self.atoms = atoms.copy()
            self.transitions = transitions
            self.atoms = ["Start"] + self.atoms + ["End"]
            for t in range(len(self.transitions)):
                (t0, t1) = self.transitions[t]
                if t0 == "e":
                    self.transitions[t] = (t0, ["Start"] + t1 + ["End"])

            self.count = len(self.atoms)
            self.forward = [(i + 1) for i in range(self.count)]
            self.backward = [(i - 1) for i in range(self.count)]
            self.forward[-1] = None
            self.backward[0] = None

            self.initialiseTransitionCandidates()

    def print_state(self):
        string = ""
        i = self.forward[0]
        # i None case happens when we just have e
        while i != None and self.atoms[i] != "End":
            string += "{}({}) ".format(self.atoms[i], i)
            i = self.forward[i]
        print(string)
        print(self.candidates)
        print("length ", self.count)

    def copy(self, candidates_to_disregard):
        new_list = AtomList(self.atoms, self.transitions, False)
        new_list.atoms = self.atoms.copy()
        new_list.transitions = self.transitions
        new_list.forward = self.forward.copy()
        new_list.backward = self.backward.copy()
        new_list.candidates = self.candidates[candidates_to_disregard:].copy()
        new_list.count = self.count
        return new_list

    def initialiseTransitionCandidates(self):
        self.candidates = []
        for pos in range(self.count):
            for (t0, t1) in self.transitions:
                if pos + len(t1) < self.count:
                    ok = True
                    for j in range(0, len(t1)):
                        if self.atoms[pos + j] != t1[j]:
                            ok = False
                            break
                    if ok:
                        self.candidates.append(
                            TransitionCandidate(pos, pos + len(t1) - 1, t0, len(t1))
                        )

    def perform_sub(self, cand):
        end_next = self.forward[cand.end]
        self.atoms[cand.start] = cand.sub
        self.forward[cand.start] = end_next
        if end_next != None:
            self.backward[end_next] = cand.start

        # Remove candidates which are now invalid
        new_candidates = []
        for c in self.candidates:
            if c.end < cand.start or c.start > cand.end:
                new_candidates.append(c)

        self.candidates = new_candidates

        # And add new candidates based on this element
        for (t0, t1) in self.transitions:
            for j in range(0, len(t1)):
                if cand.sub == t1[j]:
                    ok = True
                    pos = cand.start
                    for i in range(j - 1, -1, -1):
                        pos = self.backward[pos]
                        if pos == None or self.atoms[pos] != t1[i]:
                            ok = False
                            break
                    if ok:
                        new_start = pos
                        pos = cand.start
                        for i in range(j + 1, len(t1)):
                            pos = self.forward[pos]
                            if pos == None or self.atoms[pos] != t1[i]:
                                ok = False
                                break
                        if ok:
                            self.candidates.append(
                                TransitionCandidate(new_start, pos, t0, len(t1))
                            )

        self.count += 1 - cand.length

    def recurse(self, steps, best):
        # TODO: this is a cheat based on patterns.
        if best:
            return best
        print("Steps: ", steps, best)
        self.print_state()
        if self.single_electron():
            return steps
        if steps == best:
            return best
        for c in range(len(self.candidates)):
            cand = self.candidates[c]
            if steps < 50:
                print("Iterating at: ", steps, c, len(self.candidates))
            new_list = self.copy(c + 1)
            new_list.perform_sub(cand)
            score = new_list.recurse(steps + 1, best)
            if best == None or score < best:
                best = score
        return best

    def single_electron(self):
        # Actually just electron first, but we configure things so we can't get here
        # otherwise
        return self.forward[0] == None


# TODO: look at patterns and do a new parser


def minCount(atoms, transitions):
    atom_list = AtomList(atoms, transitions)
    atom_list.print_state()
    return atom_list.recurse(0, None)
    return 0


def part_a(input, part_b=False):
    part_a = not part_b
    transitions = []
    transitions_collection = True
    for line in input_generator(input):
        if transitions_collection:
            if line == "":
                transitions_collection = False
            else:
                fields = line.split(" => ")
                transitions.append((fields[0], stringToAtoms(fields[1])))
        else:
            if part_a:
                return replacement(stringToAtoms(line), transitions)
            else:
                return minCount(stringToAtoms(line), transitions)


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2015_19().run_cmdline()

# Idea: at top level work out a list of first steps. Take the best one, come up with a new list below. Backtrack and ensure we block out rejected ones. Also never do an e one unless that's everything.
# Parsing in such a way that we break into the elements first might be nice, but not essential.

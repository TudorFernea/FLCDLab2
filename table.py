class HashTable:
    def __init__(self):
        self.capacity = 6151
        self.size = 0
        self.table = {}


    def insert(self, key, value):
        position = hash(key)
        self.size += 1

        if position not in self.table:
            self.table[position] = []

        self.table[position].append((key,value))

    def get(self, key):
        position = hash(key)

        if position not in self.table:
            return -1

        for pair in self.table[position]:
            if pair[0] == key:
                return pair[1]

        return -1

    def hash(self, key):
        hashsum = 0
        for c in enumerate(key):
            hashsum += ord(c)
        return hashsum % self.capacity

    def __str__(self):
        res = ""
        entries = []

        for t in self.table.values():
            for entry in t:
                entries.append(entry)

        entries.sort(key=lambda x: x[1])

        for entry in entries:
            res += str(entry) + "\n"

        return res


""""
symtable = HashTable()

symtable.insert("ab","num")
symtable.insert("ba","num")
symtable.insert("abcd","list")

print(symtable.get("ba"))
"""
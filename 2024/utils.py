class Input:
    def __iter__(self, input_file : str):
        self.i = 0
        with open(input) as f:
            lines = f.readlines()
            self.max=len(lines)
            return self

    def __next__(self):
        x = self.i
        self.i += 1
        if x < self.max:
            return x.rstrip()


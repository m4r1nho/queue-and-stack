class Queue:
    def __init__(self, vector):  #
        self.vector = vector

    # ↓ function to create a stack
    def create_stack(self):
        size = int(input("What the size? "))  # Entering the size
        for i in range(size):  # loop
            n = float(input(f"Enter the value {i + 1}: "))  # the value for position
            self.vector.append(n)  # adding in the vector
        return self.vector

    # ↓ function to add in stack, increase the stack
    def function_add(self):
        new_value = float(input("Enter the new value: "))  # the new and last value
        self.vector.append(new_value)  # adding in the vector
        return self.vector

    # ↓ “First in, first out” (FIFO)
    def function_remove(self):
        print("Removing value ")
        self.vector.pop(0)
        return self.vector

    # ↓ checking the top
    def function_confer(self):
        print(self.vector)
        if len(self.vector) > 0:
            top_value = self.vector[0]
            print(f'In the top:{top_value} ')

    # cleaning it
    def function_clean(self):
        print("Cleaning ")
        self.vector = []
        return self.vector

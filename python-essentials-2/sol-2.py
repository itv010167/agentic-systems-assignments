class StudentScores:
    def __init__(self, scores):
        """Takes a list of scores as input."""
        self.scores = scores

    def highest_last_two(self):
        """Finds the highest score among the last two using negative indexing."""
        try:
            # Using negative indexing: -1 is the last-2 is the second to last
            last_two = [self.scores[-2], self.scores[-1]]
            highest = max(last_two)
            print(f"Highest score among last two is: {highest}")
        except IndexError:
            # Handles cases where the list has less than 2 items
            print("Not enough scores to find highest value")

# --- Example Usage ---
# Case 1: Example Input
scores1 = [45, 67, 89, 72]
s1 = StudentScores(scores1)
s1.highest_last_two() # Output: Highest score among last two is: 89

# Case 2: Less than 2 scores
scores2 = [50]
s2 = StudentScores(scores2)
s2.highest_last_two() # Output: Not enough scores to find highest value

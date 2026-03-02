class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            # Using negative indexing for the last score
            difference = self.scores[-1] - self.scores[0]
            print(f"Difference between last and first score is: {difference}")
        except (IndexError, TypeError):
            # Handles empty lists or invalid inputs
            print("No scores available to calculate difference")

# --- Example Usage ---
scores = [55, 65, 75, 85]
student1 = StudentPerformance(scores)
student1.score_difference()  # Output: Difference between last and first score is: 30

# --- Edge Case: Empty List ---
empty_student = StudentPerformance([])
empty_student.score_difference() # Output: No scores available to calculate difference

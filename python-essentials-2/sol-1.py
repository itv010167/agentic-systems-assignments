class StudentMarks:
    def __init__(self, marks):
        """
        Initializes the StudentMarks object with a list of marks.
        """
        self.marks = marks

    def last_three_avg(self):
        """
        Calculates and prints the average of the last three marks using negative indexing.
        Handles lists with less than 3 marks using exception handling.
        """
        try:
            # Check if the list has at least 3 elements
            if len(self.marks) < 3:
                # Intentionally cause an IndexError if condition not met, 
                # or handle explicitly to print a custom message.
                # Here we raise an error to be caught by the except block for demonstration.
                raise IndexError("List has less than 3 marks")
            
            # Use slicing with negative indexing to get the last three marks
            last_three = self.marks[-3:]
            
            # Calculate the average
            average = sum(last_three) / len(last_three)
            
            print(f"Average of last 3 marks is: {average:.1f}")
        
        except (IndexError, TypeError):
            # Catches the custom IndexError raised above, or any TypeError 
            # if the input list contains non-numeric values.
            print("Not enough marks to calculate average")

# Example Usage:

# Input 1: More than 3 marks
marks1 = [50, 60, 70, 80, 90]
student1 = StudentMarks(marks1)
student1.last_three_avg()

print("-" * 30)

# Input 2: Less than 3 marks (example for exception handling)
marks2 = [50, 60]
student2 = StudentMarks(marks2)
student2.last_three_avg()

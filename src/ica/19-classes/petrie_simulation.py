import random

class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee.
        """
        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0

    def __str__(self):
        """
        Produces a printable string format for this employee.
        (Optional modification included to show commenter status)
        """
        commenter_status = "Commenter" if self.will_comment else "Non-commenter"
        return (f"{self.gender:<5} ({commenter_status:^13}): "
                f"{self.comments_received} sexist comments received")

    def set_commenter_status(self, status):
        """
        Sets the will_comment attribute to the given boolean status.
        """
        self.will_comment = status

    def receive_sexist_comment(self):
        """
        Increments the count of comments received by this employee by one.
        """
        self.comments_received += 1

    def get_gender(self):
        """Returns the employee's gender."""
        return self.gender

    def get_commenter_status(self):
        """Returns True if the employee is a commenter, False otherwise."""
        return self.will_comment

    def get_comments_received(self):
        """Returns the number of comments received by the employee."""
        return self.comments_received


def print_employee_list(employee_list):
    """
    Takes in a list of Employee objects and prints each one.
    """
    for employee in employee_list:
        print(f"  {employee}")


def create_employees(num_employees):
    """
    Generates and returns a list of Employee objects with an 80/20
    male-to-female ratio. All employees are initially non-commenters.
    """
    num_men = int(num_employees * 0.8)
    num_women = num_employees - num_men

    employees = []
    for _ in range(num_men):
        employees.append(Employee("Man", False))
    for _ in range(num_women):
        employees.append(Employee("Woman", False))
    return employees


def create_commenters(employee_list):
    """
    Modifies the employee list in-place. Each employee has a 20% chance
    of being set as a commenter.
    """
    for employee in employee_list:
        if random.random() < 0.2:
            employee.set_commenter_status(True)


def generate_comments(employee_list):
    """
    Simulates one round of comments. Each commenter makes a sexist remark
    directed at a randomly chosen employee of a different gender.
    """
    men = [emp for emp in employee_list if emp.get_gender() == "Man"]
    women = [emp for emp in employee_list if emp.get_gender() == "Woman"]

    # Proceed only if there are members of both genders to target
    if not men or not women:
        return

    # Men comment on women
    for man in men:
        if man.get_commenter_status():
            target = random.choice(women)
            target.receive_sexist_comment()

    # Women comment on men
    for woman in women:
        if woman.get_commenter_status():
            target = random.choice(men)
            target.receive_sexist_comment()


def average_comments(employee_list):
    """
    Calculates the average number of comments received by men and women.
    Returns a tuple: (average_for_men, average_for_women).
    """
    male_comment_counts = []
    female_comment_counts = []

    for employee in employee_list:
        if employee.get_gender() == "Man":
            male_comment_counts.append(employee.get_comments_received())
        else:
            female_comment_counts.append(employee.get_comments_received())

    avg_male = sum(male_comment_counts) / len(male_comment_counts) if male_comment_counts else 0
    avg_female = sum(female_comment_counts) / len(female_comment_counts) if female_comment_counts else 0

    return avg_male, avg_female


def main():
    """
    Runs the main simulation.
    """
    num_employees = 100
    comment_iterations = 50

    print(f"--- Starting Petrie Multiplier Simulation ---")
    print(f"Population: {num_employees} (80% Men, 20% Women)")
    print(f"Commenter Probability: 20%")
    print(f"Comment Iterations: {comment_iterations}\n")

    # Step 1: Create the employee population
    employees = create_employees(num_employees)

    # Step 2: Assign commenter status
    create_commenters(employees)
    print("--- Initial Population (with commenters assigned) ---")
    print_employee_list(employees)
    print("-" * 50)

    # Step 3: Run the comment generation
    for i in range(comment_iterations):
        generate_comments(employees)

    print("\n--- Final Results After Simulation ---")
    print_employee_list(employees)
    print("-" * 50)

    # Step 4: Calculate and print the averages
    avg_men, avg_women = average_comments(employees)
    print("\n--- Average Comments Received ---")
    print(f"Average for Men:   {avg_men:.2f}")
    print(f"Average for Women: {avg_women:.2f}")


if __name__ == '__main__':
    main()

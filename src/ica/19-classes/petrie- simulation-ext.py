import random


class EmployeeExt:
    """
    An extended Employee class where each employee has a probability of
    making a sexist comment, rather than a fixed status.
    """

    def __init__(self, gender, comment_prob):
        self.gender = gender
        self.comment_probability = comment_prob
        self.comments_received = 0

    def __str__(self):
        prob_percent = self.comment_probability * 100
        return (f"{self.gender:<5} (Prob: {prob_percent:3.0f}%): "
                f"{self.comments_received} sexist comments received")

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender

    def get_comment_probability(self):
        return self.comment_probability

    def get_comments_received(self):
        return self.comments_received


def _assign_comment_prob(gender):
    """
    Helper function to create an EmployeeExt instance with a comment
    probability based on the specified distribution.
    """
    rand_val = random.random()
    if rand_val < 0.50:
        prob = 0.0  # 50%
    elif rand_val < 0.60:
        prob = 0.2  # 10%
    elif rand_val < 0.70:
        prob = 0.4  # 10%
    elif rand_val < 0.80:
        prob = 0.6  # 10%
    elif rand_val < 0.90:
        prob = 0.8  # 10%
    else:
        prob = 1.0  # 10%
    return EmployeeExt(gender, prob)


def create_employees_ext(num_employees):
    """
    Generates a list of EmployeeExt objects with an 80/20 male-to-female
    ratio and assigns comment probabilities based on the extension rules.
    """
    num_men = int(num_employees * 0.8)
    num_women = num_employees - num_men

    employees = []
    for _ in range(num_men):
        employees.append(_assign_comment_prob("Man"))
    for _ in range(num_women):
        employees.append(_assign_comment_prob("Woman"))
    return employees


def run_conversation_simulation(num_conversations, employee_list):
    """
    Runs the main simulation based on a number of conversations.
    """
    for _ in range(num_conversations):
        # Determine conversation size
        rand_val = random.random()
        if rand_val < 0.30:
            size = 2
        elif rand_val < 0.50:
            size = 3
        elif rand_val < 0.60:
            size = 4
        elif rand_val < 0.70:
            size = 5
        elif rand_val < 0.80:
            size = 6
        elif rand_val < 0.90:
            size = 7
        else:
            size = 8

        # Select random participants for the conversation
        participants = random.sample(employee_list, min(size, len(employee_list)))

        # Split participants by gender
        men = [p for p in participants if p.get_gender() == "Man"]
        women = [p for p in participants if p.get_gender() == "Woman"]

        # Men can comment if not outnumbered and women are present
        if len(men) >= len(women) and women:
            for man in men:
                if random.random() < man.get_comment_probability():
                    target = random.choice(women)
                    target.receive_sexist_comment()

        # Women can comment if not outnumbered and men are present
        if len(women) >= len(men) and men:
            for woman in women:
                if random.random() < woman.get_comment_probability():
                    target = random.choice(men)
                    target.receive_sexist_comment()


def average_comments_ext(employee_list):
    """
    Calculates the average number of comments received by men and women.
    Returns a tuple: (average_for_men, average_for_women).
    """
    male_counts = [e.get_comments_received() for e in employee_list if e.get_gender() == "Man"]
    female_counts = [e.get_comments_received() for e in employee_list if e.get_gender() == "Woman"]

    avg_male = sum(male_counts) / len(male_counts) if male_counts else 0
    avg_female = sum(female_counts) / len(female_counts) if female_counts else 0

    return avg_male, avg_female


def print_employee_list_ext(employee_list):
    """Helper to print the list of extended employees."""
    for emp in employee_list:
        print(f"  {emp}")


def main_ext():
    """Runs the extended simulation."""
    num_employees = 100
    num_conversations = 5000

    print(f"--- Starting Extended Petrie Multiplier Simulation ---")
    print(f"Population: {num_employees} (80% Men, 20% Women)")
    print(f"Number of Conversations: {num_conversations}\n")

    employees = create_employees_ext(num_employees)
    print("--- Initial Population (with comment probabilities) ---")
    print_employee_list_ext(employees)
    print("-" * 60)

    run_conversation_simulation(num_conversations, employees)

    print("\n--- Final Results After Simulation ---")
    print_employee_list_ext(employees)
    print("-" * 60)

    avg_men, avg_women = average_comments_ext(employees)
    print("\n--- Average Comments Received ---")
    print(f"Average for Men:   {avg_men:.2f}")
    print(f"Average for Women: {avg_women:.2f}")


if __name__ == '__main__':
    main_ext()
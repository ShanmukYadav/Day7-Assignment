"""Personal Finance Calculator for Employee Benefits Portal."""


def get_employee_inputs():
    """Collect and validate employee financial information."""

    name = input("Enter employee name: ").strip()

    while True:
        try:
            annual_salary = float(input("Enter annual salary (₹): "))
            if annual_salary <= 0:
                print("Salary must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    while True:
        try:
            tax_bracket = float(input("Enter tax bracket percentage (0-50): "))
            if not 0 <= tax_bracket <= 50:
                print("Tax must be between 0 and 50%.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    while True:
        try:
            monthly_rent = float(input("Enter monthly rent (₹): "))
            if monthly_rent <= 0:
                print("Rent must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    while True:
        try:
            savings_goal = float(input("Enter savings goal percentage (0-100): "))
            if not 0 <= savings_goal <= 100:
                print("Savings goal must be between 0 and 100%.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    return name, annual_salary, tax_bracket, monthly_rent, savings_goal


def calculate_financials(annual_salary, tax_bracket, monthly_rent, savings_goal):
    """Calculate monthly and annual financial values."""

    monthly_salary = annual_salary / 12
    tax_deduction = monthly_salary * (tax_bracket / 100)
    net_salary = monthly_salary - tax_deduction

    rent_ratio = (monthly_rent / net_salary) * 100 if net_salary > 0 else 0
    savings_amount = net_salary * (savings_goal / 100)
    disposable_income = net_salary - monthly_rent - savings_amount

    return {
        "monthly_salary": monthly_salary,
        "tax_deduction": tax_deduction,
        "net_salary": net_salary,
        "monthly_rent": monthly_rent,
        "rent_ratio": rent_ratio,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "annual_tax": tax_deduction * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }


def format_currency(amount):
    """Format number using Indian numbering system (lakhs/crores)."""
    amount_str = f"{amount:.2f}"
    integer_part, decimal_part = amount_str.split(".")

    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        parts = []

        while len(remaining) > 2:
            parts.insert(0, remaining[-2:])
            remaining = remaining[:-2]

        if remaining:
            parts.insert(0, remaining)

        formatted_integer = ",".join(parts) + "," + last_three
    else:
        formatted_integer = integer_part

    return f"₹{formatted_integer}.{decimal_part}"


def print_report(name, annual_salary, tax_bracket, savings_goal, financials):
    """Print a formatted financial summary report."""

    f = financials
    health_score = calculate_health_score(f, savings_goal)

    print("════════════════════════════════════════════")
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f"Employee : {name}")
    print(f"Annual Salary : {format_currency(annual_salary)}")
    print("────────────────────────────────────────────")
    print("Monthly Breakdown:")
    print(f"Gross Salary : {format_currency(f['monthly_salary'])}")
    print(f"Tax ({tax_bracket}%) : {format_currency(f['tax_deduction'])}")
    print(f"Net Salary : {format_currency(f['net_salary'])}")
    print(
        f"Rent : {format_currency(f['monthly_rent'])} "
        f"({f['rent_ratio']:.1f}% of net)"
    )
    print(f"Savings ({savings_goal}%) : {format_currency(f['savings_amount'])}")
    print(f"Disposable : {format_currency(f['disposable_income'])}")
    print("────────────────────────────────────────────")
    print("Annual Projection:")
    print(f"Total Tax : {format_currency(f['annual_tax'])}")
    print(f"Total Savings : {format_currency(f['annual_savings'])}")
    print(f"Total Rent : {format_currency(f['annual_rent'])}")
    print("────────────────────────────────────────────")
    print(f"Financial Health Score : {health_score}/100")
    print("════════════════════════════════════════════")

    f = financials

    print("════════════════════════════════════════════")
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f"Employee : {name}")
    print(f"Annual Salary : {format_currency(annual_salary)}")
    print("────────────────────────────────────────────")
    print("Monthly Breakdown:")
    print(f"Gross Salary : {format_currency(f['monthly_salary'])}")
    print(f"Tax ({tax_bracket}%) : {format_currency(f['tax_deduction'])}")
    print(f"Net Salary : {format_currency(f['net_salary'])}")
    print(
        f"Rent : {format_currency(f['monthly_rent'])} "
        f"({f['rent_ratio']:.1f}% of net)"
    )
    print(f"Savings ({savings_goal}%) : {format_currency(f['savings_amount'])}")
    print(f"Disposable : {format_currency(f['disposable_income'])}")
    print("────────────────────────────────────────────")
    print("Annual Projection:")
    print(f"Total Tax : {format_currency(f['annual_tax'])}")
    print(f"Total Savings : {format_currency(f['annual_savings'])}")
    print(f"Total Rent : {format_currency(f['annual_rent'])}")
    print("════════════════════════════════════════════")


def main():
    """Main program execution."""

    print("Enter details for Employee 1")
    name1, salary1, tax1, rent1, savings1 = get_employee_inputs()
    financials1 = calculate_financials(salary1, tax1, rent1, savings1)

    print("\nEnter details for Employee 2")
    name2, salary2, tax2, rent2, savings2 = get_employee_inputs()
    financials2 = calculate_financials(salary2, tax2, rent2, savings2)

    print("\n===== EMPLOYEE 1 REPORT =====")
    print_report(name1, salary1, tax1, savings1, financials1)

    print("\n===== EMPLOYEE 2 REPORT =====")
    print_report(name2, salary2, tax2, savings2, financials2)

    print("\n===== COMPARISON SUMMARY =====")
    score1 = calculate_health_score(financials1, savings1)
    score2 = calculate_health_score(financials2, savings2)

    print(f"{name1} Health Score : {score1}/100")
    print(f"{name2} Health Score : {score2}/100")

    if score1 > score2:
        print(f"{name1} has better financial health.")
    elif score2 > score1:
        print(f"{name2} has better financial health.")
    else:
        print("Both employees have equal financial health.")


def calculate_health_score(financials, savings_goal):
    """Calculate financial health score out of 100."""

    score = 0

    # Rent score (max 30)
    rent_ratio = financials["rent_ratio"]
    if rent_ratio < 30:
        score += 30
    elif rent_ratio < 40:
        score += 20
    elif rent_ratio < 50:
        score += 10

    # Savings score (max 40)
    if savings_goal >= 30:
        score += 40
    elif savings_goal >= 20:
        score += 30
    elif savings_goal >= 10:
        score += 20
    elif savings_goal > 0:
        score += 10

    # Disposable score (max 30)
    disposable_percent = (
        financials["disposable_income"] / financials["monthly_salary"]
    ) * 100

    if disposable_percent >= 30:
        score += 30
    elif disposable_percent >= 20:
        score += 20
    elif disposable_percent >= 10:
        score += 10

    return score

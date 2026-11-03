
class Employee:
    def __init__(self, first, last, ssn):
        self.first = first
        self.last = last
        self.ssn = ssn

    def earnings(self):
        raise NotImplementedError("Cannot call abstract method")


class SalariedEmployee(Employee):
    def __init__(self, first, last, ssn, salary):
        super().__init__(first, last, ssn)
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary >= 0:
            self.salary = salary
        else:
            raise ValueError("Invalid value")

    def earnings(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, first, last, ssn, hourly_wage, hours_worked):
        super().__init__(first, last, ssn)
        self.set_hourly_wage(hourly_wage)
        self.set_hours_worked(hours_worked)

    def set_hourly_wage(self, hourly_wage):
        if hourly_wage > 0:
            self.hourly_wage = hourly_wage
        else:
            raise ValueError("Το ποσό πρέπει να είναι μεγαλύτερο από 0.0")

    def get_hourly_wage(self):
        return self.hourly_wage

    def set_hours_worked(self, hours_worked):
        if 0.0 <= hours_worked <= 168.0:
            self.hours_worked = hours_worked
        else:
            raise ValueError("Το ποσό πρέπει να είναι μεταξύ 0.0 και 168.0")

    def get_hours_worked(self):
        return self.hours_worked

    def earnings(self):
        if self.get_hours_worked() <= 40:
            return self.get_hourly_wage() * self.get_hours_worked()
        else:
            overtime = self.get_hours_worked() - 40
            return 40 * self.get_hourly_wage() + overtime * self.get_hourly_wage() * 1.5


class CommissionEmployee(Employee):
    def __init__(self, first, last, ssn, gross_sales, commission_rate):
        super().__init__(first, last, ssn)
        self.set_gross_sales(gross_sales)
        self.set_commission_rate(commission_rate)

    def set_commission_rate(self, commission_rate):
        if 0.0 < commission_rate < 1.0:
            self.commission_rate = commission_rate
        else:
            raise ValueError("Το ποσό πρέπει να είναι μεταξύ 0.0 και 1.0")

    def get_commission_rate(self):
        return self.commission_rate

    def set_gross_sales(self, gross_sales):
        if gross_sales >= 0.0:
            self.gross_sales = gross_sales
        else:
            raise ValueError("Το ποσό πρέπει να είναι μεγαλύτερο ή ίσο με 0.0")

    def get_gross_sales(self):
        return self.gross_sales

    def earnings(self):
        return self.get_gross_sales() * self.get_commission_rate()


class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, first, last, ssn, gross_sales, commission_rate, base_salary):
        super().__init__(first, last, ssn, gross_sales, commission_rate)
        self.set_base_salary(base_salary)

    def set_base_salary(self, base_salary):
        if base_salary >= 0.0:
            self.base_salary = base_salary
        else:
            raise ValueError("Το ποσό πρέπει να είναι μεγαλύτερο ή ίσο με 0.0")

    def get_base_salary(self):
        return self.base_salary

    def earnings(self):
        return self.get_base_salary() + super().earnings()


# --- Δημιουργία αντικειμένων ---
e = SalariedEmployee("John", "Smith", "111-11-1111", 800.00)
h = HourlyEmployee("Karen", "Price", "222-22-2222", 16.75, 40)
c = CommissionEmployee("Sue", "Jones", "333-33-3333", 10000, 0.06)  # διόρθωσα 0.6 σε 0.06 (πιο ρεαλιστικό)
b = BasePlusCommissionEmployee("Bob", "Lewis", "444-44-4444", 5000, 0.04, 300)

print("Salaried Employee")
print(e.earnings())

print("\nHourly Employee")
print(h.earnings())

print("\nCommission Employee")
print(c.earnings())

print("\nBase Plus Commission Employee")
print(b.earnings())

print("\nTable elements")
table = [e, h, c, b]          # πρόσθεσα και το c

for emp in table:
    print(emp.earnings())

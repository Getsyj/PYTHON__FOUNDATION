class Shareholder:
    def __init__(self, name, shareholder_id, shares, company, contact):
        self.name = name
        self.shareholder_id = shareholder_id
        self.shares = shares
        self.company = company
        self.contact = contact

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.shareholder_id}")
        print(f"Shares: {self.shares}")
        print(f"Company: {self.company}")
        print(f"Contact: {self.contact}")
        print("-" * 30)

    def update_shares(self, new_shares):
        self.shares = new_shares
        print(f"{self.name}'s shares updated to {self.shares}")

    def calculate_value(self, price_per_share):
        total_value = self.shares * price_per_share
        print(f"Total value of shares: ₹{total_value}")
        return total_value

# Creating two objects
s1 = Shareholder("Alice", "SH101", 100, "TechCorp", "alice@email.com")
s2 = Shareholder("Bob", "SH102", 200, "BioLabs", "bob@email.com")

# Using class functions and data members
s1.display_info()
s1.update_shares(120)
s1.calculate_value(50)

s2.display_info()
s2.update_shares(250)
s2.calculate_value(60)

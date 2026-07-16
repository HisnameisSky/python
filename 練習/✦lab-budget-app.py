class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        
        title = f"{self.name:*^30}\n"
        
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:23}{amt:>7}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    
    spendings = []
    for category in categories:
        spend = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spend += abs(item["amount"])
        spendings.append(spend)
    
    total_spent = sum(spendings)

    percentages = []
    for spend in spendings:
        if total_spent > 0:
            percentage = (spend / total_spent) * 100
            percentages.append(int(percentage // 10) * 10)
        else:
            percentages.append(0)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
            
    return chart
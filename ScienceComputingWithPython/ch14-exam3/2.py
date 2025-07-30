class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0

    def __str__(self):
        header = self.description.center(30, "*") + "\n"
        line_end = f'Total: {self.get_balance()}'
        lines = self._print()
        return header + lines + '\n' + line_end
        
    def _print(self):
        lines = []
        for i in self.ledger:
            length = len(i['description'])
            if length >= 23:
                des = i['description'][:23]
            else:
                des = i['description'] + ' ' * (23 - length)

            amount_length = len('%.2f' % i['amount'])
            amount = ' ' * (7 - amount_length) + '%.2f' % i['amount']
            lines.append(des + amount)
        return '\n'.join(lines)

    def deposit(self, amount, description=""):
        """存钱"""
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        """取钱"""
        if self.check_funds(amount):
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        """查询余额"""
        return self.__balance

    def transfer(self, amount, category_instance):
        """转账"""
        if self.withdraw(amount, f"Transfer to {category_instance.description}"):
            category_instance.deposit(amount, f"Transfer from {self.description}")
            return True
        return False

    def check_funds(self, amount):
        """检查预算是否充足"""
        if self.__balance >= amount:
            return True
        return False
    
    def get_total_withdraw(self):
        """获取总支出金额"""
        withdraws = [i['amount'] for i in self.ledger if i['amount'] < 0]
        total = - sum(withdraws)
        return total


def create_spend_chart(categories):
    """创建开支表"""
    spent_amounts = [category.get_total_withdraw() for category in categories]

    total = sum(spent_amounts)
    spent_percentage = [int(((spent_amount / total * 10) // 1) * 10) for spent_amount in spent_amounts]

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += '%3d|' % value
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += " " * 3
        chart += " \n"

    footer = " "*4 + "-" * (3 * len(categories) + 1) + "\n"

    descriptions = [category.description for category in categories]
    max_length = max([len(description) for description in descriptions])
    descriptions = [description.ljust(max_length) for description in descriptions]

    for description in zip(*descriptions):
        footer += "    " + "".join(char.center(3) for char in description) + " \n"

    return (header + chart + footer).rstrip("\n") 

if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
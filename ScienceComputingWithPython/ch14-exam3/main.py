class Category:
    
    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        space_num1 = int((30 - len(self.category)) / 2)
        space_num2 = 30 - len(self.category) - space_num1
        line1 = f"{'*' * space_num1}{self.category}{'*' * space_num2}\n"
        line_end = f'Total: {self.get_balance()}'
        lines = self._print()
        return line1 + lines + '\n' + line_end
        
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
            

    def deposit(self, amount, description=''):
        """存款"""
        deposit_item = {
            'amount': amount,
            'description': description,
        }
        self.ledger.append(deposit_item)

    def withdraw(self, amount, description=''):
        """取款"""
        if self.check_funds(amount):
            amount = - amount
            withdraw_item = {
                'amount': amount,
                'description': description,
            }
            self.ledger.append(withdraw_item)
            return True
        else:
            return False

    def get_balance(self):
        """查询余额"""
        funds = [i['amount'] for i in self.ledger]
        balance = sum(funds)
        return balance

    def transfer(self, amount, category):
        """将本类别的预算转移一部分到其他类别"""
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
        

    def check_funds(self, amount):
        """检查预算是否充足"""
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True
        
    def get_total_withdraw(self):
        """获取总支出金额"""
        withdraws = [i['amount'] for i in self.ledger if i['amount'] < 0]
        total = - sum(withdraws)  # 转为正数表示支出
        return total


def create_spend_chart(categories):
    """创建支出百分比柱状图，修复格式问题"""
    # 计算每个类别的总支出
    withdraws = [category.get_total_withdraw() for category in categories]
    total = sum(withdraws)
    
    # 计算每个类别的支出百分比（向下取整到最近的10）
    percents = []
    for wd in withdraws:
        if total == 0:
            percent = 0
        else:
            percent = (wd / total) * 100  # 计算百分比
            percent = (percent // 10) * 10  # 向下取整到最近的10
        percents.append(percent)
    
    # 图表标题
    chart_lines = ["Percentage spent by category"]
    
    # 构建百分比行（从100到0）
    for percent in range(100, -1, -10):
        # 左侧百分比标签，确保3个字符宽度
        line = f"{percent:3d}|"
        # 为每个类别添加柱形
        for p in percents:
            if p >= percent:
                line += " o "
            else:
                line += "   "
        # 最后添加两个空格，确保每行长度一致
        line += "  "
        chart_lines.append(line)
    
    # 水平线：每个类别3个连字符，总长度超过最后一个柱子2个字符
    num_categories = len(categories)
    horizontal_line = "    " + "-" * (3 * num_categories) + "-"
    chart_lines.append(horizontal_line)
    
    # 类别名称（垂直显示）
    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        line = "    "  # 与百分比标签对齐（4个空格）
        for category in categories:
            if i < len(category.category):
                line += f" {category.category[i]} "
            else:
                line += "   "  # 空出位置保持对齐
        # 最后添加两个空格，确保与其他行长度一致
        line += "  "
        chart_lines.append(line)
    
    # 连接所有行并返回，确保末尾没有换行符
    return '\n'.join(chart_lines) + '\n'


if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    
    # 测试支出图表
    auto = Category('Auto')
    auto.deposit(1000)
    auto.withdraw(150)
    print(create_spend_chart([food, clothing, auto]))
    print(len(create_spend_chart([food, clothing, auto])))
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(create_spend_chart([food, clothing, auto]))
        
    
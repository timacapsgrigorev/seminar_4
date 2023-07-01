def atm():
    balance = 0
    operations_count = 0

    while True:
        print(f"Текущий баланс: {balance} у.е.")
        action = input("Выберите действие: пополнить, снять или выйти: ")

        if action.lower() == "выйти":
            print("Работа с банкоматом завершена.")
            break

        if action.lower() == "пополнить":
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма пополнения должна быть кратной 50 у.е.")
                continue

            balance += amount
            operations_count += 1
            if operations_count % 3 == 0:
                interest = balance * 0.03
                balance += interest

        elif action.lower() == "снять":
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма снятия должна быть кратной 50 у.е.")
                continue

            if amount > balance:
                print("Недостаточно средств на счете.")
                continue

            withdrawal_fee = min(max(amount * 0.015, 30), 600)
            balance -= amount + withdrawal_fee
            operations_count += 1
            if operations_count % 3 == 0:
                interest = balance * 0.03
                balance += interest

        else:
            print("Недопустимое действие. Пожалуйста, выберите пополнить, снять или выйти.")

        if balance > 5000000:
            wealth_tax = balance * 0.1
            balance -= wealth_tax

atm()

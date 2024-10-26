money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i=0
while money_capital>=0:
    if money_capital+salary>=spend*(1+increase)**(i):
        i+=1
    money_capital+=salary-spend*(1+increase)**(i-1)
print("Количество месяцев, которое можно протянуть без долгов:", i)

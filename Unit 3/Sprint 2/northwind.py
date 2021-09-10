"""For Unit 3 Sprint 2 Part 2;
Analyes data from northwind_small.sqlite3

Robert Davis
2021/09/10"""


import sqlite3


expensive_items = '''SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;'''


avg_hire_age = '''SELECT AVG(HireDate - BirthDate) as AverageHireAge
FROM Employee;'''


avg_age_by_city = '''SELECT City, AVG(AverageHireAge)
FROM (
    SELECT City, HireDate - BirthDate as AverageHireAge
    FROM Employee
    )
GROUP BY City;'''


ten_most_expensive = '''SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN (
    SELECT Id, CompanyName
    FROM Supplier
    ) as Sup
ON Product.SupplierId = Sup.Id
ORDER BY UnitPrice DESC
LIMIT 10;'''


largest_category = '''SELECT CategoryName, COUNT(CategoryName) AS Total
FROM Product
JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY Total DESC
LIMIT 1;'''


most_territories = '''SELECT Id, LastName, FirstName, Territories
FROM Employee
JOIN (
    SELECT EmployeeId, COUNT(*) as Territories
    FROM EmployeeTerritory
    GROUP BY EmployeeId
    ) as EmpTerr
ON Employee.Id = EmpTerr.EmployeeId
ORDER BY Territories DESC
LIMIT 1;'''


if __name__ == '__main__':
    con = sqlite3.connect('/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/Sprint 2/northwind_small.sqlite3')
    cur = con.cursor()

    cur.execute(expensive_items)
    print('\033[34mTen Most Expensive:')
    for row in cur:
        print(row)
    print()

    cur.execute(avg_hire_age)
    for x in cur:
        print('\033[36mThe average hire age of employees is', x[0])
    print()

    cur.execute(avg_age_by_city)
    print('\033[34mAverage Age by City:')
    for city, age in cur:
        print(f'{city}: {age}')
    print()

    cur.execute(ten_most_expensive)
    print('\033[36mTen Most Expensive:')
    for row in cur:
        print(row)
    print()

    cur.execute(largest_category)
    for x in cur:
        print('\033[34mLargest Category:', x[0], 'with', x[1])
    print()

    cur.execute(most_territories)
    for x in cur:
        print('\033[36mEmployee with Most Territories:')
        print(x)

import json

def stats():
    branchNumber=int(input("Enter the number of company branches: "))
    
    #loop for each branches
    for i in range(branchNumber):
        employeeInBranch=(int(input("Enter the number of employee in branch {}: ".format(i+1))))
        avgSalaryInBranch=(float(input("Enter the average salary of employee in branch {}: ".format(i+1))))
        incomeOfBranch=(float(input("Enter the total income of branch {}: ".format(i+1))))
        expenseOfBranch=(float(input("Enter the total expenses of branch {}: ".format(i+1))))
        
        #calculation of net Income of a particular branch
        netIncomeofBranch=(incomeOfBranch)-(employeeInBranch × avgSalaryInBranch)-(expenseOfBranch)
        
        # Data to be written into json
        data = {
        "Branch" : i+1,
        "Employee In Branch" : employeeInBranch,
        "Average Salary of employees" : avgSalaryInBranch,
        "Total Income of Branch" : incomeOfBranch,
        "Total expense of Branch" : expenseOfBranch,
        "Net Income of Branch" : netIncomeofBranch
        }
        
        # we are saving all data to a json file using below lines
        with open("output.json", "w") as outfile:
            json.dump(data, outfile)

#calling stats function
stats()

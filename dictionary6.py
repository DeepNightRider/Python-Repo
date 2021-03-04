# Initialize dictionary with default values
# Given:
#
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

result=dict.fromkeys(employees,defaults)
print(result)

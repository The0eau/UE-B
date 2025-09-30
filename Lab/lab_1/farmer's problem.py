from pulp import LpProblem, LpMaximize, LpVariable, lpSum, listSolvers

# Data
profit = {'Wheat' : 170, 'Corn': 150, 'Sugar_Beet_under': 30, 'Sugar_Beet_over': 10}
planting_cost = {'Wheat' : 150, 'Corn': 230, 'Sugar_Beet': 260}
buy_cost = {'Wheat' : 238, 'Corn': 210, 'Sugar_Beet': 0}


# Initialize LpPb
prob = LpProblem("Farmer's problem", LpMaximize)

# Decision variables
x = LpVariable.dicts("Crops", planting_cost, lowBound=0)
y = LpVariable.dicts("Sell", profit, lowBound=0)
w = LpVariable.dicts("Buy", planting_cost, lowBound=0)

# Function to optimize
prob += (lpSum([profit[crop] * y[crop] for crop in profit])
        -lpSum([planting_cost[crop] * x[crop] + buy_cost[crop] * w[crop] for crop in planting_cost])), 'Total profit'

# Constraints
prob += lpSum([x[crop] for crop in planting_cost]) <= 500, "Land constraint"
prob += y['Wheat'] - 2.5*x['Wheat'] - w['Wheat'] <= -200, "Wheat production constraint"
prob += y['Corn'] - 3*x['Corn'] - w['Corn'] <= -240, "Corn production constraint"
prob += y["Sugar_Beet_under"] + y["Sugar_Beet_over"] <= 20*x["Sugar_Beet"], "Sugar Beet production constraint"
# Scenario +20%
# prob += y['Wheat'] - 2.5*1.20*x['Wheat'] - w['Wheat'] <= -200, "Wheat production constraint"
# prob += y['Corn'] - 3*1.20*x['Corn'] - w['Corn'] <= -240, "Corn production constraint"
# prob += y["Sugar_Beet_under"] + y["Sugar_Beet_over"] <= 20*1.20*x["Sugar_Beet"], "Sugar Beet production constraint"
# Scenario -20%
# prob += y['Wheat'] - 2.5*0.8*x['Wheat'] - w['Wheat'] <= -200, "Wheat production constraint"
# prob += y['Corn'] - 3*0.8*x['Corn'] - w['Corn'] <= -240, "Corn production constraint"
# prob += y["Sugar_Beet_under"] + y["Sugar_Beet_over"] <= 20*0.8*x["Sugar_Beet"], "Sugar Beet production constraint"
prob += y["Sugar_Beet_under"] <= 6000, "Quota"



status = prob.solve()
solver_list = listSolvers()
print(solver_list)

print(status)
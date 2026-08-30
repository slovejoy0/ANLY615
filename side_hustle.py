"""
ANLY 615: Week 1 Homework Assignment
File: side_hustle.py
Name: [Sheralee Lovejoy]
Purpose: Compute projected consulting earnings and goal achievement metrics.
"""

# --- CONFIGURATION VARIABLES ---
# We assume a freelance year consists of 48 operational weeks
WORKING_WEEKS_PER_YEAR = 48
# -------------------------------

# TODO 1: Print a professional business title header
# The header must display:
# =========================================
#       FREELANCE ANALYST CALCULATOR
# =========================================

print("=========================================")
print("      FREELANCE ANALYST CALCULATOR      ")
print("=========================================")


# TODO 2: Capture the user's inputs (Hustle Name, Rate, Hours, Goal)
# Strip all text inputs. Cast all numerical inputs to float types!
# Save as variables: hustle_name, hourly_rate, weekly_hours, savings_goal

hustle_name = input("What is the name of your side hustle? ").strip()
hourly_rate = float(input("What is your hourly rate? $"))
weekly_hours = float(input("How many hours do you plan to work per week? "))
savings_goal = float(input("What is your savings goal for the year? $"))

# TODO 3: Implement your business calculations
# Use the math formulas outlined in the assignment brief to calculate:
# weekly_revenue, annual_revenue, and weeks_to_goal

weekly_revenue = float(hourly_rate) * float(weekly_hours)
print(f"Weekly revenue is ${weekly_revenue:.2f}")
annual_revenue = float(weekly_revenue) * WORKING_WEEKS_PER_YEAR
print(f"Annual revenue is ${annual_revenue:.2f}")
weeks_to_goal = float(savings_goal) / float(weekly_revenue)
print(f"Weeks to goal is {weeks_to_goal:.1f}")

# TODO 4: Print the clean, formatted financial report
# Ensure your output format precisely matches the target output structure.
# Currency fields must display with 2 decimal places (:.2f)
# Time-to-goal must display with exactly 1 decimal place (:.1f)
#
# Target layout:
# =========================================
#        WEEKLY FINANCIAL PROJECTOR
# =========================================
# Service Type:       [hustle_name]
# Hourly Rate:        $[hourly_rate]/hr
# Estimated Hours:    [weekly_hours] hrs/week
# -----------------------------------------
# Weekly Gross:       $[weekly_revenue]
# Annual Projection:  $[annual_revenue]
# Target Savings Goal:$[savings_goal]
# -----------------------------------------
# To hit your goal, you must work for
# exactly [weeks_to_goal] consecutive weeks.
# =========================================

print("=========================================")
print("        WEEKLY FINANCIAL PROJECTOR       ")
print("=========================================")
print(f"Service Type:       {hustle_name}")
print(f"Hourly Rate:        ${hourly_rate:.2f}/hr")
print(f"Estimated Hours:    {weekly_hours} hrs/week")
print("-----------------------------------------")
print(f"Weekly Gross:       ${weekly_revenue:.2f}")
print(f"Annual Projection:  ${annual_revenue:.2f}")
print(f"Target Savings Goal:${savings_goal:.2f}")
print("-----------------------------------------")
print(f"To hit your goal, you must work for")
print(f"exactly {weeks_to_goal:.1f} consecutive weeks.")
print("=========================================")

"""
ANLY 615: Week 1 In-Class Assignment
File: aggie_profile.py
Name: [Sheralee Lovejoy]
"""

# --- CONFIGURATION VARIABLES ---
# We want to project where our career stands in the milestone year of 2030


PROJECTED_YEAR = 2030
# -------------------------------

# TODO 1: Print a welcoming header to the terminal
# The header must display:
# =========================================
#       THE AGGIE NETWORK ONBOARDER
# =========================================
print("=========================================")
print("      THE AGGIE NETWORK ONBOARDER      ")
print("=========================================")

# TODO 2: Capture user inputs. Make sure to use strip() to clean up trailing spaces!
# Capture: Full Name, Undergraduate/Prior University, and Selected Industry (e.g., Tech, Finance)
# Save these inputs as: user_name, prior_school, target_industry

user_name = input("What is your full name? ").strip()
prior_school = input("What is your undergraduate/prior university? ").strip()
target_industry = input(
    "What is your selected industry (e.g., Tech, Finance)? ").strip()
# TODO 3: Capture the year the user joined the Aggie Family (their TAMU graduate cohort start year)
# Hint: You must cast this input to an integer to do mathematical calculations!
# Save this input as: cohort_year

cohort_year = int(PROJECTED_YEAR) - 4
print(f"Cohort year is {cohort_year}")

# TODO 4: Calculate the total years they will have been part of the Aggie network by 2030
# Formula: network_years = PROJECTED_YEAR - cohort_year
network_years = int(PROJECTED_YEAR) - int(cohort_year)
print(f"Network years is {network_years}")

# TODO 5: Print the formatted Aggie Network Card
# Ensure your output matches this EXACT layout, substituting your variables inside f-strings!
# Note the indentation of the fields to align them vertically.
#
# =========================================
#            AGGIE NETWORK CARD
# =========================================
# Name:          [user_name]
# Prior School:  [prior_school]
# Target Sector: [target_industry]
# Cohort Year:   [cohort_year]
# By [PROJECTED_YEAR], you will have been an
# Aggie for [network_years] proud years!
# =========================================

print("=========================================")
print("            AGGIE NETWORK CARD           ")
print("=========================================")
print(f"Name:          {user_name}")
print(f"Prior School:  {prior_school}")
print(f"Target Sector: {target_industry}")
print(f"Cohort Year:   {cohort_year}")
print(f"By {PROJECTED_YEAR}, you will have been an")
print(f"Aggie for {network_years} proud years!")

""" solve cutomer query and provide prompt to llm in struture way """
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("city: ")
main_customer = input("Main Customer: ")
monthly_budget = int(input("Monthly Budget (PKR): "))
heading = """=========================================
   AI Prompt Kit for Sweet Crumbs
========================================= """

marketing= f"""[1] Marketing
Write a short Instagram post for {business_name}, a {business_type} in Lahore.
Target university students. Friendly tone, 1 call to action. """
customer_service = f""" [2] Customer Service
You are the manager of {business_name}. Write a polite reply to a customer
whose order arrived late. Apologise and offer a small discount."""
growth = f"""[3] Growth
Suggest 3 low-cost AI tools a bakery in {city} can use
to attract university students with a budget of {monthly_budget} PKR per month."""

update = f"""[4] new item launch 
**Prompt:** Create a launch strategy and an SMS marketing script for a brand new menu item at {business_name} (a {business_type} in {city}). 
The campaign should specifically target {main_customer} and fit cleanly within a total monthly operation budget of {monthly_budget:,} PKR."""

print(heading, marketing, customer_service, growth,update, sep='\n')

company = "Example Company"
financial_year = 2025
revenue = 1250.5
previous_revenue = 0.0
currency = "GBP"
unit = "million"

if previous_revenue == 0:
    revenue_growth = None
else:
    revenue_growth = ((revenue - previous_revenue) / previous_revenue) * 100

print(f"Company: {company}")
print(f"Financial year: {financial_year}")
print(f"Revenue: {revenue} {currency} {unit}")

if revenue_growth is None:
    print("Revenue growth: cannot calculate from zero previous revenue")
else:
    print(f"Revenue growth: {revenue_growth:.2f}%")
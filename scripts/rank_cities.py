import requests

def get_city_data(city_name):
    # Placeholder function to get data for a city using provided APIs
    # Replace with actual API calls and data processing
    return {
        "City Name": city_name,
        "University/Program Name": "Example University",
        "Rent Cost (Shared Apartment)": 500,
        "Percentage of Young People with Roommates": 50,
        "Housing Availability": "Moderate",
        "Program Affordability": "Affordable",
        "Survivability on $10,000": "Yes",
        "Safety Rating": "Medium risk",
        "LGBTQ+ Friendliness": "Yes",
        "Anglophone Expat Community": "Yes",
        "Visa Ease": "Moderate",
        "Career Prospects (Post-Program, Particularly for the USA)": "Medium",
        "Program Application Status (for February 11, 2025)": "Open",
        "Final Index Score": 75
    }

def rank_cities(cities):
    city_data_list = [get_city_data(city) for city in cities]
    ranked_cities = sorted(city_data_list, key=lambda x: x["Final Index Score"], reverse=True)
    return ranked_cities

def main():
    cities = ["Berlin", "Amsterdam", "Barcelona", "Paris", "Vienna"]
    ranked_cities = rank_cities(cities)
    
    for city in ranked_cities:
        print(f"City Name: {city['City Name']}")
        print(f"University/Program Name: {city['University/Program Name']}")
        print(f"Rent Cost (Shared Apartment): ${city['Rent Cost (Shared Apartment)']}/month")
        print(f"Percentage of Young People with Roommates: {city['Percentage of Young People with Roommates']}%")
        print(f"Housing Availability: {city['Housing Availability']}")
        print(f"Program Affordability: {city['Program Affordability']}")
        print(f"Survivability on $10,000: {city['Survivability on $10,000']}")
        print(f"Safety Rating: {city['Safety Rating']}")
        print(f"LGBTQ+ Friendliness: {city['LGBTQ+ Friendliness']}")
        print(f"Anglophone Expat Community: {city['Anglophone Expat Community']}")
        print(f"Visa Ease: {city['Visa Ease']}")
        print(f"Career Prospects (Post-Program, Particularly for the USA): {city['Career Prospects (Post-Program, Particularly for the USA)']}")
        print(f"Program Application Status (for February 11, 2025): {city['Program Application Status (for February 11, 2025)']}")
        print(f"Final Index Score: {city['Final Index Score']}/100")
        print()

if __name__ == "__main__":
    main()

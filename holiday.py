city_flight = str(input("What city would you like to fly to? (Santa Cruz, New York, London): "))

while city_flight.lower() != "santa cruz" and  city_flight.lower() != "new york" and city_flight.lower() != "london":
    print("Try again")
    city_flight = str(input("What city would you like to fly to? (Santa Cruz, New York, London): "))
# Created a loop to ensure that user inputs one of the cites and handles invalid cities

while True:
    try:
        num_nights = int(input("How many nights will you be staying at a hotel? "))
        if num_nights <= 0:
            print("Please enter number greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a whole number.")
    # Loop that checks for negative and non=integer values

while True:
    try:
        rental_days = int(input("How many days will you be renting a car? "))
        if rental_days <= 0:
            print("Please enter number greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a whole number.")
    # Loop that checks for negative and non=integer values




def hotel_cost(num_nights):
    hotel_total = num_nights * 100
    return hotel_total
# Calculates Hotel total
def plane_cost(city_flight):
    if city_flight.lower() == 'santa cruz':
        flight_total = 300
    elif city_flight.lower() == 'new york':
        flight_total = 200
    elif city_flight.lower() == 'london':
        flight_total = 1000
    return flight_total
# Returns flight cost

def car_rental(rental_days):
    car_total = rental_days * 50
    # Calculates car rental total
    return car_total

def holiday_cost(num_nights,city_flight,rental_days):
    total_cost =  hotel_cost(num_nights)+ plane_cost(city_flight) + car_rental(rental_days)
    return total_cost
# Calculates total cost of the holiday

print(f'Your flight will cost you: ${plane_cost(city_flight)} ')
print(f'Your hotel will cost you: ${hotel_cost(num_nights)} ')
print(f'Your car rental will cost you: ${car_rental(rental_days)} ')
print(f'Sum = ${holiday_cost(num_nights,city_flight,rental_days)}')
# Consistent currency formatting



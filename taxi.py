#constants for the fare
BASE_FARE = 3.00
RATE_FOR_140M = 0.36

#function to calculate the fare based on distance travelled km
def calculate_taxi_fare(distance_km):
    #convert km to m
    distance_m = distance_km * 1000

    #calculate num of 140m segments
    num_segments = distance_m/140

    #round up to nearest segment
    num_segments = round(num_segments + 0.5)

    #calculate fare amount
    fare = BASE_FARE + num_segments * RATE_FOR_140M

    #return fare calculation
    return fare


if __name__ == "__main__":
    distance_km = float(input("Enter your distance travelled in km: "))
    fare = calculate_taxi_fare(distance_km)
    print("The total fare for your trip distance of ", distance_km, "km is $", round(fare, 2))


    
    

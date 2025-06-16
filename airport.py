import json
import math

def load_airports(json_file):
    """Loads airport data from a JSON file."""
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_coordinates(airports, code):
    """Retrieves the (latitude, longitude) of an airport using its IATA code."""
    for airport in airports:
        if airport["code"].upper() == code.upper():
            return float(airport["lat"]), float(airport["lon"])
    return None

def haversine(lat1, lon1, lat2, lon2):
    """Calculates the distance in kilometers between two geographical points using the Haversine formula."""
    R = 6371  # Average radius of the Earth in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Distance in kilometers

def distance_between_airports(json_file):
    """Allows the user to enter two IATA codes and calculates the distance between them."""
    try:
        airports = load_airports(json_file)

        # Ask the user for IATA codes
        code1 = input("Enter the IATA code of the first airport: ").strip().upper()
        code2 = input("Enter the IATA code of the second airport: ").strip().upper()

        coords1 = get_coordinates(airports, code1)
        coords2 = get_coordinates(airports, code2)

        if coords1 and coords2:
            distance = haversine(*coords1, *coords2)
            print(f"The distance between {code1} and {code2} is {distance:.2f} km.")
            print("Coordinates of the first airport:", coords1)
            print("Coordinates of the second airport:", coords2)
        else:
            print("Error: One or both IATA codes were not found in the database.")

    except FileNotFoundError:
        print("Error: The file airports.json was not found.")
    except json.JSONDecodeError:
        print("Error: The JSON file is not properly formatted.")

# Run the program
json_file = r"C:\Users\elitebook\OneDrive\Desktop\Airports-Calculator-Distance\airports.json"  # Make sure the file exists at this path
distance_between_airports(json_file)

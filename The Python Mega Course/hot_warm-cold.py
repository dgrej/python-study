def temperature(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <=25:
        return "Warm"
    else:
        return "Cold"

print(temperature(10))
print(temperature(15))
print(temperature(26))

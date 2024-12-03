### Python program to determine voter eligibility based on specific criteria.

print("Welcome to my first python script by SIMON UGORJI \n\nNow, Let us get to know you better \n")

## Request for Their Nationality

nationality = input("> Please enter your nationality: ")

## Request for Their Age

age = int(input("> Please enter your age: "))

## Request for number of years they have lived in Nigeria

years_in_nigeria = int(input("> Please enter the number of years you have lived in Nigeria: "))

## Compute output

if "nigeria" in nationality.lower() and age >= 18 and years_in_nigeria >= 10:
    print("\nCongratulations! You are eligible to vote in the upcoming elections.")
else:
    print("\nSorry, you are not eligible to vote in the upcoming elections.")
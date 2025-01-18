import requests
from pprint import pprint
API_KEY = "33ec7c73f8a4eb6b9b5b5f95118b2275"
url = f"http://data.fixer.io/api/latest?access_key={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if not data.get("success"):
        print("Error with the Fixer.io API response:", data.get("error", "Unknown error"))
        exit()
    fx = data["rates"]
except requests.exceptions.RequestException as e:
    print(f"Error fetching currency rates: {e}")
    exit()

currencies = [
    "AED : Emirati Dirham, United Arab Emirates Dirham",
    "AFN : Afghan Afghani, Afghanistan Afghani",
    "ALL : Albanian Lek, Albania Lek",
    "INR : Indian Rupee, India Rupee, Bhutan, Nepal",
    "USD : US Dollar, United States Dollar, America",
    "EUR : Euro, Euro Member Countries",
    "CVE : Cape Verdean Escudo,Cape Verde Escudo",
     "CZK : Czech Koruna,Czech Republic Koruna",
     "DJF : Djiboutian Franc,Djibouti Franc",
     "DKK : Danish Krone,Denmark Krone,Faroe Islands,Greenland",
     "DOP : Dominican Peso,Dominican Republic Peso",
     "DZD : Algerian Dinar,Algeria Dinar",
     "EGP : Egyptian Pound,Egypt Pound,Gaza Strip",
     "ERN : Eritrean Nakfa,Eritrea Nakfa",
     "ETB : Ethiopian Birr,Ethiopia Birr,Eritrea",
     "FJD : Fijian Dollar,Fiji Dollar",
     "FKP : Falkland Island Pound,Falkland Islands (Malvinas) Pound",
     "GEL : Georgian Lari,Georgia Lari",
     "GGP : Guernsey Pound,Guernsey Pound",
     "GHS : Ghanaian Cedi,Ghana Cedi",
     "GIP : Gibraltar Pound,Gibraltar Pound",
     "GMD : Gambian Dalasi,Gambia Dalasi",
     "GNF : Guinean Franc,Guinea Franc",
     "GTQ : Guatemalan Quetzal,Guatemala Quetzal",
     "GYD : Guyanese Dollar,Guyana Dollar",
     "HKD : Hong Kong Dollar,Hong Kong Dollar",
     "HNL : Honduran Lempira,Honduras Lempira",
     "HRK : Croatian Kuna,Croatia Kuna",
     "HTG : Haitian Gourde,Haiti Gourde",
     "HUF : Hungarian Forint,Hungary Forint",
     "IDR : Indonesian Rupiah,Indonesia Rupiah,East Timor",
     "ILS : Israeli Shekel,Israel Shekel,Palestinian Territories",
     "IMP : Isle of Man Pound,Isle of Man Pound",
     "INR : Indian Rupee,India Rupee,Bhutan,Nepal",
     "IQD : Iraqi Dinar,Iraq Dinar",
     "IRR : Iranian Rial,Iran Rial",
     "ISK : Icelandic Krona,Iceland Krona",
     "JEP : Jersey Pound,Jersey Pound",
     "JMD : Jamaican Dollar,Jamaica Dollar",
     "JOD : Jordanian Dinar,Jordan Dinar",
     "JPY : Japanese Yen,Japan Yen",
     "KES : Kenyan Shilling,Kenya Shilling",
     "KGS : Kyrgyzstani Som,Kyrgyzstan Som",
     "KHR : Cambodian Riel,Cambodia Riel",
     "KMF : Comorian Franc,Comorian Franc",
     "KPW : North Korean Won,Korea (North) Won",
     "KRW : South Korean Won,Korea (South) Won",
     "KWD : Kuwaiti Dinar,Kuwait Dinar",
     "KYD : Caymanian Dollar,Cayman Islands Dollar",
     "KZT : Kazakhstani Tenge,Kazakhstan Tenge",


]

def function1():
    while True:

        print("*"*60)
        print("Welcome to Currency Converter")
        print("*" * 60)
        print("\t\t 1.Convert")
        print("\t\t 2.Show ")
        print("\t\t 3.Quit")
        ch=int(input("Enter your Choice :"))
        if ch == 1:
            try:
                print("*"*60)
                query = input("Enter the Amount With Currency to Currency eg :100 INR USD :").strip()
                print("*" * 60)
                qty, fromC, toC = query.split()
                qty = float(qty)
                fromC = fromC.upper()
                toC = toC.upper()

                if fromC not in fx or toC not in fx:
                    print(f"Invalid currency codes: {fromC} or {toC}. Please try again.")
                    continue

                amount = round(qty * fx[toC] / fx[fromC], 2)

                print(f"{qty} {fromC} is equal to {amount} {toC} as per the current rates.")

            except ValueError:
                print("Invalid input format. Please provide input as:Amount Currency to_Currency")
            except KeyError:
                print("Invalid currency code. Please try again.")

        elif ch == 2:
            pprint(currencies)
            continue
        elif ch == 3:
            print("*"*60)
            print("Thanks for using...")
            break



try:
    function1()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")

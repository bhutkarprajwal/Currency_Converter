
# Currency Converter

This is a Python-based Currency Converter application that uses the Fixer.io API to fetch real-time currency exchange rates. The program allows users to convert amounts between currencies, view a list of supported currencies, and exit the application gracefully.

---

## Features

1. **Convert Currency**: Allows users to convert a specified amount from one currency to another based on real-time exchange rates.
2. **Show Supported Currencies**: Displays a comprehensive list of supported currencies and their descriptions.
3. **User-Friendly Interface**: Easy-to-navigate menu system for choosing between conversion, viewing supported currencies, or exiting.
4. **Real-Time Rates**: Fetches the latest exchange rates using the Fixer.io API.

---

## Prerequisites

- Python 3.6 or higher
- Internet connection (required to fetch currency exchange rates from the Fixer.io API)
- API Key for Fixer.io (you can obtain one by registering at [Fixer.io](https://fixer.io))

---

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-repository/currency-converter.git
   cd currency-converter
   ```

2. Install required dependencies:
   ```bash
   pip install requests
   ```

3. Replace the placeholder `API_KEY` in the script with your Fixer.io API key:
   ```python
   API_KEY = "your_fixer_api_key"
   ```

---

## Usage

1. Run the script:
   ```bash
   python currency_converter.py
   ```

2. Choose an option from the menu:
   - **1. Convert**: Enter the amount and currency codes in the format:
     ```
     100 INR USD
     ```
     The program will display the equivalent amount in the target currency.
   - **2. Show**: Displays the list of supported currencies.
   - **3. Quit**: Exits the program.

---

## Example

```text
************************************************************
Welcome to Currency Converter
************************************************************
		 1.Convert
		 2.Show
		 3.Quit
Enter your Choice : 1
************************************************************
Enter the Amount With Currency to Currency eg :100 INR USD : 100 INR USD
************************************************************
100 INR is equal to 1.21 USD as per the current rates.
```

---

## Supported Currencies

The program supports a wide range of currencies, including:

- **INR**: Indian Rupee
- **USD**: US Dollar
- **EUR**: Euro
- **AED**: Emirati Dirham
- **JPY**: Japanese Yen

...and many more. Run the program and choose option 2 to view the complete list.

---

## Error Handling

- **Invalid Input Format**: If the input does not match the required format, the program will prompt the user to re-enter.
- **Invalid Currency Code**: If unsupported currency codes are entered, an error message is displayed.
- **Network Issues**: If the API request fails, a descriptive error message is shown.

---

## Limitations

1. The program depends on the Fixer.io API and requires an active internet connection.
2. Free-tier Fixer.io API keys only support EUR as the base currency. Consider upgrading for full functionality.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## Acknowledgments

- [Fixer.io](https://fixer.io) for providing the currency exchange rates API.
- Python community for helpful libraries like `requests` and `pprint`.


# EAN-13 Code Generator



## Overview

This Python script generates random EAN-13 codes, a standard for product identification. It calculates the check digit and ensures the generated codes are valid. This application is designed for generating fictitious EAN-13 codes for testing purposes.


>**Disclaimer:**
This is a tool for generating fictitious EAN-13 codes for testing. It's important to note that fictitious codes may not behave exactly like real-world codes in all scenarios. Fictitious means that the EAN-13 code has not been assigned to a company or product, but it adheres to the specific algorithm for its generation.


## How to Use

### Prerequisites

- <code>Python 3.11.2</code> installed on your machine

### Running the Script

1. Clone the repository:

   ```bash
   git clone https://github.com/loginLayer/ean13-code-gen.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ean13-code-gen
   ```

3. Run the script:

   ```bash
   python ean13_gen.py
   ```
   This will print 10 randomly generated EAN-13 codes.


## Functionality

### <em>generate_ean13()</em>

This function generates a random EAN-13 code.

* Parameters: None
* Returns: str: The generated EAN-13 code.


## Example Output

Here's an example of the script's output:

```python
EAN-13 codes

4912345678902
6012457839108
...
```

## Contributions

Feel free to contribute by opening issues or submitting pull requests.


## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE.md file for details.



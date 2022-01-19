# Pagination using python, RestAPI, Flask, and MongoDB

These are the codes on the article I wrote concerning the title. You can read it [here](https://nodebe.xyz)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Instruction
To insert test data into database, goto books_api/books.py, uncomment line 27 and run the application. After the first instance, you can comment it back.

## Usage

Run the application using. It runs on port 2424. You can change that in the app.py file

```bash
python app.py
```

You can make an endpoint call to 'http://127.0.0.1:2424/books' set body as {"page": 3, "limit": 5}

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
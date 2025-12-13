# Tally Invoice Generator Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:coderbdsust/tallyInvoiceGenerator.git
$ cd tallyInvoiceGenerator
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd tallyInvoiceGenerator
(env)$ python manage.py runserver
```

And Bengali Pdf Generate `[POST] http://localhost:8000/invoice/generate?locale=bn`.

```json
{
    "id": "8adb5e14-dcd6-41ce-a940-852b78f1fca9",
    "barcode": "",
    "invoiceNumber": "INUFM-20251122-DBAE9CFF",
    "invoiceDate": [
        2025,
        11,
        22
    ],
    "deliveryDate": [
        2025,
        11,
        22
    ],
    "deliveryCharge": 0.0,
    "totalDiscount": 0.0,
    "vatRate": 7.5,
    "taxRate": 0.0,
    "invoiceStatus": "PARTIALLY_PAID",
    "customer": {
        "id": "eef0ece9-e3c9-419e-84d4-e2cd95260036",
        "name": "Susama",
        "email": "susama@gmail.com",
        "mobile": "01937999999",
        "address": "465/28-1, West Rampura, Ulon, Bondhunibas, Dhaka",
        "postcode": "1219"
    },
    "ownerOrganization": {
        "id": "ff214200-f071-4e32-90c0-5bce8e06b52f",
        "orgName": "নিউ উদয়ন ফার্নিচার মার্ট",
        "orgRegNumber": "REG1221209212313",
        "orgTinNumber": "TIN123456789121321",
        "orgVatNumber": "VAT12345678912313",
        "orgMobileNo": "01937999999",
        "orgEmail": "new.udayan.furniture.mart@gmail.com",
        "orgOpenAt": "8am Morning",
        "orgOpenInWeek": "Open 7 days a week",
        "orgOpeningTitle": "Quality over Quantity",
        "owner": "শান্তি ভূষণ দেবনাথ",
        "banner": null,
        "avatar": "http://localhost:7070/tallyapp/a489e00a-e5c3-47a8-9818-4fbbf7bcaa59.jpeg",
        "logo": "http://localhost:7070/tallyapp/d28a0296-52e3-471c-ab7d-192cdddb9ca9.png",
        "logoB64": "",
        "tax": 0.0,
        "vat": 7.5,
        "since": [
            1984,
            12,
            1
        ],
        "orgAddressLine": "391/1, West Rampura",
        "orgAddressCity": "Dhaka",
        "orgAddressPostcode": "1219",
        "orgAddressCountry": "Bangladesh",
        "status": "ACTIVE",
        "totalEmployees": 2,
        "totalProducts": 3,
        "totalOwners": 1
    },
    "productSales": [
        {
            "id": "7c2b0337-2bef-4d27-a816-542c34f078bb",
            "quantitySold": 1.0,
            "pricePerUnit": 60000.0,
            "soldDate": [
                2025,
                11,
                22
            ],
            "totalAmount": 60000.0,
            "code": "T8DWCV",
            "description": "Size  - 5' x 7'",
            "name": "Bed",
            "unitType": "UNIT"
        },
        {
            "id": "7bc58e2e-dfdf-4b88-a58b-1fcc3d52be27",
            "quantitySold": 1.0,
            "pricePerUnit": 50000.0,
            "soldDate": [
                2025,
                12,
                13
            ],
            "totalAmount": 50000.0,
            "code": "PPDFLK",
            "description": "ক্ষ ঞ্জ ক্ত স্ক র্ক ষ্ঠ ঙ্গ",
            "name": "ক্ষ ঞ্জ ক্ত স্ক র্ক ষ্ঠ ঙ্গ - Bed",
            "unitType": "UNIT"
        }
    ],
    "payments": [
        {
            "id": "5f47aaf3-560a-4bef-b317-03241a8e815b",
            "amount": 20000.0,
            "paymentDate": [
                2025,
                11,
                22
            ],
            "paymentMethod": "Cash",
            "reference": ""
        }
    ],
    "totalPaid": 20000.0,
    "productSubTotal": 110000.0,
    "productTotalTax": 0.0,
    "productTotalVat": 8250.0,
    "totalAmount": 118250.0,
    "remainingAmount": 98250.0,
    "fullyPaid": false
}
```

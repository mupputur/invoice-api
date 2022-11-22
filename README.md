# invoice-api
## How To Use This
1. Set up MySQL Workbench
2. Create Database, and create customer and invoice tables with below columns
    **customer**: (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Email)
    **invoice**: (InvoiceId, CusomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingContry, BillingPostalCode, Total)
3. Install git
4. Create a new directory by running mkdir <directory name> and nevigate into the new directory by running cd <direcotry name>
5. Clone the source code by running git clone and navigate into new directory by running cd invoice-api
6. activate a new virtual environment
7. run pip install -r requirements.txt to install dependencies
8. Update config.json with your Database details(host, user, password and database name)
9. Run python app.py
10. Navigate to http://127.0.0.1:5000/ in your browser
  
## Testing
  

class Account:
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        # Update instance attributes using kwargs (e.g., addr, zip, etc.)
        self.__dict__.update(kwargs)
        
        # Set the account ID
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        
        # Set the account name
        self.name = name
        
        # Ensure the value attribute exists and is not negative
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        
        # Ensure name is a string
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
        # Ensure the ID is an integer
        if not isinstance(self.id, int):
            raise AttributeError("Attribute id must be an int object.")
        
        # Ensure value is an int or float
        if not isinstance(self.value, (int, float)):
            raise AttributeError("Attribute value must be an int or a float.")

    def transfer(self, amount):
        # Update value by adding the amount
        self.value += amount


class Bank:
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        # Check if the new_account is of the Account type
        if not isinstance(new_account, Account):
            raise ValueError("Account should be an instance of Account class.")
        
        # Check if account with the same name already exists
        if any(account.name == new_account.name for account in self.accounts):
            raise ValueError(f"An account with the name {new_account.name} already exists.")
        
        # Validate the account using the security checks
        if not self.is_valid_account(new_account):
            raise ValueError("The account is corrupted.")
        
        # Add the account to the bank if all checks pass
        self.accounts.append(new_account)
    
    def is_valid_account(self, account):
        # Check if the account has an even number of attributes
        if len(account.__dict__) % 2 == 0:
            return False
        
        # Check if the account has an attribute starting with 'b'
        if any(attr.startswith('b') for attr in account.__dict__):
            return False
        
        # Check if the account has attributes starting with 'zip' or 'addr'
        if any(attr.startswith('zip') or attr.startswith('addr') for attr in account.__dict__):
            return False
        
        # Check if the account does not have 'name', 'id', or 'value' attributes
        required_attrs = {'name', 'id', 'value'}
        if not required_attrs.issubset(account.__dict__):
            return False
        
        # Check if the name is a string
        if not isinstance(account.name, str):
            return False
        
        # Check if the id is an integer
        if not isinstance(account.id, int):
            return False
        
        # Check if the value is an int or float
        if not isinstance(account.value, (int, float)):
            return False
        
        return True
    
    def transfer(self, origin_name, dest_name, amount):
        # Find the origin and destination accounts
        origin_account = next((account for account in self.accounts if account.name == origin_name), None)
        dest_account = next((account for account in self.accounts if account.name == dest_name), None)
        
        # Check if both accounts exist
        if origin_account is None or dest_account is None:
            raise ValueError("One or both of the accounts do not exist.")
        
        # Validate the origin and destination accounts
        if not self.is_valid_account(origin_account) or not self.is_valid_account(dest_account):
            raise ValueError("One or both of the accounts are corrupted.")
        
        # Check if the amount is valid
        if amount < 0:
            raise ValueError("Amount must be greater than or equal to 0.")
        
        if origin_account.value < amount:
            raise ValueError("Insufficient funds.")
        
        # Perform the transfer
        if origin_name != dest_name:
            origin_account.transfer(-amount)  # Deduct from origin
            dest_account.transfer(amount)  # Add to destination
        # No funds move if the origin and destination are the same account
        return True


# Example usage:
bank = Bank()

# Create valid accounts
account1 = Account(name="Alice", value=100)
account2 = Account(name="Bob", value=50)

# Add accounts to the bank
bank.add(account1)
bank.add(account2)

# Make a valid transfer
bank.transfer("Alice", "Bob", 30)  # Alice transfers 30 to Bob

# Print updated account values
print(account1.name, account1.value)  # Alice 70
print(account2.name, account2.value)  # Bob 80

# Attempt an invalid transfer
try:
    bank.transfer("Alice", "Bob", 100)  # Alice doesn't have enough funds
except ValueError as e:
    print(e)  # Output: Insufficient funds.

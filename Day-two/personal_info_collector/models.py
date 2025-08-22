class Person:
    def __init__(self, name: str, age: int, email: str, phone: str,country:str):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        if not country.strip():
            raise ValueError("Country cannot be empty.")

        if not str(age).isdigit() or int(age) <= 0:
            raise ValueError("Age must be a positive number.")

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")

        if not phone.isdigit() or len(phone) < 7:
            raise ValueError("Invalid phone number.")

        self.name = name
        self.age = int(age)
        self.email = email
        self.phone = phone
        self.country = country

    def __str__(self):
        return f"{self.name} ({self.age}) | {self.email} | {self.phone} | {self.country}"

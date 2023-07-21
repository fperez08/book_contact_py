from database.repositories.contact_repository import ContactRepository
from database.services.contact_service import ContactService

contact_repo = ContactRepository("book_contact.db")
service = ContactService(contact_repo)
contact = {"name": "franciscos", "phone": "6446546", "email": "sasdh@askh.com"}
service.create_contact(contact)
print(service.get_all_contacts())

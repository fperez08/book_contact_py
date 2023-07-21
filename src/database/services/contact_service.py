class ContactService:
    def __init__(self, repository):
        self._repository = repository

    def get_all_contacts(self):
        return self._repository.get_all()

    def get_contact_by_id(self, id):
        return self._repository.get_by_id(id)

    def create_contact(self, contact):
        return self._repository.create(contact)

    def update_contact(self, contact):
        contact_to_update = self._repository.get_by_id(contact["id"])
        if contact_to_update is None:
            return False
        contact_to_update["name"] = contact["name"]
        contact_to_update["phone"] = contact["phone"]
        contact_to_update["email"] = contact["email"]
        return self._repository.update(contact_to_update)

    def delete_contact(self, id):
        return self._repository.delete(id)

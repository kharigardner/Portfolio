# this module is used to store the database contacts in a in-memory graph datanase, it contains crud functions and an option to write the database to a highly compressed pickle file

from typing import *
from uuid import UUID, uuid4
from pydantic import *
from pickle import dump, load

# defining the classes for the database, the graphs are stored as dictionaries, the keys are the uuids of the nodes and the values are the nodes themselves
class Contact(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    notes: str

class Group(BaseModel):
    id: UUID
    name: str
    description: str

class ContactGroup(Group):
    contacts: List[UUID]

class RelationshipEdge(BaseModel):
    id: UUID
    source: UUID
    target: UUID
    relationship: str

class ContactGraph:
    contacts: Dict[UUID, Contact]
    groups: Dict[UUID, Group]
    contact_groups: Dict[UUID, ContactGroup]
    relationships: Dict[UUID, RelationshipEdge]

# defining the database, all the class models above are stored as dictionaries/pickles in the database file
# the database is a dictionary with the keys being the uuids of the nodes and the values being the nodes themselves

class ContactBook:
    # defining the database file
    def __init__(self, database_file: str):
        self.database_file = database_file
        self.database = ContactGraph()
        self.database.contacts = {}
        self.database.groups = {}
        self.database.contact_groups = {}
        self.database.relationships = {}
    def create_contact(self, contact: Contact) -> Contact:
        contact.id = uuid4()
        self.database.contacts[contact.id] = contact
        return contact
    def get_contact(self, id: UUID) -> Contact:
        return self.database.contacts[id]
    def get_all_contacts(self) -> List[Contact]:
        return list(self.database.contacts.values())
    def update_contact(self, contact: Contact) -> Contact:
        self.database.contacts[contact.id] = contact
        return contact
    def delete_contact(self, id: UUID) -> None:
        del self.database.contacts[id]
        return "{message: 'deleted'}"
    def create_relationship(self, relationship: RelationshipEdge) -> RelationshipEdge:
        relationship.id = uuid4()
        self.database.relationships[relationship.id] = relationship
        return relationship
    def relationship_traversal(self, **kwargs) -> RelationshipEdge:
        # this function is used to traverse the graph, it takes in a dictionary of key value pairs and returns a list of nodes that match the key value pairs
        traversal_dict = {}
        for key, value in kwargs.items():
            traversal_dict[key] = value
        traversal_list = []
        traversal_list.append(traversal_dict)
        return traversal_list
    



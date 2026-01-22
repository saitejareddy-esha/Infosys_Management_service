Project Name:Backend home assignment

 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

Data Model
 Dataset
- id
- name (unique)
- description
- created_at

 DataElement
- id
- dataset (FK)
- dateofbirth
- data_type(string,date)
- required
- email

 Design Decisions
Data modeling- Used relational database using correct fields
Description- modeled datasets and data elements using a normalized relational design, enforced constraints at DB level, exposed REST APIs using DRF generic views,
 and ensured business rules like unique fields via model constraints.
constraints-implemented unique together model on the data element model

 Assumptions & Trade-offs
- Authentication is not implemented
- SQLite used for simplicity
- Pagination not included

 API Endpoints
- GET /api/datasets/
- POST /api/datasets/
- GET /api/datasets/{id}/

How to Run
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run migrations
5. Start server

How to Test
- Use browser or Postman
- Sample payloads provided
FLOW FOR ABOVE CODE
  -firstly we are going to create models for the dataset, for each dataset there can be many data elements for it,after that we are going to convert it into seralizers for the convertion of python objects to json, so we use generic classes because it gives balance between apiview and viewset for  using we have generic classes to write the business logic. 
  



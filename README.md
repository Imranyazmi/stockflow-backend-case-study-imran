# stockflow-backend-case-study-imran
Inventory Management System for B2B SaaS
Author

Mohd Imran Azmi Yunus
Backend Engineering Intern – Case Study Submission

Overview

StockFlow is a B2B inventory management platform designed for small and mid-sized businesses to manage products across multiple warehouses, track inventory changes, and maintain supplier relationships.

This case study focuses on:
Debugging and improving backend API logic
Designing a scalable relational database schema
Implementing a low-stock alert API with real-world constraints
Reasoning clearly with incomplete requirements

Tech Stack
Language: Python
Framework: Flask
ORM: SQLAlchemy
Database: Relational (PostgreSQL / MySQL)
API Style: REST

Part 1 – Code Review & Debugging

The original product creation endpoint had several production-critical issues, including missing input validation, lack of transaction safety, incorrect price handling, and improper coupling of products to warehouses.

The corrected implementation:
Validates required inputs
Uses atomic database transactions
Stores monetary values using DECIMAL
Decouples product creation from inventory creation
Handles integrity and runtime errors safely

Part 2 – Database Design

The database design supports:
Multiple companies and warehouses
Products stored across multiple warehouses
Inventory quantity tracking per warehouse
Inventory change history for auditing
Supplier relationships
Product bundles

Key design principles:
Separation of product and inventory data
Use of relational constraints to maintain consistency
Extensibility for future features such as analytics and automation

Part 3 – Low Stock Alerts API
An API endpoint is implemented to generate low-stock alerts for a company based on business rules.

Key considerations:
Low-stock thresholds vary by product
Alerts are generated only for products with recent sales activity
Multiple warehouses are handled independently
Supplier information is included to support reordering
Assumptions & Open Questions

Due to incomplete requirements, the following assumptions were made and would be clarified with the product team before production use:
SKU uniqueness scope (global vs per company)
Definition of “recent sales activity”
Whether products can have multiple suppliers
How bundles affect inventory calculations
Whether inventory updates should be event-driven
Trade-offs & Future Improvements

Trade-offs:
Sales velocity assumed to be precomputed
Inventory updates handled synchronously
Simple REST-based approach used

Future improvements:
Event-driven inventory updates
Background jobs for stock prediction
Supplier reorder automation
Role-based access control

Caching for large-scale deployments

How to Run:
pip install -r requirements.txt
flask run

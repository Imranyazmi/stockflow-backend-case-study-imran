# StockFlow – Backend Case Study (Bynry Inc)

This repository contains my solution for the Backend Engineering Intern case study at **Bynry Inc**.

## Overview
StockFlow is a B2B inventory management platform designed to support:
- Multiple companies
- Multiple warehouses per company
- Products stored across warehouses
- Low-stock alert generation

## Parts Covered
- API design and implementation (Low-stock alerts)
- Database schema design
- Backend best practices and assumptions

## Tech Stack
- Python
- Flask
- SQLAlchemy
- SQLite (for simplicity)

## Implemented Endpoint

### GET /api/companies/{company_id}/alerts/low-stock

Returns low-stock alerts for products belonging to a company based on:
- Current inventory levels
- Product-specific low-stock thresholds
- Recent sales activity (assumed)

### Sample Response
```json
{
  "alerts": [],
  "total_alerts": 0
}

Assumptions:
Recent sales = last 30 days
Average daily sales mocked for case study
Supplier handling demonstrated conceptually
Authentication not included (out of scope)

How to Run:
pip install -r requirements.txt
python app.py

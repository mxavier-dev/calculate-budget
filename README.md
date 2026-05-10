# 🏠 R.M Real Estate Budget System

A Python application developed to automate the generation of monthly rental budgets for a real estate company.

The system calculates rental prices based on property type, bedrooms, garage spaces, discounts, and contract fees, following predefined business rules.

---

# 📌 Features

* Generate rental budgets for:

  * Apartments
  * Houses
  * Studios
* Automatic monthly rent calculation
* Additional fees based on bedrooms and garage spaces
* Apartment discount rules
* Contract installment calculation
* CSV export with 12 monthly installments
* Modular project structure using Object-Oriented Programming (OOP)

---

# 🧠 Business Rules

## Base Rental Values

| Property Type | Base Price |
| ------------- | ---------- |
| Apartment     | R$ 700     |
| House         | R$ 900     |
| Studio        | R$ 1200    |

---

## Additional Rules

### Apartment

* +R$ 200 for 2 bedrooms
* +R$ 300 for garage
* 5% discount for clients without children

### House

* +R$ 250 for 2 bedrooms
* +R$ 300 for garage

### Studio

* +R$ 250 for 2 parking spaces
* +R$ 60 for each additional parking space

### Contract

* Fixed contract fee: R$ 2000
* Installment option up to 5x

---

# 🏗️ Project Structure

```bash
calculate_budget/
│
├── main.py
│
├── models/
│   └── imovel.py
│
├── services/
│   └── csv_service.py
│
├── data/
│   └── orcamentos.csv
│
└── README.md
```

---

# ⚙️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* CSV Module

---

# ▶️ How to Run

## Clone the repository

```bash
git clone https://github.com/mxavier-dev/calculate-budget.git
```

## Access the project folder

```bash
cd calculate-budget/
```

## Run the application

```bash
python3 main.py
```

---

# 📄 CSV Export

The application generates a `.csv` file containing the 12 monthly rental installments.

Example:

```csv
Month,Value
1,1200
2,1200
3,1200
...
12,1200
```

---

# 📚 Concepts Applied

* Object-Oriented Programming
* Inheritance
* Abstraction
* Business Rule Implementation
* Modular Architecture
* File Manipulation with CSV

---

# 🎯 Academic Purpose

This project was developed as a college assignment focused on applying programming logic, object-oriented programming, and system modeling concepts.

---

## 📫 Contact

Developed by **Matheus de Freitas Xavier** • [Linkedin Profile](https://www.linkedin.com/in/matheus-xavier-a14b0732a)

import json
import os
from datetime import date


FILE = "data.json"


def load_expenses():
    """Читает список трат из файла. Если файла нет — возвращает пустой список."""
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(expenses):
    """Сохраняет список трат в файл."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


def add_expense(category, amount):
    """Добавляет новую трату и возвращает её."""
    expenses = load_expenses()
    expense = {
        "category": category,
        "amount": amount,
        "date": date.today().isoformat(),
    }
    expenses.append(expense)
    save_expenses(expenses)
    return expense

from flask import Blueprint, request, jsonify
from models.expense import Expense
from services.currency_converter import convert_currency
from backend import db  # Ensure correct import

expense_bp = Blueprint("expense_bp", __name__)

@expense_bp.route("/", methods=["POST"])
def add_expense():
    data = request.get_json()
    converted_amount = convert_currency(data["amount"], data["currency"], "USD")
    new_expense = Expense(
        project_id=data["project_id"],
        amount=converted_amount,
        contributor=data["contributor"],
        comment=data["comment"],
        currency="USD",
        status="Pending"
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201

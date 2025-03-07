import yfinance as yf
import pandas as pd
from flask import Flask, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/financialstatement")
def generate_financial_statement():
    ticker_symbol = "AMZN"
    company = yf.Ticker(ticker_symbol)
    type = "cashflow"
    sheet = pd.DataFrame()
    if type == "balance":
        sheet = company.balance_sheet
    elif type == "income":
        sheet = company.income_stmt
    elif type == "cashflow":
        sheet = company.cash_flow
    else:
        return jsonify({"error": "Invalid Sheet Type"}), 400
    
    financial_statement = sheet.to_dict()
    return jsonify(financial_statement)



    



if __name__ == '__main__':
    app.run(debug=True)



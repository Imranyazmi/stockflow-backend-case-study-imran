from flask import Flask, jsonify
from models import db, Inventory, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockflow.db'
db.init_app(app)

@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    inventories = Inventory.query.join(Product)\
        .filter(Product.company_id == company_id).all()

    for inv in inventories:
        avg_daily_sales = inv.get_avg_daily_sales(days=30)
        if avg_daily_sales <= 0:
            continue

        days_left = inv.quantity / avg_daily_sales
        threshold = inv.product.low_stock_threshold

        if inv.quantity < threshold:
            alerts.append({
                "product_id": inv.product.id,
                "product_name": inv.product.name,
                "sku": inv.product.sku,
                "warehouse_id": inv.warehouse.id,
                "warehouse_name": inv.warehouse.name,
                "current_stock": inv.quantity,
                "threshold": threshold,
                "days_until_stockout": int(days_left),
                "supplier": None
            })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })

if __name__ == "__main__":
    app.run(debug=True)

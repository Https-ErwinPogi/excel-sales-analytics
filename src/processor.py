def get_total_sales(data):
    total = 0

    for row in data:
        total += row["Quantity"] * row["UnitPrice"]

    return total


def group_by(data, key):
    result = {}

    for row in data:
        group_value = row.get(key)
        sales = row.get("TotalPrice", 0)

        if group_value is None:
            continue

        if group_value not in result:
            result[group_value] = 0

        result[group_value] += sales

    return result


def get_average_delivery_time(data):
    from datetime import datetime

    total_days = 0
    count = 0

    for row in data:
        date = row.get("Date")
        delivery = row.get("DeliveryDate")

        if date and delivery:
            if isinstance(date, str):
                date = datetime.strptime(date, "%Y-%m-%d")

            if isinstance(delivery, str):
                delivery = datetime.strptime(delivery, "%Y-%m-%d")

            total_days += (delivery - date).days
            count += 1

    return total_days / count if count > 0 else 0


def top_products_per_region(data, top_n=3):
    region_product_sales = {}

    for row in data:
        region = row.get("Region")
        product = row.get("Product")
        sales = row.get("TotalPrice", 0)

        if region is None or product is None:
            continue

        if region not in region_product_sales:
            region_product_sales[region] = {}

        if product not in region_product_sales[region]:
            region_product_sales[region][product] = 0

        region_product_sales[region][product] += sales

    top_products = {}

    for region, products in region_product_sales.items():
        sorted_products = sorted(
            products.items(),
            key=lambda x: x[1],
            reverse=True
        )

        top_products[region] = sorted_products[:top_n]

    return top_products


def get_top_item(grouped_data):
    top_key = None
    top_value = -1

    for key, value in grouped_data.items():
        if value > top_value:
            top_value = value
            top_key = key

    return top_key, top_value

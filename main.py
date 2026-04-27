from src.loader import load_data
from src.processor import get_total_sales, group_by, get_average_delivery_time, top_products_per_region, get_top_item
from src.writer import create_report

file_path = "data/Product-Sales-Region.xlsx"

data = load_data(file_path)

total_sales = get_total_sales(data)

region_sales = group_by(data, "Region")
product_sales = group_by(data, "Product")
customer_sales = group_by(data, "CustomerType")

top_product = get_top_item(product_sales)
top_region = get_top_item(region_sales)

avg_delivery_time = get_average_delivery_time(data)

top_products = top_products_per_region(data, top_n=3)

# Generate report
create_report(
    total_sales,
    region_sales,
    product_sales,
    customer_sales,
    top_product,
    top_region,
    avg_delivery_time,
    top_products
)


def main():
    # your logic here
    print("Running project")


if __name__ == "__main__":
    main()

# print(total_sales)
# print(region_sales)
# print(product_sales)
# # print(customer_sales)

# # print(delivery_avg)
# # print(top_products)

# print(get_top_item(product_sales))

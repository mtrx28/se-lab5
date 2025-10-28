"""
Inventory System Module

This module manages a simple inventory system that supports adding,
removing, saving, loading, and printing items along with
logging and validation.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add_item(item="default", qty=0, logs=None, stock_data=None):
    """Add a quantity of an item to stock_data."""
    if logs is None:
        logs = []
    if stock_data is None:
        stock_data = {}

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for add_item: item=%s, qty=%s",
                        item, qty)
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)
    return stock_data


def remove_item(item, qty, stock_data):
    """Remove a quantity of an item from stock_data."""
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in stock.")
        if not isinstance(qty, int) or qty < 0:
            raise ValueError("Quantity must be a positive integer.")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)

    except KeyError as e:
        logging.warning(str(e))
    except ValueError as e:
        logging.error(str(e))


def get_qty(item, stock_data):
    """Return quantity of the specified item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty inventory.",
                        file_name)
        stock_data = {}
    return stock_data


def save_data(stock_data, file_name="inventory.json"):
    """Save inventory data to file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)
    logging.info("Inventory data saved to %s.", file_name)


def print_data(stock_data):
    """Print current inventory data."""
    logging.info("Printing current inventory data:")
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return items with quantity below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    stock_data = {}
    stock_data = add_item("apple", 10, stock_data=stock_data)
    stock_data = add_item("banana", 5, stock_data=stock_data)
    stock_data = add_item(123, "ten",
                          stock_data=stock_data)  # invalid input logged
    remove_item("apple", 3, stock_data)
    remove_item("orange", 1, stock_data)
    print(f"Apple stock: {get_qty('apple', stock_data)}")
    print(f"Low items: {check_low_items(stock_data)}")
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


if __name__ == "__main__":
    main()

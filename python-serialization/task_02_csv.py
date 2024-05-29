#!/usr/bin/python3
"""A module that reads data from a CSV file to JSON format"""
import json
import csv


def convert_csv_to_json(filename):
    """Converts a CSV file to a JSON"""

    data = []
    try:
        with open(filename, "r", encoding="utf-8") as csvfile:
            csvReader = csv.DictReader(csvfile)
            for rows in csvReader:
                data.append(rows)

        with open("data.json", "w", encoding="utf-8") as jfile:
            json.dump(data, jfile)
            return True

    except Exception:
        return False

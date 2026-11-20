"""Преобразования CSV, упрощённого YAML и JSON для LAB07."""

import json
import re


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    headers = [cell.strip() for cell in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [cell.strip() for cell in line.split(",")]
        records.append(dict(zip(headers, values)))
    return records


def _parse_value(value: str) -> bool | int | float | str:
    normalized = value.lower()
    if normalized in ("true", "yes"):
        return True
        
    if normalized in ("false", "no"):
        return False
    if re.fullmatch(r"[+-]?[0-9]+", value):
        return int(value)
    if re.fullmatch(r"[+-]?(?:[0-9]+\.[0-9]*|\.[0-9]+)", value):
        return float(value)
    return value


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None
    for raw_line in lines:
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- "):
            if current_list is not None:
                current_list.append(_parse_value(line[2:].strip()))
            continue

        key, separator, value = line.partition(":")
        if not separator:
            continue
        key = key.strip()
        value = value.strip()
        if value:
            settings[key] = _parse_value(value)
            current_list = None
        else:
            current_list = []
            settings[key] = current_list
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        details = extra.get(row[key], {}) if key in row else {}
        merged.append({**details, **row})
    return merged


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, sort_keys=True, indent=2)

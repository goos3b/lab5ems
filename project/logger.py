"""
Журнал ошибок: хранит сообщения в памяти и дублирует в файл input_errors.log.
"""
from __future__ import annotations

import datetime
import os

from constants import LOG_FILE

_entries: list[str] = []


def log_error(message: str) -> None:
    """Записать сообщение об ошибке ввода."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}"
    _entries.append(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        pass


def get_entries() -> list[str]:
    """Вернуть копию журнала ошибок."""
    return list(_entries)


def clear() -> None:
    """Очистить журнал: список в памяти и файл на диске (файл остаётся пустым)."""
    _entries.clear()
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            pass  # перезаписываем файл пустым
    except OSError:
        pass

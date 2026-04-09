#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._index: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        try:
            return self._data.pop(0)
        except IndexError:
            print(' No data to output')
            return (-1, '')


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if not self.validate(data):
                raise ValueError(' - Got exception: Improper numeric data')
            print(f' Processing data: {data}')
            if isinstance(data, list):
                for sub_data in data:
                    self._data.append((self._index, str(sub_data)))
                    self._index += 1
            else:
                self._data.append((self._index, str(data)))
                self._index += 1
        except ValueError as e:
            print(f''' Test invalid ingestion of string '{data}' '''
                  f'without prior validation:\n {e}')


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        try:
            if not self.validate(data):
                raise ValueError(' - Got exception: Improper str data')
            print(f' Processing data: {data}')
            if isinstance(data, list):
                for sub_data in data:
                    self._data.append((self._index, str(sub_data)))
                    self._index += 1
            else:
                self._data.append((self._index, str(data)))
                self._index += 1

        except ValueError as e:
            print(f''' Test invalid ingestion of string '{data}' '''
                  f'without prior validation:\n {e}')


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, dict) and
                       len(item) == 2 and
                       all(isinstance(k, str) and isinstance(v, str)
                           for k, v in item.items())
                       for item in data)
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        try:
            if not self.validate(data):
                raise ValueError(' - Got exception: Improper log data or '
                                 'Dict must have exactly 2 string '
                                 'key-value pairs')
            print(f' Processing data: {data}')
            if isinstance(data, list):
                for sub_data in data:
                    values = list(sub_data.values())
                    word = str(f'{values[0]}: {values[1]}')
                    self._data.append((self._index, word))
                    self._index += 1

        except ValueError as e:
            print(f''' Test invalid ingestion of dict '{data}' '''
                  f'without prior validation:\n {e}')


def main() -> None:
    print('=== Code Nexus - Data Processor ===')

    print('\nTesting Numeric Processor...')
    numeric = NumericProcessor()
    print(f''' Trying to validate input '42': {numeric.validate(42)}''')
    print(f''' Trying to validate input 'Hello': '''
          f'''{numeric.validate('Hello')}''')
    numeric.ingest('foo')
    numeric.ingest([1, 2, 3, 4, 5])
    n = 3
    print(f' Extracting {n} values...')
    for i in range(n):
        value = numeric.output()
        print(f' - Numeric value {value[0]}: {value[1]}')

    print('\nTesting Text Processor...')
    text_procesor = TextProcessor()
    print(f''' Trying to validate input '42': {text_procesor.validate(42)}''')
    print(f''' Trying to validate input 'Hello': '''
          f'''{text_procesor.validate('Hello')}''')
    words = ['Nexus', 'Hello', 'World']
    print(f''' Trying to validate input '{words}': '''
          f'{text_procesor.validate(words)}''')
    text_procesor.ingest(['hello', 42])
    text_procesor.ingest(words)
    n = 1
    print(f' Extracting {n} values...')
    for i in range(n):
        value = text_procesor.output()
        print(f' - Numeric value {value[0]}: {value[1]}')

    log = LogProcessor()
    print('\nTesting Log Processor...')
    print(f''' Trying to validate input '42': {log.validate(42)}''')
    print(f''' Trying to validate input 'Hello': {log.validate('Hello')}''')
    print(f''' Trying to validate input '{words}': {log.validate(words)}''')
    logs = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message':  'Unauthorized access!!'}]
    print(f''' Trying to validate input '{logs}': {log.validate(logs)}''')
    log.ingest(['hello', 42])
    log.ingest(logs)
    n = 2
    print(f' Extracting {n} values...')
    for i in range(n):
        log_procesor = log.output()
        print(f' - Log entry {log_procesor[0]}: {log_procesor[1]}')


if __name__ == '__main__':
    main()

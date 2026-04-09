#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)
            print(f' --- Registering {proc.__class__.__name__}')

    def process_stream(self, stream: list[Any]) -> None:
        print('\n**--** Send batch of data on stream:', stream)
        for data in stream:
            try:
                flaj = False
                for process in self.processors:
                    if process.validate(data):
                        process.ingest(data)
                        flaj = True
                        break
                if not flaj:
                    raise ValueError(
                        f'Can\'t process element in stream: {data}'
                    )
            except ValueError as e:
                print(f'DataStream error - {e}')

    def print_processors_stats(self) -> None:
        print('\n                 ====== DataStream statistics ======')
        if not self.processors:
            print('No processor found, no data\n')
            return
        for proc in self.processors:
            print(f' - {proc.__class__.__name__}: '
                  f'total {proc._index} items processed, '
                  f'remaining {len(proc._data)} on processor')

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            group_proc = []
            for _ in range(nb):
                item = proc.output()
                if item[0] == -1:
                    break
                group_proc.append(item)
            plugin.process_output(group_proc)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('CSV Output:')
        values = [value[1] for value in data]
        print(', '.join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('JSON Output:')
        values = []
        for value in data:
            values.append(f'"item_{value[0]}": "{value[1]}"')
        print(f'{{ {', '.join(values)} }}')


def main() -> None:
    print('=== Code Nexus - Data Pipeline ===')
    print('Initialize Data Stream...')
    stream = DataStream()
    stream.print_processors_stats()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message':
               'Telnet access! Use ssh instead'},
              {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]
    stream.process_stream(batch)
    stream.print_processors_stats()

    print('\nSend 3 processed data from each processor to a CSV plugin:')
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message':
                'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print('\nSend 5 processed data from each processor to a JSON plugin:')
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()


if __name__ == '__main__':
    main()

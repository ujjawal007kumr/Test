from collections import defaultdict

class DataStream:
    def __init__(self):
        self.last_timestamps = defaultdict(lambda: float('-inf'))

    def should_output_data_str(self, timestamp, data_string):
        if timestamp >= self.last_timestamps[data_string] + 5:
            self.last_timestamps[data_string] = timestamp
            return True
        else:
            return False

data_stream = DataStream()

output_results = [
    data_stream.should_output_data_str(timestamp=0, data_string="hello"),
    data_stream.should_output_data_str(timestamp=1, data_string="world"),
    data_stream.should_output_data_str(timestamp=6, data_string="hello"),
    data_stream.should_output_data_str(timestamp=7, data_string="hello"),
    data_stream.should_output_data_str(timestamp=8, data_string="world"),
]

print(output_results)
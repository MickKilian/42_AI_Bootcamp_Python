import csv

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        """
        Initializes the CsvReader class.
        :param filename: Name of the CSV file to read.
        :param sep: Separator for the CSV file (default is comma).
        :param header: Boolean flag indicating if the first row is a header.
        :param skip_top: Number of rows to skip at the top.
        :param skip_bottom: Number of rows to skip at the bottom.
        """
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []
        self.headers = None

    def __enter__(self):
        """
        Opens the CSV file and prepares it for reading.
        :return: CsvReader object for data access.
        """
        try:
            self.file = open(self.filename, mode='r', newline='', encoding='utf-8')
            reader = csv.reader(self.file, delimiter=self.sep)
            
            # Skip top rows
            for _ in range(self.skip_top):
                next(reader, None)
            
            # Read the CSV file and store records in data
            for row in reader:
                if len(row) == 0:
                    continue
                self.data.append(row)

            # Skip bottom rows
            self.data = self.data[:-self.skip_bottom] if self.skip_bottom > 0 else self.data

            # Store header if it is present
            if self.header:
                self.headers = self.data[0]
                self.data = self.data[1:]
                
            return self

        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the CSV file after processing.
        """
        if self.file:
            self.file.close()

    def getdata(self):
        """
        Retrieves the data/records from skip_top to skip_bottom.
        Returns:
            nested list (list of lists) representing the data.
        """
        return self.data

    def getheader(self):
        """
        Retrieves the header from the CSV file (if self.header is True).
        Returns:
            list: representing the header data (if header is True).
            None: if header is False.
        """
        return self.headers if self.header else None


# Example usage:
if __name__ == "__main__":
    # Handling a properly formatted CSV file
    with CsvReader('good.csv') as file:
        if file:
            data = file.getdata()
            header = file.getheader()
            print("Header:", header)
            print("Data:", data)

    # Handling a potentially corrupted CSV file
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")

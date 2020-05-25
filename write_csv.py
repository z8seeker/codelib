from csv import DictWriter
import os


def write_csv(headlines, rows, filename):
    dir = os.path.dirname(os.path.realpath(__file__))
    fp = os.path.join(dir, filename)
    with open(filename, 'w') as f:
        dw = DictWriter(f, fieldnames=headlines)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


import csv

file_path = "mydata.csv"

data = [
    ["Name", "Age", "City"],
    ["John", "20", "Seoul"],
    ["Jane", "35", "Busan"],
    ["Bob", "35", "Jeju"]
]

with open(file_path, 'w', encoding="utf-8", newline="") as file:
    csv_writer = csv.writer(file)
    # csv_writer.writerow(['이름', '나이'])
    # csv_writer.writerow(['Alice', 40])
    # csv_writer.writerow(['Bob', 30])
    # for d in data:
    #     csv_writer.writerow(d)
    csv_writer.writerows(data)

print('csv 파일 작성 완료')    
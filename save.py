import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w",encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["title","company","location","link"])
    for job in jobs:
        writer.writerow(list(job.values())) #dictionary에서 key빼고 values만 불러오기 -> list형식으로 변환해서 csv에 작성
    return
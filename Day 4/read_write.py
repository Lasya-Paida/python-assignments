import csv
from collections import defaultdict

subject_scores = defaultdict(list)

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subject = row["Subject"]
        score = int(row["Score"])
        subject_scores[subject].append(score)

summary_lines = []
for subject, scores in subject_scores.items():
    avg_score = sum(scores) / len(scores)
    summary_lines.append(f"Subject: {subject}, Average Score: {avg_score:.2f}")

with open("summary.txt", "w") as txtfile:
    txtfile.write("Summary of Average Scores by Subject\n")
    txtfile.write("=" * 40 + "\n")
    for line in summary_lines:
        txtfile.write(line + "\n")

print("Summary written to summary.txt")

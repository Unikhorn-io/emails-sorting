import csv

# Files to compare
complete_file = "complete.csv"    # Complete list of contacts
sent_file = "lot1.csv"     # List of contacts who received an email
output_file = "lot2.csv"     # List of contacts who did not receive an email

# Compare the list of contacts who received an email with the complete list
with open(sent_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    emails_sent = {row[0].strip() for row in reader}  # We assume that emails are in the first column

# Compare the list of contacts who did not receive an email with the complete list
with open(complete_file, "r", encoding="utf-8") as f, open(output_file, "w", encoding="utf-8", newline="") as out:
    reader = csv.reader(f)
    writer = csv.writer(out)

    for row in reader:
        email = row[0].strip()  # We assume that emails are in the first column
        if email not in emails_sent:
            writer.writerow([email])  # Write the row in the output file

print(f"✅ Sorting done! The remaining emails are in '{output_file}'")

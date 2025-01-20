import csv
from datetime import datetime

def notionToMarkdown(csvFile, markdownFile):
    # read file
    with open(csvFile, 'r',encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    #initiate creating markdown file
    with open(markdownFile, 'w',encoding='utf-8-sig') as f:
        # Write the header
        header = rows[0].keys()
        # Write the rows
        for row in rows:
            rowData = []
            for key in header:
                #check if row has URL
                if key == 'URL':
                    link = f"[{row['Name']}]({row['URL']})"  # Replace with a Markdown link
                    rowData.append(link)
                #use "🔺" if important property is check on
                if key == "IMPORTANT" and row["IMPORTANT"]=="Yes":
                    priority = f" 🔺"
                    rowData.append(priority)
                #created date using "➕ YYYY-MM-DD " format
                if key == "Created":
                    dateString = row["Created"]
                    parsedDate = datetime.strptime(dateString, "%B %d, %Y %I:%M %p")
                    formattedDate = parsedDate.strftime("%Y-%m-%d")
                    rowData.append("➕ "+formattedDate)
                #turn labels as tags
                if key == "Label":
                    labelString = row["Label"]
                    formattedString = " ".join(f"#{part.strip()}" for part in labelString.split("/"))
                    rowData.append(" "+formattedString)
            f.write(''.join(rowData) + '\n')

notionToMarkdown('./CSV-to-Markdown/notion1.csv', './CSV-to-Markdown/output2.md')

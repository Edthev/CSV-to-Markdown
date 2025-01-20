# CSV-to-Markdown

### What is this project?
This project provides a Python script to seamlessly migrate my data from [Notion](https://www.notion.so/) to [Obsidian](https://obsidian.md/).

### Problems:
1) **CSV to MD:**Obsidian requires markdown for notes
2) **Link Formatting:** Instead of a plain list of links, the "Name" property in Notion is transformed into markdown embeds using "URL" property.
3) **Preserving "Important" Property:** Retain "Important" property and convert it to a compatible format for obsidian
4) **Date Conversiom:** Notion uses the date format "Month DD, YYYY H:MM", but obsidian uses "YYYY-MM-DD"
6) **String Manipulation:** Notion "Multi-select" datatype is formatted as "Tag1 / Tag2 / Tag3", obsidian tags are formatted as "#Tag1 #Tag2 #Tag3"
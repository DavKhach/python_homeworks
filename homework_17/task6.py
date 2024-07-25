def generate_report(title, author, *sections, summary="No summary", conclusion="No conclusion"):
    report = f"Title: {title}\nAuthor: {author}\n\n"
    for i, section in enumerate(sections, start=1):
        report += f"Section {i}: {section}\n\n"
    report += f"Summary: {summary}\n\nConclusion: {conclusion}"
    return report

required_sections = ["Introduction", "Methodology", "Results", "Discussuion"]

report = generate_report("Research on Ai", "John Doe", *required_sections, summary="This research explores AI achievments", conclusion="Ai has big potential")
print(report)

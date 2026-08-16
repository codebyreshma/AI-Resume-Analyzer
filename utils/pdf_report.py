from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

from datetime import datetime


def generate_pdf(
    filename,
    resume_score,
    ats_score,
    match_score,
    result
):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.HexColor("#2563EB")

    heading = styles["Heading2"]
    normal = styles["BodyText"]

    story = []

    # ==========================
    # Title
    # ==========================

    story.append(
        Paragraph("🤖 AI Resume Analyzer", title_style)
    )

    story.append(
        Paragraph("Professional Resume Report", heading)
    )

    story.append(Spacer(1, 0.3 * inch))

    # ==========================
    # Date
    # ==========================

    date = datetime.now().strftime("%d %B %Y")

    story.append(
        Paragraph(f"<b>Date:</b> {date}", normal)
    )

    story.append(Spacer(1, 0.2 * inch))

    # ==========================
    # Score Table
    # ==========================

    data = [
        ["Resume Score", resume_score],
        ["ATS Score", ats_score],
        ["Match Score", match_score]
    ]

    table = Table(data, colWidths=[220, 120])

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563EB")),

        ("TEXTCOLOR", (0,0), (-1,-1), colors.black),

        ("GRID", (0,0), (-1,-1), 1, colors.grey),

        ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#E8F0FE")),

        ("BOTTOMPADDING", (0,0), (-1,-1), 10),

        ("TOPPADDING", (0,0), (-1,-1), 10),

        ("ALIGN", (0,0), (-1,-1), "CENTER")

    ]))

    story.append(table)

    story.append(Spacer(1, 0.4 * inch))

    # ==========================
    # AI Analysis
    # ==========================

    story.append(
        Paragraph("AI Analysis", heading)
    )

    story.append(Spacer(1, 0.1 * inch))

    story.append(
        Paragraph(
            result.replace("\n", "<br/>"),
            normal
        )
    )

    doc.build(story)
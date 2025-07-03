from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import pandas as pd
from fpdf import FPDF
import os

# OpenAI APIキーを環境変数から取得（安全）
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# クライアント初期化
client = OpenAI(api_key=OPENAI_API_KEY)

# CSVファイルを読み込み
df = pd.read_csv("sample_logs.csv")

# ログをGPTで要約
def summarize_logs_v1(log_df):
    log_text = log_df.to_csv(index=False)
    system_prompt = "あなたは優秀なセキュリティアナリストです。以下のログから、要約、リスク評価、そして具体的な対応策を提案してください。"
    user_prompt = f"以下はセキュリティログです：\n```\n{log_text}\n```"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()

# Markdown出力
def save_markdown(summary, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# セキュリティログ要約レポート\n\n")
        f.write(summary)

# Markdown→PDF（日本語フォント対策済）
def markdown_to_pdf(md_path, pdf_path, font_path):
    pdf = FPDF()
    pdf.add_page()

    # IPAフォントを使って日本語対応
    pdf.add_font("IPAexGothic", "", font_path, uni=True)
    pdf.set_font("IPAexGothic", "", 12)

    with open(md_path, "r", encoding="utf-8") as f:
        for line in f:
            pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)

# 実行部分
summary = summarize_logs_v1(df)
md_path = "security_log_report.md"
pdf_path = "security_log_report.pdf"
font_path = "ipaexg.ttf"  # ← IPAexフォントに変更

save_markdown(summary, md_path)
markdown_to_pdf(md_path, pdf_path, font_path)

print("✅ PDFレポート作成完了:", pdf_path)

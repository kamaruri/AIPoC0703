# AIセキュリティログ要約レポート PoC

このプロジェクトは、Azureなどで出力されたセキュリティログを対象に、GPTを活用して自動で「要約」「リスク評価」「対応策提案」を行い、PDFレポートとして出力するPoC（Proof of Concept）です。

セキュリティアナリストによる初期判断の代替を想定し、SOC・CSIRTの省力化・スキル支援を目指しています。

---

## フォルダ構成

<pre><code>
.
├── ai_log_report_v1.py          # メイン処理スクリプト
├── sample_logs.csv              # 入力用ログファイル（仮ログ）
├── security_log_report.md       # AI生成レポート（Markdown）
├── security_log_report.pdf      # PDF形式レポート（可視化用）
├── DejaVuSans.ttf               # 日本語PDF対応フォント
└── README.md                    # このファイル
</code></pre>
---

## 使用ライブラリ

- `openai`
- `pandas`
- `fpdf`
- `python-dotenv`

### インストール方法

```bash
pip install openai pandas fpdf python-dotenv
```

## 実行方法
.env ファイルを作成し、以下を記載：

env
コピーする
編集する
OPENAI_API_KEY=sk-xxxxx
スクリプトを実行：

bash
コピーする
編集する
python ai_log_report_v1.py
実行後、以下のファイルが生成されます：

security_log_report.md：AIによる要約＆リスク評価レポート

security_log_report.pdf：PDF形式レポート（日本語フォント対応）

## 出力例（要約）
pgsql
コピーする
編集する
ログには3つのイベントが記録されており、ログオン失敗が2回、成功が1回。

特定IPアドレス（192.168.1.25, 192.168.1.30）からの不審なログオン試行を検知。

成功ログオンはadminアカウントであったため、正当と思われるが監視対象。
🛠 出力例（対応策）
markdown
コピーする
編集する
1. userAおよびuserBに対してアカウントロックポリシーを適用し、不正アクセスを防止。
2. adminアカウントに関して、アクセスの正当性を定期的に確認。
3. 全体として、ログ監視の強化とユーザーへのセキュリティ教育を推奨。
📌 .gitignore 推奨設定
bash
コピーする
編集する
.env
*.pdf

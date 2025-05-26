<div align="center">

![おみくじアプリバナー](assets/omikuji-banner.svg)

</div>

# 🎋 おみくじアプリ

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)

**日本の伝統的なおみくじをモチーフにしたStreamlitベースのWebアプリケーション**

</div>

## 📖 概要

このアプリケーションは、ユーザーが仮想的におみくじを引いて今日の運勢を占うことができるシンプルで楽しいWebアプリです。7種類の運勢結果があり、それぞれに特色のあるメッセージとアドバイスが表示されます。

### 🎯 主な目的
- 日本の伝統文化であるおみくじをデジタル化
- 毎日のモチベーション向上のためのツール
- Streamlitの基本機能を活用したサンプルアプリケーション

## ✨ 機能

- **🎯 おみくじを引く**: ボタンをクリックして運勢を占う
- **🌈 カラフルなUI**: 運勢ごとに異なる色でカードを表示
- **💭 メッセージ表示**: 運勢に応じたメッセージとアドバイス
- **📅 日時表示**: 現在の日時をリアルタイムで表示
- **🔄 再実行機能**: 何度でもおみくじを引き直し可能
- **ℹ️ サイドバー情報**: おみくじの種類と詳細な説明
- **🎈 視覚エフェクト**: バルーンアニメーションで結果を華やかに演出

## 🎲 運勢の種類

| 運勢 | 確率 | 説明 | カラーテーマ |
|------|------|------|-------------|
| 大吉 | 1/7 | 最高の運勢 | #ff6b6b (赤) |
| 中吉 | 1/7 | とても良い運勢 | #4ecdc4 (ターコイズ) |
| 小吉 | 1/7 | 良い運勢 | #45b7d1 (青) |
| 吉 | 1/7 | 普通の運勢 | #96ceb4 (緑) |
| 末吉 | 1/7 | 後半良くなる運勢 | #feca57 (黄) |
| 凶 | 1/7 | 注意が必要 | #ff9ff3 (ピンク) |
| 大凶 | 1/7 | 困難な時期 | #54a0ff (ライトブルー) |

## 🛠️ 技術スタック

- **Python 3.8+**: プログラミング言語
- **Streamlit 1.28.0+**: Webアプリケーションフレームワーク
- **HTML/CSS**: カスタムスタイリング
- **datetime**: 日時処理
- **random**: ランダム選択機能

## 📦 インストール

### 前提条件
- Python 3.8以上がインストールされていること
- pipが利用可能であること

### セットアップ手順

1. **リポジトリをクローンします：**
```bash
git clone https://github.com/Sunwood-ai-labs/claude-code-gh-action-examples-001.git
cd claude-code-gh-action-examples-001
```

2. **仮想環境を作成します（推奨）：**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **必要なパッケージをインストールします：**
```bash
pip install -r requirements.txt
```

## 🚀 使用方法

### アプリケーションの起動

```bash
streamlit run omikuji_app.py
```

アプリケーションが起動すると、ブラウザが自動的に開き、通常は `http://localhost:8501` でアクセスできます。

### 基本的な使い方

1. **アプリケーションにアクセス** - ブラウザでローカルホストを開く
2. **おみくじを引く** - 「🎯 おみくじを引く」ボタンをクリック
3. **結果を確認** - カラフルなカードで運勢結果を表示
4. **メッセージを読む** - 今日のメッセージとアドバイスを確認
5. **再挑戦** - 「🔄 もう一度引く」ボタンで再度実行
6. **詳細情報** - サイドバーでおみくじの詳細情報を確認

## 📁 ファイル構成

```
claude-code-gh-action-examples-001/
├── README.md           # プロジェクト説明書（このファイル）
├── omikuji_app.py     # メインアプリケーションファイル
├── requirements.txt   # 必要なPythonパッケージリスト
└── .gitignore         # Git除外ファイル設定
```

### ファイル詳細

- **`omikuji_app.py`**: Streamlitアプリケーションのメインファイル
  - おみくじの結果データ定義
  - UI/UXの実装
  - ランダム選択ロジック
- **`requirements.txt`**: 依存パッケージの管理
- **`README.md`**: プロジェクト情報とドキュメント

## 🎨 デザイン特徴

- **レスポンシブデザイン**: 様々な画面サイズに自動対応
- **日本語対応**: 完全な日本語インターフェース
- **視覚的フィードバック**: バルーンエフェクトと色分けされた結果表示
- **直感的UI**: ワンクリックで簡単操作
- **モダンなスタイリング**: CSS3を活用したグラデーションとシャドウ効果

## 🔧 カスタマイズ

### 運勢の追加・変更

`omikuji_app.py`の`OMIKUJI_RESULTS`リストを編集することで、運勢の種類やメッセージをカスタマイズできます：

```python
OMIKUJI_RESULTS = [
    {
        "result": "超大吉",  # 運勢名
        "color": "#ff0000",  # カラーコード
        "message": "カスタムメッセージ",
        "advice": "カスタムアドバイス"
    }
    # 他の運勢...
]
```

### UIスタイルの変更

HTMLとCSSを直接編集することで、カードのデザインや色彩を変更できます。

## 🧪 テスト

基本的な動作確認：

```bash
# アプリケーションが正常に起動するかテスト
streamlit run omikuji_app.py --server.headless true
```

## 🤝 貢献ガイドライン

プロジェクトへの貢献を歓迎します！以下の方法で参加できます：

### 貢献方法

1. **イシューの報告** - バグや改善提案をGitHub Issuesで報告
2. **機能追加** - 新機能のプルリクエストを作成
3. **ドキュメント改善** - READMEやコメントの改善
4. **翻訳** - 多言語対応への貢献

### プルリクエストのガイドライン

1. フォークしてブランチを作成
2. 変更を加えてテスト
3. コミットメッセージは明確に記述
4. プルリクエストで詳細な説明を提供

## 📋 今後の予定

- [ ] 運勢の詳細情報ページ追加
- [ ] ユーザーカスタマイズ機能
- [ ] 運勢履歴の保存機能
- [ ] 多言語対応（英語、中国語など）
- [ ] モバイルアプリ版の開発
- [ ] API機能の追加

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 👥 作者情報

- **開発元**: [Sunwood AI Labs](https://github.com/Sunwood-ai-labs)
- **メンテナー**: Sunwood AI Labs チーム
- **サポート**: GitHub Issues を通じてサポートを提供

## 🙏 謝辞

- Streamlitコミュニティの皆様
- 日本の伝統文化であるおみくじに敬意を表して
- オープンソースコミュニティへの感謝

---

<div align="center">

**Made with ❤️ using [Streamlit](https://streamlit.io/)**

[🏠 ホーム](https://github.com/Sunwood-ai-labs/claude-code-gh-action-examples-001) | 
[📊 Issues](https://github.com/Sunwood-ai-labs/claude-code-gh-action-examples-001/issues) | 
[🔄 Pull Requests](https://github.com/Sunwood-ai-labs/claude-code-gh-action-examples-001/pulls)

</div>
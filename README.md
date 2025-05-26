<div align="center">

![JupyterLab Kitバナー](assets/jupyterlab-kit-banner.svg)

</div>

# 🔬 JupyterLab Kit

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![JupyterLab](https://img.shields.io/badge/JupyterLab-4.0+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)

**JupyterLab環境と統合されたデータサイエンス・開発キット**

</div>

## 📖 概要

JupyterLab Kitは、データサイエンスと開発作業を効率化するための統合環境です。JupyterLabの強力な機能に加えて、Streamlitを使ったWebアプリケーション開発も可能な、オールインワンの開発キットとなっています。

### 🎯 主な目的
- JupyterLabとStreamlitの統合開発環境の提供
- データサイエンスワークフローの効率化
- Webアプリケーション開発の学習とプロトタイピング
- Dockerを使った再現可能な開発環境の構築

## ✨ 主要機能

### 🔬 JupyterLab環境
- **📊 データ分析**: NumPy、Pandas、Matplotlib、Seaborn、Plotlyなどの主要ライブラリ
- **🧠 機械学習**: scikit-learn統合環境
- **📝 ノートブック**: インタラクティブな開発・分析環境
- **🌐 Webインターフェース**: ブラウザベースの直感的なUI

### 🚀 Streamlitアプリ開発
- **⚡ 高速プロトタイピング**: Streamlitによる迅速なWebアプリ開発
- **🔄 ホットリロード**: リアルタイムでのコード変更反映
- **📱 レスポンシブ**: モバイル対応のWebインターフェース
- **📈 データ可視化**: インタラクティブなデータ表示機能

### 🐳 Docker統合
- **📦 コンテナ化**: 環境の一貫性と再現性を保証
- **⚙️ Docker Compose**: マルチサービス環境の簡単セットアップ
- **🔧 GPU対応**: NVIDIA GPU環境での機械学習ワークロード（GPUバージョン）
- **🔗 ポート管理**: JupyterLab（8888）とStreamlit（8501）の同時アクセス

## 🛠️ 技術スタック

### 核心技術
- **Python 3.9+**: プログラミング言語
- **JupyterLab 4.0+**: インタラクティブ開発環境
- **Streamlit 1.28.0+**: Webアプリケーションフレームワーク
- **Docker & Docker Compose**: コンテナ化とオーケストレーション

### データサイエンスライブラリ
- **NumPy**: 数値計算ライブラリ
- **Pandas**: データ操作・分析ライブラリ
- **Matplotlib & Seaborn**: データ可視化ライブラリ
- **Plotly**: インタラクティブ可視化ライブラリ
- **scikit-learn**: 機械学習ライブラリ

### 開発・実行環境
- **Jupyter Widgets**: インタラクティブウィジェット
- **HTML/CSS**: カスタムスタイリング
- **Linux**: ベースOS（Docker環境）

## 📦 インストールと起動

### 🐳 Docker Compose使用（推奨）

最も簡単な方法は、Docker Composeを使用することです：

```bash
# リポジトリをクローン
git clone https://github.com/Sunwood-ai-labs/jupyterlab-kit.git
cd jupyterlab-kit

# 環境を起動
docker-compose up -d
```

起動後、以下のURLでアクセス可能です：
- **JupyterLab**: http://localhost:8888
- **Streamlitアプリ**: http://localhost:8501

### 🚀 ローカルインストール

Docker環境を使わない場合：

#### 前提条件
- Python 3.9以上がインストールされていること
- pipが利用可能であること

#### セットアップ手順

1. **リポジトリをクローンします：**
```bash
git clone https://github.com/Sunwood-ai-labs/jupyterlab-kit.git
cd jupyterlab-kit
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

### 🐳 Docker環境での使用

```bash
# 環境を起動
docker-compose up -d

# ログを確認
docker-compose logs -f

# 環境を停止
docker-compose down
```

### 💻 ローカル環境での使用

#### JupyterLabの起動
```bash
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

#### Streamlitアプリの起動
```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

### 🌐 アクセス方法

起動後、以下のURLでアクセスできます：
- **JupyterLab**: http://localhost:8888 - データ分析・開発環境
- **Streamlitアプリ**: http://localhost:8501 - データサイエンスデモアプリ

### 📊 基本的な使い方

#### JupyterLab環境
1. **ノートブック作成** - 新しいPythonノートブックを作成
2. **データ分析** - 統合されたライブラリでデータ分析を実行
3. **可視化** - Matplotlib、Seaborn、Plotlyで美しいグラフを作成
4. **機械学習** - scikit-learnで予測モデルを構築

#### Streamlitアプリ
1. **デモ実行** - 「📈 サンプルデータ生成」ボタンをクリック
2. **データ表示** - 生成されたデータをテーブル形式で確認
3. **可視化確認** - 時系列データとカテゴリ分布のグラフを確認
4. **統計情報** - データの統計サマリーを確認

## 📁 ファイル構成

```
jupyterlab-kit/
├── README.md              # プロジェクト説明書（このファイル）
├── CLAUDE.md              # Claude AIアシスタント設定
├── app.py                 # Streamlitデモアプリケーション
├── requirements.txt       # Pythonパッケージリスト
├── Dockerfile             # 標準Docker設定
├── Dockerfile.gpu         # GPU対応Docker設定
├── docker-compose.yml     # 標準コンテナ構成
├── docker-compose.gpu.yml # GPU対応コンテナ構成
├── docker-compose.dev.yml # 開発用コンテナ構成
├── README.gpu.md          # GPU環境セットアップガイド
└── assets/
    └── jupyterlab-kit-banner.svg # プロジェクトバナー
```

### ファイル詳細

#### 🔬 コア環境ファイル
- **`Dockerfile`**: 標準Python環境でのJupyterLab + Streamlit統合
- **`Dockerfile.gpu`**: NVIDIA GPU対応環境設定
- **`docker-compose.yml`**: 本番用マルチサービス構成
- **`docker-compose.dev.yml`**: 開発用のボリュームマウント設定

#### 📱 アプリケーションファイル
- **`app.py`**: Streamlitデータサイエンスデモアプリケーション
- **`requirements.txt`**: データサイエンス・Web開発ライブラリ

#### 📖 ドキュメント
- **`README.md`**: プロジェクト情報とセットアップガイド
- **`README.gpu.md`**: GPU環境での機械学習ワークロード用ガイド
- **`CLAUDE.md`**: AI開発アシスタント設定ファイル

## 🎨 環境特徴

### 🔬 JupyterLab環境
- **統合開発環境**: ブラウザベースでの直感的な操作
- **マルチカーネル対応**: Python、R、Scalaなど多言語サポート
- **拡張機能**: 豊富なプラグインエコシステム
- **版管理統合**: Gitとの seamless な連携

### 🚀 Streamlit統合
- **レスポンシブデザイン**: 様々な画面サイズに自動対応
- **日本語対応**: 完全な日本語インターフェース
- **リアルタイムプレビュー**: コード変更の即座反映
- **直感的UI**: ワンクリックで簡単操作

### 🐳 Docker利点
- **環境一貫性**: 開発・本番環境の統一
- **簡単セットアップ**: ワンコマンドでの環境構築
- **スケーラビリティ**: 需要に応じた簡単なスケーリング
- **分離性**: ホストシステムからの完全分離

## 🔧 カスタマイズとデベロップメント

### 🚀 Streamlitアプリのカスタマイズ

`app.py`を編集することで、独自のデータサイエンスアプリケーションを開発できます：

```python
# カスタムデータ処理
def custom_data_processing():
    # あなたの処理をここに実装
    pass
```

### 🔬 JupyterLab拡張

新しいデータサイエンスライブラリやJupyterLab拡張機能を追加：

```dockerfile
# Dockerfileに追加
RUN pip install --no-cache-dir \
    your-new-library \
    another-extension
```

### 🐳 Docker環境のカスタマイズ

#### GPU対応の有効化
GPU環境での機械学習ワークロードには：
```bash
docker-compose -f docker-compose.gpu.yml up -d
```

#### 開発モードの使用
コードの変更をリアルタイムで反映：
```bash
docker-compose -f docker-compose.dev.yml up -d
```

## 🧪 テストと検証

### 🐳 Docker環境の動作確認

```bash
# 全サービスの状態確認
docker-compose ps

# ログ出力の確認
docker-compose logs

# 特定サービスのログ確認
docker-compose logs jupyterlab

# ヘルスチェック
curl http://localhost:8888  # JupyterLab
curl http://localhost:8501  # Streamlit
```

### 💻 ローカル環境の動作確認

```bash
# JupyterLabの起動テスト
jupyter lab --version

# Streamlitアプリの起動テスト
streamlit run app.py --server.headless true
```

### 📊 データサイエンス環境のテスト

JupyterLabで以下のセルを実行して環境を確認：

```python
# 基本ライブラリのインポートテスト
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn import datasets

# 簡単なデータ可視化テスト
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("Environment test successful! 🎉")
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

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 👥 作者情報

- **開発元**: [Sunwood AI Labs](https://github.com/Sunwood-ai-labs)
- **メンテナー**: Sunwood AI Labs チーム
- **サポート**: GitHub Issues を通じてサポートを提供

## 🙏 謝辞

- JupyterLabコミュニティの皆様
- Streamlitコミュニティの皆様
- オープンソースコミュニティへの感謝

---

<div align="center">

**Made with ❤️ using [JupyterLab](https://jupyter.org/) & [Streamlit](https://streamlit.io/)**

[🏠 ホーム](https://github.com/Sunwood-ai-labs/jupyterlab-kit) | 
[📊 Issues](https://github.com/Sunwood-ai-labs/jupyterlab-kit/issues) | 
[🔄 Pull Requests](https://github.com/Sunwood-ai-labs/jupyterlab-kit/pulls) |
[📖 Docs](https://github.com/Sunwood-ai-labs/jupyterlab-kit/wiki)

</div>
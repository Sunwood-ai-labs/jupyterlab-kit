FROM python:3.9-slim

LABEL maintainer="Sunwood AI Labs"
LABEL description="JupyterLab environment for data science"

WORKDIR /workspace

# システムパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# JupyterLabと追加パッケージをインストール
RUN pip install --no-cache-dir \
    jupyterlab \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    plotly \
    scikit-learn \
    jupyter-widgets \
    ipywidgets

# JupyterLab拡張機能をインストール
RUN jupyter lab build

# アプリケーションファイルをコピー
COPY . .

# ポートを公開
EXPOSE 8888

# JupyterLabを起動
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
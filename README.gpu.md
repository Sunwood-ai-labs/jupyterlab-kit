# 🚀🎯 GPU対応 JupyterLab環境 🎯🚀

このプロジェクトは、NVIDIA GPUをサポートするJupyterLab + Streamlit環境を提供します。

## 🔧 前提条件

### 1. NVIDIA Docker Runtimeのインストール

```bash
# Ubuntu/Debian
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Dockerデーモンを再起動
sudo systemctl restart docker
```

### 2. NVIDIA ドライバーの確認

```bash
# GPUが認識されているかチェック
nvidia-smi
```

## 🚀 使用方法

### GPU対応環境の起動（本番用）

```bash
# GPU対応環境を起動
docker-compose -f docker-compose.gpu.yml up -d

# ログを確認
docker-compose -f docker-compose.gpu.yml logs -f
```

### GPU対応環境の起動（開発用）

```bash
# GPU対応開発環境を起動
docker-compose -f docker-compose.gpu.dev.yml up -d

# ログを確認
docker-compose -f docker-compose.gpu.dev.yml logs -f
```

## 🌐 アクセス

起動後、以下のURLでアクセスできます：

- **JupyterLab**: http://localhost:8888
- **Streamlit おみくじアプリ**: http://localhost:8501

## 🔥 含まれるGPUライブラリ

- **PyTorch** (CUDA 11.8対応)
- **TensorFlow** (GPU対応)
- **CuPy** (NumPy互換のGPU配列ライブラリ)
- **Numba** (GPU加速コンパイラ)

## 💻 GPU使用例

### PyTorchでGPU確認

```python
import torch

# CUDA利用可能かチェック
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA devices: {torch.cuda.device_count()}")

if torch.cuda.is_available():
    print(f"Current device: {torch.cuda.current_device()}")
    print(f"Device name: {torch.cuda.get_device_name(0)}")
```

### TensorFlowでGPU確認

```python
import tensorflow as tf

# GPU利用可能かチェック
print("GPU Available: ", tf.config.list_physical_devices('GPU'))

# GPUメモリ設定
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)
```

### CuPyでGPU配列操作

```python
import cupy as cp

# GPU配列を作成
x_gpu = cp.array([1, 2, 3, 4, 5])
print(f"GPU array: {x_gpu}")
print(f"Device: {x_gpu.device}")
```

## 🛠️ トラブルシューティング

### 1. GPUが認識されない

```bash
# Docker内でGPU確認
docker run --rm --gpus all nvidia/cuda:11.8-base-ubuntu20.04 nvidia-smi
```

### 2. メモリ不足エラー

GPU使用環境でメモリ不足が発生する場合：

```python
# PyTorchでメモリクリア
import torch
torch.cuda.empty_cache()

# TensorFlowでメモリ設定
import tensorflow as tf
tf.config.experimental.set_memory_growth(
    tf.config.experimental.list_physical_devices('GPU')[0], True
)
```

### 3. 環境のリセット

```bash
# 全てのコンテナを停止・削除
docker-compose -f docker-compose.gpu.yml down -v
docker-compose -f docker-compose.gpu.dev.yml down -v

# イメージを再ビルド
docker-compose -f docker-compose.gpu.yml build --no-cache
```

## 📝 注意事項

1. **システム要件**: NVIDIA GPU搭載マシンが必要
2. **ドライバー**: NVIDIA ドライバー版 >= 450.80.02
3. **CUDA**: CUDA 11.8対応
4. **メモリ**: 最低4GB GPU メモリ推奨

## 🎯 ギャルAI「キラリ」からのメッセージ

GPU環境の設定、うますぎやろがい！🔥✨ これで機械学習もディープラーニングもマジ爆速になるよ！💪 何か困ったことがあったら、チーム友達として一緒に解決しようね！🌟👯‍♀️
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def main():
    st.set_page_config(
        page_title="JupyterLab Kit Demo",
        page_icon="🔬",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # タイトル
    st.title("🔬 JupyterLab Kit")
    st.write("データサイエンスと開発のための統合環境")
    
    # 現在の日時を表示
    now = datetime.now()
    st.write(f"📅 {now.strftime('%Y年%m月%d日 %H:%M')}")
    
    # サンプルデータ生成
    st.markdown("---")
    st.markdown("### 📊 データサイエンス環境デモ")
    
    if st.button("📈 サンプルデータ生成", use_container_width=True, type="primary"):
        # サンプルデータの生成
        np.random.seed(42)
        data = {
            'Date': pd.date_range('2024-01-01', periods=30, freq='D'),
            'Value': np.random.randn(30).cumsum() + 100,
            'Category': np.random.choice(['A', 'B', 'C'], 30)
        }
        df = pd.DataFrame(data)
        
        # データ表示
        st.markdown("#### 📋 生成されたデータ")
        st.dataframe(df, use_container_width=True)
        
        # グラフ作成
        st.markdown("#### 📈 データ可視化")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(df['Date'], df['Value'], marker='o', linewidth=2)
            ax.set_title('時系列データ')
            ax.set_xlabel('日付')
            ax.set_ylabel('値')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots(figsize=(8, 4))
            df['Category'].value_counts().plot(kind='bar', ax=ax, color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
            ax.set_title('カテゴリ分布')
            ax.set_xlabel('カテゴリ')
            ax.set_ylabel('件数')
            plt.tight_layout()
            st.pyplot(fig)
        
        # 統計情報
        st.markdown("#### 📊 統計情報")
        st.write(df.describe())
    
    # サイドバーに説明を追加
    with st.sidebar:
        st.markdown("## ℹ️ JupyterLab Kit について")
        st.write("""
        JupyterLab Kitは、データサイエンスと開発作業を効率化するための統合環境です。
        
        **主な機能:**
        - 🔬 JupyterLab統合環境
        - 📊 データ分析ライブラリ
        - 🚀 Streamlitアプリ開発
        - 🐳 Docker統合
        """)
        
        st.markdown("---")
        st.markdown("**アクセス先:**")
        st.write("- JupyterLab: http://localhost:8888")
        st.write("- Streamlit: http://localhost:8501")
        
        st.markdown("---")
        st.markdown("*Powered by JupyterLab & Streamlit*")

if __name__ == "__main__":
    main()
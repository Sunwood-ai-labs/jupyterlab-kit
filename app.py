import streamlit as st
import random
from datetime import datetime

# おみくじの結果リスト
OMIKUJI_RESULTS = [
    {
        "result": "大吉",
        "color": "#ff6b6b",
        "message": "とても良い運勢です！何事も積極的に取り組むと良い結果が得られるでしょう。",
        "advice": "新しいことにチャレンジするのに最適な時期です。"
    },
    {
        "result": "中吉",
        "color": "#4ecdc4",
        "message": "運勢は上々です。慎重に行動すれば良い結果が期待できます。",
        "advice": "焦らずに着実に進んでいきましょう。"
    },
    {
        "result": "小吉",
        "color": "#45b7d1",
        "message": "まずまずの運勢です。小さな幸せを大切にしてください。",
        "advice": "身近な人との関係を大切にすると良いでしょう。"
    },
    {
        "result": "吉",
        "color": "#96ceb4",
        "message": "穏やかな運勢です。日々の努力が報われるでしょう。",
        "advice": "継続は力なり。今の努力を続けてください。"
    },
    {
        "result": "末吉",
        "color": "#feca57",
        "message": "後半に向けて運勢が上昇します。希望を持って進みましょう。",
        "advice": "今は準備の時期。将来のために力を蓄えましょう。"
    },
    {
        "result": "凶",
        "color": "#ff9ff3",
        "message": "少し注意が必要な時期です。慎重に行動しましょう。",
        "advice": "無理をせず、体調管理に気をつけてください。"
    },
    {
        "result": "大凶",
        "color": "#54a0ff",
        "message": "困難な時期ですが、必ず乗り越えられます。",
        "advice": "今は耐える時期。周りの人に相談することも大切です。"
    }
]

def main():
    st.set_page_config(
        page_title="おみくじアプリ",
        page_icon="🎋",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # タイトル
    st.title("🎋 おみくじアプリ")
    st.write("今日の運勢を占ってみましょう！")
    
    # 現在の日時を表示
    now = datetime.now()
    st.write(f"📅 {now.strftime('%Y年%m月%d日 %H:%M')}")
    
    # おみくじを引くボタン
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🎯 おみくじを引く", use_container_width=True, type="primary"):
            # ランダムにおみくじの結果を選択
            result = random.choice(OMIKUJI_RESULTS)
            
            # 結果を表示
            st.balloons()
            
            # 結果のカードを表示
            st.markdown("---")
            st.markdown(f"### 🎋 あなたの運勢")
            
            # 結果を大きく表示
            st.markdown(
                f"""
                <div style="
                    background-color: {result['color']};
                    color: white;
                    padding: 30px;
                    border-radius: 15px;
                    text-align: center;
                    margin: 20px 0;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                ">
                    <h1 style="margin: 0; font-size: 3em; font-weight: bold;">
                        {result['result']}
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # メッセージとアドバイス
            st.markdown("#### 💭 今日のメッセージ")
            st.info(result['message'])
            
            st.markdown("#### 💡 アドバイス")
            st.success(result['advice'])
            
            # もう一度引くボタン
            if st.button("🔄 もう一度引く", use_container_width=True):
                st.rerun()
    
    # サイドバーに説明を追加
    with st.sidebar:
        st.markdown("## ℹ️ おみくじについて")
        st.write("""
        このおみくじアプリは、日本の伝統的なおみくじをモチーフにしています。
        
        **運勢の種類:**
        - 大吉 (最高の運勢)
        - 中吉 (とても良い運勢)
        - 小吉 (良い運勢)
        - 吉 (普通の運勢)
        - 末吉 (後半良くなる運勢)
        - 凶 (注意が必要)
        - 大凶 (困難な時期)
        
        毎日新しい気持ちでおみくじを引いてみてください！
        """)
        
        st.markdown("---")
        st.markdown("*Made with ❤️ using Streamlit*")

if __name__ == "__main__":
    main()

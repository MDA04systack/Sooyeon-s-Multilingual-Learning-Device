# %% [1] 라이브러리 설치 (필요한 경우 터미널에서 실행하거나 이 셀을 실행하세요)
# pip install streamlit googletrans==4.0.0-rc1 gTTS
# pip install deep-translator gTTS streamlit

# %% [2] 라이브러리 임포트
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# %% [3] 앱 설정 및 UI 구성
st.set_page_config(page_title="박수연의 다국어 학습기", page_icon="🔊", layout="centered")

st.title("박수연의 다국어 학습기")
st.markdown("🇰🇷 한국어 → 다국어 번역 및 음성")
st.markdown("입력한 한국어를 외국어로 번역하고 음성을 생성합니다.")

# 언어 설정 (deep-translator용)
lang_dict = {
    '영어 (English)': 'en',
    '일본어 (Japanese)': 'ja',
    '중국어 (Chinese)': 'zh-CN',
    '스페인어 (Spanish)': 'es'
}

# %% [4] 사용자 인터페이스 (입력부)
# 1. 언어 선택
target_lang_name = st.selectbox(
    "1. 번역할 언어를 선택하세요", 
    list(lang_dict.keys()), 
    key="lang_select_v3"
)
target_code = lang_dict[target_lang_name]

# 2. 음성 속도 선택 (1번 방법: gTTS 기본 slow 옵션 활용)
# 사용자가 이 체크박스를 체크하면 음성이 느리게 나옵니다.
is_slow = st.checkbox("🐢 천천히 읽어주세요 (느린 속도)", key="speed_check_v3")

# 3. 텍스트 입력
user_input = st.text_area(
    "2. 번역할 한국어 내용을 입력하세요", 
    height=15)
# %% [5] 번역 및 음성 처리 함수
def process_translation():
    if st.button("번역 및 음성 생성", key="btn_v3"):
        if not user_input.strip():
            st.warning("내용을 입력해주세요.")
        else:
            with st.spinner('번역 및 음성 파일 생성 중...'):
                try:
                    # 번역 실행
                    translator = GoogleTranslator(source='ko', target=target_code)
                    translated_text = translator.translate(user_input)
                    
                    st.divider()
                    
                    # 결과 출력
                    st.subheader(f"🌐 {target_lang_name} 번역 결과")
                    st.success(translated_text)
                    
                    # 음성 생성 (gTTS)
                    # slow=True 면 느리게, slow=False 면 보통 속도로 생성됩니다.
                    tts = gTTS(
                        text=translated_text, 
                        lang=target_code.split('-')[0].lower(), 
                        slow=is_slow
                    )
                    
                    audio_file = "translated_voice.mp3"
                    tts.save(audio_file)
                    
                    # 오디오 플레이어 출력
                    st.audio(audio_file)
                    
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")
                    st.info("Tip: 인터넷 연결 상태를 확인하거나 잠시 후 다시 시도해 주세요.")

# %% [6] 실행부
if __name__ == "__main__":
    process_translation()
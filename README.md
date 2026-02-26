# 박수연의 다국어 학습기 (Sooyeon's Multilingual Learning Device)

이 프로젝트는 입력된 한국어를 다양한 외국어로 번역하고, 번역된 문장을 음성으로 들어볼 수 있는 Streamlit 기반 웹 애플리케이션입니다.

## 1. 프로젝트의 주요 기능과 목적
**목적:** 사용자가 한국어 문장을 쉽게 다른 언어로 번역하고 발음을 학습할 수 있도록 돕는 다국어 번역 및 음성 학습 도구입니다.

**주요 기능:**
- **다국어 번역:** 한국어를 영어, 일본어, 중국어, 스페인어로 번역합니다 (`deep-translator`의 `GoogleTranslator` 사용).
- **TTS (텍스트-음성 변환) 지원:** 번역된 결과물을 음성으로 읽어줍니다 (`gTTS` 사용).
- **학습자 맞춤형 속도 조절:** 텍스트를 천천히 읽어주는 '느린 속도' 옵션을 제공하여 초보 학습자도 정확한 발음을 들을 수 있습니다.
- **직관적인 UI:** Streamlit을 활용하여 언어 선택, 입력, 결과 확인 및 재생까지 한 화면에서 간단하게 이용 가능합니다.

## 2. 설치 방법

### 사전 요구 사항
- Python 3.8 이상이 설치되어 있어야 합니다.

### 설치 및 실행 순서
1. **저장소 클론 (Clone Repository)**
   ```bash
   git clone https://github.com/MDA04systack/Sooyeon-s-Multilingual-Learning-Device.git
   cd Sooyeon-s-Multilingual-Learning-Device
   ```

2. **필요 파이썬 패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```
   *(참고: 필수 패키지는 `streamlit`, `deep-translator`, `gTTS` 등입니다.)*

3. **애플리케이션 실행**
   ```bash
   streamlit run translater_app_v2.py
   ```
   웹 브라우저가 자동으로 실행되며 앱을 사용할 수 있습니다.

## 3. 문제 해결 방법
- **[오류] `ModuleNotFoundError` 발생:** 패키지 설치가 누락된 경우입니다. 터미널에서 `pip install -r requirements.txt`를 실행하여 의존성 패키지를 다시 설치해 주세요.
- **[오류] 번역 및 음성 생성이 되지 않음:** `deep-translator`와 `gTTS`는 구글 서비스와 통신해야 하므로 **인터넷 연결이 필수**입니다. 인터넷 연결 상태를 확인해 주세요.
- **[오류] 음성 재생 불가:** 사용 중인 브라우저(Safari 등)의 보안 설정에 따라 자동 재생이나 오디오 파일 재생이 차단될 수 있습니다. Chrome이나 Edge 브라우저 사용을 권장합니다.

## 4. 지원 창구
- 앱 사용 중 문제나 버그를 발견하신 경우, 혹은 추가로 원하는 기능이 있다면 이 저장소의 **[Issues]** 탭을 통해 제보 및 문의해 주세요.

## 5. 라이선스 정보
이 프로젝트는 [MIT License](LICENSE)를 따릅니다. 누구나 자유롭게 사용, 수정, 배포가 가능합니다. 단, 코드 내 사용된 외부 라이브러리(`gTTS`, `deep-translator` 등)의 라이선스 정책도 함께 참고하시기 바랍니다.

## 6. 변경 로그
- **v1.0.0** 
  - 기본 UI(언어 선택, 텍스트 입력 영역) 구현 완료
  - 한국어 → 영어, 일본어, 중국어, 스페인어 번역 연동
  - gTTS 음성 합성 및 느린 재생 옵션 기능 추가

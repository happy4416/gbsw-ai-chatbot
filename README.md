# 🎓 경북소프트웨어마이스터고 도우미 AI

> RAG 기반 학교 정보 챗봇 - 학생들의 궁금증을 해결해드립니다!

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14+-black.svg)](https://nextjs.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Latest-orange.svg)](https://ollama.ai/)
<img width="1068" height="832" alt="스크린샷 2026-04-28 181106" src="https://github.com/user-attachments/assets/e4e2f0cf-f33c-4b0f-9a7f-db0d9e521739" />

## 📌 프로젝트 소개

경북소프트웨어마이스터고등학교의 학생들을 위한 AI 도우미입니다.
학교 정보, 학과 안내, 입학 정보 등을 RAG(Retrieval-Augmented Generation) 기술을 활용하여 정확하고 친절하게 답변합니다.

### ✨ 주요 기능

- 🤖 **AI 기반 질의응답**: Ollama를 활용한 자연스러운 대화
- 📚 **RAG 시스템**: ChromaDB를 통한 정확한 정보 검색
- 🏫 **학교 정보 제공**: 3개 학과, 입학 안내, 특전 등 상세 정보
- 💬 **실시간 채팅**: 빠르고 직관적인 웹 인터페이스
- 🔄 **자동 업데이트**: 학교 정보 자동 크롤링 및 업데이트

## 🛠️ 기술 스택

### Backend
- **FastAPI**: 고성능 Python 웹 프레임워크
- **Ollama**: 로컬 LLM 실행 (neural-chat 모델)
- **ChromaDB**: 벡터 데이터베이스 (로컬 저장)
- **BeautifulSoup4**: 웹 크롤링

### Frontend
- **Next.js 14**: React 기반 풀스택 프레임워크
- **TypeScript**: 타입 안정성
- **Axios**: HTTP 클라이언트

## 📦 설치 방법

### 사전 요구사항

- Python 3.11 이상
- Node.js 18 이상
- Ollama 설치 ([다운로드](https://ollama.ai/))

### 1️⃣ Ollama 설치 및 모델 다운로드

```bash
# Ollama 설치 (Windows)
# https://ollama.ai/download 에서 다운로드

# 모델 다운로드
ollama pull neural-chat
```

### 2️⃣ 백엔드 설정

```bash
cd backend

# 가상환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 3️⃣ 프론트엔드 설정

```bash
cd frontend

# 패키지 설치
npm install

# 개발 서버 실행
npm run dev
```

### 4️⃣ 접속

브라우저에서 http://localhost:3000 접속

## 🚀 사용 방법

1. 웹 브라우저에서 챗봇 접속
2. 학교에 대해 궁금한 점을 입력
3. AI가 학교 정보를 바탕으로 답변 제공

### 💡 예시 질문

- "학교 위치가 어디인가요?"
- "어떤 학과가 있나요?"
- "임베디드소프트웨어과에서 뭘 배우나요?"
- "입학하려면 어떻게 해야 하나요?"
- "병역특례가 가능한가요?"
- "기숙사가 있나요?"

## 📂 프로젝트 구조

```
gbsw-ai-chatbot/
├── backend/
│   ├── app.py                      # FastAPI 메인 애플리케이션
│   ├── requirements.txt            # Python 패키지
│   └── services/
│       ├── crawler_service.py      # 학교 정보 크롤러
│       ├── ollama_service.py       # Ollama API 클라이언트
│       └── vector_service.py       # ChromaDB 벡터 저장소
├── frontend/
│   ├── app/
│   │   ├── page.tsx               # 메인 페이지
│   │   └── layout.tsx             # 레이아웃
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

## 🎯 주요 API 엔드포인트

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/` | 서버 상태 확인 |
| GET | `/api/health` | 시스템 헬스 체크 |
| GET | `/api/models` | 사용 가능한 모델 목록 |
| POST | `/api/chat` | 채팅 메시지 전송 |
| GET | `/api/stats` | 통계 정보 조회 |
| POST | `/api/recrawl` | 학교 정보 재크롤링 |

## 📊 학교 정보

현재 포함된 정보:
- ✅ 학교 기본 정보 (위치: 경상북도 의성군)
- ✅ 3개 학과 상세 정보
  - 임베디드소프트웨어과
  - 스마트IoT과
  - 인공지능소프트웨어과
- ✅ 입학 안내
- ✅ 특전 및 혜택 (병역특례, 기숙사, 장학금 등)
- ✅ 교육 과정 및 진로 정보

## 🔧 개발 환경

- **OS**: Windows 11
- **GPU**: NVIDIA RTX A4000 (16GB VRAM)
- **CUDA**: 12.4
- **Python**: 3.12
- **Node.js**: 18+

## 📝 TODO

- [ ] NEIS API 연동으로 공식 학교 정보 가져오기
- [ ] 더 많은 학교 정보 추가 (동아리, 행사 등)
- [ ] 다국어 지원 (영어, 중국어)
- [ ] 음성 인식 기능 추가
- [ ] 모바일 앱 버전 개발
- [ ] 사용자 피드백 시스템

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 👥 개발자

- **경북소프트웨어마이스터고등학교 학생**

## 🙏 감사의 말

- [Ollama](https://ollama.ai/) - 로컬 LLM 실행 환경
- [ChromaDB](https://www.trychroma.com/) - 벡터 데이터베이스
- [FastAPI](https://fastapi.tiangolo.com/) - 백엔드 프레임워크
- [Next.js](https://nextjs.org/) - 프론트엔드 프레임워크

---

<div align="center">
  <strong>Made with ❤️ by GBSW Students</strong>
  <br>
  <sub>경북소프트웨어마이스터고등학교</sub>
</div>

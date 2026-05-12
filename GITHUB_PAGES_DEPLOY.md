# GitHub Pages 배포 가이드

## 🚀 배포 방법

### 1단계: 빌드 및 배포

```bash
cd frontend
npm run deploy
```

이 명령어가 자동으로:
1. Next.js 빌드 (`npm run build`)
2. `out` 폴더 생성
3. `gh-pages` 브랜치에 푸시

### 2단계: GitHub Pages 활성화

1. GitHub 저장소 접속: https://github.com/happy4416/gbsw-ai-chatbot
2. **Settings** → **Pages** 클릭
3. **Source** 섹션에서:
   - Branch: `gh-pages` 선택
   - Folder: `/ (root)` 선택
4. **Save** 클릭

### 3단계: 배포 확인

약 1~2분 후:
- 배포 URL: https://happy4416.github.io/gbsw-ai-chatbot

---

## ⚠️ 중요 사항

### 백엔드 연결
GitHub Pages는 정적 사이트만 지원하므로 **백엔드는 로컬에서 실행**해야 합니다:

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
```

### CORS 설정
백엔드 `app.py`에 GitHub Pages URL 추가:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://happy4416.github.io"  # 추가
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🔧 재배포

코드 수정 후 재배포:

```bash
cd frontend
npm run deploy
```

자동으로 업데이트됩니다!

---

## 📊 배포 상태 확인

GitHub 저장소 → **Actions** 탭에서 배포 진행 상황 확인 가능

---

## 🐛 트러블슈팅

### 404 에러
- GitHub Pages 설정 확인
- `gh-pages` 브랜치 존재 확인

### API 연결 안 됨
- 백엔드 실행 확인
- CORS 설정 확인
- 브라우저 콘솔에서 에러 확인

### 빌드 오류
```bash
cd frontend
rm -rf .next out
npm run build
```

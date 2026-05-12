# 배포 가이드

## 🚀 배포 방법

### 방법 1: Vercel (프론트엔드) + Railway (백엔드) - 추천!

#### 백엔드 배포 (Railway)

1. **Railway 계정 생성**
   - https://railway.app 접속
   - GitHub 계정으로 로그인

2. **새 프로젝트 생성**
   - "New Project" 클릭
   - "Deploy from GitHub repo" 선택
   - 이 저장소 선택

3. **환경 변수 설정**
   ```
   OLLAMA_API_URL=https://your-ollama-server.com
   PORT=8000
   ```

4. **배포 확인**
   - Railway가 자동으로 Dockerfile.backend 감지
   - 빌드 및 배포 완료 대기
   - 생성된 URL 복사 (예: https://your-app.railway.app)

#### 프론트엔드 배포 (Vercel)

1. **Vercel 계정 생성**
   - https://vercel.com 접속
   - GitHub 계정으로 로그인

2. **새 프로젝트 생성**
   - "Add New Project" 클릭
   - 이 저장소 선택
   - Root Directory: `frontend` 설정

3. **환경 변수 설정**
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.railway.app
   ```

4. **배포**
   - "Deploy" 클릭
   - 배포 완료 대기

---

### 방법 2: Docker Compose (로컬/서버)

#### 사전 요구사항
- Docker 설치
- Docker Compose 설치
- Ollama 실행 중

#### 배포 명령어

```bash
# 빌드 및 실행
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 중지
docker-compose down
```

#### 접속
- 프론트엔드: http://localhost:3000
- 백엔드: http://localhost:8000

---

### 방법 3: 수동 배포

#### 백엔드

```bash
cd backend

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### 프론트엔드

```bash
cd frontend

# 패키지 설치
npm install

# 빌드
npm run build

# 프로덕션 서버 실행
npm start
```

---

## ⚠️ 주의사항

### Ollama 서버
- **로컬 배포**: Ollama가 로컬에서 실행 중이어야 함
- **클라우드 배포**: Ollama를 별도 서버에 배포하거나 API 서비스 사용 필요

### 환경 변수
백엔드 `.env` 파일 (선택사항):
```
OLLAMA_API_URL=http://localhost:11434
```

프론트엔드 `.env.local` 파일:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### CORS 설정
프로덕션 배포 시 `backend/app.py`의 CORS 설정 수정:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🔧 트러블슈팅

### Ollama 연결 오류
- Ollama 서버가 실행 중인지 확인
- `OLLAMA_API_URL` 환경 변수 확인
- 방화벽 설정 확인

### ChromaDB 오류
- `chroma_db` 디렉토리 권한 확인
- 볼륨 마운트 설정 확인

### 프론트엔드 API 연결 오류
- `NEXT_PUBLIC_API_URL` 환경 변수 확인
- CORS 설정 확인
- 백엔드 서버 상태 확인

---

## 📊 성능 최적화

### 백엔드
- Gunicorn 사용 (멀티 워커)
- Redis 캐싱 추가
- 로드 밸런싱

### 프론트엔드
- Next.js ISR/SSG 활용
- 이미지 최적화
- CDN 사용

---

## 🔒 보안

- API 키 환경 변수로 관리
- HTTPS 사용
- Rate limiting 추가
- 입력 검증 강화

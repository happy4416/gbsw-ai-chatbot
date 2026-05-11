import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time

class CrawlerService:
    def __init__(self):
        self.base_url = "https://gbsw.hs.kr"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def crawl_school_info(self) -> List[Dict[str, str]]:
        """학교 정보 크롤링"""
        documents = []
        
        # 기본 학교 정보 (공식 홈페이지 기반)
        documents.append({
            "title": "경북소프트웨어마이스터고등학교 기본 정보",
            "content": """
경북소프트웨어마이스터고등학교는 대한민국 경상북도 의성군에 위치한 소프트웨어 특성화 마이스터고등학교입니다.

📍 학교 정보:
- 정식 명칭: 경북소프트웨어마이스터고등학교
- 영문명: Gyeongbuk Software Meister High School
- 약칭: 경소마고, GBSW
- 설립: 2016년
- 주소: 경상북도 의성군 봉양면 봉호로 14
- 홈페이지: https://gbsw.hs.kr
- 전화: 교무실 054-832-2903, 행정실 054-832-2900
- 팩스: 054-833-2877

🎯 교육 비전:
"미래의 삶을 코딩하는 글로벌 소프트웨어 인재양성"

🏫 학교 유형:
- 마이스터고등학교 (소프트웨어 특성화)
- 전국 단위 모집
- 공립 특성화 고등학교

💡 교육 목표:
- 소프트웨어 분야의 전문 기술인 양성
- 글로벌 경쟁력을 갖춘 인재 육성
- 산업체 맞춤형 실무 교육
- 창의적 문제해결 능력 배양

학과 정보:
1. 임베디드소프트웨어과
   - IoT, 임베디드 시스템 개발
   - 하드웨어와 소프트웨어 융합 교육
   - 마이크로컨트롤러, 센서, 액추에이터 제어
   - Arduino, Raspberry Pi, STM32 등 실습

2. 스마트IoT과
   - 사물인터넷(IoT) 기술
   - 스마트 디바이스 개발
   - 클라우드 및 빅데이터 연동
   - 모바일 앱 개발 (Android, iOS)

3. 인공지능소프트웨어과
   - AI, 머신러닝, 딥러닝
   - 데이터 분석 및 AI 모델 개발
   - Python, TensorFlow, PyTorch
   - 컴퓨터 비전, 자연어 처리

🎁 특전 및 혜택:
- ✅ 병역특례 (산업기능요원) 가능
- ✅ 취업 연계 프로그램 운영 (대기업, IT기업)
- ✅ 기업 맞춤형 교육 제공
- ✅ 전액 장학금 지원 (수업료 무료)
- ✅ 기숙사 제공 (전교생 수용 가능, 무료)
- ✅ 최신 실습 장비 및 개발 환경 제공
- ✅ 1인 1노트북 지급
- ✅ 24시간 개발 환경 제공

📚 교육 과정:
- 3년 과정 (일반계 고등학교와 동일)
- 전문 교과 70% + 보통 교과 30%
- 프로젝트 기반 학습 (PBL)
- 기업 연계 현장실습
- 자격증 취득 지원 (정보처리기능사, 리눅스마스터, 네트워크관리사 등)

💼 졸업 후 진로:
- 대기업 및 중견기업 취업 (삼성전자, LG전자, 네이버, 카카오, 쿠팡 등)
- 소프트웨어 개발자, 시스템 엔지니어, AI 엔지니어
- 스타트업 창업 지원
- 대학 진학 (특별전형, 재직자 전형)

🏆 학교 특색:
- 동아리 활동 활성화 (해킹, 게임 개발, 앱 개발, 로봇 등)
- 각종 대회 참가 지원 (해커톤, 공모전, 경진대회)
- 선배-후배 멘토링 시스템
- 기업 협약 및 산학협력
- AI 리터러시 및 AI 윤리 교육
- 경북형 온자람 공간 (창의적 학습 공간)
            """,
            "source": "학교 기본 정보"
        })
        
        # 학과별 상세 정보
        documents.append({
            "title": "임베디드소프트웨어과 상세 정보",
            "content": """
임베디드소프트웨어과는 하드웨어와 소프트웨어를 융합한 임베디드 시스템 전문가를 양성합니다.

주요 학습 내용:
- C/C++ 프로그래밍
- 마이크로컨트롤러 (Arduino, Raspberry Pi)
- 임베디드 리눅스
- 센서 및 액추에이터 제어
- RTOS (Real-Time Operating System)
- 펌웨어 개발

실습 장비:
- 각종 개발 보드 (STM32, ESP32 등)
- 오실로스코프, 멀티미터
- 3D 프린터
- 납땜 장비

진로:
- 임베디드 소프트웨어 개발자
- 펌웨어 엔지니어
- IoT 디바이스 개발자
- 자동차 전장 개발자
            """,
            "source": "학과 정보"
        })
        
        documents.append({
            "title": "스마트IoT과 상세 정보",
            "content": """
스마트IoT과는 사물인터넷 기술을 활용한 스마트 시스템 전문가를 양성합니다.

주요 학습 내용:
- IoT 플랫폼 개발
- 센서 네트워크
- 클라우드 컴퓨팅 (AWS, Azure)
- 빅데이터 처리
- 모바일 앱 개발 (Android, iOS)
- 웹 개발 (HTML, CSS, JavaScript)

실습 프로젝트:
- 스마트 홈 시스템
- 스마트 팜
- 환경 모니터링 시스템
- 헬스케어 IoT

진로:
- IoT 솔루션 개발자
- 클라우드 엔지니어
- 모바일 앱 개발자
- 풀스택 개발자
            """,
            "source": "학과 정보"
        })
        
        documents.append({
            "title": "인공지능소프트웨어과 상세 정보",
            "content": """
인공지능소프트웨어과는 AI 및 데이터 분석 전문가를 양성합니다.

주요 학습 내용:
- Python 프로그래밍
- 머신러닝 (Scikit-learn)
- 딥러닝 (TensorFlow, PyTorch)
- 데이터 분석 (Pandas, NumPy)
- 컴퓨터 비전 (OpenCV)
- 자연어 처리 (NLP)

실습 프로젝트:
- 이미지 인식 시스템
- 챗봇 개발
- 추천 시스템
- 예측 모델 개발

진로:
- AI 엔지니어
- 데이터 사이언티스트
- 머신러닝 엔지니어
- AI 연구원
            """,
            "source": "학과 정보"
        })
        
        documents.append({
            "title": "입학 및 지원 안내",
            "content": """
경북소프트웨어마이스터고등학교 입학 안내

모집 시기:
- 매년 10월~11월 원서 접수
- 12월 면접 및 합격자 발표

지원 자격:
- 중학교 졸업 예정자 또는 졸업자
- 전국 단위 모집 (거주지 제한 없음)
- 소프트웨어 분야에 관심과 열정이 있는 학생

전형 방법:
1. 1단계: 서류 전형 (내신 성적)
2. 2단계: 면접 전형 (인성, 적성, 열정 평가)

우대 사항:
- 정보 관련 자격증 보유자
- 소프트웨어 관련 대회 수상자
- 봉사활동 우수자
- 특기자 (프로그래밍 포트폴리오)

제출 서류:
- 입학원서
- 중학교 생활기록부
- 자기소개서
- 학업계획서

문의:
- 학교 홈페이지: https://gbsw.hs.kr
- 전화 문의: 학교 행정실

장학금:
- 성적 우수 장학금
- 가정형편 곤란 장학금
- 기업 후원 장학금
            """,
            "source": "입학 안내"
        })
        
        return documents
    
    def _extract_text(self, soup: BeautifulSoup) -> str:
        """HTML에서 텍스트 추출"""
        # 불필요한 태그 제거
        for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()
        
        # 본문 영역 찾기
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        if main_content:
            text = main_content.get_text(separator='\n', strip=True)
        else:
            text = soup.get_text(separator='\n', strip=True)
        
        # 빈 줄 제거 및 정리
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)

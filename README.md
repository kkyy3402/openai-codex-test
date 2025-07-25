# openai-codex-test

이 저장소는 Next.js + TypeScript로 작성된 클라이언트와 FastAPI 기반 서버 예제를 포함합니다. 서버는 다양한 주식 및 차트 전략을 조회할 수 있는 API를 제공하며, 클라이언트는 간단한 UI로 해당 데이터를 표시합니다.

## 구조

- `client/` – Next.js 애플리케이션
- `server/` – FastAPI 애플리케이션

## 사용 방법

1. 서버와 클라이언트 디렉터리 각각에 `.env` 파일을 생성하여 필요한 값을 입력합니다.
2. 의존성 설치:

```bash
cd server && pip install -r requirements.txt
cd ../client && npm install
```

3. API 서버 실행:

```bash
cd server
uvicorn main:app --reload
```

4. Next.js 개발 서버 실행:

```bash
cd client
npm run dev
```

실행 후 브라우저에서 주식 전략과 차트 데이터를 확인할 수 있습니다.

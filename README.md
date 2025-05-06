# deepfake_rag

Retrieval‑Augmented **Deepfake Detection + Verification**

영상 (or 이미지) 속 얼굴이 **딥페이크**인지 판별하고,

실존 인물이라면 외부 지식(위키·뉴스)을 RAG로 검색해 **팩트체크**까지 수행합니다.

deepfake_rag/
├── requirements.txt # 의존 라이브러리
├── [config.py](http://config.py/) # 경로·모델 설정
├── [crawler.py](http://crawler.py/) # 위키·뉴스 크롤링
├── build_passages.py # RAG 용 jsonl 패시지 생성
├── register_faces.py # 알려진 인물 얼굴 임베딩 등록
├── detect_and_verify.py # 딥페이크 탐지 + RAG 검증
├── [main.py](http://main.py/) # CLI 진입점
└── data/
├── raw_text/ # 크롤링 원문
├── external_data_passages.jsonl
├── faiss_index
├── known_faces.pkl
└── known_faces_images/ # ★손흥민.jpg 등 넣기

## 2. 외부 지식 구축

1. **RAW 텍스트 수집**
    
    ```bash
    python crawler.py                # config 안 persons 리스트 수정 가능
    
    ```
    
2. **패시지(jsonl) 생성**
    
    ```bash
    python build_passages.py
    
    ```
    
3. **FAISS 인덱스 자동 구축**
    
    첫 실행 시 `transformers` 가 passages 파일을 읽어 인덱스를 만듭니다
    
    (생성된 인덱스는 `data/faiss_index` 에 캐싱).
    

---

## 3. 알려진 얼굴 등록

`data/known_faces_images/` 폴더에

`손흥민.jpg`, `이재명.png` … 처럼 **1 인 1 파일**로 넣은 뒤:

```bash
python register_faces.py

```

> face_recognition 으로 128‑d 임베딩을 뽑아 known_faces.pkl 로 저장합니다.
> 

---

## 4. 사용법

```bash
python main.py -i sample.jpg

```

출력 예시

```
Person Identified: 손흥민
Deepfake Detected: True (score: 0.87)
RAG Context Verification:
손흥민은 최근 토트넘 홋스퍼에서 프리미어리그 17호골을 기록했다 …

```

- **Deepfake score** ≥ 0.5 → 가짜로 간주
- 얼굴 미식별 시 `Person Identified: None`

---

## 5. 코드 내부 흐름

1. **detect_and_verify.py**
    
    
    | 단계 | 설명 |
    | --- | --- |
    | Deepfake Detector | 🤗 `prithivMLmods/Deep‑Fake‑Detector-Model` 이미지 분류 파이프라인 |
    | Face ID | `face_recognition` ‑ 128d 임베딩 ❯ 최근접 매칭 |
    | RAG | `facebook/rag-sequence-nq` + 커스텀 passages + FAISS 검색 |
    | 출력 | `{person, deepfake(bool), score(float), context(str)}` |

---# Deepfake_plus_RAG

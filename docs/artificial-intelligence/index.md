# 인공지능

인공지능 과목 학습 내용을 정리합니다. 교재 *Artificial Intelligence: A Modern Approach* (Russell & Norvig) 기반 **이론** 과 YOLO를 이용한 **실무 프로젝트(실습)** 로 나뉩니다.

---

## 🎯 다가오는 시험 안내 — 중간고사 (이론 전체)

| 구분 | 일정 | 범위 | 출제 유형 (교수님 공지) | 대비 자료 |
|---|---|---|---|---|
| **중간고사 (이론)** | **2026-11-17 (화)** | **이론 전 범위 (7개 단원)**<br>(마지막 장 지식 표현은 `p.21` 시맨틱 네트워크까지) | **단답형 + 중요한 용어·개념을 설명하는 문제** | **[🔥 중간고사 완벽 대비 (필수 용어·비교표·예상 35제)](./midterm-review.md)** |
| **기말고사 (실습)** | 12월 예정 | **실습에 대한 것만 출제** (실무 프로젝트 1·2 등) | 실습 기반 | 아래 실무 프로젝트 노트 참고 |

---

## 이론 (중간고사 시험 범위 전체)

| 장 | 주제 | 원본 |
|---|---|---|
| [Chapter 1. 인공지능 개요](./01-introduction.md) | AI의 네 가지 접근, Turing Test(6대 능력), Rational Agent, 역사 | `AI-ch01.pdf` |
| [Chapter 2. 지능형 에이전트](./02-intelligent-agents.md) | 에이전트 함수 vs 프로그램, 합리성 4요소, PEAS, 환경 6유형, 에이전트 4구조·학습 에이전트 | `AI-ch02.pdf` |
| [Chapter 3. 탐색](./03-search.md) | 문제 정의 4요소, 평가 4기준, 무정보 탐색(BFS·UCS·DFS·DLS·IDS), 휴리스틱 탐색(Greedy·A\*) | `AI-ch03.pdf` |
| [Chapter 7. 논리적 에이전트](./05-logical-agents.md) | 지식 기반 에이전트(`Tell`/`Ask`), 웜푸스 세계, 명제 논리, 함의($\models$)·도출($\vdash$), 건전성·완전성 | `AI-ch07.pdf` |
| [Chapter 8. 일차 논리 (First-Order Logic)](./07-first-order-logic.md) | 객체·관계·함수, 존재론적·인식론적 개입, 모델과 해석, 한정사($\forall, \exists$), DB 의미론(UNA·CWA·DC), 상황 미적분·프레임 문제 | `AI-ch08.pdf` |
| [제4장. 전문가 시스템 (Expert Systems)](./08-expert-systems.md) | 생성 규칙(`IF-THEN`), 장기 기억(규칙)·단기 기억(사실), 순방향·역방향 추론, 충돌 해법 3가지 | `제4장 전문가 시스템.pptx` |
| [Chapter 10 (제5장). 지식 표현 (Knowledge Representation)](./09-knowledge-representation.md) | 온톨로지(어휘·이론), 범주와 실체화(Reification), `Disjoint`·`Partition`, `PartOf`·`Bunch`, 사건 미적분(6대 술어), 시간 구간·유동체, 시맨틱 네트워크(`p.21`까지) | `제05장 지식표현(강의)-변경.key` |
| **[📋 중간고사 대비 총정리](./midterm-review.md)** | **전 범위 단답형 필수 용어 사전 · 10대 핵심 비교표 · 단답/개념 설명 실전 예상 35제** | **시험 대비 요약본** |

---

## 실무 프로젝트 (실습 · 기말고사 범위)

| 회차 | 주제 | 날짜 |
|---|---|---|
| [실무 프로젝트 1. Computer Vision과 Object Detection](./04-YOLO.md) | CNN·풀링, YOLO 구조, IoU·mAP, 사전 학습 모델로 이미지 탐지 | 2026-09-21 |
| [실무 프로젝트 2. YOLO 학습(Fine-tuning)과 응용](./06-YOLO-finetuning.md) | 데이터셋 구조, COCO8 학습, 이미지·영상·웹캠 탐지 | 2026-10-13 |

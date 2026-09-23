# Chapter 2. 지능형 에이전트 (Intelligent Agents)

> 인공지능 2번째 강의 정리 노트
> 원본: `AI-ch02.pdf` (Russell & Norvig, *Artificial Intelligence: A Modern Approach* 2장 기반)

---

## 📌 목차

1. [에이전트와 환경 (Agents and Environments)](#1-에이전트와-환경-agents-and-environments)
2. [합리성 (Rationality)](#2-합리성-rationality)
3. [PEAS: 작업 환경 명세](#3-peas-작업-환경-명세)
4. [환경의 유형 (Environment Types)](#4-환경의-유형-environment-types)
5. [에이전트의 구조 (The Structure of Agents)](#5-에이전트의-구조-the-structure-of-agents)
6. [요약](#6-요약-summary)
7. [셀프 체크 퀴즈](#7-셀프-체크-퀴즈)

### 이 장의 핵심 질문

- **에이전트**란 무엇이고, 환경과 어떻게 상호작용하는가?
- "**합리적**으로 행동한다"는 것은 정확히 무슨 뜻인가?
- 에이전트를 설계하려면 문제(작업 환경)를 어떻게 **명세**해야 하는가?
- 환경의 성질에 따라 에이전트 설계는 어떻게 달라지는가?
- 에이전트 프로그램은 어떤 **구조**로 만들 수 있는가?

---

## 1. 에이전트와 환경 (Agents and Environments)

### 1.1 에이전트의 정의

**에이전트(agent)** 는 **센서(sensors)** 로 환경을 **인지(percept)** 하고, **액추에이터(actuators)** 로 환경에 **행동(action)** 하는 모든 것이다.

```
          percepts (인지)
   ┌──────────────────────────┐
   │                          ▼
┌──┴──────────┐         ┌──────────┐
│ Environment │         │  Agent   │
│   (환경)     │         │  sensors │
│             │         │    ?     │  ← 여기서 무엇을 할지 "결정"
│             │         │ actuators│
└─────────────┘         └────┬─────┘
   ▲                          │
   └──────────────────────────┘
          actions (행동)
```

- 에이전트의 예: **사람, 로봇, 소프트봇(softbot, 소프트웨어 에이전트), 온도조절기(thermostat)** 등
- 가운데 **`?`** 부분이 바로 AI가 설계해야 하는 부분이다 — "지금까지 본 것을 바탕으로 무엇을 할 것인가?"

| 에이전트 | 센서 | 액추에이터 |
|---|---|---|
| 사람 | 눈, 귀, 피부 | 손, 발, 입 |
| 로봇 | 카메라, 적외선 거리 센서 | 모터, 그리퍼 |
| 소프트봇 | 키 입력, 파일 내용, 네트워크 패킷 | 화면 출력, 파일 쓰기, 패킷 전송 |
| 온도조절기 | 온도 센서 | 난방기 on/off 스위치 |

### 1.2 에이전트 함수 vs 에이전트 프로그램 ⭐

이 구분은 시험에 자주 나오는 핵심 개념이다.

**에이전트 함수 (agent function)**: 지금까지의 **인지 이력(percept history)** 을 **행동**으로 대응시키는 수학적 함수

$$
f : \mathcal{P}^* \rightarrow \mathcal{A}
$$

- $\mathcal{P}$: 가능한 인지(percept)들의 집합
- $\mathcal{P}^*$: 인지들의 **모든 가능한 시퀀스** (Kleene star, 길이 0 이상의 모든 나열)
- $\mathcal{A}$: 가능한 행동들의 집합

**에이전트 프로그램 (agent program)**: 에이전트 함수를 실제로 구현한 **코드**. 물리적 **아키텍처(architecture)** 위에서 실행되어 $f$를 만들어낸다.

| 구분 | 에이전트 함수 | 에이전트 프로그램 |
|---|---|---|
| 성격 | 추상적인 수학적 명세 | 구체적인 구현 |
| 입력 | 인지 **시퀀스 전체** | 보통 **현재 인지 하나** (필요하면 내부에 기억) |
| 비유 | "무엇을 해야 하는가" | "어떻게 계산하는가" |

$$
\text{agent} = \text{architecture} + \text{program}
$$

> 💡 **이해 포인트**: 함수는 "이 상황에서는 이렇게 행동한다"는 **표(명세)**, 프로그램은 그 표를 **작고 효율적으로 계산해내는 코드**다. 같은 함수를 여러 프로그램으로 구현할 수 있다.

### 1.3 예제: 진공청소기 세계 (Vacuum-cleaner World)

```
┌─────────┬─────────┐
│    A    │    B    │
│  🤖 💩  │   💩    │
└─────────┴─────────┘
```

- 칸은 **A, B** 두 개뿐
- **인지(Percepts)**: `[위치, 상태]` — 예) `[A, Dirty]`
- **행동(Actions)**: `Left`, `Right`, `Suck`(빨아들이기), `NoOp`(아무것도 안 함)

**에이전트 함수 (일부를 표로 표현)**

| 인지 시퀀스 (Percept sequence) | 행동 (Action) |
|---|---|
| `[A, Clean]` | `Right` |
| `[A, Dirty]` | `Suck` |
| `[B, Clean]` | `Left` |
| `[B, Dirty]` | `Suck` |
| `[A, Clean], [A, Clean]` | `Right` |
| `[A, Clean], [A, Dirty]` | `Suck` |
| ... | ... |

→ 표는 인지 시퀀스가 길어질수록 **무한히** 커진다.

**이 함수를 구현한 작은 에이전트 프로그램**

```
function REFLEX-VACUUM-AGENT([location, status]) returns an action
    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

- 무한한 표 대신 **3줄짜리 규칙**으로 같은 행동을 만들어낸다.

> ❓ 강의 속 질문
> - **어떤 함수가 "올바른(right)" 함수인가?** → 이것을 판단하는 기준이 다음 절의 **합리성(성능 척도)** 이다.
> - **작은 에이전트 프로그램으로 구현할 수 있는가?** → 이것이 5절 **에이전트 구조**의 주제다.

---

## 2. 합리성 (Rationality)

### 2.1 성능 척도 (Performance Measure)

에이전트가 "잘 했는지"를 판단하려면 **고정된 성능 척도**가 필요하다. 성능 척도는 **환경 상태의 시퀀스**를 평가한다 (에이전트의 속마음이 아니라 **결과로 나타난 세상**을 평가).

진공청소기에서 가능한 성능 척도 후보들:

| 성능 척도 후보 | 문제점 / 고려사항 |
|---|---|
| 시간 $T$ 동안 치운 먼지의 양 | 먼지를 치우고 → 다시 쏟고 → 또 치우는 "꼼수" 에이전트가 고득점 |
| 매 시간 단계마다 치운 칸 하나당 1점 | 위와 비슷한 문제 |
| 매 시간 단계마다 **깨끗한 칸** 하나당 1점, 이동 1회당 −1점 | 불필요한 움직임까지 억제 → 더 현실적 |
| $k$개 초과의 더러운 칸, 전기 사용, 소음에 벌점 | 실제 요구사항을 더 반영 |
| 깨끗한 바닥 상태 유지 | 궁극적으로 원하는 것 |

> ⭐ **설계 원칙**
> 성능 척도는 **에이전트가 어떻게 행동해야 한다고 생각하는지**가 아니라, **환경에서 실제로 원하는 것**에 따라 설계해야 한다.
> (예: "먼지를 많이 빨아라" ❌ → "바닥이 깨끗하게 유지되어야 한다" ✅)

### 2.2 합리적 에이전트의 정의 ⭐

> **합리적 에이전트(rational agent)** 는 **지금까지의 인지 시퀀스**가 주어졌을 때, **성능 척도의 기댓값(expected value)** 을 **최대화**하는 행동을 선택한다.

키워드 세 개를 꼭 기억하자: **기댓값 / 최대화 / 지금까지의 인지 시퀀스**

### 2.3 합리성을 결정하는 4가지 요소

어떤 시점에서 무엇이 합리적인지는 다음 네 가지에 달려 있다.

1. 성공 기준을 정의하는 **성능 척도**
2. 환경에 대한 에이전트의 **사전 지식(prior knowledge)**
3. 에이전트가 수행할 수 있는 **행동**
4. 지금까지의 **인지 시퀀스**

**예: 진공청소기 에이전트는 합리적인가?** 다음 가정 하에서는 **합리적이다**.

- 성능 척도: 1000 시간 단계 동안, 매 단계마다 깨끗한 칸 하나당 1점
- 환경의 **지리(칸 배치)는 미리 알려져 있음**. 하지만 먼지 분포와 에이전트 초기 위치는 모름
- 깨끗한 칸은 계속 깨끗함, `Suck`은 현재 칸을 청소함
- `Left`/`Right`는 이동하되, 환경 밖으로 나가려 하면 제자리
- 가능한 행동은 `Left`, `Right`, `Suck` 뿐
- 에이전트는 자신의 위치와 먼지 유무를 **정확히 인지**함

> 💡 만약 조건이 바뀌면(예: 이동마다 −1점 벌점) 두 칸이 모두 깨끗한 뒤에도 계속 왔다갔다하는 이 에이전트는 **더 이상 합리적이지 않다**. → 합리성은 **조건에 상대적**이다.

### 2.4 전지함, 학습, 자율성 (Omniscience, Learning, Autonomy)

#### 합리적 ≠ 전지적 (Rational ≠ Omniscient)

- 인지가 **모든 관련 정보를 제공하지 않을 수 있다**
- 행동의 결과가 **예상과 다를 수 있다**
- 예: 길을 건너기 전 **양쪽을 살피지 않는** 에이전트 — 이것이 합리적인가? → ❌ 정보를 얻을 수 있는데 얻지 않았으므로 비합리적
- **정보 수집(information gathering, exploration)**: 미래의 인지를 바꾸기 위해 행동하는 것 (예: 길 건너기 전 좌우 살피기) 도 합리적 행동의 일부

#### 합리적 ≠ 성공적 (Rational ≠ Successful)

- 합리성은 **실제 결과**가 아니라 **기대 성능**을 최대화하는 것
- 좌우를 잘 살피고 건넜는데도 하늘에서 떨어진 물건에 맞았다면 → 결과는 실패지만 행동은 **합리적**이었다

#### 자율성 (Autonomy)

- 합리적 에이전트는 **불완전하거나 틀린 사전 지식을 보완**하기 위해 배울 수 있는 것은 배워야 한다
- **초기 지식 + 학습 능력**
- 설계자의 사전 지식에만 의존하는 에이전트는 자율성이 부족하다

$$
\text{Rational} \Rightarrow \text{exploration, learning, autonomy}
$$

| 개념 | 의미 |
|---|---|
| 전지(Omniscience) | 행동의 **실제 결과**를 미리 앎 → 현실적으로 불가능 |
| 합리성(Rationality) | **기대** 성능을 최대화 |
| 성공(Success) | 실제 결과가 좋음 (운도 작용) |
| 자율성(Autonomy) | 경험으로부터 학습하여 사전 지식의 한계를 보완 |

---

## 3. PEAS: 작업 환경 명세

합리적 에이전트를 설계하려면 먼저 **작업 환경(task environment)** 을 명세해야 한다. 이를 **PEAS** 로 기술한다.

| 약자 | 영문 | 의미 |
|---|---|---|
| **P** | Performance measure | 성능 척도: 무엇이 "잘 한 것"인가 |
| **E** | Environment | 환경: 에이전트가 활동하는 세계 |
| **A** | Actuators | 액추에이터: 행동 수단 |
| **S** | Sensors | 센서: 인지 수단 |

### 3.1 자율주행 택시 (Automated Taxi)

| PEAS | 내용 |
|---|---|
| **P** | 안전, 목적지 도착, 수익, 법규 준수, 승차감, ... |
| **E** | 도로/고속도로, 교통, 보행자, 포트홀, 물웅덩이, 날씨, ... |
| **A** | 조향(steering), 가속 페달, 브레이크, 경적, 스피커/디스플레이, ... |
| **S** | 비디오 카메라, 속도계, 가속도계, 주행거리계, 엔진 센서, GPS, ... |

> 💡 성능 척도끼리 **충돌**할 수 있다 (안전 vs 빠른 도착 vs 수익). 이런 **트레이드오프**가 나중에 **효용 기반 에이전트**의 필요성으로 이어진다.

### 3.2 인터넷 쇼핑 에이전트 (Internet Shopping Agent)

| PEAS | 내용 |
|---|---|
| **P** | 가격, 품질, 적합성, 효율성 |
| **E** | 현재와 미래의 웹사이트, 판매자, 배송업체 |
| **A** | 사용자에게 표시, URL 따라가기, 폼 입력 |
| **S** | HTML 페이지 (텍스트, 그래픽, 스크립트) |

### 3.3 의료 진단 시스템 (Medical Diagnosis System)

| PEAS | 내용 |
|---|---|
| **P** | 환자의 건강, 비용 절감 |
| **E** | 환자, 병원, 의료진 |
| **A** | 질문 표시, 검사, 진단, 처방/치료 |
| **S** | 증상·소견·환자 답변의 키보드 입력 |

### 3.4 대화형 영어 튜터 (Interactive English Tutor)

| PEAS | 내용 |
|---|---|
| **P** | 학생의 시험 점수 |
| **E** | 학생 집단, 시험 기관 |
| **A** | 연습문제 표시, 제안, 교정 |
| **S** | 키보드 입력 |

> ✍️ **연습**: 로봇 청소기, 스팸 메일 필터, 체스 프로그램의 PEAS를 직접 작성해 보자.

---

## 4. 환경의 유형 (Environment Types)

환경의 성질은 에이전트 설계에 결정적인 영향을 준다. 다음 차원(dimension)으로 분류한다.

### 4.1 완전 관측 vs 부분 관측 (Fully vs Partially Observable)

- **완전 관측(Fully observable)**: 매 시점에 센서가 환경의 **완전한 상태**에 접근할 수 있음 (행동 선택에 관련된 부분 전체)
- **부분 관측(Partially observable)**: 노이즈, 부정확한 센서, 센서가 없는 부분 등으로 상태 일부를 알 수 없음
  - 예: 진공청소기가 **현재 칸**의 먼지만 감지 → 다른 칸은 모름
- 완전 관측이면 에이전트가 **내부 상태(기억)를 유지할 필요가 없다**

### 4.2 단일 에이전트 vs 다중 에이전트 (Single vs Multi-agent)

- 핵심 질문: 에이전트 A(예: 택시 운전사)가 객체 B(다른 차량)를 **에이전트로** 취급해야 하는가, 아니면 **물리 법칙을 따르는 단순 물체**로 봐도 되는가?
- 판단 기준: **B의 행동이, A의 행동에 따라 값이 달라지는 성능 척도를 최대화하는 것으로 가장 잘 설명되는가?**
  - 그렇다면 B는 에이전트다.
- 다중 에이전트 환경의 종류
  - **경쟁적(competitive)**: 체스 — 상대의 성능 최대화 = 나의 성능 최소화
  - **협력적(cooperative)**: 택시 — 충돌 회피는 모두에게 이득 (부분적으로는 경쟁적: 주차 공간 경쟁)
  - 테니스(복식): 팀 내부는 협력, 팀 간은 경쟁

### 4.3 결정적 vs 확률적 (Deterministic vs Stochastic)

- **결정적(Deterministic)**: 환경의 다음 상태가 **현재 상태 + 에이전트의 행동**으로 **완전히 결정**됨
- **확률적(Stochastic)**: 결과에 **불확실성**이 있고, 그 불확실성을 **확률**로 표현
- **불확실(Uncertain)**: 완전 관측이 아니거나 결정적이지 않은 경우
- **비결정적(Nondeterministic)**: 행동이 **가능한 결과들의 집합**으로 표현됨 (확률은 **붙어 있지 않음** — 확률적 환경과의 차이!)

| 구분 | 다음 상태 표현 | 예 |
|---|---|---|
| 결정적 | 딱 하나 | 크로스워드 퍼즐 |
| 확률적 | 결과 + **확률** | "70% 확률로 성공, 30% 확률로 미끄러짐" |
| 비결정적 | 결과들의 **집합** (확률 없음) | "성공하거나 미끄러지거나" |

### 4.4 에피소드형 vs 순차형 (Episodic vs Sequential)

- **에피소드형(Episodic)**: 경험이 독립적인 에피소드로 나뉘며, **다음 에피소드는 이전 에피소드의 행동에 의존하지 않음**
  - 예: 조립 라인에서 불량품 검출 — 이번 부품 판정이 다음 부품에 영향 없음
- **순차형(Sequential)**: 현재 결정이 **미래의 모든 결정에 영향**
  - 예: 체스, 택시 운전 → 미리 생각(계획)해야 함

### 4.5 정적 vs 동적 (Static vs Dynamic)

- **정적(Static)**: 에이전트가 **숙고하는 동안** 환경이 변하지 않음
- **동적(Dynamic)**: 에이전트가 생각하는 동안에도 환경이 변함 → 아무것도 안 하면 "아무것도 안 하기로 결정한 것"과 같음
- **준동적(Semi-dynamic)**: 환경 자체는 변하지 않지만 **에이전트의 성능 점수가 시간에 따라 변함**
  - 예: **시간 제한이 있는 체스(chess with clock)**

### 4.6 이산 vs 연속 (Discrete vs Continuous)

- **환경의 상태**, **시간을 다루는 방식**, 에이전트의 **인지와 행동**에 적용
- 체스: 상태·행동 수가 유한 → **이산**
- 택시 운전: 속도·위치·조향각이 연속적으로 변함 → **연속**

### 4.7 알려진 vs 알려지지 않은 (Known vs Unknown)

- 이것은 **환경 자체의 성질이 아니라**, 환경의 **"물리 법칙"(행동의 결과)** 에 대한 **에이전트(설계자)의 지식 상태**를 말한다
- **Known ≠ Observable** ⚠️
  - **솔리테어**(카드 게임): 규칙은 **알려져 있지만(known)**, 뒤집힌 카드는 **보이지 않음(partially observable)**
  - 처음 해보는 **비디오 게임**: 화면은 **다 보이지만(fully observable)**, 버튼이 무엇을 하는지 **모름(unknown)**

### 4.8 환경 유형 분류표 ⭐

| 작업 환경 | 관측 | 에이전트 | 결정성 | 에피소드 | 정적 | 이산 |
|---|---|---|---|---|---|---|
| 크로스워드 퍼즐 | Fully | Single | Deterministic | Sequential | Static | Discrete |
| 시간제한 체스 | Fully | Multi | Deterministic | Sequential | **Semi** | Discrete |
| 포커 | **Partially** | Multi | Stochastic | Sequential | Static | Discrete |
| 백개먼 | Fully | Multi | **Stochastic** | Sequential | Static | Discrete |
| 택시 운전 | Partially | Multi | Stochastic | Sequential | Dynamic | Continuous |
| 의료 진단 | Partially | Multi | Stochastic | Sequential | Dynamic | Continuous |
| 이미지 분석 | Fully | Single | Deterministic | **Episodic** | Semi | Continuous |
| 부품 집기 로봇 | Partially | Single | Stochastic | **Episodic** | Dynamic | Continuous |
| 정유 공장 제어기 | Partially | Single | Stochastic | Sequential | Dynamic | Continuous |
| 대화형 영어 튜터 | Partially | Multi | Stochastic | Sequential | Dynamic | Discrete |

**표를 읽는 요령**
- 포커 → 상대 카드가 안 보이므로 **Partially**, 카드 섞기 때문에 **Stochastic**
- 백개먼 → 판은 다 보이지만 **주사위** 때문에 **Stochastic**
- 이미지 분석 / 부품 집기 → 한 장(한 개)씩 독립 처리 → **Episodic**
- 시간제한 체스 → 판은 안 변하지만 시간이 흐르며 점수에 영향 → **Semi**

> ⭐ **가장 어려운 환경**: **부분 관측, 다중 에이전트, 확률적, 순차적, 동적, 연속, 알려지지 않은** 환경 → 현실 세계 (예: 택시 운전)

---

## 5. 에이전트의 구조 (The Structure of Agents)

$$
\text{agent} = \text{architecture} + \text{program}
$$

**일반성이 증가하는 순서**로 네 가지 기본 유형이 있다.

1. 단순 반사 에이전트 (Simple reflex agents)
2. 상태를 가진 반사 에이전트 / 모델 기반 반사 에이전트 (Reflex agents with state)
3. 목표 기반 에이전트 (Goal-based agents)
4. 효용 기반 에이전트 (Utility-based agents)

→ 이 모든 유형은 **학습 에이전트(learning agents)** 로 바꿀 수 있다.

### 5.0 테이블 기반 에이전트 (Table-Driven Agent) — 왜 안 되는가?

```
function TABLE-DRIVEN-AGENT(percept) returns an action
    persistent: percepts, a sequence, initially empty
                table, a table of actions, indexed by percept sequences,
                       initially fully specified

    append percept to the end of percepts
    action ← LOOKUP(percepts, table)
    return action
```

- 에이전트 함수를 **그대로 표로** 만들어 조회하는 방식
- $P$ = 가능한 인지의 집합, $T$ = 에이전트의 수명(총 인지 횟수)이라 할 때, 룩업 테이블의 항목 수는

$$
\sum_{t=1}^{T} |P|^t
$$

- 예) 카메라 한 프레임만 해도 가능한 인지 수가 천문학적 → 1시간 운전하면 표 크기가 우주의 원자 수를 훨씬 넘음

**문제점**
- 물리적으로 저장 불가능
- 설계자가 표를 만들 시간이 없음
- 에이전트가 경험으로 표를 학습하는 것도 불가능
- 어떻게 채워야 할지 지침조차 없음

> 💡 AI의 핵심 과제: 거대한 표 대신 **작은 프로그램**으로 합리적 행동을 만들어내는 것

### 5.1 단순 반사 에이전트 (Simple Reflex Agents)

```
┌─────────────────────── Agent ───────────────────────┐
│                                                     │
│  Sensors ──▶ [ 지금 세상은 어떤가? ]                  │
│                       │                             │
│   [조건-행동 규칙] ──▶ [ 지금 무엇을 해야 하나? ]       │
│                       │                             │
│                       ▼                             │
│                   Actuators                         │
└─────────────────────────────────────────────────────┘
```

- **현재 인지만** 보고 **조건–행동 규칙(condition–action rules, if-then)** 으로 행동을 선택
- 인지 이력(과거)은 무시
- 예: "앞차가 브레이크를 밟으면 → 나도 브레이크를 밟는다"
  - 단, 이 규칙은 **현재 프레임 하나만으로 판단 가능**(완전 관측)할 때만 잘 작동

**진공청소기 예제 (의사코드)**

```
function REFLEX-VACUUM-AGENT([location, status]) returns an action
    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

**Lisp 구현 (강의 자료)**

```lisp
(defun make-reflex-vacuum-agent-program ()
  #'(lambda (percept)
      (let ((location (first percept)) (status (second percept)))
        (cond ((eq status 'dirty) 'Suck)
              ((eq location 'A) 'Right)
              ((eq location 'B) 'Left)))))
```

**참고: Python으로 옮기면**

```python
def reflex_vacuum_agent(percept):
    location, status = percept
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"
```

**한계**
- **완전 관측** 환경에서만 제대로 동작
- 부분 관측 환경에서는 **무한 루프**에 빠지기 쉬움 (예: 위치 센서가 없는 청소기는 영원히 Left만 할 수도 있음)

### 5.2 상태를 가진 반사 에이전트 (Reflex Agents with State = 모델 기반 반사 에이전트)

```
┌────────────────────────── Agent ──────────────────────────┐
│                                                           │
│  [State] ──────────┐                                      │
│  [세상은 어떻게 변하나] ─┤                                  │
│  [내 행동이 무엇을 하나] ┼──▶ [ 지금 세상은 어떤가? ] ◀── Sensors
│                      │              │                     │
│   [조건-행동 규칙] ──────────▶ [ 지금 무엇을 해야 하나? ]    │
│                                     ▼                     │
│                                 Actuators                 │
└───────────────────────────────────────────────────────────┘
```

- **부분 관측** 문제를 해결하기 위해 **내부 상태(state)** 를 유지
- 상태를 갱신하려면 두 가지 지식(= **세계 모델, world model**)이 필요
  1. **세상이 어떻게 변하는가** (How the world evolves) — 에이전트와 무관하게
  2. **내 행동이 세상에 어떤 영향을 주는가** (What my actions do)
- 결과적으로 "지금 세상이 어떤지"에 대한 **최선의 추정(best guess)** 을 한다

**진공청소기 예제 (Lisp, 강의 자료)**

```lisp
(defun make-reflex-vacuum-agent-with-state-program ()
  (let ((last-A infinity) (last-B infinity))
    #'(lambda (percept)
        (let ((location (first percept)) (status (second percept)))
          (incf last-A) (incf last-B)
          (cond
            ((eq status 'dirty)
             (if (eq location 'A) (setq last-A 0) (setq last-B 0))
             'Suck)
            ((eq location 'A) (if (> last-B 3) 'Right 'NoOp))
            ((eq location 'B) (if (> last-A 3) 'Left 'NoOp)))))))
```

**Python 버전과 해설**

```python
import math

def make_reflex_vacuum_agent_with_state():
    last_A = math.inf   # A를 마지막으로 청소한 뒤 지난 시간
    last_B = math.inf   # B를 마지막으로 청소한 뒤 지난 시간

    def program(percept):
        nonlocal last_A, last_B
        location, status = percept
        last_A += 1
        last_B += 1
        if status == "Dirty":
            if location == "A": last_A = 0
            else:               last_B = 0
            return "Suck"
        elif location == "A":
            return "Right" if last_B > 3 else "NoOp"
        elif location == "B":
            return "Left" if last_A > 3 else "NoOp"

    return program
```

- `last_A`, `last_B`: 각 칸을 **마지막으로 청소한 이후 경과 시간** (내부 상태)
- 반대편 칸을 청소한 지 **3 단계 이하**면 굳이 이동하지 않고 `NoOp` → 불필요한 이동 감소
- → 이동에 벌점이 있는 성능 척도에서 단순 반사 에이전트보다 **더 합리적**

### 5.3 목표 기반 에이전트 (Goal-based Agents)

```
State + 세계 모델 ──▶ [지금 세상은 어떤가?]
                         │
                         ▼
               [행동 A를 하면 세상이 어떻게 될까?]   ← 미래 예측
                         │
          [Goals] ──────▶│
                         ▼
               [지금 무엇을 해야 하나?] ──▶ Actuators
```

- 현재 상태만으로는 부족할 때가 있다 — 예: 교차로에서 좌/우/직진 중 무엇을 할지는 **목적지(목표)** 에 달림
- **"행동 A를 하면 어떻게 될까?"** 를 예측하고, 그 결과가 **목표(goal)** 를 달성하는지 판단
- **탐색(search)** 과 **계획(planning)** 이 이 유형의 핵심 도구 (이후 장에서 학습)
- 장점: **유연성** — 목표만 바꾸면 행동이 바뀜 (반사 에이전트는 규칙을 모두 다시 써야 함)

### 5.4 효용 기반 에이전트 (Utility-based Agents)

```
State + 세계 모델 ──▶ [지금 세상은 어떤가?]
                         │
                         ▼
               [행동 A를 하면 세상이 어떻게 될까?]
                         │
          [Utility] ────▶ [그 상태에서 나는 얼마나 행복할까?]
                         │
                         ▼
               [지금 무엇을 해야 하나?] ──▶ Actuators
```

- 목표는 **행복/불행의 이분법**(달성했나? 못 했나?)만 제공
- **효용 함수(utility function)** 는 상태를 **실수값**(얼마나 좋은가)으로 평가
- 효용이 필요한 경우
  - **상충하는 목표(conflicting goals)** 사이의 트레이드오프: 예) 속도 vs 안전
  - **불확실한 목표(uncertain goals)**: 어떤 목표도 확실히 달성할 수 없을 때, 성공 가능성과 목표의 중요도를 저울질
- 합리적 에이전트는 **기대 효용(expected utility)** 을 최대화하는 행동을 선택 → 2.2의 합리성 정의와 직결

### 5.5 학습 에이전트 (Learning Agents)

```
          Performance standard (성능 기준)
                   │
                   ▼
   Sensors ──▶  [Critic 비평가] ── feedback ──▶ [Learning element 학습 요소]
      │                                           │         ▲        │
      │                                   changes │ knowledge│  learning goals
      │                                           ▼         │        ▼
      └─────────────────────────────▶ [Performance element] │  [Problem generator]
                                          수행 요소  ────────┘     문제 생성기
                                              │                      │
                                              ▼                      │
                                          Actuators ◀────────────────┘
```

| 구성 요소 | 역할 | 비유 (택시) |
|---|---|---|
| **수행 요소 (Performance element)** | 인지를 받아 행동을 선택 — 지금까지 배운 **에이전트 그 자체** (5.1~5.4 중 하나) | 운전하는 부분 |
| **비평가 (Critic)** | 고정된 **성능 기준**에 비춰 에이전트가 얼마나 잘하는지 **피드백** | 급정거 후 다른 운전자들의 경적·욕설 |
| **학습 요소 (Learning element)** | 피드백을 바탕으로 수행 요소를 **개선** | "급정거는 나쁘다"는 규칙 학습 |
| **문제 생성기 (Problem generator)** | 새롭고 유익한 경험을 할 수 있는 **탐색적 행동** 제안 | "다른 노면에서 브레이크를 시험해보자" |

- 성능 기준은 **에이전트 외부에 고정**되어야 한다 (에이전트가 스스로 기준을 바꿔버리면 안 됨)
- 문제 생성기 = 2.4절의 **탐색(exploration)** 과 연결 → 단기적으로는 손해여도 장기적으로 더 나은 행동 발견

### 5.6 에이전트 유형 비교 정리 ⭐

| 유형 | 결정 근거 | 내부 상태 | 미래 예측 | 장점 | 한계 |
|---|---|---|---|---|---|
| 테이블 기반 | 인지 시퀀스 전체 조회 | 인지 이력 전부 | ✗ | 개념상 단순 | 표가 천문학적 크기 |
| 단순 반사 | 현재 인지 + 규칙 | ✗ | ✗ | 빠르고 단순 | 완전 관측에서만 동작 |
| 상태 있는 반사 | 내부 상태 + 규칙 | ✓ | ✗ | 부분 관측 대응 | 목표 변화에 비유연 |
| 목표 기반 | 목표 달성 여부 | ✓ | ✓ | 유연함 (목표만 교체) | 좋음의 "정도" 표현 불가 |
| 효용 기반 | 기대 효용 최대화 | ✓ | ✓ | 트레이드오프·불확실성 처리 | 효용 함수 설계 어려움 |
| 학습 | 위 요소 + 피드백 | ✓ | ✓ | 미지의 환경 적응, 자율성 | 학습 비용·시간 |

---

## 6. 요약 (Summary)

- **에이전트**는 **센서**와 **액추에이터**를 통해 **환경**과 상호작용한다.
- **에이전트 함수**는 모든 상황에서 에이전트가 무엇을 하는지 기술한다. ($f:\mathcal{P}^*\to\mathcal{A}$)
- **성능 척도**는 **환경 상태의 시퀀스**를 평가한다.
- **완벽하게 합리적인** 에이전트는 **기대 성능**을 최대화한다.
- **에이전트 프로그램**은 (일부) 에이전트 함수를 구현한다.
- **PEAS** 기술로 작업 환경을 정의한다.
- 환경은 여러 차원으로 분류된다: **관측 가능? 결정적? 에피소드형? 정적? 이산? 단일 에이전트?**
- 기본 에이전트 아키텍처: **반사, 상태 있는 반사, 목표 기반, 효용 기반, 학습**

### 🧠 한 장 요약 마인드맵

```
Intelligent Agents
├── 에이전트와 환경
│   ├── 센서 → 인지(percept) / 액추에이터 → 행동(action)
│   ├── 에이전트 함수 f: P* → A  (명세)
│   └── 에이전트 프로그램 (구현), agent = architecture + program
├── 합리성
│   ├── 성능 척도: "원하는 환경 상태" 기준으로 설계
│   ├── 기대 성능 최대화 (지금까지의 인지 기준)
│   ├── 4요소: 성능척도 / 사전지식 / 가능한 행동 / 인지 시퀀스
│   └── 합리 ≠ 전지, 합리 ≠ 성공 → 탐색·학습·자율성
├── PEAS: Performance, Environment, Actuators, Sensors
├── 환경 유형
│   ├── Fully / Partially observable
│   ├── Single / Multi agent (경쟁/협력)
│   ├── Deterministic / Stochastic / Nondeterministic
│   ├── Episodic / Sequential
│   ├── Static / Semi / Dynamic
│   ├── Discrete / Continuous
│   └── Known / Unknown (≠ observable)
└── 에이전트 구조
    ├── (Table-driven: 비현실적)
    ├── Simple reflex
    ├── Reflex with state (model-based)
    ├── Goal-based
    ├── Utility-based
    └── Learning (Critic, Learning element, Performance element, Problem generator)
```

---

## 7. 셀프 체크 퀴즈

> 답을 먼저 생각해본 뒤 `▶ 정답 보기`를 눌러 확인하자.

**Q1.** 에이전트 함수와 에이전트 프로그램의 차이를 설명하라.

<details><summary>▶ 정답 보기</summary>

에이전트 함수는 인지 시퀀스 전체를 행동으로 대응시키는 **추상적 수학 명세**($f:\mathcal{P}^*\to\mathcal{A}$)이고, 에이전트 프로그램은 그 함수를 물리적 아키텍처 위에서 **구현한 코드**다. 프로그램은 보통 현재 인지 하나만 입력으로 받는다.
</details>

**Q2.** 합리적 에이전트의 정의를 쓰라.

<details><summary>▶ 정답 보기</summary>

지금까지의 인지 시퀀스와 내장된 사전 지식이 주어졌을 때, 성능 척도의 **기댓값**을 최대화할 것으로 예상되는 행동을 선택하는 에이전트.
</details>

**Q3.** "합리적 ≠ 성공적"인 이유는?

<details><summary>▶ 정답 보기</summary>

합리성은 **기대** 성능을 최대화하는 것이지 **실제** 결과를 보장하는 것이 아니다. 에이전트는 전지적이지 않으므로, 합리적인 선택을 해도 예측 못한 사건으로 실패할 수 있다.
</details>

**Q4.** 성능 척도 "시간 T 동안 치운 먼지의 양"의 문제점은?

<details><summary>▶ 정답 보기</summary>

먼지를 치웠다가 다시 쏟고 또 치우는 식으로 점수를 부풀릴 수 있다. 성능 척도는 에이전트의 행동 방식이 아니라 **원하는 환경 상태**(깨끗한 바닥)를 기준으로 설계해야 한다.
</details>

**Q5.** 로봇 청소기의 PEAS를 작성하라.

<details><summary>▶ 예시 답안</summary>

- P: 청소 면적/청결도, 소요 시간, 배터리 소모, 충돌 횟수 최소화
- E: 방, 바닥 재질, 가구, 먼지, 사람·반려동물
- A: 바퀴(구동 모터), 흡입 모터, 브러시, 알림음
- S: 먼지 센서, 범퍼(충돌) 센서, 낙하 방지 센서, 카메라/LiDAR, 휠 엔코더
</details>

**Q6.** 백개먼은 판 전체가 보이는데 왜 Stochastic인가?

<details><summary>▶ 정답 보기</summary>

**주사위**를 굴려 다음 상태가 결정되므로, 현재 상태와 행동만으로 다음 상태가 완전히 결정되지 않는다. (관측 가능성과 결정성은 별개의 차원)
</details>

**Q7.** Stochastic과 Nondeterministic의 차이는?

<details><summary>▶ 정답 보기</summary>

둘 다 결과가 여러 개일 수 있지만, Stochastic은 각 결과에 **확률**이 붙어 있고, Nondeterministic은 가능한 결과들의 **집합만** 주어지고 확률은 없다.
</details>

**Q8.** 시간 제한 체스가 "Semi-dynamic"인 이유는?

<details><summary>▶ 정답 보기</summary>

에이전트가 생각하는 동안 판(환경 상태)은 변하지 않지만, 시계가 흐르므로 **성능 점수**가 시간에 따라 변하기 때문이다.
</details>

**Q9.** Known vs Unknown과 Fully vs Partially observable을 예를 들어 구분하라.

<details><summary>▶ 정답 보기</summary>

- 솔리테어: 규칙을 앎(**known**) + 뒤집힌 카드가 안 보임(**partially observable**)
- 처음 하는 비디오 게임: 화면은 다 보임(**fully observable**) + 조작 결과를 모름(**unknown**)

Known/Unknown은 환경이 아니라 **에이전트의 지식 상태**에 대한 구분이다.
</details>

**Q10.** 테이블 기반 에이전트의 표 크기와 문제점은?

<details><summary>▶ 정답 보기</summary>

크기 $\sum_{t=1}^{T}|P|^t$ — 인지 종류 수와 수명에 대해 **지수적**으로 증가. 저장 불가, 설계 불가, 학습 불가.
</details>

**Q11.** 단순 반사 에이전트가 실패하는 전형적 상황은?

<details><summary>▶ 정답 보기</summary>

**부분 관측** 환경. 현재 인지만으로 올바른 행동을 결정할 수 없어 잘못된 행동이나 무한 루프에 빠질 수 있다. → 내부 상태를 가진(모델 기반) 반사 에이전트로 해결.
</details>

**Q12.** 목표 기반 에이전트 대신 효용 기반 에이전트가 필요한 두 가지 경우는?

<details><summary>▶ 정답 보기</summary>

1. **상충하는 목표**가 있어 트레이드오프가 필요할 때 (속도 vs 안전)
2. 목표 달성이 **불확실**하여 성공 확률과 목표의 중요도를 저울질해야 할 때
</details>

**Q13.** 학습 에이전트의 4가지 구성 요소와 역할은?

<details><summary>▶ 정답 보기</summary>

- **Performance element**: 행동 선택
- **Critic**: 성능 기준에 따라 피드백 제공
- **Learning element**: 피드백으로 수행 요소 개선
- **Problem generator**: 새로운 경험을 위한 탐색적 행동 제안
</details>

**Q14.** 상태 있는 진공청소기 예제에서 `last-B > 3` 조건의 의미는?

<details><summary>▶ 정답 보기</summary>

B를 마지막으로 청소한 지 3 단계가 넘었을 때만 B로 이동하고, 그렇지 않으면 `NoOp`으로 제자리에 있는다. B가 아직 깨끗할 가능성이 높으므로 **불필요한 이동을 줄이는** 전략이다.
</details>

---

### 📚 핵심 용어 사전

| 영어 | 한국어 | 한 줄 정의 |
|---|---|---|
| Agent | 에이전트 | 센서로 인지하고 액추에이터로 행동하는 존재 |
| Percept | 인지 | 특정 시점에 센서로 받아들인 입력 |
| Percept sequence | 인지 시퀀스 | 지금까지 받은 인지의 전체 이력 |
| Agent function | 에이전트 함수 | $\mathcal{P}^* \to \mathcal{A}$ 매핑 |
| Agent program | 에이전트 프로그램 | 에이전트 함수의 구현 |
| Architecture | 아키텍처 | 프로그램이 실행되는 물리적 장치 |
| Performance measure | 성능 척도 | 환경 상태 시퀀스의 바람직함을 평가 |
| Rational agent | 합리적 에이전트 | 기대 성능을 최대화하는 에이전트 |
| Omniscience | 전지 | 행동의 실제 결과를 미리 아는 것 |
| Autonomy | 자율성 | 경험으로 사전 지식의 한계를 보완하는 능력 |
| Task environment | 작업 환경 | PEAS로 기술되는 문제 |
| Condition–action rule | 조건–행동 규칙 | if 조건 then 행동 |
| Utility | 효용 | 상태의 바람직함을 나타내는 실수값 |
| Critic | 비평가 | 학습 에이전트에서 피드백을 주는 요소 |
| Problem generator | 문제 생성기 | 탐색적 행동을 제안하는 요소 |

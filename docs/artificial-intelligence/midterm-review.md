# 인공지능 중간고사 대비 — 이론 전 범위 핵심 용어·개념 총정리

> **시험일**: **2026년 11월 17일(화)**
> **시험 범위**: 이번 학기 **이론 수업 전체 (7개 단원)** — 마지막 장([Chapter 10. 지식 표현](./09-knowledge-representation.md))은 **슬라이드 `p.21` 시맨틱 네트워크(`Fly_17` 인스턴스)까지**
> **출제 유형 (교수님 공지)**: **"단답형 + 중요한 용어와 개념을 설명하는 문제"** (기말고사는 실습만 출제)

---

## 📌 목차

1. [시험 범위 7개 단원 한눈에 보기](#_1-시험-범위-7개-단원-한눈에-보기)
2. [Part 1. 단원별 필수 용어·개념 사전 (단답형·개념 설명 직결)](#_2-part-1-단원별-필수-용어·개념-사전-단답형·개념-설명-직결)
   - [Ch.1 인공지능 개요](#_2-1-chapter-1-인공지능-개요)
   - [Ch.2 지능형 에이전트](#_2-2-chapter-2-지능형-에이전트)
   - [Ch.3 탐색 (Search)](#_2-3-chapter-3-탐색)
   - [Ch.7 논리적 에이전트 (명제 논리)](#_2-4-chapter-7-논리적-에이전트)
   - [Ch.8 일차 논리 (First-Order Logic)](#_2-5-chapter-8-일차-논리)
   - [제4장 전문가 시스템 (Expert Systems)](#_2-6-제4장-전문가-시스템)
   - [Ch.10 (제5장) 지식 표현 (`p.21`까지)](#_2-7-chapter-10-제5장-지식-표현-—-p-21까지)
3. [Part 2. 시험에 바로 쓰는 10대 핵심 비교표](#_3-part-2-시험에-바로-쓰는-10대-핵심-비교표)
4. [Part 3. 실전 예상 문제 35선 (단답형 + 개념 설명형)](#_4-part-3-실전-예상-문제-35선-단답형-개념-설명형)

---

## 1. 시험 범위 7개 단원 한눈에 보기

| 순서 | 단원 (강의 노트 링크) | 원본 자료 | 최우선 출제 키워드 |
|---|---|---|---|
| **1** | **[Chapter 1. 인공지능 개요](./01-introduction.md)** | `AI-ch01.pdf` | AI의 4가지 접근(Thinking/Acting × Humanly/Rationally), 튜링 테스트(6대 능력), 합리적 에이전트 |
| **2** | **[Chapter 2. 지능형 에이전트](./02-intelligent-agents.md)** | `AI-ch02.pdf` | 에이전트 함수 vs 에이전트 프로그램, 합리성의 4요소, **PEAS**, 환경의 6가지 유형, 에이전트의 4대 구조 + 학습 에이전트 |
| **3** | **[Chapter 3. 탐색](./03-search.md)** | `AI-ch03.pdf` | 문제 정의 4요소, 탐색 평가 4기준(완전성·최적성·시간·공간), 무정보 탐색(BFS·UCS·DFS·DLS·IDS), 휴리스틱 탐색(Greedy·**A\***, 허용성·일관성) |
| **4** | **[Chapter 7. 논리적 에이전트](./05-logical-agents.md)** | `AI-ch07.pdf` | 지식 베이스(KB) + 추론 엔진, 선언적 접근(`Tell`/`Ask`), 구문(Syntax) vs 의미(Semantics), 모델($M(\alpha)$), **함의($\models$) vs 도출($\vdash$)**, 건전성(Soundness) vs 완전성(Completeness), 타당성·충족 가능성 |
| **5** | **[Chapter 8. 일차 논리](./07-first-order-logic.md)** | `AI-ch08.pdf` | 객체·관계·함수, 존재론적·인식론적 개입, 항(Term) vs 원자 문장, **해석(Interpretation)**, 한정사($\forall + \Rightarrow$, $\exists + \land$), **DB 의미론(UNA·CWA·DC)**, 치환($\sigma$), **상황 미적분** 과 **프레임 문제·후속 상태 공리** |
| **6** | **[제4장. 전문가 시스템](./08-expert-systems.md)** | `제4장 전문가 시스템.pptx` | GPS 한계와 MYCIN, 3대 구성 요소(KB·추론 엔진·UI), 데이터·정보·지식, 생성 규칙(`IF-THEN`), **장기 기억(규칙) vs 단기 기억(사실)**, **순방향 추론 vs 역방향 추론**, **충돌 해법 3가지** |
| **7** | **[Chapter 10 (제5장). 지식 표현](./09-knowledge-representation.md)** | `제05장 지식표현.key`<br>(`p.21`까지!) | **온톨로지(어휘+이론)**, 상위 온톨로지(Things vs Stuff), 범주와 **실체화(Reification)**, `Disjoint`·`ExhaustiveDecomposition`·`Partition`, `PartOf`와 `Bunch`, **사건 미적분(6대 술어)**, 프로세스(부분 구간), 시간 구간(`Meet` 등), **유동체(Fluent)**, **시맨틱 네트워크**(상속·오버라이딩·사건 인스턴스 `Fly_17`) |

---

## 2. Part 1. 단원별 필수 용어·개념 사전 (단답형·개념 설명 직결)

> 💡 **활용 팁**: 교수님이 예고하신 **"단답형 용어 및 개념 설명"** 에 그대로 답안으로 작성할 수 있도록 **핵심 정의 1~2문장** 으로 압축했습니다.

### 2.1 [Chapter 1. 인공지능 개요](./01-introduction.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **AI의 4가지 접근법**<br>(Four Approaches to AI) | 연구 대상이 **사고(Thinking)인가 행동(Acting)인가**, 성공 기준이 **인간다움(Humanly)인가 합리성(Rationally)인가** 에 따라 ① 인간처럼 행동하기(Turing Test), ② 인간처럼 생각하기(인지과학), ③ 합리적으로 생각하기(사고의 법칙·논리), ④ **합리적으로 행동하기(합리적 에이전트 — 본 강의의 중심 관점)** 로 나뉜다. |
| **튜링 테스트 (Turing Test)**<br>/ Imitation Game | "기계가 생각할 수 있는가?"라는 추상적 질문을 **"기계가 지능적으로 행동할 수 있는가?"** 라는 관찰 가능한 행동 기준(Operational test)으로 바꾼 시험. 질문자가 텍스트 대화만으로 사람과 기계를 구별할 수 없으면 지능이 있다고 본다. |
| **튜링 테스트 통과를 위한 6대 능력** | ① **자연어 처리(NLP)** (의사소통), ② **지식 표현(Knowledge Representation)** (정보 저장), ③ **자동 추론(Automated Reasoning)** (질문 답변·새 결론 도출), ④ **기계 학습(Machine Learning)** (새 상황 적응·패턴 발견), (전체 튜링 테스트 추가) ⑤ **컴퓨터 비전**, ⑥ **로보틱스**. |
| **인지과학 (Cognitive Science)** | 인간처럼 생각하기(Thinking Humanly) 접근으로, 컴퓨터 모델과 심리학 실험을 결합해 인간 마음의 실제 작동 원리를 규명하는 학문. |
| **사고의 법칙 (Laws of Thought)** | 합리적으로 생각하기(Thinking Rationally) 접근으로, 아리스토텔레스의 삼단논법처럼 참인 전제에서 항상 참인 결론을 도출하는 형식 논리 규칙 체계. (한계: 비형식적·불확실한 지식 표현이 어렵고 계산 복잡도가 높음) |
| **합리적 에이전트 (Rational Agent)** | 합리적으로 행동하기(Acting Rationally) 접근의 핵심 주체로, 주어진 환경과 불확실성 속에서 **최선의 기대 결과(성능 척도 극대화)를 달성하도록 행동하는 주체**. |

---

### 2.2 [Chapter 2. 지능형 에이전트](./02-intelligent-agents.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **에이전트 (Agent)** | **센서(Sensors)** 를 통해 환경을 **인지(Percept)** 하고, **액추에이터(Actuators)** 를 통해 환경에 **행동(Action)** 을 가하는 모든 주체. |
| **에이전트 함수 vs 에이전트 프로그램** ⭐ | **에이전트 함수($f: \mathcal{P}^* \rightarrow \mathcal{A}$)** 는 지금까지의 **인지 이력(percept sequence) 전체** 를 행동으로 매핑하는 추상적·수학적 명세이고, **에이전트 프로그램** 은 물리적 **아키텍처(Architecture)** 위에서 돌아가며 이 함수를 실제로 구현한 구체적인 코드이다 ($\text{Agent} = \text{Architecture} + \text{Program}$). |
| **합리성 (Rationality)의 4가지 결정 요소** ⭐ | 어느 시점에 무엇이 합리적인지는 ① **성능 척도(Performance measure)**, ② 환경에 대한 **사전 지식(Prior knowledge)**, ③ 에이전트가 할 수 있는 **가능한 행동들(Actions)**, ④ 지금까지의 **인지 시퀀스(Percept sequence)** 에 의해 결정된다. |
| **전지성(Omniscience) vs 합리성(Rationality)** | **전지성** 은 행동의 실제 결과를 미리 완벽히 아는 것(불가능)이고, **합리성** 은 지금까지 인지한 정보와 지식을 바탕으로 **기대 성능을 최대화** 하는 것이다. 따라서 합리적 에이전트는 완벽한 성공을 보장하지 않으며 정보 수집(탐험)과 학습을 수행한다. |
| **자율성 (Autonomy)** | 에이전트가 설계자가 넣어준 사전 지식에만 의존하지 않고, **자신의 경험(인지와 학습)을 통해 행동을 결정하고 보완하는 능력**. |
| **PEAS** ⭐ | 에이전트가 작동할 작업 환경(Task Environment)을 정의하는 4가지 요소: **P** erformance measure(성능 척도), **E** nvironment(환경), **A** ctuators(액추에이터/구동기), **S** ensors(센서/감지기). |
| **환경의 6가지 분류 기준** ⭐ | ① **완전 관측(Fully observable) vs 부분 관측(Partially observable)**, ② **결정론적(Deterministic) vs 확률적(Stochastic)** (다른 에이전트만 불확실하면 전략적 Strategic), ③ **일화적(Episodic) vs 순차적(Sequential)**, ④ **정적(Static) vs 동적(Dynamic)** (환경은 안 변해도 시간 경과로 점수가 깎이면 준동적 Semidynamic), ⑤ **이산적(Discrete) vs 연속적(Continuous)**, ⑥ **단일 에이전트(Single) vs 다중 에이전트(Multi-agent)**. |
| **에이전트 프로그램의 4가지 기본 구조** ⭐ | ① **단순 반사 에이전트(Simple reflex)**: 현재 인지만 보고 조건-행동 규칙(`if-then`)으로 반응.<br>② **모델 기반 반사 에이전트(Model-based reflex)**: 보이지 않는 세계의 **내부 상태(state)** 를 추적하여 부분 관측 환경을 다룸.<br>③ **목표 기반 에이전트(Goal-based)**: 상태가 목표에 도달하는지 미래 결과를 예측·탐색하여 행동 선택.<br>④ **효용 기반 에이전트(Utility-based)**: 여러 목표 달성 경로 중 얼마나 바람직한지(행복도)를 수치화한 **효용 함수(Utility function)** 를 극대화. |
| **학습 에이전트 (Learning Agent)의 4대 요소** ⭐ | ① **학습 요소(Learning element)**: 개선을 담당, ② **수행 요소(Performance element)**: 외부 행동 선택(기존 에이전트 전체), ③ **비평가(Critic)**: 외부 성능 기준에 비추어 에이전트가 얼마나 잘하고 있는지 피드백 제공, ④ **문제 생성기(Problem generator)**: 새로운 경험을 얻기 위한 탐험적 행동을 제안. |

---

### 2.3 [Chapter 3. 탐색](./03-search.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **문제 해결의 4단계** | ① **목표 설정(Formulate goal)** $\rightarrow$ ② **문제 정의(Formulate problem)** $\rightarrow$ ③ **해 탐색(Find solution)** $\rightarrow$ ④ **실행(Execute)**. |
| **문제 정의(Problem Formulation) 4요소** ⭐ | ① **초기 상태(Initial state)**, ② 가능한 **행동(Actions)** 과 **전이 모델(Transition model / Successor function)**, ③ **목표 검사(Goal test)**, ④ **경로 비용(Path cost, 단계 비용 $c(x, a, y)$의 합)**. |
| **상태(State) vs 탐색 노드(Node)** ⭐ | **상태(State)** 는 물리적 환경의 구성(예: 현재 도시 `Arad`)이고, **탐색 노드(Node)** 는 탐색 트리를 구성하는 자료구조로 **상태, 부모 노드 포인터, 적용한 행동, 경로 비용 $g(n)$, 깊이 $d$** 를 모두 담는다. |
| **프린지 (Fringe / Frontier)** | 탐색 트리에서 생성되었으나 **아직 확장(expand)되지 않고 대기 중인 리프 노드들의 집합** (오픈 리스트). 큐(FIFO, LIFO, 우선순위 큐)로 구현하여 탐색 전략을 결정한다. |
| **탐색 전략의 4가지 평가 기준** ⭐ | ① **완전성(Completeness)**: 해가 존재할 때 반드시 해를 찾는가?<br>② **최적성(Optimality)**: 가장 비용이 적은 최적의 해를 찾는가?<br>③ **시간 복잡도(Time complexity)**: 해를 찾는 데 생성되는 노드 수.<br>④ **공간 복잡도(Space complexity)**: 메모리에 동시에 저장되는 최대 노드 수. ($b$: 분기 계수, $d$: 최단 해의 깊이, $m$: 상태 공간 최대 깊이) |
| **무정보 탐색 (Uninformed / Blind Search)** | 문제 정의에 주어진 정보 외에 목표까지 얼마나 남았는지에 대한 **추가 정보(휴리스틱)가 전혀 없는 탐색** (BFS, UCS, DFS, DLS, IDS). |
| **정보 탐색 / 휴리스틱 탐색 (Informed Search)** | 현재 노드 $n$에서 목표까지의 추정 비용을 알려 주는 **평가 함수 $f(n)$과 휴리스틱 함수 $h(n)$** 을 활용하여 유망한 노드를 먼저 확장하는 탐색 (Greedy Best-First, A\*). |
| **휴리스틱 함수 $h(n)$** | 노드 $n$의 상태에서 목표 상태까지 가는 **가장 저렴한 경로의 추정 비용**. (단, 목표 노드에서는 $h(\text{goal}) = 0$) |
| **탐욕적 최선 우선 탐색 (Greedy Best-First Search)** | 평가 함수 $f(n) = h(n)$을 사용하여 **당장 목표에 가장 가까워 보이는 노드** 부터 확장하는 탐색. 빠를 수 있으나 **완전하지도 않고 최적성도 보장하지 못한다**. |
| **A\* 탐색 (A\* Search)** ⭐ | 평가 함수 **$f(n) = g(n) + h(n)$** (시작점부터 현재까지의 실제 비용 $g(n)$ + 목표까지의 추정 비용 $h(n)$, 즉 노드 $n$을 거쳐 가는 해의 추정 총비용)이 가장 작은 노드부터 확장하는 탐색. |
| **허용 가능한 휴리스틱 (Admissible Heuristic)** ⭐ | 모든 노드 $n$에 대해 **$0 \le h(n) \le h^*(n)$** (실제 최소 잔여 비용 $h^*(n)$을 **절대 과대평가하지 않음**, 낙관적 추정)을 만족하는 휴리스틱. **트리 탐색에서 A\*의 최적성을 보장하는 조건** 이다. (예: 직선거리 $h_{\text{SLD}}$) |
| **일관된 휴리스틱 (Consistent Heuristic / 단조성)** | 모든 노드 $n$과 후계 노드 $n'$에 대해 삼각부등식 **$h(n) \le c(n, a, n') + h(n')$** 을 만족하는 성질. **그래프 탐색(중복 상태 제거)에서 A\*의 최적성을 보장** 한다. |
| **지배 (Dominance)와 완화된 문제 (Relaxed Problem)** | 두 허용 가능한 휴리스틱 중 모든 $n$에서 $h_2(n) \ge h_1(n)$이면 **$h_2$가 $h_1$을 지배($h_2$가 더 적은 노드를 확장해 더 효율적)** 한다. 문제의 제약 조건을 줄인 **완화된 문제(Relaxed problem)의 정확한 최적 비용** 은 원래 문제의 허용 가능한 휴리스틱이 된다. |

---

### 2.4 [Chapter 7. 논리적 에이전트](./05-logical-agents.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **지식 베이스 (Knowledge Base, KB)** | 형식 언어(formal language)로 표현된 **문장(sentence)들의 집합** 으로, 특정 도메인에 특화된 사실과 규칙을 저장한다. |
| **추론 엔진 (Inference Engine)** | 지식 베이스(KB)의 문장들로부터 새로운 사실이나 행동을 이끌어내는 **도메인 독립적인(domain-independent) 알고리즘**. |
| **선언적 접근 (Declarative Approach)과 `Tell` / `Ask`** | 어떻게 행동할지 절차를 코딩하는 대신, 에이전트가 알아야 할 지식을 **`Tell`(KB에 문장 추가)** 로 알려 주고 해야 할 행동을 **`Ask`(KB에 질의)** 로 추론하게 하는 방식. |
| **구문 (Syntax) vs 의미 (Semantics)** | **구문(Syntax)** 은 어떤 기호 배열이 문법적으로 올바른 문장(well-formed sentence)인지 정의하고, **의미(Semantics)** 는 각 가능한 세계(**모델, Model**)에서 문장의 **참/거짓(Truth)** 을 정의한다. |
| **모델 (Model)과 $M(\alpha)$** | **모델** 은 문장의 참·거짓을 평가할 수 있도록 모든 변수/명제 기호의 진릿값이 정해진 '가능한 세계'이며, **$M(\alpha)$** 는 문장 $\alpha$가 참이 되는 모든 모델들의 집합이다. |
| **논리적 함의 (Entailment, $\text{KB} \models \alpha$)** ⭐ | **"지식베이스 $\text{KB}$가 참인 모든 모델(가능한 세계)에서 문장 $\alpha$도 반드시 참이다"** 라는 의미론적 관계. 집합 기호로는 **$M(\text{KB}) \subseteq M(\alpha)$** 와 동치이다. |
| **추론 / 도출 (Inference, $\text{KB} \vdash_i \alpha$)** | 추론 알고리즘 $i$가 구문적 조작을 통해 지식베이스 $\text{KB}$로부터 문장 $\alpha$를 이끌어내는(도출하는) 절차적 과정. |
| **건전성 (Soundness) vs 완전성 (Completeness)** ⭐ | - **건전성(Soundness, 진리 보존)**: 추론 알고리즘 $i$가 도출한 문장은 실제로 함의된 참인 문장뿐이다 ($\text{KB} \vdash_i \alpha \Rightarrow \text{KB} \models \alpha$). 거짓을 지어내지 않음.<br>- **완전성(Completeness)**: $\text{KB}$가 함의하는 모든 참인 문장을 알고리즘 $i$가 빠짐없이 도출해 낼 수 있다 ($\text{KB} \models \alpha \Rightarrow \text{KB} \vdash_i \alpha$). |
| **타당성 (Validity) / 항진명제 (Tautology)** | 문장이 **모든 가능한 모델에서 항상 참** 인 성질 (예: $P \lor \lnot P$). **연역 정리**: $\text{KB} \models \alpha$일 필요충분조건은 $(\text{KB} \Rightarrow \alpha)$가 **타당(valid)** 한 것이다. |
| **충족 가능성 (Satisfiability) vs 충족 불가능성 (Unsatisfiability)** | **충족 가능** 은 문장이 참이 되는 모델이 **적어도 하나 존재** 하는 것이고, **충족 불가능(모순)** 은 어떤 모델에서도 참이 될 수 없는 것이다. $\text{KB} \models \alpha$일 필요충분조건은 **$By \text{ 귀류법}: (\text{KB} \land \lnot\alpha)$가 충족 불가능(unsatisfiable)** 한 것이다. |

---

### 2.5 [Chapter 8. 일차 논리](./07-first-order-logic.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **명제 논리(PL)의 한계와 일차 논리(FOL)의 등장** | 명제 논리는 세상에 단순 사실(`facts`)만 존재한다고 보아 **"인접한 칸에 구덩이가 있으면 바람이 분다" 같은 일반 규칙을 한 문장으로 표현할 수 없고 칸마다 중복 작성해야 하는 표현력의 한계** 가 있다. 일차 논리는 세상을 **객체(Objects), 관계(Relations), 함수(Functions)** 로 기술하고 변수와 한정사($\forall, \exists$)를 도입해 자연어에 가깝게 표현력을 확장했다. |
| **존재론적 개입 (Ontological Commitment) vs 인식론적 개입 (Epistemological Commitment)** ⭐ | - **존재론적 개입**: 논리 언어가 **실제 세상에 무엇이 존재한다고 가정하는가** (명제 논리 = `facts`, 일차 논리 = `facts, objects, relations`, 시간 논리 = `+ times`).<br>- **인식론적 개입**: 에이전트가 문장에 대해 가질 수 있는 **지식(믿음)의 상태** (명제·일차·시간 논리 = `true/false/unknown`, 확률 이론 = `degree of belief` $\in [0, 1]$, 퍼지 논리 = `known interval value`). |
| **항 (Term) vs 원자 문장 (Atomic Sentence)** ⭐ | - **항(Term)**: 상수, 변수, 또는 함수 호출(`LeftLegOf(John)`)처럼 **세상 속의 객체(Object)를 가리키는 논리 표현**(진릿값이 아님).<br>- **원자 문장(Atomic Sentence)**: 술어 기호에 항들을 넣은 표현($\text{Brother}(\text{Richard}, \text{John})$)이나 항들의 등호($\text{term}_1 = \text{term}_2$)로, **참/거짓 진릿값을 가지는 최소 단위 문장**. |
| **해석 (Interpretation)** ⭐ | 논리식의 구문 기호(Syntax)들이 모델(실제 세계) 속의 어떤 지시 대상(Referent)을 가리키는지 짝지어 주는 매핑 규칙:<br>① **상수 기호(Constant symbols) $\rightarrow$ 객체(Objects)**<br>② **술어 기호(Predicate symbols) $\rightarrow$ 관계(Relations)**<br>③ **함수 기호(Function symbols) $\rightarrow$ 함수적 관계(Functional relations)** |
| **전칭 한정사($\forall$)와 존재 한정사($\exists$) 및 주 연결사 규칙** ⭐ | - **전칭 한정사($\forall x$, 모든 $x$)**: 모델의 모든 객체에 대해 참이어야 하며, 논리곱($\land$)의 나열과 같다. **주 연결사로 항상 함의($\Rightarrow$)를 사용** 한다 ($\forall x \; \text{At}(x, \text{D21}) \Rightarrow \text{Smart}(x)$).<br>- **존재 한정사($\exists x$, 어떤 $x$)**: 모델의 적어도 한 객체에 대해 참이면 되며, 논리합($\lor$)의 나열과 같다. **주 연결사로 항상 논리곱($\land$)을 사용** 한다 ($\exists x \; \text{At}(x, \text{Stanford}) \land \text{Smart}(x)$). |
| **데이터베이스 의미론 (Database Semantics)의 3대 가정 (UNA · CWA · DC)** ⭐ | 일반 지식베이스(KB, 열린 세계 가정)와 달리 데이터베이스(DB)가 짧은 사실 나열만으로 완전한 추론을 하기 위해 전제하는 3가지 가정:<br>① **고유 이름 가정(UNA, Unique Names Assumption)**: 서로 다른 상수 기호는 서로 다른 객체를 가리킨다.<br>② **닫힌 세계 가정(CWA, Closed World Assumption)**: 참이라고 알려지지 않은 원자 문장은 모두 거짓(`false`)이다.<br>③ **영역 폐쇄 가정(DC, Domain Closure)**: 상수 기호로 이름 붙여진 개체 외에 다른 개체는 존재하지 않는다. (단, 인터넷 환경에서는 이 3가지 가정이 성립하지 않음) |
| **치환 (Substitution / Binding List, $\sigma$)** | 일차 논리 KB에 존재 질의($\text{Ask}(\text{KB}, \exists a \; \text{Action}(a, 5))$)를 했을 때, 변수를 어떤 항으로 바인딩하면 참이 되는지 나타내는 목록(예: $\sigma = \{a/\text{Shoot}\}$). 문장 $S$에 $\sigma$를 적용한 문장을 $S\sigma$라 표기한다. |
| **진단 규칙 (Diagnostic Rule) vs 인과 규칙 (Causal Rule)** | - **진단 규칙**: 관측된 **결과(바람)로부터 숨겨진 원인(구덩이)을 추론** 하는 규칙 ($\forall y \; \text{Breezy}(y) \Rightarrow \exists x \; \text{Pit}(x) \land \text{Adjacent}(x, y)$).<br>- **인과 규칙**: **원인(구덩이)으로부터 결과(바람)를 추론** 하는 규칙 ($\forall x, y \; \text{Pit}(x) \land \text{Adjacent}(x, y) \Rightarrow \text{Breezy}(y)$). |
| **상황 미적분 (Situation Calculus)** ⭐ | 일차 논리에서 시간에 따른 상태 변화를 표현하기 위해, 변하는 술어마다 **상황(Situation) 인자 $s$** 를 추가하고, 상황 $s$에서 행동 $a$를 수행한 결과 상황을 **`Result(a, s)` 함수** 로 연결하는 표기 체계. |
| **효과 공리(Effect Axiom) vs 프레임 공리(Frame Axiom)** | - **효과 공리**: 행동으로 인해 **변하는 속성** 을 기술하는 공리.<br>- **프레임 공리**: 행동과 무관하여 **변하지 않고 그대로 유지되는 속성(non-changes)** 을 기술하는 공리. |
| **프레임 문제 (Frame Problem), 자격 문제 (Qualification Problem), 파생 문제 (Ramification Problem)** ⭐ | - **프레임 문제**: 행동이 일어날 때 **변하지 않는 대다수의 사실들을 프레임 공리로 일일이 다 적어야 하고(표현 문제) 매 단계 복사해 추론해야 하는(추론 문제) 문제**.<br>- **자격 문제**: 행동이 성공하기 위한 현실 세계의 **수많은 예외 전제조건(미끄러운 금 등)을 모두 나열할 수 없는 문제**.<br>- **파생 문제**: 행동으로 인해 발생하는 **수많은 부수적·2차적 결과(먼지 이동, 장갑 마모 등)를 모두 기술할 수 없는 문제**. |
| **후속 상태 공리 (Successor-State Axiom)** ⭐ | 표현상의 **프레임 문제를 해결** 하기 위해, 행동마다 공리를 적는 대신 **술어 $P$ 하나마다** "행동 후 $P$가 참 $\Leftrightarrow$ [방금 행동이 $P$를 참으로 만들었거나 $\lor$ (이미 $P$가 참이었고 방금 행동이 $P$를 거짓으로 만들지 않음)]" 형태로 정의한 공리. |

---

### 2.6 [제4장. 전문가 시스템](./08-expert-systems.md)

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **전문가 시스템 (Expert System)과 등장 배경** | 초창기 범용 탐색 시스템(**GPS**, General Problem Solver)이 제한된 장난감 문제만 풀 수 있었던 한계를 극복하기 위해, **특정 전문 영역의 도메인 지식(규칙)** 을 담아 인간 전문가의 의사결정을 모방하도록 만든 최초의 성공적인 AI 소프트웨어. |
| **MYCIN (마이신)** | 박테리아 혈액 감염을 진단하고 적절한 항생제를 처방하기 위해 약 450여 개의 `IF-THEN` 규칙으로 구축된 초기 대표 의료 전문가 시스템. |
| **전문가 시스템의 3대 구성 요소와 인적 역할** ⭐ | - **3대 구성 요소**: ① **지식 베이스(Knowledge Base)**, ② **추론 엔진(Inference Engine)**, ③ **사용자 인터페이스(User Interface)** (+ 설명 기능).<br>- **인적 역할**: 도메인 지식을 제공하는 **인간 전문가(Expert)**, 지식을 추출해 규칙으로 코딩하는 **지식 공학자(Knowledge Engineer)**, 질의하는 **사용자(User)**. |
| **데이터(Data) · 정보(Information) · 지식(Knowledge)** | - **데이터**: 가공되지 않은 원시 사실 (예: `빨간색, 7시 30분`).<br>- **정보**: 데이터를 **처리** 하여 의미를 부여한 사실 (예: `사거리 신호등이 빨간색으로 바뀌었다`).<br>- **지식**: 정보를 **일반화·정렬** 하여 **추론과 행동 결정에 사용하는 규칙화된 정보** (예: `신호등이 빨간색으로 바뀌었으므로 차를 멈추어야 한다`). |
| **생성 규칙 (Production Rule)** | 지식을 **`IF <조건/전제(Antecedent)> THEN <행동/결론(Consequent)>`** 형태로 표현하는 규칙. 인간이 이해하고 작성하기 가장 자연스러운 지식 표현법이다. |
| **장기 기억장치 (Long-Term Memory) vs 단기 기억장치 (Short-Term Memory)** ⭐ | 전문가 시스템에서 **장기 기억장치** 는 영구적인 도메인 지식인 **규칙(Rules, 지식 베이스)** 을 저장하고, **단기 기억장치** 는 현재 문제의 관측 데이터와 추론된 중간 결과인 **사실(Facts, 작업 기억)** 을 저장한다. |
| **순방향 추론 (Forward Chaining) vs 역방향 추론 (Backward Chaining)** ⭐ | - **순방향 추론(자료 구동형)**: 알려진 **사실(Facts)** 에서 출발해 조건이 맞는 규칙을 점화하여 결론을 도출하는 방식 (단점: 목표와 무관한 규칙들도 점화될 수 있음).<br>- **역방향 추론(목표 구동형)**: 확인할 **목표(Goal, 결과)** 에서 출발해 그 목표를 결론으로 갖는 규칙들의 전제 조건을 역추적하며 사실이 뒷받침하는지 검증하는 방식 (**필요한 규칙만 검사하므로 더 효율적**). |
| **충돌 해법 (Conflict Resolution) 3가지** ⭐ | 동일한 사실에 대해 여러 규칙의 조건이 동시에 만족되어 상반된 결론이 나올 때 점화할 규칙을 고르는 방법:<br>① **우선순위(Priority) 방식**: 가장 높은 우선순위가 부여된 규칙 점화.<br>② **특수성(Specificity) 방식**: 조건(`IF`)이 가장 구체적이고 까다로운 특수한 규칙 먼저 점화.<br>③ **최신성(Recency) 방식**: 단기 기억장치에 가장 최근에 입력된 사실 데이터를 사용하는 규칙 점화. |

---

### 2.7 [Chapter 10 (제5장). 지식 표현](./09-knowledge-representation.md) — `p.21`까지

| 용어 (영문 / 한글) | 시험 답안용 핵심 개념 설명 |
|---|---|
| **온톨로지 (Ontology)와 온톨로지 공학** ⭐ | 현실 세계의 특정 영역을 표현하기 위한 **어휘(Vocabulary)와 이론(Theory)의 체계** ("어휘와 이론으로 지식을 표현하는 방법"). 모든 도메인에 공통 적용되는 최상위 개념 틀을 **범용/상위 온톨로지(General-purpose / Upper ontology)** 라 하며, 대규모 구축 사례로 **CYC**(전문가 팀 수작업), **DBpedia**(위키 DB 추출), **ReVerb**(문서 추출), **OpenMind**(대중 상식 입력)가 있다. |
| **사물(Things) vs 물질(Stuff)** | 상위 온톨로지에서 물리적 객체(`PhysicalObjects`)를 나누는 기준으로, **Things(개별 사물)** 는 사람·공처럼 경계가 뚜렷해 셀 수 있고 쪼개면 성질을 잃는 대상이며, **Stuff(물질)** 는 물·공기·버터처럼 쪼개도 같은 성질을 유지하는 불가산 물질이다. (사건에서는 **이산 사건 Discrete Events vs 프로세스 Processes** 의 구분과 대응됨) |
| **범주 (Category)와 실체화 (Reification)** ⭐ | 추론은 개별 객체가 아닌 **범주(Category, 공통 속성을 가진 객체들의 부류)** 수준에서 이루어진다. 일차 논리에서 술어(`Basketball(b)`)나 사건(`Fly(...)`)을 **`Basketballs`나 `Fly_17` 같은 하나의 독립된 '객체(Object)'로 변환하는 기법을 실체화(Reification: turning a proposition into an object)** 라 한다. |
| **서로소 (`Disjoint`), 완전 분해 (`ExhaustiveDecomposition`), 분할 (`Partition`)** ⭐ | - **`Disjoint(s)`**: 범주 집합 $s$ 안의 어떤 두 범주도 공통 원소가 없음(교집합 $=\emptyset$).<br>- **`ExhaustiveDecomposition(s, c)`**: 상위 범주 $c$의 모든 원소가 $s$의 하위 범주 중 적어도 하나에 속함(빠짐없음).<br>- **`Partition(s, c)`**: **서로소(`Disjoint`)이면서 동시에 완전 분해(`ExhaustiveDecomposition`)** 인 관계 (겹치지도 않고 남지도 않게 쪼갬). |
| **복합 객체 (`PartOf`)와 다발 (`Bunch`)** | - **`PartOf(x, y)`**: 부분-전체 포함 관계로 **추이적(transitive)** 이고 **반사적(reflexive)** 이다.<br>- **`Bunch` (다발)**: 확정된 부분(`parts`)들로 이루어져 있으나 **특별한 구조(structure)가 없는 물리적 복합 객체** (예: 봉지 속 사과 3개 `BunchOf(Apple1, Apple2, Apple3)`). 추상적 집합(`Set`)과 달리 무게 등 물리적 속성을 가질 수 있으며 논리적 최소화(Logical minimization)로 정의된다. |
| **측정치 (Measurements)와 단위 함수 (Unit Functions)** | 길이, 질량, 가격 등의 정량적 속성값을 표현할 때 숫자에 **`Inches(1.5)`, `Centimeters(3.81)`, `Hours(24)` 같은 단위 함수를 적용한 객체** 로 표현하여 단위 혼동을 막고 변환 공리를 적용한다. |
| **사건 미적분 (Event Calculus)과 6대 술어** ⭐ | 연속적인 행동 도중(during)에 일어나는 일과 동시 발생 행동을 표현하지 못하는 상황 미적분의 한계를 극복하기 위해 사건(`Event`)과 시간 구간(`Interval`)을 도입한 체계.<br>- **6대 술어**: **$T(f, t)$** (시각 $t$에 유동체 $f$가 참), **$\text{Happens}(e, i)$** (구간 $i$에 사건 $e$ 발생), **$\text{Initiates}(e, f, t)$** ($e$가 $f$를 시작시킴), **$\text{Terminates}(e, f, t)$** ($e$가 $f$를 종료시킴), **$\text{Clipped}(f, i)$** (구간 $i$ 도중 $f$가 끊김), **$\text{Restored}(f, i)$** (구간 $i$ 도중 $f$가 복구됨). |
| **이산 사건 (Discrete Events) vs 프로세스 (Processes / Liquid Events)** | **이산 사건** 은 시작·중간·끝이 있어 중단되면 다른 사건이 되지만, **프로세스(연속/액체 사건, 예: `Flyings`)** 는 어떤 시간 구간 $(t_1, t_4)$ 동안 일어나면 **그 안의 임의의 부분 구간(subinterval, $(t_2, t_3)$) 동안에도 여전히 똑같은 프로세스로 성립** 한다. |
| **순간 (`Moments`)과 시간 구간 관계 (`Meet`, `Overlap`, `During` 등)** | 시간 구간(`Intervals`)은 길이가 0인 **`Moments`(순간)** 와 **`ExtendedIntervals`(연장된 구간)** 로 분할된다. 구간 $i, j$ 사이의 관계로 **$\text{Meet}(i, j) \Leftrightarrow \text{End}(i) = \text{Begin}(j)$ ($i$가 끝나자마자 $j$가 시작)**, `Before`, `After`, `During`, `Overlap`, `Starts`, `Finishes`, `Equals`를 사용한다. |
| **유동체 (State Fluents) vs 물리적 객체 (Physical Objects)** ⭐ | 미국(`USA`) 같은 **물리적 객체** 는 시공간의 한 덩어리(실체)이고, **`President(USA)`(미국의 대통령)** 나 `Population(USA)`처럼 **시간에 따라 가리키는 대상이나 값이 바뀌는 상태를 유동체(Fluent)** 라 한다 (예: 1790년에는 `President(USA)`라는 유동체가 `GeorgeWashington`이라는 인물 객체와 같음). |
| **시맨틱 네트워크 (Semantic Networks / 의미망)** ⭐ | 개념(범주·인스턴스)을 **노드** 로, 관계(`SubsetOf`, `MemberOf` 등)를 **링크(화살표)** 로 표현한 그래프 형태의 온톨로지 표현법(현대 **지식 그래프** 의 모태). 상위 범주의 기본값을 하위 노드가 물려받는 **상속(Inheritance)** 과 특정 노드의 예외 값을 덮어쓰는 **오버라이딩(Overriding)** 이 직관적이며, 인자가 3개 이상인 다항 관계($\text{Fly}(\text{Shankar}, \text{NewYork}, \text{NewDelhi}, \text{Yesterday})$)는 사건 자체를 **`Fly_17` 인스턴스 노드로 실체화(Reification)** 하여 이항 링크들로 연결해 표현한다. |

---

## 3. Part 2. 시험에 바로 쓰는 10대 핵심 비교표

### 비교 1. 탐색 알고리즘 총정리 비교표 (Ch.3) ⭐

| 알고리즘 | 프린지 자료구조 | 완전성 | 최적성 | 시간 복잡도 | 공간 복잡도 | 핵심 특징 |
|---|---|---|---|---|---|---|
| **BFS** (너비 우선) | FIFO 큐 | ✅ ($b$ 유한) | ✅ (단계 비용 동일 시) | $O(b^{d+1})$ | $O(b^{d+1})$ | 얕은 노드부터 확장, **메모리 소모가 가장 큰 문제** |
| **UCS** (균일 비용) | 우선순위 큐 ($g(n)$) | ✅ ($c \ge \epsilon > 0$) | ✅ | $O(b^{1+\lfloor C^*/\epsilon \rfloor})$ | $O(b^{1+\lfloor C^*/\epsilon \rfloor})$ | 누적 경로 비용 $g(n)$ 최소 노드부터 확장 |
| **DFS** (깊이 우선) | LIFO 스택 | ❌ (무한 경로 시) | ❌ | $O(b^m)$ | **$O(bm)$** | **공간 복잡도가 선형($bm$)으로 매우 작음** |
| **DLS** (깊이 제한) | LIFO 스택 (깊이 $l$) | ❌ ($d > l$일 때) | ❌ | $O(b^l)$ | $O(bl)$ | 깊이 한계 $l$까지만 DFS 수행 |
| **IDS** (반복 깊화) ⭐ | LIFO 스택 ($l=0,1,2\dots$) | ✅ | ✅ (단계 비용 동일 시) | $O(b^d)$ | **$O(bd)$** | **BFS의 완전·최적성 + DFS의 적은 메모리를 결합한 최선책** |
| **Greedy** (탐욕적) | 우선순위 큐 ($h(n)$) | ❌ | ❌ | $O(b^m)$ | $O(b^m)$ | 당장 목표에 가까워 보이는 $h(n)$만 봄 (근시안적) |
| **A\* 탐색** ⭐ | 우선순위 큐 ($g(n)+h(n)$) | ✅ | ✅ ($h$ 허용/일관 시) | 지수적 ($h$에 좌우) | 모든 노드 저장 | **$f(n)=g(n)+h(n)$**, 허용 가능한 휴리스틱 사용 시 최적 보장 |

---

### 비교 2. 명제 논리 vs 일차 논리 vs 시간/확률/퍼지 논리 (Ch.7, Ch.8) ⭐

| 논리 / 체계 | 존재론적 개입 (Ontological Commitment)<br>*세상에 무엇이 존재하는가* | 인식론적 개입 (Epistemological Commitment)<br>*지식의 믿음 상태* |
|---|---|---|
| **명제 논리 (Propositional Logic)** | `facts` (단순 사실) | `true / false / unknown` |
| **일차 논리 (First-Order Logic)** | **`facts, objects, relations`** (사실, 객체, 관계/함수) | `true / false / unknown` |
| **시간 논리 (Temporal Logic)** | `facts, objects, relations, times` (+ 시간) | `true / false / unknown` |
| **확률 이론 (Probability Theory)** | `facts` | **`degree of belief`** $\in [0, 1]$ (확률의 정도) |
| **퍼지 논리 (Fuzzy Logic)** | `facts + degree of truth` (진리의 정도) | `known interval value` |

---

### 비교 3. 일차 논리 지식베이스(KB) vs 데이터베이스(DB) 의미론 (Ch.8) ⭐

| 비교 항목 | 일차 논리 지식베이스 (FOL KB) | 데이터베이스 (Database) |
|---|---|---|
| **세계관** | **열린 세계 가정 (OWA, Open World Assumption)** | **닫힌 세계 가정 (CWA + UNA + DC)** |
| **알려지지 않은 원자 문장** | 참인지 거짓인지 **모름 (`unknown`)** | 무조건 **거짓 (`false`)** 으로 간주 (**CWA**) |
| **서로 다른 상수 기호 (`John`, `Geoffrey`)** | 같은 객체를 가리킬 수도 있음 (`John ≠ Geoffrey` 명시 필요) | 무조건 서로 다른 객체를 가리킴 (**UNA**) |
| **도메인 내 개체의 범위** | 이름이 안 붙은 미지의 개체가 더 있을 수 있음 ($\forall x$ 제한 필요) | 상수로 이름 붙여진 개체들이 세상의 전부임 (**DC**) |
| **적용 환경** | **인터넷(웹), 시맨틱 웹, 온톨로지**, 부분 관측 AI 환경 | 통제된 정형 테이블 환경 (RDBMS 등) |

---

### 비교 4. 전문가 시스템: 장기 기억 vs 단기 기억 & 순방향 vs 역방향 추론 (제4장) ⭐

| 구분 | 장기 기억장치 (Long-Term Memory) | 단기 기억장치 (Short-Term Memory) |
|---|---|---|
| **저장 요소** | **규칙 (Rules)** — `IF 조건(전제) THEN 결론(결과)` | **사실 (Facts)** — 현재 관측된 사실 및 추론으로 도출된 사실 |
| **시스템 구성 요소** | **지식 베이스 (Knowledge Base)** | **작업 기억 (Working Memory)** |

| 구분 | 순방향 추론 (Forward Chaining) | 역방향 추론 (Backward Chaining) |
|---|---|---|
| **진행 방향** | **사실(Facts) $\rightarrow$ 결론(Conclusion)** (자료 구동형) | **목표(Goal) $\rightarrow$ 증거 사실(Facts)** (목표 구동형) |
| **효율성 및 단점** | 목표와 **무관한 규칙들까지 모두 점화** 되어 비효율적일 수 있음 | **목표 증명에 필요한 규칙만 역추적하므로 더 효율적** |

---

### 비교 5. 상황 미적분 (Ch.8) vs 사건 미적분 (Ch.10) ⭐

| 비교 항목 | 상황 미적분 (Situation Calculus, Ch.8) | 사건 미적분 (Event Calculus, Ch.10) |
|---|---|---|
| **시간/변화 표현 단위** | 이산적인 **상황(Situation)** 전이: $S_{k+1} = \text{Result}(a, S_k)$ | 연속적인 **시점(Time point $t$)** 과 **시간 구간(Time interval $i$)** |
| **핵심 표현식** | $\text{Holding}(\text{Gold}, \text{Result}(\text{Grab}, s))$ | $T(f, t)$, $\text{Happens}(e, i)$, $\text{Initiates}(e, f, t)$, $\text{Terminates}(e, f, t)$ |
| **한계 및 강점** | 행동 전후의 결과만 알 수 있고, **행동 도중(during)에 무슨 일이 일어나는지나 동시 발생 행동을 표현할 수 없음** | 욕조 물 채우기 같은 **연속적 행동(Processes)과 동시 발생 사건, 시간 구간 관계를 자연스럽게 표현 가능** |

---

## 4. Part 3. 실전 예상 문제 35선 (단답형 + 개념 설명형)

### [Ch.1 ~ Ch.2] 인공지능 개요 및 지능형 에이전트 (Q1 ~ Q8)

**Q1. [단답·개념 설명]** 인공지능을 정의하는 4가지 접근법을 두 가지 기준 축으로 나누어 쓰고, 본 강의가 채택하는 중심 관점이 무엇인지 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **두 가지 기준 축**: ① 연구 대상이 **사고 과정(Thinking)** 인가 **외부 행동(Acting)** 인가, ② 성공 기준이 **인간(Humanly)** 인가 **합리성(Rationally)** 인가.
- **4가지 접근법**:
  1. 인간처럼 행동하기 (Acting Humanly — 튜링 테스트)
  2. 인간처럼 생각하기 (Thinking Humanly — 인지과학)
  3. 합리적으로 생각하기 (Thinking Rationally — 사고의 법칙)
  4. **합리적으로 행동하기 (Acting Rationally — 합리적 에이전트)**
- **본 강의의 중심 관점**: **합리적으로 행동하기(합리적 에이전트)** 이다. 논리적 추론도 결국 합리적 행동을 선택하기 위한 한 수단으로 포괄할 수 있고, 인간 뇌의 실제 메커니즘에 얽매이지 않고 공학적으로 최선의 결과를 내는 시스템을 설계할 수 있기 때문이다.
</details>

**Q2. [단답형]** 에이전트가 자연어로 소통하고 지식을 저장·추론·학습하여 튜링 테스트를 통과하기 위해 갖춰야 할 4가지 핵심 능력(전체 튜링 테스트 포함 시 6가지)을 쓰시오.

<details><summary>▶ 모범 답안 보기</summary>

1. **자연어 처리 (Natural Language Processing)** — 의사소통
2. **지식 표현 (Knowledge Representation)** — 알고 있는 것과 들은 것을 저장
3. **자동 추론 (Automated Reasoning)** — 저장된 지식으로 질문에 답하고 새 결론 도출
4. **기계 학습 (Machine Learning)** — 새로운 상황에 적응하고 패턴을 발견
- *(사물 인지와 물리적 조작을 포함하는 **전체 튜링 테스트 Total Turing Test** 의 경우)*: 5. **컴퓨터 비전 (Computer Vision)**, 6. **로보틱스 (Robotics)** 추가.
</details>

**Q3. [개념 설명]** 에이전트 함수(Agent Function)와 에이전트 프로그램(Agent Program)의 차이를 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **에이전트 함수 ($f: \mathcal{P}^* \rightarrow \mathcal{A}$)**: 에이전트가 지금까지 받은 모든 **인지 시퀀스(percept history)** 를 행동으로 대응시키는 **추상적·수학적 명세** 이다.
- **에이전트 프로그램**: 물리적 **아키텍처(Architecture)** 위에서 실행되며, 현재 인지를 입력받아 에이전트 함수를 실제로 계산하고 구현하는 **구체적인 소프트웨어 코드** 이다 ($\text{Agent} = \text{Architecture} + \text{Program}$).
</details>

**Q4. [단답·개념 설명]** 에이전트의 합리성(Rationality)을 판단하는 4가지 기준 요소를 쓰고, 왜 합리성이 전지성(Omniscience)과 다른지 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **합리성의 4가지 요소**: ① 성공을 정의하는 **성능 척도(Performance measure)**, ② 환경에 대한 에이전트의 **사전 지식(Prior knowledge)**, ③ 에이전트가 수행할 수 있는 **행동들(Actions)**, ④ 현재까지의 **인지 시퀀스(Percept sequence)**.
- **전지성과의 차이**: 전지성은 행동의 **실제 결과** 를 미리 완벽히 아는 것(현실에서 불가능)이지만, 합리성은 현재까지 주어진 인지 정보와 지식을 바탕으로 **기대 성능(Expected performance)을 최대화** 하는 행동을 선택하는 것이다.
</details>

**Q5. [단답형]** 작업 환경(Task Environment)을 설계할 때 명세하는 **PEAS** 의 약자를 풀어서 쓰고, '자율주행 택시'에 대해 각각 예시를 1개씩 드시오.

<details><summary>▶ 모범 답안 보기</summary>

- **P (Performance measure, 성능 척도)**: 안전성, 목적지 정확 도달, 승객 편안함, 수익 극대화 등
- **E (Environment, 환경)**: 도로, 다른 차량, 보행자, 신호등, 날씨 등
- **A (Actuators, 액추에이터)**: 핸들(조향장치), 가속 페달, 브레이크, 방향지시등 등
- **S (Sensors, 센서)**: 카메라, 라이다(LiDAR), 속도계, GPS, 가속도계 등
</details>

**Q6. [개념 설명]** 환경의 유형 중 ① 완전 관측 vs 부분 관측, ② 일화적(Episodic) vs 순차적(Sequential), ③ 정적(Static) vs 동적(Dynamic)의 차이를 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

1. **완전 관측 vs 부분 관측**: 센서로 매 시점 환경의 **전체 상태를 모두 감지** 할 수 있으면 완전 관측(예: 체스), 센서 노이즈나 시야 제한으로 일부만 감지하면 부분 관측(예: 포커, 자율주행)이다.
2. **일화적 vs 순차적**: 각 에피소드(인지 후 행동)가 **독립적이어서 현재의 행동이 다음 에피소드에 영향을 주지 않으면** 일화적(예: 불량 부품 이미지 분류), 현재 행동이 미래의 상태와 보상에 연쇄적으로 영향을 미치면 순차적(예: 체스, 택시 운전)이다.
3. **정적 vs 동적**: 에이전트가 행동을 고민하는 동안 환경이 변하지 않으면 정적(예: 십자말풀이), 고민하는 도중에도 환경이 계속 변하면 동적(예: 자율주행)이다.
</details>

**Q7. [개념 설명]** 에이전트의 4가지 기본 구조(단순 반사, 모델 기반 반사, 목표 기반, 효용 기반)가 각각 어떤 한계를 극복하기 위해 발전했는지 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

1. **단순 반사 에이전트**: 현재 인지만 보고 조건-행동 규칙으로 반응하므로 **완전 관측 환경** 에서만 제대로 작동한다.
2. **모델 기반 반사 에이전트**: **부분 관측 환경** 을 다루기 위해 세계가 어떻게 변하는지(전이 모델)를 이용해 보이지 않는 **내부 상태(Internal state)** 를 유지·갱신한다.
3. **목표 기반 에이전트**: 상태만으로는 무엇을 해야 할지 알 수 없을 때, 달성하고자 하는 **목표(Goal)** 정보를 두고 미래 행동을 **탐색·계획** 하여 목표에 도달하는 행동을 고른다.
4. **효용 기반 에이전트**: 목표에 도달하는 경로가 여러 개이거나 상충하는 목표들(예: 속도 vs 안전)이 있을 때, 상태의 바람직한 정도를 실수 값으로 매기는 **효용 함수(Utility function)** 를 통해 기대 효용을 극대화한다.
</details>

**Q8. [단답형]** 학습 에이전트(Learning Agent)를 구성하는 4가지 핵심 구성 요소를 쓰시오.

<details><summary>▶ 모범 답안 보기</summary>

1. **학습 요소 (Learning element)**: 피드백을 받아 수행 요소를 개선함.
2. **수행 요소 (Performance element)**: 인지를 받아 실제 행동을 선택함.
3. **비평가 (Critic)**: 외부 성능 기준에 비추어 현재 에이전트의 행동이 얼마나 좋은지 평가 피드백을 줌.
4. **문제 생성기 (Problem generator)**: 학습에 도움이 되는 새로운 정보와 경험을 얻도록 탐험적 행동을 제안함.
</details>

---

### [Ch.3] 탐색을 통한 문제 해결 (Q9 ~ Q14)

**Q9. [단답형]** 탐색 문제(Problem)를 형식적으로 정의하는 4가지 구성 요소와, 탐색 전략을 평가하는 4가지 기준을 각각 쓰시오.

<details><summary>▶ 모범 답안 보기</summary>

- **문제 정의 4요소**: ① 초기 상태(Initial state), ② 행동 및 전이 모델(Actions / Successor function), ③ 목표 검사(Goal test), ④ 경로 비용(Path cost).
- **탐색 전략 평가 4기준**: ① 완전성(Completeness), ② 최적성(Optimality), ③ 시간 복잡도(Time complexity), ④ 공간 복잡도(Space complexity).
</details>

**Q10. [개념 설명]** 너비 우선 탐색(BFS)과 깊이 우선 탐색(DFS)의 장단점을 비교하고, 반복 깊화 탐색(IDS, Iterative Deepening Search)이 왜 대규모 무정보 탐색에서 선호되는지 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **BFS**: 가장 얕은 목표를 찾으므로 **완전하고 최적(단계 비용 동일 시)** 이지만, 확장한 모든 레벨의 노드를 메모리에 유지해야 해서 **공간 복잡도가 $O(b^{d+1})$로 지수적** 이라는 치명적 단점이 있다.
- **DFS**: 현재 경로의 분기만 저장하므로 **공간 복잡도가 $O(bm)$으로 매우 작지만**, 무한 경로에 빠져 해를 못 찾을 수 있고(**불완전**) 찾은 해가 최적이 아니다(**비최적**).
- **IDS의 장점**: 깊이 제한 $l=0, 1, 2, \dots, d$를 늘려가며 DFS를 반복 수행함으로써, **공간 복잡도는 DFS처럼 $O(bd)$로 선형 수준을 유지하면서 BFS처럼 완전성과 최적성을 동시에 달성** 하기 때문에 상태 공간이 크고 해의 깊이를 모를 때 가장 선호된다.
</details>

**Q11. [단답·개념 설명]** 균일 비용 탐색(UCS), 탐욕적 최선 우선 탐색(Greedy Best-First Search), A\* 탐색의 평가 함수 $f(n)$을 각각 쓰고 비교하시오.

<details><summary>▶ 모범 답안 보기</summary>

1. **균일 비용 탐색 (UCS)**: $f(n) = g(n)$ — 시작 노드부터 현재 노드 $n$까지의 **실제 누적 경로 비용** 만 보고 최소 비용 노드를 확장한다 (완전·최적이나 방향성이 없음).
2. **탐욕적 최선 우선 탐색 (Greedy)**: $f(n) = h(n)$ — 현재 노드 $n$에서 목표까지의 **추정 잔여 비용(휴리스틱)** 만 보고 확장한다 (목표 지향적이나 지금까지 쓴 비용 $g(n)$을 무시해 불완전·비최적).
3. **A\* 탐색**: **$f(n) = g(n) + h(n)$** — 지금까지 든 실제 비용 $g(n)$과 앞으로 들 추정 비용 $h(n)$을 합친 **노드 $n$을 경유하는 해의 추정 총비용** 이 최소인 노드를 확장한다.
</details>

**Q12. [개념 설명]** A\* 탐색에서 **허용 가능한 휴리스틱(Admissible Heuristic)** 과 **일관된 휴리스틱(Consistent Heuristic)** 의 정의와 수식을 쓰고, 왜 이 조건이 중요한지 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **허용 가능성 (Admissibility)**: 모든 노드 $n$에 대해 **$0 \le h(n) \le h^*(n)$**, 즉 목표까지의 실제 최소 비용 $h^*(n)$을 **절대 과대평가하지 않는(낙관적인) 성질** 이다. **트리 탐색에서 A\*가 최적의 해를 찾음을 보장** 한다.
- **일관성 (Consistency / Monotonicity)**: 모든 노드 $n$과 행동 $a$로 도달한 후계 노드 $n'$에 대해 삼각부등식 **$h(n) \le c(n, a, n') + h(n')$** 을 만족하는 성질이다. 경로를 따라갈수록 $f(n)$ 값이 절대 감소하지 않게 하여 **그래프 탐색(중복 상태 제거)에서 A\*가 최적의 해를 찾음을 보장** 한다.
</details>

**Q13. [개념 설명]** 8-퍼즐 문제에서 두 휴리스틱 $h_1$(제자리에 있지 않은 타일 수)과 $h_2$(맨해튼 거리 합) 중 어느 것이 더 우수한지 **지배(Dominance)** 개념으로 설명하고, 이러한 허용 가능한 휴리스틱을 자동으로 고안하는 **완화된 문제(Relaxed Problem)** 기법을 설명하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **지배(Dominance)**: 모든 상태 $n$에서 $h_1(n) \le h_2(n) \le h^*(n)$이 성립하므로 **$h_2$(맨해튼 거리)가 $h_1$을 지배** 한다. 지배하는 휴리스틱($h_2$)은 실제 비용에 더 가까우므로 A\* 탐색 시 불필요하게 확장하는 노드 수가 항상 더 적거나 같다.
- **완화된 문제(Relaxed Problem)**: 원래 문제의 행동 제약 조건을 제거하거나 완화한 문제(예: "타일을 빈칸 여부와 상관없이 아무 인접 칸으로나 옮길 수 있다" $\rightarrow h_2$)이다. 완화된 문제의 최적 해 비용은 원래 문제보다 클 수 없으므로 **자동으로 허용 가능한(그리고 일관된) 휴리스틱** 이 된다.
</details>

---

### [Ch.7] 논리적 에이전트와 명제 논리 (Q14 ~ Q18)

**Q14. [개념 설명]** 논리에서 **함의(Entailment, $\text{KB} \models \alpha$)** 와 **추론/도출(Inference, $\text{KB} \vdash_i \alpha$)** 의 차이를 설명하고, 모델 집합 $M(\text{KB})$와 $M(\alpha)$의 포함 관계로 함의를 표현하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **함의 ($\text{KB} \models \alpha$)**: **의미론적(Semantic) 개념** 으로, 지식베이스 $\text{KB}$가 참이 되는 **모든 가능한 세계(모델)에서 문장 $\alpha$도 반드시 참** 이라는 뜻이다. 모델 집합의 포함 관계로는 **$M(\text{KB}) \subseteq M(\alpha)$** 로 표현된다.
- **도출 ($\text{KB} \vdash_i \alpha$)**: **구문론적·절차적(Syntactic) 개념** 으로, 추론 알고리즘 $i$가 기호 조작 규칙을 적용해 $\text{KB}$로부터 문장 $\alpha$를 계산해 내는 것이다.
</details>

**Q15. [단답·개념 설명]** 추론 알고리즘의 **건전성(Soundness)** 과 **완전성(Completeness)** 을 정의하시오.

<details><summary>▶ 모범 답안 보기</summary>

- **건전성 (Soundness, 진리 보존)**: 알고리즘 $i$가 $\text{KB}$로부터 도출한 모든 문장 $\alpha$는 실제로 $\text{KB}$가 함의하는 참인 문장이다 ($\text{KB} \vdash_i \alpha \Rightarrow \text{KB} \models \alpha$). 즉, 거짓 결론을 만들어내지 않는다.
- **완전성 (Completeness)**: $\text{KB}$가 함의하는 모든 문장 $\alpha$를 알고리즘 $i$가 빠짐없이 도출해 낼 수 있다 ($\text{KB} \models \alpha \Rightarrow \text{KB} \vdash_i \alpha$).
</details>

**Q16. [단답·개념 설명]** 문장의 **타당성(Validity)** 과 **충족 가능성(Satisfiability)** 을 정의하고, 각각을 이용해 $\text{KB} \models \alpha$를 판정하는 방법을 쓰시오.

<details><summary>▶ 모범 답안 보기</summary>

- **타당성 (Validity / 항진명제)**: 문장이 **모든 모델에서 참** 인 성질. $\text{KB} \models \alpha$일 필요충분조건은 **$(\text{KB} \Rightarrow \alpha)$가 타당(valid)** 한 것이다 (연역 정리).
- **충족 가능성 (Satisfiability)**: 문장이 참이 되는 모델이 **적어도 하나 존재** 하는 성질. $\text{KB} \models \alpha$일 필요충분조건은 **$(\text{KB} \land \lnot\alpha)$가 충족 불가능(unsatisfiable, 모순)** 한 것이다 (귀류법 / 도출 반박의 원리).
</details>

**Q17. [개념 설명]** 명제 논리(Propositional Logic)의 장점 4가지와 가장 치명적인 단점 1가지를 설명하시오. (`Ch.8 p.3`)

<details><summary>▶ 모범 답안 보기</summary>

- **장점 4가지**:
  1. **선언적(Declarative)**: 구문 조각이 세상의 사실에 대응한다.
  2. **부분·선언($\lor$)·부정($\lnot$) 정보 표현 가능**: 일반 데이터베이스와 달리 불완전한 정보도 다룬다.
  3. **합성적(Compositional)**: 복합 문장의 의미가 각 구성 문장의 의미로부터 합성된다.
  4. **문맥 독립적(Context-independent)**: 자연어와 달리 문맥에 따라 의미가 변하지 않는다.
- **치명적 단점**: **표현력(Expressive power)이 매우 제한적** 이다. 객체와 변수, 한정사가 없어서 "구덩이 인접 칸에는 바람이 분다" 같은 일반 규칙을 한 문장으로 쓸 수 없고 모든 칸마다 별도의 문장으로 중복 작성해야 한다.
</details>

---

### [Ch.8] 일차 논리 (First-Order Logic) (Q18 ~ Q24)

**Q18. [단답·개념 설명]** 일차 논리(FOL)에서 **존재론적 개입(Ontological Commitment)** 과 **인식론적 개입(Epistemological Commitment)** 이 각각 무엇인지 설명하시오. (`Ch.8 p.5`)

<details><summary>▶ 모범 답안 보기</summary>

- **존재론적 개입 (Ontological Commitment)**: 논리가 실제 세상에 무엇이 존재한다고 가정하는지를 뜻하며, 일차 논리는 세상에 **사실(`facts`), 객체(`objects`), 관계(`relations`, 함수 포함)** 가 존재한다고 가정한다.
- **인식론적 개입 (Epistemological Commitment)**: 에이전트가 문장에 대해 가질 수 있는 믿음의 상태를 뜻하며, 일차 논리는 명제 논리와 동일하게 **`true`(참) / `false`(거짓) / `unknown`(모름)** 의 3가지 상태를 가진다.
</details>

**Q19. [단답·개념 설명]** 일차 논리의 의미론에서 **해석(Interpretation)** 이 무엇인지 정의하고, 상수 기호·술어 기호·함수 기호가 각각 무엇에 매핑되는지 쓰시오. (`Ch.8 p.10`)

<details><summary>▶ 모범 답안 보기</summary>

- **해석(Interpretation)의 정의**: 논리식에 적힌 구문 기호(Syntax)들이 실제 세계(Model)의 어떤 지시 대상(Referent)을 가리키는지 짝지어 주는 규칙이다.
- **3가지 매핑**:
  1. **상수 기호 (Constant symbols)** $\rightarrow$ **객체 (Objects)**
  2. **술어 기호 (Predicate symbols)** $\rightarrow$ **관계 (Relations)** (참/거짓 판별 대상)
  3. **함수 기호 (Function symbols)** $\rightarrow$ **함수적 관계 (Functional relations)** (입력 객체에 대해 유일한 결과 객체를 반환)
</details>

**Q20. [개념 설명]** 전칭 한정사($\forall$)와 존재 한정사($\exists$)를 사용할 때 각각 어떤 논리 연결사와 짝지어 써야 하는지 쓰고, 반대로 썼을 때 발생하는 의미상의 오류를 예시와 함께 설명하시오. (`Ch.8 p.13`~`p.16`)

<details><summary>▶ 모범 답안 보기</summary>

1. **전칭 한정사($\forall$)는 함의($\Rightarrow$)와 결합**:
   - 예: $\forall x \; \text{At}(x, \text{D21}) \Rightarrow \text{Smart}(x)$ ("D21 강의실에 있는 모든 사람은 똑똑하다").
   - 만약 $\land$를 써서 $\forall x \; \text{At}(x, \text{D21}) \land \text{Smart}(x)$라고 쓰면 **"세상의 모든 개체가 D21에 있고 세상의 모든 개체가 똑똑하다"** 라는 지나치게 강한 뜻이 된다.
2. **존재 한정사($\exists$)는 논리곱($\land$)과 결합**:
   - 예: $\exists x \; \text{At}(x, \text{Stanford}) \land \text{Smart}(x)$ ("스탠퍼드에 있으면서 똑똑한 사람이 존재한다").
   - 만약 $\Rightarrow$를 써서 $\exists x \; \text{At}(x, \text{Stanford}) \Rightarrow \text{Smart}(x)$라고 쓰면, 가정($\text{At}(x, \text{Stanford})$)이 거짓인 대상(스탠퍼드에 없는 사람/사물)이 하나만 있어도 문장 전체가 무조건 참이 되는 오류가 발생한다.
</details>

**Q21. [개념 설명]** 일차 논리 지식베이스(KB)와 데이터베이스(DB)의 차이를 만드는 **데이터베이스 의미론의 3가지 기본 가정(UNA, CWA, DC)** 을 설명하고, 인터넷 환경에서의 추론에는 왜 이를 적용할 수 없는지 설명하시오. (`Ch.8 p.19`)

<details><summary>▶ 모범 답안 보기</summary>

- **데이터베이스의 3가지 기본 가정**:
  1. **UNA (Unique Names Assumption, 고유 이름 가정)**: 서로 다른 상수 기호는 무조건 서로 다른 객체를 가리킨다 ($\text{John} \neq \text{Geoffrey}$ 생략 가능).
  2. **CWA (Closed World Assumption, 닫힌 세계 가정)**: 참이라고 알려지지 않은(저장되지 않은) 원자 문장은 모두 거짓(`false`)이다.
  3. **DC (Domain Closure, 영역 폐쇄 가정)**: 상수 기호로 이름 붙여진 개체들 외에 추가적인 개체는 존재하지 않는다.
- **인터넷 추론에 적용할 수 없는 이유**: 인터넷(웹)에서는 하나의 대상을 여러 이름/URL로 부르고(UNA 위배), 웹페이지에 안 적힌 정보가 거짓이 아니라 미확인 상태이며(CWA 위배), 새로운 개체가 계속 생겨나므로(DC 위배) 열린 세계 가정(OWA)을 따르는 지식베이스 추론을 써야 한다.
</details>

**Q22. [단답·개념 설명]** 일차 논리에서 변화를 추적하는 **상황 미적분(Situation Calculus)** 의 핵심 요소 2가지를 쓰고, 행동 기술 시 발생하는 **프레임 문제(Frame Problem)** 와 그 해결책인 **후속 상태 공리(Successor-State Axiom)** 를 설명하시오. (`Ch.8 p.23`~`p.25`)

<details><summary>▶ 모범 답안 보기</summary>

- **상황 미적분의 핵심 요소**: ① 시간에 따라 변하는 술어에 **상황(Situation) 인자 $s$** 를 추가함, ② 상황 $s$에서 행동 $a$를 수행한 다음 상황을 **`Result(a, s)` 함수** 로 나타냄.
- **프레임 문제 (Frame Problem)**: 행동으로 변하는 속성은 극소수인데, **행동과 무관하여 변하지 않는(non-change) 수많은 속성들을 프레임 공리로 일일이 기술하고 매 단계 복사 추론해야 하는 비효율 문제**.
- **후속 상태 공리 (Successor-State Axiom)**: 행동마다 공리를 적는 대신 **술어 $P$마다** "행동 후 $P$가 참 $\Leftrightarrow$ [방금 행동이 $P$를 참으로 만들었거나 $\lor$ (원래 $P$가 참이었고 방금 행동이 $P$를 거짓으로 만들지 않음)]" 으로 묶어 표현상의 프레임 문제를 해결한다.
</details>

**Q23. [단답형]** 일차 논리에서 지식 공학(Knowledge Engineering)을 수행할 때, 도메인 개념들을 술어·함수·상수 등의 논리 어휘(Vocabulary)로 결정·번역한 결과물을 무엇이라 하는가? (`Ch.8 p.26`)

<details><summary>▶ 모범 답안 보기</summary>

**온톨로지 (Ontology)**
</details>

---

### [제4장] 전문가 시스템 (Expert Systems) (Q24 ~ Q29)

**Q24. [단답·개념 설명]** 전문가 시스템(Expert System)의 정의와 3대 구성 요소를 쓰고, 초기 대표 의료 전문가 시스템의 이름을 쓰시오. (`제4장 p.5`~`p.7`)

<details><summary>▶ 모범 답안 보기</summary>

- **정의**: 특정 전문 영역에서 인간 전문가의 지식을 규칙(`IF-THEN`)으로 담아 전문가의 의사결정 능력을 흉내 내는 컴퓨터 시스템.
- **3대 구성 요소**: ① **지식 베이스(Knowledge Base)**, ② **추론 엔진(Inference Engine)**, ③ **사용자 인터페이스(User Interface)**.
- **초기 대표 의료 전문가 시스템**: **MYCIN (마이신)** (박테리아 감염 진단 및 항생제 처방).
</details>

**Q25. [단답·개념 설명]** 전문가 시스템에서 **장기 기억장치(Long-Term Memory)** 와 **단기 기억장치(Short-Term Memory)** 에 각각 무엇이 저장되는지 쓰고, 추론 엔진이 이 둘을 어떻게 사용해 추론하는지 설명하시오. (`제4장 p.15`~`p.17`)

<details><summary>▶ 모범 답안 보기</summary>

- **장기 기억장치**: 도메인 전문가의 노하우인 **규칙(Rules, `IF A THEN B`)** 이 저장된다 (= 지식 베이스).
- **단기 기억장치**: 현재 문제의 초기 관측 데이터와 추론으로 도출된 **사실(Facts, `A가 참이다`)** 이 저장된다 (= 작업 기억).
- **추론 과정**: 추론 엔진은 단기 기억장치의 **사실** 들과 장기 기억장치 규칙의 **`IF` 전제(Antecedent)** 를 매칭하여, 조건이 맞으면 규칙을 점화(fire)시켜 **`THEN` 결과(Consequent)** 를 단기 기억장치의 새로운 사실로 추가한다.
</details>

**Q26. [개념 설명]** 전문가 시스템의 **순방향 추론(Forward Chaining)** 과 **역방향 추론(Backward Chaining)** 의 동작 원리와 장단점을 비교 설명하시오. (`제4장 p.18`~`p.24`, `Ch.8 p.27` 필기)

<details><summary>▶ 모범 답안 보기</summary>

1. **순방향 추론 (Forward Chaining)**:
   - **원리**: 단기 기억에 알려진 **사실(Facts)** 들로부터 출발하여 조건(`IF`)이 충족되는 규칙들을 차례로 점화해 최종 결론을 이끌어내는 방식.
   - **단점**: 입력된 사실을 바탕으로 자연스럽게 진행되지만, **최종 목표와 관련 없는 규칙들까지 모두 점화** 되어 비효율적일 수 있다.
2. **역방향 추론 (Backward Chaining)**:
   - **원리**: 확인하고자 하는 **목표(Goal, 결과)** 를 먼저 설정하고, 그 목표를 결론(`THEN`)으로 갖는 규칙을 찾아 전제 조건(`IF`)을 하위 목표로 삼아 사실 데이터가 이를 뒷받침하는지 역추적하는 방식.
   - **장점**: **목표 증명에 필요한 규칙만 선택적으로 검사하므로 순방향 추론보다 더 효율적** 이라는 평가를 받는다.
</details>

**Q27. [단답·개념 설명]** 전문가 시스템에서 동일한 사실에 대해 상반된 결론을 내리는 여러 규칙이 동시에 만족될 때 이를 해결하는 **충돌 해법(Conflict Resolution) 3가지** 를 설명하시오. (`제4장 p.27`~`p.28`)

<details><summary>▶ 모범 답안 보기</summary>

1. **우선순위(Priority) 방식**: 각 규칙에 중요도/우선순위 점수를 부여하고 가장 높은 우선순위를 가진 규칙을 점화한다.
2. **특수성(Specificity) 우선 방식**: 조건절(`IF`)에 더 많은 조건이 결합되어 **가장 구체적이고 특수한 상황을 다루는 규칙** 을 먼저 점화한다.
3. **최신성(Recency) 우선 방식**: 단기 기억장치에 **가장 최근에 입력(또는 도출)된 사실 데이터** 를 조건으로 사용하는 규칙을 먼저 점화한다.
</details>

**Q28. [개념 설명]** 전문가 시스템의 장점 2가지와 단점 3가지를 쓰시오. (`제4장 p.29`)

<details><summary>▶ 모범 답안 보기</summary>

- **장점 2가지**:
  1. `IF-THEN` 규칙은 인간 전문가의 지식을 표현하는 직관적이고 자연스러운 방법이다.
  2. **지식 베이스와 추론 엔진이 분리** 되어 있어, 지식 베이스만 바꾸면 다른 도메인 영역에도 쉽게 적용할 수 있다.
- **단점 3가지**:
  1. 스스로 **지식을 학습(Learning)할 수 없다** (수동 규칙 입력 필요).
  2. 규칙과 사실이 많아지면 **탐색이 비효율적** 이다.
  3. 규칙의 개수가 많아지면 규칙 간 충돌 등으로 **유지보수하기가 매우 어렵다**.
</details>

---

### [Ch.10 (제5장)] 지식 표현 (`p.21` 시맨틱 네트워크까지) (Q29 ~ Q35)

**Q29. [단답·개념 설명]** 온톨로지(Ontology)란 무엇인지 정의하고, 대규모 온톨로지를 구축하는 4가지 대표 방식(프로젝트명 포함)을 쓰시오. (`Ch.10 p.3`)

<details><summary>▶ 모범 답안 보기</summary>

- **온톨로지의 정의**: 현실 세계의 특정 영역에 대한 **어휘(Vocabulary)와 이론(Theory)** 으로 지식을 표현하는 체계.
- **4가지 구축 방식과 대표 프로젝트**:
  1. 훈련된 온톨로지 전문가 팀이 직접 구축 — **CYC**
  2. 데이터베이스(위키피디아 등)로부터 개념을 임포트 — **DBpedia**
  3. 텍스트 문서로부터 정보를 자동 추출 — **ReVerb**
  4. 일반 대중 누구나 상식 지식을 입력하도록 초대(크라우드소싱) — **OpenMind**
</details>

**Q30. [단답·개념 설명]** 일차 논리에서 범주(Category)나 사건(Event)을 표현할 때 사용하는 **실체화(Reification)** 란 무엇이며, 어떤 이점이 있는지 설명하시오. (`Ch.10 p.4`, `p.21`)

<details><summary>▶ 모범 답안 보기</summary>

- **실체화 (Reification)의 정의**: 원래 술어(명제)나 사건이었던 것을 **하나의 독립된 '객체(Object)'로 변환** 하는 기법 (`turning a proposition into an object`).
- **이점**:
  1. 범주(`Basketball(b)`)를 집합 객체(`Basketballs`)로 실체화하면, $b \in \text{Basketballs}$뿐만 아니라 $\text{Basketballs} \subset \text{Balls}$처럼 **범주 자체를 인자로 넣어 분류 계층(부분집합 관계)이나 범주 전체의 속성을 표현** 할 수 있다.
  2. 사건(`Fly(...)`)을 사건 인스턴스 객체(`Fly_17`)로 실체화하면, 시맨틱 네트워크처럼 **이항 관계만 지원하는 구조에서도 다항 사건의 각 역할(`Agent`, `Origin`, `Destination`, `During`)을 자유롭게 연결** 할 수 있다.
</details>

**Q31. [개념 설명]** 범주들의 분류 계층(`Taxonomical hierarchy`)에서 인스턴스 관계(`is-a`)와 부분집합 관계(`Subset`)를 구분하고, 하위 범주가 아닌 관계인 **`Disjoint`**, **`ExhaustiveDecomposition`**, **`Partition`** 을 각각 설명하시오. (`Ch.10 p.5`~`p.6`)

<details><summary>▶ 모범 답안 보기</summary>

- **인스턴스 관계(`is-a`, $\in / \text{Member}$)** 와 **부분집합 관계(`Subset`, $\subset$)**: 인스턴스 관계는 **개별 원소** 가 범주에 속함($b \in \text{Basketballs}$)을 뜻하고, 부분집합 관계는 **하위 범주 전체** 가 상위 범주에 포함됨($\text{Basketballs} \subset \text{Balls}$)을 뜻하며 상위 속성의 **상속(Inheritance)** 을 가능하게 한다.
- **비하위 범주 관계 3가지**:
  1. **`Disjoint(s)` (서로소)**: 범주 집합 $s$에 속한 범주들이 서로 겹치는 공통 원소가 전혀 없다.
  2. **`ExhaustiveDecomposition(s, c)` (완전 분해)**: 상위 범주 $c$의 모든 원소가 $s$의 하위 범주 중 적어도 하나에 속한다(빠짐없음).
  3. **`Partition(s, c)` (분할)**: `Disjoint(s)`이면서 동시에 `ExhaustiveDecomposition(s, c)`인 관계, 즉 상위 범주 $c$를 겹치지도 않고 빠짐도 없이 분할한 것이다.
</details>

**Q32. [단답·개념 설명]** 복합 객체에서 부분-전체 관계를 나타내는 `PartOf`의 두 가지 수학적 성질(추이성·반사성)을 쓰고, 추상적 집합(`Set`)과 구별되는 **`Bunch`(다발)** 의 개념을 설명하시오. (`Ch.10 p.7`~`p.8`)

<details><summary>▶ 모범 답안 보기</summary>

- **`PartOf`의 성질**:
  1. **추이성 (Transitive)**: $\text{PartOf}(x, y) \land \text{PartOf}(y, z) \Rightarrow \text{PartOf}(x, z)$
  2. **반사성 (Reflexive)**: $\text{PartOf}(x, x)$
- **`Bunch` (다발)**: 확정된 부분(`parts`)들로 구성되어 있으나 **특정한 구조(structure)는 없는 물리적 복합 객체** 이다 (예: $\text{BunchOf}(\text{Apple}_1, \text{Apple}_2, \text{Apple}_3)$). 수학적 집합(`Set`)은 추상적 객체라 무게나 부피가 없지만, `Bunch`는 사과들을 원소가 아닌 물리적 부품(`PartOf`)으로 묶은 가장 작은 복합 객체(논리적 최소화)이므로 "사과 다발의 무게가 2파운드다" 같은 물리적 속성을 부여할 수 있다.
</details>

**Q33. [개념 설명]** 상황 미적분(Situation Calculus)의 한계를 극복하기 위해 등장한 **사건 미적분(Event Calculus)** 의 특징과 6가지 기본 술어를 설명하시오. (`Ch.10 p.11`~`p.13`)

<details><summary>▶ 모범 답안 보기</summary>

- **특징 (도입 이유)**: 상황 미적분은 이산적 행동 전후만 다룰 수 있어 **연속적인 행동 도중(during the action)에 무슨 일이 일어나는지** 와 **동시에 여러 행동이 일어나는 상황** 을 표현할 수 없다. 사건 미적분은 시점($t$)과 시간 구간($i$)을 도입하여 사건이 특정 시간 구간 동안 발생하고 유동체(상태, $f$)를 작동(`Initiates`)시키거나 종료(`Terminates`)시키는 것으로 변화를 표현한다.
- **6가지 기본 술어**:
  1. **$T(f, t)$**: 유동체 $f$가 시각 $t$에 참이다.
  2. **$\text{Happens}(e, i)$**: 사건 $e$가 시간 구간 $i$ 동안 발생한다.
  3. **$\text{Initiates}(e, f, t)$**: 사건 $e$가 시각 $t$에 유동체 $f$를 참이 되도록 시작시킨다.
  4. **$\text{Terminates}(e, f, t)$**: 사건 $e$가 시각 $t$에 유동체 $f$를 거짓이 되도록 종료시킨다.
  5. **$\text{Clipped}(f, i)$**: 시간 구간 $i$ 도중 어떤 사건에 의해 $f$가 종료되어 끊겼다.
  6. **$\text{Restored}(f, i)$**: 시간 구간 $i$ 도중 어떤 사건에 의해 $f$가 다시 시작되어 복구되었다.
</details>

**Q34. [단답·개념 설명]** 사건 미적분에서 **이산 사건(Discrete Events)** 과 **프로세스(Processes / Liquid Events)** 의 차이를 설명하고, 시간 구간 술어 중 **$\text{Meet}(i, j)$** 와 상태 **유동체(State Fluent)** 의 의미를 쓰시오. (`Ch.10 p.15`~`p.19`)

<details><summary>▶ 모범 답안 보기</summary>

- **이산 사건 vs 프로세스**: 이산 사건(예: 여행 전체)은 시작·중간·끝이 있어 도중에 자르면 원래 사건이 아니지만, **프로세스(예: `Flyings` 비행 중)** 는 어떤 시간 구간 동안 일어나면 **그 안의 임의의 작은 부분 구간(subinterval) 동안에도 여전히 같은 프로세스가 성립** 한다 (물리적 객체의 `Things` vs `Stuff` 구분과 동일).
- **$\text{Meet}(i, j)$**: $\text{End}(i) = \text{Begin}(j)$, 즉 **시간 구간 $i$가 끝나자마자 바로 이어서 구간 $j$가 시작** 되는 관계.
- **상태 유동체 (State Fluent)**: 물리적 실체(예: `USA`)와 대비되는 개념으로, **`President(USA)`** 처럼 **시간에 따라 가리키는 값이나 인물 객체(워싱턴 $\rightarrow$ 애덤스 $\rightarrow$ 제퍼슨)가 바뀌는 상태 객체** 를 뜻한다.
</details>

**Q35. [개념 설명]** **시맨틱 네트워크(Semantic Networks)** 에서 ① 속성 **상속(Inheritance)** 과 **오버라이딩(Overriding)** 이 어떻게 작동하는지 `Persons`/`John`의 다리 개수(`Legs`) 예제로 설명하고, ② `Fly(Shankar, NewYork, NewDelhi, Yesterday)`를 시맨틱 네트워크로 표현하는 원리를 설명하시오. (`Ch.10 p.20`~`p.21`)

<details><summary>▶ 모범 답안 보기</summary>

1. **상속(Inheritance)과 오버라이딩(Overriding)**:
   - 상위 범주인 `Persons` 노드에 기본값으로 `Legs → 2`가 지정되어 있으면, 하위 범주(`FemalePersons`)의 원소인 `Mary`는 별도 지정 없이도 `SubsetOf`와 `MemberOf` 링크를 따라 **다리가 2개라는 기본값을 자동으로 상속** 받는다.
   - 반면 `John` 노드에 직접 `Legs → 1` 링크가 연결되어 있으면, 더 구체적인 자신만의 속성값이 상위 범주(`Persons`)의 기본값(`2`)을 **재정의(Overriding)** 하여 다리가 1개인 것으로 추론한다 ($\forall x \; x \in \text{Persons} \land x \neq \text{John} \Rightarrow \text{Legs}(x, 2)$).
2. **`Fly(Shankar, NewYork, NewDelhi, Yesterday)`의 표현 원리**:
   - 시맨틱 네트워크의 화살표는 두 노드만 잇는 이항 관계만 표현할 수 있으므로, 4항 관계인 비행 사건 자체를 **`Fly_17`이라는 사건 인스턴스(객체) 노드로 실체화(Reification)** 한다.
   - 그 뒤 `Fly_17` 노드에서 `FlyEvents`(`MemberOf`), `Shankar`(`Agent`), `NewYork`(`Origin`), `NewDelhi`(`Destination`), `Yesterday`(`During`)로 향하는 이항 링크들을 연결하여 표현한다.
</details>

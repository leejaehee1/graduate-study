# Chapter 3. 탐색을 통한 문제 해결 (Solving Problems by Searching)

> 인공지능 3번째 강의 정리 노트
> 원본: `AI-ch03.pdf` (Russell & Norvig, *Artificial Intelligence: A Modern Approach* 3장 기반)
>
> *"한 번의 행동으로는 목표를 이룰 수 없을 때, 에이전트가 목표를 달성하는 **행동의 시퀀스**를 어떻게 찾는지 살펴본다."*

---

## 📌 목차

0. [2장과의 연결: 왜 탐색인가?](#0-2장과의-연결-왜-탐색인가)
1. [문제 해결 에이전트 (Problem-solving Agents)](#1-문제-해결-에이전트-problem-solving-agents)
2. [문제 정의 (Problem Formulation)](#2-문제-정의-problem-formulation)
3. [트리 탐색과 탐색 전략의 평가 기준](#3-트리-탐색과-탐색-전략의-평가-기준)
4. [무정보 탐색 (Uninformed Search)](#4-무정보-탐색-uninformed-search)
5. [정보 탐색 / 휴리스틱 탐색 (Informed Search)](#5-정보-탐색--휴리스틱-탐색-informed-search)
6. [요약](#6-요약-summary)
7. [셀프 체크 퀴즈](#7-셀프-체크-퀴즈)
8. [부록: Python 실습 코드](#8-부록-python-실습-코드)

> 📝 표기: **[보충]** 이 붙은 내용은 슬라이드에 없지만 이해를 돕거나 교재에서 가져온 설명이다.

---

## 0. 2장과의 연결: 왜 탐색인가?

2장에서 배운 에이전트 유형 중 **목표 기반 에이전트(goal-based agent)** 를 떠올려 보자.

- 단순 반사 에이전트는 "지금 이 상황이면 이 행동"만 안다.
- 목표 기반 에이전트는 "**행동 A를 하면 어떻게 될까?**"를 예측해서 목표에 도달하는 행동을 고른다.
- 그런데 목표가 **한 번의 행동으로는 도달할 수 없을 만큼 멀리** 있다면? → 여러 행동을 **미리 머릿속에서 이어 붙여 보는 것**, 이것이 바로 **탐색(search)** 이다.

이 장에서 다루는 에이전트는 **문제 해결 에이전트(problem-solving agent)** 로, 목표 기반 에이전트의 한 종류다.

---

## 1. 문제 해결 에이전트 (Problem-solving Agents)

### 1.1 대표 예제: 루마니아 여행 🇷🇴

> 루마니아에서 휴가 중이고, 지금 **Arad**에 있다. 내일 **Bucharest**에서 비행기가 출발한다.

문제 해결 에이전트는 다음 순서로 생각한다.

| 단계 | 내용 | 루마니아 예 |
|---|---|---|
| ① **목표 설정** (Formulate goal) | 무엇을 이루고 싶은가 | Bucharest에 도착하기 |
| ② **문제 정의** (Formulate problem) | 어떤 상태·행동을 고려할까 (**추상화 수준**, granularity 결정) | 상태 = 여러 도시, 행동 = 도시 간 운전 |
| ③ **해 탐색** (Find solution) | 목표에 이르는 행동 시퀀스 찾기 | Arad → Sibiu → Fagaras → Bucharest |
| ④ **실행** (Execute) | 찾은 행동을 차례로 수행 | 실제로 운전 |

> 💡 **"granularity(세분화 수준)"** 란? 행동을 "핸들을 3도 돌린다" 수준으로 볼지, "Arad에서 Sibiu로 간다" 수준으로 볼지 정하는 것. 너무 세밀하면 탐색이 불가능할 만큼 커지고, 너무 거칠면 실행할 수 없는 계획이 된다.

### 1.2 루마니아 지도 (도로 거리, km)

```
                    Oradea
                 71 /     \ 151
               Zerind       \          Neamt
            75 /             \           | 87
          Arad ──── 140 ──── Sibiu ─ 99 ─ Fagaras       Iasi
          |                   |             \             | 92
      118 |                80 |              \ 211       Vaslui
          |            Rimnicu Vilcea         \           | 142
      Timisoara               |  \ 97          \          |
          |               146 |   Pitesti ─101─ Bucharest ─85─ Urziceni ─98─ Hirsova
      111 |                   |  / 138          | 90                           | 86
        Lugoj                Craiova          Giurgiu                       Eforie
          | 70                |
       Mehadia ── 75 ── Drobeta ─ 120 ─┘
```

> 위 그림은 대략적인 배치다. 연결 관계와 거리는 아래 표를 기준으로 보자.

**도로 목록 (정확한 값)**

| 도로 | 거리 | 도로 | 거리 | 도로 | 거리 |
|---|---|---|---|---|---|
| Arad–Zerind | 75 | Arad–Sibiu | 140 | Arad–Timisoara | 118 |
| Zerind–Oradea | 71 | Oradea–Sibiu | 151 | Timisoara–Lugoj | 111 |
| Lugoj–Mehadia | 70 | Mehadia–Drobeta | 75 | Drobeta–Craiova | 120 |
| Craiova–Rimnicu Vilcea | 146 | Craiova–Pitesti | 138 | Sibiu–Fagaras | 99 |
| Sibiu–Rimnicu Vilcea | 80 | Rimnicu Vilcea–Pitesti | 97 | Fagaras–Bucharest | 211 |
| Pitesti–Bucharest | 101 | Bucharest–Giurgiu | 90 | Bucharest–Urziceni | 85 |
| Urziceni–Hirsova | 98 | Hirsova–Eforie | 86 | Urziceni–Vaslui | 142 |
| Vaslui–Iasi | 92 | Iasi–Neamt | 87 | | |

> 이 지도는 이 장 전체에서 계속 쓰이므로 **Arad → Bucharest** 경로 두 개는 외워 두자.
> - Arad → Sibiu → Fagaras → Bucharest = 140 + 99 + 211 = **450**
> - Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest = 140 + 80 + 97 + 101 = **418** ← **최적**

### 1.3 이 장에서 가정하는 환경의 성질

2장의 환경 분류를 다시 사용한다. 이 장의 탐색은 **가장 쉬운 환경**을 가정한다.

| 성질 | 의미 | 왜 필요한가 |
|---|---|---|
| **관측 가능 (observable)** | 에이전트가 항상 현재 상태를 앎 | 출발점을 알아야 계획을 세움 |
| **이산 (discrete)** | 어느 상태에서든 선택할 수 있는 행동이 **유한** | 행동을 하나씩 나열해 볼 수 있음 |
| **알려진 (known)** | 각 행동이 어떤 상태로 이어지는지 앎 | 머릿속 시뮬레이션이 가능 |
| **결정적 (deterministic)** | 각 행동의 결과가 **정확히 하나** | 계획이 실행 중에 어긋나지 않음 |

> 💡 이 가정이 모두 성립하면 해답은 **고정된 행동 시퀀스**이고, 실행 중에 인지(percept)를 볼 필요도 없다. 눈을 감고 실행해도 된다 → 이를 **개루프(open-loop)** 시스템이라 한다. **[보충]**

### 1.4 문제의 유형 (Problem Types)

환경 가정이 깨지면 문제의 성격이 달라진다.

| 환경 | 문제 유형 | 에이전트가 아는 것 | 해답의 형태 |
|---|---|---|---|
| 결정적 + 완전 관측 | **단일 상태 문제** (single-state) | 자신이 어느 상태에 있게 될지 **정확히** 앎 | 행동 **시퀀스** |
| 관측 불가 (센서 없음) | **순응 문제** (conformant, sensorless) | 자신이 어디 있는지 **모를 수도** 있음 | 행동 **시퀀스** (있다면) |
| 비결정적 그리고/또는 부분 관측 | **우발 상황 문제** (contingency) | 인지가 현재 상태에 대한 **새 정보**를 줌 | **조건부 계획** (contingent plan) 또는 **정책** (policy) |
| 상태 공간 자체를 모름 | **탐험 문제** (exploration, "online") | 거의 모름 | 직접 돌아다니며 배워야 함 |

- **우발 상황 문제**에서는 **탐색과 실행을 번갈아(interleave)** 하는 경우가 많다.
  - 예: Arad → Sibiu → Rimnicu Vilcea로 갈 계획이지만, 실수로 Sibiu 대신 **Zerind에 도착한 경우**에 대비한 **비상 계획**도 필요할 수 있다.

### 1.5 예제: 진공청소기 세계의 세 가지 문제 유형

진공청소기 세계의 상태는 **8가지**다 (로봇 위치 2가지 × 칸 A의 먼지 유무 2가지 × 칸 B의 먼지 유무 2가지 = 2 × 2² = 8).

```
 상태 번호    [ A칸 | B칸 ]      (🤖 = 로봇 위치, 💩 = 먼지)
    1        [🤖💩 |  💩 ]
    2        [  💩 |🤖💩 ]
    3        [🤖💩 |     ]
    4        [  💩 |🤖   ]
    5        [🤖   |  💩 ]
    6        [     |🤖💩 ]
    7        [🤖   |     ]      ← 목표 상태
    8        [     |🤖   ]      ← 목표 상태
```

**① 단일 상태 문제: #5에서 시작**
- 로봇은 A에 있고 A는 깨끗, B는 더러움. 모든 것을 앎.
- 해: **`[Right, Suck]`** → #6 → #8 (목표)

**② 순응 문제: {1,2,3,4,5,6,7,8} 중 어디서 시작하는지 모름** (센서 없음)
- 에이전트는 "**믿음 상태**(belief state, 가능한 상태들의 집합)" 위에서 추론한다.
- `Right`를 하면 어디서 시작했든 로봇은 B에 있게 됨 → {2, 4, 6, 8}
- 해: **`[Right, Suck, Left, Suck]`**
  - Right → {2,4,6,8} → Suck → {4,8} → Left → {3,7} → Suck → {7} ✅
- 💡 센서가 없어도 상태 집합을 **좁혀 가는** 행동 시퀀스로 목표에 도달할 수 있다.

**③ 우발 상황 문제: #5에서 시작**
- **머피의 법칙**: 깨끗한 카펫에서 `Suck`을 하면 오히려 **더러워질 수 있음** (비결정적)
- **국지적 감지**: 현재 칸의 먼지와 위치만 감지 가능 (부분 관측)
- 해: **`[Right, if dirt then Suck]`**
  - 고정된 시퀀스가 아니라 **인지에 따라 분기하는 조건부 계획**이 필요하다.

---

## 2. 문제 정의 (Problem Formulation)

### 2.1 단일 상태 문제의 5요소 ⭐⭐

**문제(problem)** 는 다음 **5가지 요소**로 정의된다. 시험에 매우 자주 나온다.

| # | 요소 | 설명 | 루마니아 예 |
|---|---|---|---|
| 1 | **초기 상태** (initial state) | 에이전트가 시작하는 상태 | `In(Arad)` |
| 2 | **행동** (actions) | `ACTIONS(s)`: 상태 $s$에서 **적용 가능한** 행동들의 집합 | `ACTIONS(In(Arad))` = {`Go(Sibiu)`, `Go(Timisoara)`, `Go(Zerind)`} |
| 3 | **전이 모델** (transition model) | `RESULT(s, a)`: 상태 $s$에서 행동 $a$를 하면 도달하는 상태 (**후속 함수**, successor function) | `RESULT(In(Arad), Go(Zerind))` = `In(Zerind)` |
| 4 | **목표 검사** (goal test) | 주어진 상태가 목표인지 판별 | 명시적: $x$ = "Bucharest에 있음" / 암묵적: $x$ = 체크메이트 |
| 5 | **경로 비용** (path cost) | 경로에 비용을 매기는 함수 (**가산적**, additive). 에이전트의 성능 척도를 반영 | 거리의 합, 수행한 행동 수 등 |

- **단계 비용(step cost)**: $c(s, a, s')$ — 상태 $s$에서 행동 $a$로 $s'$에 갈 때의 비용. **$c(s, a, s') \ge 0$ 으로 가정**
- 경로 비용 = 경로를 이루는 단계 비용들의 **합**

$$
\text{path cost} = \sum_{i} c(s_i, a_i, s_{i+1})
$$

- **해(solution)**: 초기 상태에서 목표 상태로 이어지는 **행동의 시퀀스**
- **최적해(optimal solution)**: 모든 해 중 **경로 비용이 가장 낮은** 해 **[보충]**

**목표 검사의 명시적 vs 암묵적**

| 구분 | 의미 | 예 |
|---|---|---|
| 명시적 (explicit) | 목표 상태를 **직접 나열**할 수 있음 | "Bucharest에 있다" |
| 암묵적 (implicit) | 목표 상태가 만족해야 할 **성질**만 알고 있음 | 체스의 "체크메이트" — 해당하는 판 배치가 너무 많아 나열 불가 |

> 💡 **상태 공간(state space)** **[보충]**: 초기 상태 + 행동 + 전이 모델이 합쳐지면 "초기 상태에서 도달 가능한 모든 상태"와 그 연결 관계가 정해진다. 이를 **그래프**로 볼 수 있다 (노드 = 상태, 간선 = 행동). 루마니아 지도 자체가 상태 공간 그래프다.

### 2.2 상태 공간의 선택: 추상화 (Abstraction)

실제 세계는 **터무니없이 복잡**하다 → 문제를 풀려면 상태 공간을 **추상화**해야 한다.

| 추상적인 것 | 실제로 의미하는 것 |
|---|---|
| (추상) **상태** | 실제 상태들의 **집합** — "Arad에 있음" = 동승자, 라디오, 날씨, 창밖 풍경 등은 무시 |
| (추상) **행동** | 실제 행동들의 **복잡한 조합** — "Arad → Zerind" = 가능한 여러 경로, 우회로, 휴게소 정차 등 |
| (추상) **해** | 실제 세계에서 해가 되는 **실제 경로들의 집합** |

**좋은 추상화의 조건**

1. **실현 가능성 보장 (guaranteed realizability)**: "Arad에 있는" **어떤** 실제 상태에서 출발하더라도, "Zerind에 있는" **어떤** 실제 상태에 도달할 수 있어야 한다.
2. 각 추상 행동은 **원래 문제보다 "쉬워야" 한다**. ("Arad → Zerind 운전하기"는 사람 운전자가 추가 계획 없이 할 수 있어야 함)

> 💡 **정리**: 추상화는 **유효해야 하고(valid, 실제로 실행 가능)** 동시에 **유용해야 한다(useful, 문제를 쉽게 만듦)**.

### 2.3 예제: 진공청소기 세계의 상태 공간 그래프

```
        R →                     R →
   (1) ⇄ (2)               (3) ⇄ (4)
        ← L                     ← L
    │S    │S                │S    │S
    ▼     └──────▶ (4)      ▼     ↺ (제자리)
   (5) ⇄ (6)               (7) ⇄ (8)
         │S                 ↺S    ↺S
         ▼
        (8)
```

**전이 모델 표** (1.5절의 상태 번호 사용. 벽 쪽으로 이동하거나 깨끗한 칸에서 `Suck`을 하면 제자리)

| 상태 | `Left` | `Right` | `Suck` |
|---|---|---|---|
| 1 `[🤖💩\|💩]` | 1 | 2 | 5 |
| 2 `[💩\|🤖💩]` | 1 | 2 | 4 |
| 3 `[🤖💩\|  ]` | 3 | 4 | 7 |
| 4 `[💩\|🤖 ]` | 3 | 4 | 4 |
| 5 `[🤖 \|💩]` | 5 | 6 | 5 |
| 6 `[  \|🤖💩]` | 5 | 6 | 8 |
| 7 `[🤖 \|  ]` | 7 | 8 | 7 |
| 8 `[  \|🤖 ]` | 7 | 8 | 8 |

> 💡 이 표로 1.5절의 순응 문제 해 `[Right, Suck, Left, Suck]` 를 직접 따라가 보자: {1..8} → {2,4,6,8} → {4,8} → {3,7} → {7}

| 요소 | 정의 |
|---|---|
| **상태** | 먼지 위치와 로봇 위치 (정수값). 먼지의 **양** 등은 무시 → 총 $2 \times 2^2 = 8$ 상태 |
| **행동** | `Left`, `Right`, `Suck`, `NoOp` |
| **전이 모델** | 위 그래프 |
| **목표 검사** | 먼지가 하나도 없음 (상태 7, 8) |
| **경로 비용** | 행동 하나당 1 (`NoOp`은 0) |

**[보충] 진공청소기 세계 vs 실제 세계**
- 칸이 $n$개라면 상태 수는 $n \cdot 2^n$ → 칸 수에 대해 **지수적**으로 증가
- 실제 세계에는 먼지의 양, 가구, 사람, 배터리 등 무한히 많은 요소가 있지만 문제 풀이에 불필요한 것은 **추상화로 제거**한다.

---

## 3. 트리 탐색과 탐색 전략의 평가 기준

### 3.1 트리 탐색 알고리즘의 기본 아이디어

- **오프라인(offline)** 으로, 즉 실제로 움직이기 전에 머릿속에서 상태 공간을 **시뮬레이션하며 탐험**
- 이미 탐험한 상태의 **후속 상태(successor)** 를 생성해 나간다 → 이를 노드를 **확장(expanding)** 한다고 한다.

```
function TREE-SEARCH(problem, strategy) returns a solution, or failure
    initialize the search tree using the initial state of problem
    loop do
        if there are no candidates for expansion then return failure
        choose a leaf node for expansion according to strategy
        if the node contains a goal state then return the corresponding solution
        else expand the node and add the resulting nodes to the search tree
    end
```

**한 줄씩 해석**

1. 초기 상태 하나만 있는 **탐색 트리**로 시작
2. 확장할 후보(잎 노드)가 없으면 → **실패**
3. **전략(strategy)** 에 따라 확장할 잎 노드를 하나 **선택** ← 🎯 탐색 알고리즘마다 다른 유일한 부분!
4. 그 노드가 목표면 → 해를 반환
5. 아니면 → 확장해서 자식 노드들을 트리에 추가

> ⭐ **핵심**: 모든 탐색 알고리즘의 골격은 같다. **"어떤 노드를 먼저 확장하느냐"** 만 다르다.

**용어 정리**

| 용어 | 의미 |
|---|---|
| **노드 (node)** | 탐색 트리의 한 원소. 상태 + 부모 노드 + 행동 + 경로 비용 등을 담은 **자료구조** |
| **상태 (state)** | 세계의 구성(configuration). 노드와 다르다! 같은 상태가 여러 노드에 나타날 수 있음 |
| **확장 (expand)** | 노드에 모든 적용 가능한 행동을 적용해 자식 노드들을 **생성(generate)** 하는 것 |
| **프린지 / 프론티어 (fringe / frontier)** | 생성되었지만 **아직 확장되지 않은** 잎 노드들의 집합 |
| **탐험 집합 (explored set / closed list)** | 이미 확장한 상태들의 집합 (그래프 탐색에서 사용) |

**[보충] 노드의 구성** (슬라이드 p.22의 `CHILD-NODE` 함수)

```
function CHILD-NODE(problem, parent, action) returns a node
    return a node with
        STATE     = problem.RESULT(parent.STATE, action),
        PARENT    = parent,
        ACTION    = action,
        PATH-COST = parent.PATH-COST + problem.STEP-COST(parent.STATE, action)
```

- 부모 포인터(`PARENT`)를 따라 루트까지 거슬러 올라가면 **해 경로**를 복원할 수 있다.
- `PATH-COST`는 루트부터 이 노드까지의 비용, 보통 $g(n)$으로 표기한다.

### 3.2 트리 탐색 예제: Arad에서 출발

```
(a) 초기 상태                 Arad

(b) Arad 확장 후              Arad
                        ┌──────┼──────┐
                      Sibiu Timisoara Zerind

(c) Sibiu 확장 후             Arad
                        ┌──────┼──────┐
                      Sibiu Timisoara Zerind
                ┌──────┬┴─────┬──────┐
              Arad  Fagaras Oradea Rimnicu Vilcea
               ↑
         이미 방문한 Arad가 다시 등장!
```

> ⚠️ **반복 상태 문제**: Arad → Sibiu → **Arad** 처럼 **되돌아가는 경로(loopy path)** 가 생긴다. 트리 탐색은 이를 막지 못해서 **무한 루프**에 빠질 수 있다.
>
> 해결책 **[보충]**: **그래프 탐색(GRAPH-SEARCH)** — 이미 확장한 상태를 **탐험 집합(explored set)** 에 기억해 두고, 다시 나오면 추가하지 않는다. 슬라이드 p.22의 `BREADTH-FIRST-SEARCH`가 바로 이 방식이다.

### 3.3 탐색 전략의 평가 기준 ⭐⭐

**전략(strategy)** 은 **노드를 확장하는 순서**를 정한 것이다. 전략은 다음 4가지 기준으로 평가한다.

| 기준 | 질문 |
|---|---|
| **완전성 (completeness)** | 해가 존재한다면 **항상** 찾는가? |
| **시간 복잡도 (time complexity)** | 생성/확장하는 **노드의 수**는? |
| **공간 복잡도 (space complexity)** | 메모리에 동시에 저장하는 **최대 노드 수**는? |
| **최적성 (optimality)** | 항상 **비용이 가장 낮은** 해를 찾는가? |

시간·공간 복잡도는 다음 기호로 표현한다.

| 기호 | 의미 |
|---|---|
| $b$ | **최대 분기 계수** (branching factor): 한 노드가 가질 수 있는 최대 자식 수 |
| $d$ | **최소 비용 해의 깊이** (root → goal) |
| $m$ | 상태 공간에서 **임의의 경로의 최대 깊이** ($\infty$ 일 수도 있음) |

```
깊이 0:             ●                          1개
깊이 1:        ●    ●    ●                     b개
깊이 2:      ●●●  ●●●  ●●●                     b²개
  ⋮
깊이 d:   ....... 🎯 .......                   b^d개
```

> 💡 깊이 $d$ 까지의 노드 수는 $1 + b + b^2 + \cdots + b^d = O(b^d)$ — **지수적**으로 폭발한다.

**비용의 구분**

| 비용 | 의미 |
|---|---|
| **탐색 비용 (search cost)** | 해를 **찾는 데** 걸린 시간 (및 메모리) |
| **해 비용 (solution cost)** | 찾은 **경로 자체**의 비용 (예: 총 이동 거리) |
| **총 비용 (total cost)** | 탐색 비용 + 해 비용 |

> 💡 루마니아 예: 경로 길이 418km(해 비용)를 찾는 데 컴퓨터가 0.01초(탐색 비용)를 썼다. 두 값의 단위가 다르므로 합치려면 "1km = 몇 초"처럼 **환산 비율**이 필요하다. **[보충]**

---

## 4. 무정보 탐색 (Uninformed Search)

**무정보 탐색(uninformed / blind search)** 은 **문제 정의에 있는 정보만** 사용한다. 즉, 어느 상태가 목표에 "더 가까워 보이는지" 전혀 모른다. 목표 상태와 아닌 상태를 구분하는 것만 할 수 있다.

| 전략 | 확장 순서 | 프린지 자료구조 |
|---|---|---|
| 너비 우선 탐색 (BFS) | 가장 **얕은** 노드 먼저 | FIFO 큐 |
| 균일 비용 탐색 (UCS) | 경로 비용 $g(n)$이 **가장 낮은** 노드 먼저 | 우선순위 큐 ($g$ 기준) |
| 깊이 우선 탐색 (DFS) | 가장 **깊은** 노드 먼저 | LIFO 큐 (스택) |
| 깊이 제한 탐색 (DLS) | DFS + 깊이 제한 $l$ | 스택 / 재귀 |
| 반복 심화 탐색 (IDS) | DLS를 $l = 0, 1, 2, \ldots$ 로 반복 | 스택 / 재귀 |
| 양방향 탐색 | 시작과 목표 **양쪽에서** 동시에 | 두 개의 프린지 |

### 4.1 너비 우선 탐색 (Breadth-First Search, BFS)

- **아이디어**: 확장되지 않은 노드 중 **가장 얕은(shallowest)** 노드를 먼저 확장
- **구현**: 프린지 = **FIFO 큐** — 새 후속 노드는 **맨 뒤**에 들어감

**예제 트리** (슬라이드)

```
              A
           /     \
          B       C
         / \     / \
        D   E   F   G
```

| 단계 | 확장 | 프린지 (앞 → 뒤) |
|---|---|---|
| 0 | – | [A] |
| 1 | A | [B, C] |
| 2 | B | [C, D, E] |
| 3 | C | [D, E, F, G] |
| 4 | D | [E, F, G] |
| … | … | … |

**확장 순서: A → B → C → D → E → F → G** (층 단위로 훑음)

**그래프 탐색 버전 의사코드** (슬라이드 p.22)

```
function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    frontier ← a FIFO queue with node as the only element
    explored ← an empty set
    loop do
        if EMPTY?(frontier) then return failure
        node ← POP(frontier)          /* 프린지에서 가장 얕은 노드를 꺼냄 */
        add node.STATE to explored
        for each action in problem.ACTIONS(node.STATE) do
            child ← CHILD-NODE(problem, node, action)
            if child.STATE is not in explored or frontier then
                if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                frontier ← INSERT(child, frontier)
```

**포인트**
- `explored` 집합으로 **반복 상태를 제거**한다 (그래프 탐색).
- 목표 검사를 **노드를 생성할 때** 한다 (확장할 때가 아니라) → 한 층을 덜 만든다.

**BFS의 성질**

| 기준 | 결과 | 설명 |
|---|---|---|
| 완전성 | **예** ($b$가 유한하면) | 층 단위로 빠짐없이 훑으므로 언젠가 도달 |
| 시간 | $1 + b + b^2 + \cdots + b^d + b(b^d - 1) = O(b^{d+1})$ | 지수적 |
| 공간 | $O(b^{d+1})$ | **모든 노드를 메모리에 유지** ← 가장 큰 문제 |
| 최적성 | **예** (단계 비용이 모두 1일 때) / 일반적으로는 **아니오** | 가장 **얕은** 해 ≠ 가장 **싼** 해 |

> ⚠️ **시간 복잡도 표기 주의**
> 슬라이드의 식 $1 + b + \cdots + b^d + b(b^d - 1)$ 은 목표 검사를 **확장할 때** 하는 경우다. 깊이 $d$의 목표 노드를 확장하기 전에 깊이 $d$의 다른 노드들을 확장하면서 깊이 $d+1$의 노드까지 만들기 때문에 마지막 항 $b(b^d-1)$이 붙고, 전체는 $O(b^{d+1})$ 이 된다.
> 반면 p.22 의사코드처럼 **생성할 때** 목표 검사를 하면 $O(b^d)$ 가 된다. (교재 3판 기준) 두 경우를 구분해 기억하자.

**[보충] 왜 공간이 가장 큰 문제인가?** ($b = 10$, 노드 하나당 1KB, 초당 100만 노드 생성 가정)

| 깊이 $d$ | 노드 수 | 시간 | 메모리 |
|---|---|---|---|
| 2 | 110 | 0.11 ms | 107 KB |
| 6 | $10^6$ | 1.1 초 | 1 GB |
| 10 | $10^{10}$ | 3 시간 | 10 TB |
| 14 | $10^{14}$ | 3.5 년 | 99 PB |

→ 시간보다 **메모리가 먼저 바닥난다.**

**루마니아 예**: BFS는 **Arad → Sibiu → Fagaras → Bucharest (비용 450)** 을 찾는다. 행동 수(3개)로는 가장 짧지만, 거리로는 최적(418)이 **아니다**.

### 4.2 균일 비용 탐색 (Uniform-Cost Search, UCS)

- **아이디어**: **경로 비용 $g(n)$이 가장 낮은** 노드를 먼저 확장
- **구현**: 프린지 = 경로 비용 순으로 정렬된 큐 (**우선순위 큐**, 가장 낮은 것이 먼저)
- 모든 단계 비용이 같으면 **BFS와 동일**하다.

**[보충] BFS와 다른 두 가지 차이**
1. 목표 검사를 노드를 **확장할 때** 한다 (생성할 때가 아니라). 먼저 생성된 목표 노드가 나중에 발견되는 더 싼 경로보다 비쌀 수 있기 때문이다.
2. 프린지에 있는 노드로 가는 **더 싼 경로**를 찾으면 교체한다.

**루마니아 예: Sibiu → Bucharest** (교재의 대표 예)

```
Sibiu ──80──▶ Rimnicu Vilcea ──97──▶ Pitesti ──101──▶ Bucharest   (합 278)
Sibiu ──99──▶ Fagaras ─────────211─────────────────▶ Bucharest   (합 310)
```

| 단계 | 확장 노드 ($g$) | 프린지 |
|---|---|---|
| 1 | Sibiu (0) | Rimnicu(80), Fagaras(99), … |
| 2 | Rimnicu Vilcea (80) | Fagaras(99), Pitesti(177), … |
| 3 | Fagaras (99) | Pitesti(177), **Bucharest(310)**, … ← 목표가 생성됐지만 아직 확장 안 함! |
| 4 | Pitesti (177) | **Bucharest(278)** ← 더 싼 경로로 교체 |
| 5 | Bucharest (278) | 확장 시점에 목표 검사 → **해 발견** ✅ |

> 💡 만약 BFS처럼 생성 시점에 목표 검사를 했다면 3단계에서 비용 310짜리 경로를 반환했을 것이다.

**UCS의 성질 [보충]**

| 기준 | 결과 |
|---|---|
| 완전성 | **예** (모든 단계 비용 $\ge \epsilon > 0$ 일 때) |
| 시간 | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ ($C^*$ = 최적해 비용) |
| 공간 | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ |
| 최적성 | **예** — $g(n)$ 순서로 확장하므로, 처음 확장되는 목표 노드가 최적 |

- 비용이 0인 행동이 무한히 반복되면(예: `NoOp` 루프) 영원히 끝나지 않을 수 있으므로 $\epsilon > 0$ 조건이 필요하다.
- **Arad → Bucharest**: UCS는 **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest (418)** 을 찾는다 ✅ 최적. 하지만 방향 감각 없이 모든 방향으로 퍼져 나가므로 13개 노드를 확장한다 (Zerind, Timisoara, Oradea, Lugoj 등 엉뚱한 방향까지).

### 4.3 깊이 우선 탐색 (Depth-First Search, DFS)

- **아이디어**: 확장되지 않은 노드 중 **가장 깊은(deepest)** 노드를 먼저 확장
- **구현**: 프린지 = **LIFO 큐 (스택)** — 새 후속 노드는 **맨 앞**에 들어감

**예제 트리** (슬라이드)

```
                    A
             /             \
          B                   C
        /   \               /   \
       D     E             F     G
      / \   / \           / \   / \
     H   I J   K         L   M N   O
```

**확장 순서: A → B → D → H → I → E → J → K → C → F → L → M → G → N → O**

- 왼쪽 가지를 **끝까지** 내려간 뒤, 막히면 되돌아와서(backtrack) 옆 가지로 간다.
- 끝까지 확장해서 자식이 없는 노드는 **메모리에서 제거**할 수 있다 → 공간 효율의 비결

**DFS의 성질**

| 기준 | 결과 | 설명 |
|---|---|---|
| 완전성 | **아니오** | **무한 깊이** 공간이나 **루프**가 있는 공간에서 실패 |
| | → 경로상의 반복 상태를 피하도록 수정하면 **유한 공간에서는 완전** | |
| 시간 | $O(b^m)$ | $m$이 $d$보다 훨씬 크면 **끔찍함**. 하지만 해가 **빽빽하게(dense)** 있으면 BFS보다 훨씬 빠를 수도 있음 |
| 공간 | $O(bm)$ | **선형 공간!** ← DFS의 가장 큰 장점 |
| 최적성 | **아니오** | 예: 위 트리에서 **J와 C가 모두 목표**라면, 더 얕은 C 대신 **J**를 반환 |

> 💡 **왜 공간이 $O(bm)$인가?** 현재 탐색 중인 **경로 하나**(최대 길이 $m$)와, 그 경로 위 각 노드의 **아직 탐색하지 않은 형제들**(각각 최대 $b$개)만 저장하면 된다.
> BFS 공간 $O(b^{d+1})$ vs DFS 공간 $O(bm)$: $b=10, d=m=12$ 이면 약 $10^{13}$ vs 120 !

**루마니아 예**: 이웃 순서에 따라 결과가 달라진다. 예컨대 Zerind를 먼저 보면 Arad → Zerind → Oradea → Sibiu → Fagaras → Bucharest (**607**) 처럼 최적과 거리가 먼 해를 찾는다.

### 4.4 깊이 제한 탐색 (Depth-Limited Search, DLS)

- **아이디어**: DFS에 **깊이 제한 $l$** 을 둔다. 깊이 $l$의 노드는 **후속 노드가 없는 것처럼** 취급
- DFS의 무한 경로 문제를 해결한다.
- 대신 새로운 문제가 생긴다.
  - $l < d$ → 해가 제한보다 깊으므로 **못 찾음** (불완전성의 새로운 원인)
  - $l > d$ → 더 깊은 곳의 해를 먼저 찾을 수 있음 (**비최적성**)

**재귀 구현**

```
function DEPTH-LIMITED-SEARCH(problem, limit) returns soln/fail/cutoff
    return RECURSIVE-DLS(MAKE-NODE(INITIAL-STATE[problem]), problem, limit)

function RECURSIVE-DLS(node, problem, limit) returns soln/fail/cutoff
    cutoff-occurred? ← false
    if GOAL-TEST(problem, STATE[node]) then return node
    else if DEPTH[node] = limit then return cutoff
    else for each successor in EXPAND(node, problem) do
        result ← RECURSIVE-DLS(successor, problem, limit)
        if result = cutoff then cutoff-occurred? ← true
        else if result ≠ failure then return result
    if cutoff-occurred? then return cutoff else return failure
```

**반환값 3가지의 차이** ⭐

| 반환값 | 의미 |
|---|---|
| `solution` | 해를 찾음 |
| `cutoff` | 깊이 제한 때문에 **잘린 가지가 있었음** → 제한을 늘리면 해가 있을 **수도** 있음 |
| `failure` | 제한과 관계없이 **해가 아예 없음** (모든 가지를 끝까지 봤음) |

> 💡 **[보충] 제한을 어떻게 정할까?** 문제 지식을 활용할 수 있다. 루마니아에는 도시가 20개 → 해가 있다면 길이는 최대 19 → $l = 19$. 더 나아가 지도를 보면 **어떤 도시에서든 9번 이내로 모든 도시에 갈 수 있다**(지름 = 9) → $l = 9$ 로 충분.

### 4.5 반복 심화 탐색 (Iterative Deepening Search, IDS) ⭐

```
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution
    inputs: problem, a problem
    for depth ← 0 to ∞ do
        result ← DEPTH-LIMITED-SEARCH(problem, depth)
        if result ≠ cutoff then return result
    end
```

- 깊이 제한을 **0, 1, 2, 3, …** 으로 늘려 가며 DLS를 반복한다.
- 적절한 $l$을 몰라도 되고, **BFS의 장점(완전·최적)** 과 **DFS의 장점(선형 공간)** 을 **모두** 가진다.

**예제 트리에서의 동작**

| 제한 $l$ | 확장(방문) 순서 |
|---|---|
| 0 | A |
| 1 | A, B, C |
| 2 | A, B, D, E, C, F, G |
| 3 | A, B, D, H, I, E, J, K, C, F, L, M, G, N, O |

> ❓ **"매번 처음부터 다시 하는 건 낭비 아닌가?"**
> 대부분의 노드는 **맨 아래층**에 있기 때문에 위층을 여러 번 다시 만드는 비용은 생각보다 작다.

**IDS의 성질**

| 기준 | 결과 |
|---|---|
| 완전성 | **예** |
| 시간 | $(d+1)b^0 + d\,b^1 + (d-1)b^2 + \cdots + 1 \cdot b^d = O(b^d)$ |
| 공간 | $O(bd)$ |
| 최적성 | **예** (단계 비용 = 1일 때). 균일 비용 트리를 탐색하도록 수정할 수도 있음 |

**시간 복잡도 식 해석**: 깊이 $i$에 있는 노드($b^i$개)는 제한이 $i, i+1, \ldots, d$일 때마다 다시 생성되므로 $(d + 1 - i)$번 생성된다.

$$
N(\text{IDS}) = \sum_{i=0}^{d} (d+1-i)\, b^i
$$

**수치 비교: $b = 10$, $d = 5$, 해가 맨 오른쪽 잎에 있을 때**

$$
\begin{aligned}
N(\text{IDS}) &= 50 + 400 + 3{,}000 + 20{,}000 + 100{,}000 = 123{,}450 \\
N(\text{BFS}) &= 10 + 100 + 1{,}000 + 10{,}000 + 100{,}000 + 999{,}990 = 1{,}111{,}100
\end{aligned}
$$

- IDS 식: $5 \cdot 10 + 4 \cdot 100 + 3 \cdot 1000 + 2 \cdot 10^4 + 1 \cdot 10^5$ (루트 $b^0$ 항은 생략)
- BFS 식의 마지막 항 $999{,}990 = b(b^d - 1) = 10 \times (10^5 - 1)$ 은 확장 시점 목표 검사 때문에 생기는 깊이 $d+1$ 노드들
- 👉 이 조건에서는 IDS가 BFS보다 **오히려 약 9배 적게** 생성한다!

> ⭐ **결론**: 탐색 공간이 크고 해의 깊이를 모를 때, **무정보 탐색 중에서는 IDS가 일반적으로 가장 좋은 선택**이다. **[보충: 교재의 결론]**

### 4.6 양방향 탐색 (Bidirectional Search)

- **아이디어**: **초기 상태에서 앞으로** 한 번, **목표 상태에서 뒤로** 한 번, 두 탐색을 동시에 진행해 **중간에서 만나게** 한다.

```
   시작 ●───────▶  ◀───────● 목표
        (반경 d/2)   (반경 d/2)
```

$$
b^{d/2} + b^{d/2} \ll b^d
$$

- 예: $b = 10, d = 6$ → BFS는 약 100만 노드, 양방향은 약 2,000 노드
- **목표 검사를 대체**: "두 프린지가 **교차하는가?**" 를 검사
- 주의점
  - (슬라이드) **해가 최적이 아닐 수 있다** — 처음 만난 지점이 최적 경로 위에 있다는 보장이 없음
  - 뒤로 탐색하려면 **선행자(predecessor)** 를 계산할 수 있어야 함 (행동의 역을 알아야 함)
  - ❓ 목표가 **추상적인 기술**이라면? 예: 8-퀸 문제의 "어떤 퀸도 다른 퀸을 공격하지 않음" → 목표 상태를 구체적으로 알 수 없으니 **뒤에서 출발할 수가 없다**. 양방향 탐색은 적용하기 어렵다.

### 4.7 무정보 탐색 비교표 ⭐⭐ [보충: 교재 Fig. 3.21]

| 기준 | BFS | UCS | DFS | DLS | IDS | 양방향 |
|---|---|---|---|---|---|---|
| 완전성 | 예¹ | 예¹˒² | 아니오 | 아니오 | 예¹ | 예¹˒⁴ |
| 시간 | $O(b^d)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | $O(b^m)$ | $O(b^l)$ | $O(b^d)$ | $O(b^{d/2})$ |
| 공간 | $O(b^d)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | $O(bm)$ | $O(bl)$ | $O(bd)$ | $O(b^{d/2})$ |
| 최적성 | 예³ | 예 | 아니오 | 아니오 | 예³ | 예³˒⁴ |

- ¹ $b$가 유한할 때 ² 단계 비용 $\ge \epsilon > 0$ 일 때 ³ 단계 비용이 모두 같을 때 ⁴ 양쪽 모두 BFS를 쓸 때
- 이 표의 BFS 시간/공간은 **생성 시점 목표 검사** 기준($O(b^d)$). 슬라이드 방식이면 $O(b^{d+1})$
- 슬라이드는 양방향 탐색의 해가 "최적이 아니다"라고 설명한다. 교재는 양쪽을 BFS로 하고 단계 비용이 같을 때만 최적이라고 조건을 단다.

**한 줄 요약 암기법**
- **BFS**: 완전·최적(비용 동일)이지만 **메모리 괴물**
- **UCS**: 비용이 달라도 **최적**, 방향 감각 없음
- **DFS**: 메모리 **초절약**, 불완전·비최적
- **DLS**: DFS + 제한, 제한을 잘 정해야 함
- **IDS**: BFS의 장점 + DFS의 메모리 → **무정보 탐색의 기본 선택**
- **양방향**: $b^{d/2}$로 빠르지만 역방향 탐색이 가능해야 함

---

## 5. 정보 탐색 / 휴리스틱 탐색 (Informed Search)

**정보 탐색(informed / heuristic search)** 은 문제 정의 **이외의** 문제에 특화된 지식, 즉 "**목표까지 얼마나 남았을까?**"에 대한 추정을 사용한다.

### 5.1 휴리스틱 함수 (Heuristic Function)

$$
h(n) = \text{노드 } n \text{의 상태에서 목표 상태까지 가는 가장 싼 경로의 } \textbf{추정} \text{ 비용}
$$

- $h(\text{목표}) = 0$
- 루마니아 예: $h_{SLD}(n)$ = $n$에서 **Bucharest까지의 직선 거리** (Straight-Line Distance)
- ⚠️ $h_{SLD}$ 는 **문제 정의만으로는 계산할 수 없다**. 도시의 좌표 같은 **추가 지식**이 필요하다. 이것이 "정보(informed)"의 의미다.

**Bucharest까지의 직선 거리 $h_{SLD}$**

| 도시 | $h_{SLD}$ | 도시 | $h_{SLD}$ | 도시 | $h_{SLD}$ |
|---|---|---|---|---|---|
| Arad | 366 | Hirsova | 151 | Rimnicu Vilcea | 193 |
| Bucharest | 0 | Iasi | 226 | Sibiu | 253 |
| Craiova | 160 | Lugoj | 244 | Timisoara | 329 |
| Drobeta | 242 | Mehadia | 241 | Urziceni | 80 |
| Eforie | 161 | Neamt | 234 | Vaslui | 199 |
| Fagaras | 176 | Oradea | 380 | Zerind | 374 |
| Giurgiu | 77 | Pitesti | 100 | | |

**[보충] 최선 우선 탐색 (Best-First Search)의 틀**

정보 탐색은 **평가 함수 $f(n)$** 이 가장 작은 노드를 먼저 확장하는 **최선 우선 탐색**의 변형이다. $f$를 무엇으로 정하느냐에 따라 알고리즘이 달라진다.

| 알고리즘 | 평가 함수 $f(n)$ | 의미 |
|---|---|---|
| 균일 비용 탐색 (UCS) | $g(n)$ | 지금까지 온 비용만 봄 (과거) |
| 탐욕적 최선 우선 탐색 | $h(n)$ | 앞으로 남은 추정 비용만 봄 (미래) |
| **A\* 탐색** | $g(n) + h(n)$ | **과거 + 미래** = 전체 경로 비용 추정 |

### 5.2 탐욕적 최선 우선 탐색 (Greedy Best-First Search)

- **아이디어**: **목표에 가장 가까워 보이는** 노드, 즉 $h(n)$이 가장 작은 노드를 먼저 확장
- $f(n) = h(n)$

**루마니아 예: Arad → Bucharest** (슬라이드 p.48 그림)

```
(a) 초기 상태          ▷Arad(366)

(b) Arad 확장           Arad
                ┌────────┼────────┐
            ▷Sibiu    Timisoara  Zerind
              253        329       374

(c) Sibiu 확장          Arad
                ┌────────┼────────┐
              Sibiu   Timisoara  Zerind(374)
        ┌───────┬──┴────┬──────────┐  (329)
      Arad  ▷Fagaras  Oradea  Rimnicu Vilcea
      366     176      380       193

(d) Fagaras 확장
                     Fagaras
                   ┌────┴─────┐
                 Sibiu    ▷Bucharest
                  253         0          ← 목표!
```

| 단계 | 확장 | 선택 이유 |
|---|---|---|
| 1 | Arad (366) | 시작 |
| 2 | Sibiu (253) | Sibiu 253 < Timisoara 329 < Zerind 374 |
| 3 | Fagaras (176) | Fagaras 176 < Rimnicu 193 < … |
| 4 | Bucharest (0) | 목표 도달 |

**결과: Arad → Sibiu → Fagaras → Bucharest, 비용 140 + 99 + 211 = 450**

**생각해 볼 질문 (슬라이드)**

- ✅ **탐색 비용은 최소**다 — 해 경로 위에 없는 노드는 **하나도 확장하지 않았다**.
- ❌ **최적인가? → 아니오!** 비용 418인 Sibiu → Rimnicu Vilcea → Pitesti 경로가 있는데 450을 찾았다. Fagaras가 목표에 "가까워 보여서" 골랐지만, Fagaras → Bucharest 도로(211)가 길었다.
  - 탐욕 탐색은 **지금까지 쓴 비용 $g(n)$을 전혀 고려하지 않는다**.
- ❌ **완전한가? → 아니오!** (트리 탐색 버전)
  - 예: **Iasi → Fagaras** 문제. Fagaras까지의 직선 거리로 보면 Iasi의 이웃 중 **Neamt**가 더 가까워 보인다. 하지만 Neamt는 **막다른 길**이다.
  - Neamt → (돌아갈 곳은 Iasi뿐) → Iasi → Neamt → Iasi → … **무한 루프!**
  - 실제 해는 Iasi → Vaslui → Urziceni → Bucharest → Fagaras 인데, 첫걸음이 목표에서 **멀어지는** 방향이라 탐욕 탐색은 가지 않는다.
  - 그래프 탐색(반복 상태 제거)을 쓰면 **유한 공간에서는 완전**하다. **[보충]**

**탐욕 탐색의 성질 [보충]**

| 기준 | 결과 |
|---|---|
| 완전성 | 아니오 (루프 가능). 그래프 탐색 + 유한 공간이면 예 |
| 시간 | $O(b^m)$ (최악). 좋은 휴리스틱이면 크게 줄어듦 |
| 공간 | $O(b^m)$ (모든 노드 유지) |
| 최적성 | **아니오** |

### 5.3 A\* 탐색: 전체 추정 해 비용 최소화 ⭐⭐⭐

$$
f(n) = g(n) + h(n)
$$

| 기호 | 의미 |
|---|---|
| $g(n)$ | 시작 노드에서 노드 $n$까지 **실제로 온 비용** |
| $h(n)$ | 노드 $n$에서 목표까지의 **추정 비용** |
| $f(n)$ | **$n$을 거쳐 가는 가장 싼 해의 추정 비용** |

> 💡 **직관**: UCS는 "지금까지 적게 쓴 길"을, 탐욕 탐색은 "앞으로 적게 남은 길"을 고른다. A\*는 **둘을 더해서** "**전체적으로** 가장 싸 보이는 길"을 고른다.

**루마니아 예: Arad → Bucharest** (슬라이드 p.50–51 그림, 표기: $f = g + h$)

```
(a) 초기 상태
    ▷Arad  366 = 0 + 366

(b) Arad 확장
    ▷Sibiu      393 = 140 + 253
     Timisoara  447 = 118 + 329
     Zerind     449 =  75 + 374

(c) Sibiu 확장
     Arad            646 = 280 + 366
     Fagaras         415 = 239 + 176
     Oradea          671 = 291 + 380
    ▷Rimnicu Vilcea  413 = 220 + 193      ← 최소

(d) Rimnicu Vilcea 확장
     Craiova   526 = 366 + 160
     Pitesti   417 = 317 + 100
     Sibiu     553 = 300 + 253
    → 프린지 최소: ▷Fagaras 415

(e) Fagaras 확장
     Sibiu      591 = 338 + 253
     Bucharest  450 = 450 +   0           ← 목표가 생성됐지만 f=450
    → 프린지 최소: ▷Pitesti 417  (450보다 작으므로 Pitesti를 먼저!)

(f) Pitesti 확장
    ▷Bucharest       418 = 418 + 0        ← 최소! 확장 → 목표 ✅
     Craiova         615 = 455 + 160
     Rimnicu Vilcea  607 = 414 + 193
```

**단계별 프린지 추적표**

| 단계 | 확장한 노드 ($f$) | 확장 후 프린지 ($f$ 오름차순) |
|---|---|---|
| a | – | Arad 366 |
| b | Arad (366) | **Sibiu 393**, Timisoara 447, Zerind 449 |
| c | Sibiu (393) | **Rimnicu 413**, Fagaras 415, Timisoara 447, Zerind 449, Arad 646, Oradea 671 |
| d | Rimnicu Vilcea (413) | **Fagaras 415**, Pitesti 417, Timisoara 447, Zerind 449, Craiova 526, Sibiu 553, … |
| e | Fagaras (415) | **Pitesti 417**, Timisoara 447, Zerind 449, Bucharest 450, … |
| f | Pitesti (417) | **Bucharest 418**, Timisoara 447, Zerind 449, Bucharest 450, … |
| g | **Bucharest (418)** | 목표 → 종료 |

**결과: Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest, 비용 418** ✅ **최적!**

**핵심 관찰** ⭐
- (e)에서 Bucharest가 이미 **f = 450으로 프린지에 들어왔지만** A\*는 멈추지 않는다.
- 프린지에 **f = 417인 Pitesti**가 있다는 것은 "Pitesti를 거치면 417짜리 해가 있을지도 모른다"는 뜻이기 때문이다.
- 그래서 **목표 검사는 확장할 때** 해야 한다 (UCS와 같은 이유).

**비교: 같은 문제를 세 알고리즘으로 풀면**

| 알고리즘 | 찾은 경로 | 비용 | 확장한 노드 수 |
|---|---|---|---|
| 탐욕 탐색 | Arad → Sibiu → Fagaras → Bucharest | 450 ❌ | 4 |
| UCS | Arad → Sibiu → Rimnicu → Pitesti → Bucharest | 418 ✅ | 13 |
| **A\*** | Arad → Sibiu → Rimnicu → Pitesti → Bucharest | 418 ✅ | **6** |

→ A\*는 **UCS처럼 최적이면서 탐욕 탐색처럼 효율적**이다. (확장 노드 수는 부록 코드 실행 결과)

### 5.4 [보충] A\*가 최적이 되는 조건

슬라이드에는 없지만 A\*를 이해하는 데 반드시 필요한 개념이다.

#### ① 허용 가능성 (Admissibility)

$$
h(n) \le h^*(n) \quad \text{(모든 } n\text{에 대해)}
$$

- $h^*(n)$ = $n$에서 목표까지의 **실제** 최소 비용
- 휴리스틱이 **절대 과대평가하지 않는다** (항상 낙관적)
- $h_{SLD}$는 허용 가능하다 — 두 점 사이 **직선이 가장 짧은 길**이므로 실제 도로 거리보다 길 수 없다.
- **정리**: $h$가 허용 가능하면 **A\* 트리 탐색은 최적**이다.

#### ② 일관성 (Consistency, Monotonicity)

$$
h(n) \le c(n, a, n') + h(n')
$$

- **삼각 부등식**: "$n$에서 목표까지 추정" ≤ "$n'$로 한 걸음 가는 비용 + $n'$에서 목표까지 추정"
- 일관적이면 → 허용 가능 (역은 항상 성립하지는 않음)
- 일관적이면 **경로를 따라 $f(n)$ 값이 줄어들지 않는다** (비감소) → **A\* 그래프 탐색은 최적**
- 위 추적표에서 확장된 노드들의 $f$ 값이 366 → 393 → 413 → 415 → 417 → 418 로 **단조 증가**하는 것을 확인할 수 있다.

#### ③ A\*의 성질

| 기준 | 결과 |
|---|---|
| 완전성 | **예** (유한한 $b$, 단계 비용 $\ge \epsilon > 0$) |
| 시간 | 최악의 경우 지수적. 휴리스틱이 좋을수록 크게 줄어듦 |
| 공간 | **모든 생성 노드를 메모리에 유지** ← A\*의 가장 큰 약점 |
| 최적성 | **예** (허용 가능 $h$ + 트리 탐색, 또는 일관적 $h$ + 그래프 탐색) |

- **최적 효율성 (optimally efficient)**: 같은 휴리스틱을 쓰는 최적 알고리즘 중에서 A\*보다 **적은 노드를 확장한다고 보장되는 알고리즘은 없다**.

### 5.5 [보충] 메모리 제한 탐색 (Memory-Bounded Search)

슬라이드 요약에 언급된 "memory bounded" 탐색. A\*의 메모리 문제를 해결하려는 방법들이다.

| 알고리즘 | 아이디어 |
|---|---|
| **IDA\*** (Iterative Deepening A\*) | IDS의 아이디어를 A\*에 적용. 깊이 대신 **$f$ 값을 제한(cutoff)** 으로 쓰고, 반복할 때마다 제한을 넘은 노드 중 최소 $f$로 늘림 |
| **RBFS** (Recursive Best-First Search) | 선형 공간으로 최선 우선 탐색 흉내. 대안 경로의 최선 $f$ 값을 기억해 두었다가 현재 경로가 그보다 나빠지면 되돌아감 |
| **SMA\*** (Simplified Memory-bounded A\*) | 메모리가 찰 때까지 A\*처럼 동작, 가득 차면 **가장 나쁜 잎 노드를 버리고** 그 값을 부모에 기록 |

### 5.6 [보충] 좋은 휴리스틱 만들기: 8-퍼즐 예

```
 시작 상태          목표 상태
┌───┬───┬───┐    ┌───┬───┬───┐
│ 7 │ 2 │ 4 │    │   │ 1 │ 2 │
├───┼───┼───┤    ├───┼───┼───┤
│ 5 │   │ 6 │    │ 3 │ 4 │ 5 │
├───┼───┼───┤    ├───┼───┼───┤
│ 8 │ 3 │ 1 │    │ 6 │ 7 │ 8 │
└───┴───┴───┘    └───┴───┴───┘
```

| 휴리스틱 | 정의 | 위 예시 값 |
|---|---|---|
| $h_1$ | **제자리에 있지 않은 타일 수** | 8 (모든 타일이 틀린 위치) |
| $h_2$ | 각 타일의 목표 위치까지 **맨해튼 거리 합** | 3+1+2+2+2+3+3+2 = 18 |

- 둘 다 **허용 가능**하다 (모든 타일은 최소 그만큼은 움직여야 하므로).
- 모든 $n$에 대해 $h_2(n) \ge h_1(n)$ → **$h_2$가 $h_1$을 지배(dominate)한다** → $h_2$가 더 **정보가 많고**, A\*가 확장하는 노드가 **더 적다**.
- **완화된 문제 (relaxed problem)**: 원래 문제의 제약을 줄인 문제의 **최적해 비용**은 원래 문제의 허용 가능한 휴리스틱이 된다.
  - "타일이 **아무 칸으로나** 순간이동 가능" → $h_1$
  - "타일이 **인접 칸으로** 이동 가능 (빈칸이 아니어도)" → $h_2$
- 루마니아의 $h_{SLD}$도 "도로를 무시하고 **날아갈 수 있다**"는 완화된 문제의 해다.

---

## 6. 요약 (Summary)

- 이 장은 **결정적, 관측 가능, 정적, 완전히 알려진** 환경에서 에이전트가 행동을 선택하는 방법을 다룬다. 이런 환경에서는 목표를 달성하는 **행동 시퀀스**를 미리 구성할 수 있다 → **탐색(search)**
- 해를 탐색하기 전에 **목표를 설정**하고 **잘 정의된 문제를 수립**해야 한다.
- **문제의 5요소**: ① 초기 상태 ② 행동 집합 ③ 행동의 결과를 기술하는 전이 모델 ④ 목표 검사 함수 ⑤ 경로 비용 함수
- 탐색 알고리즘의 평가 기준: **완전성, 최적성, 시간 복잡도, 공간 복잡도**
- **무정보 탐색**: 너비 우선, 균일 비용, 깊이 우선, (깊이 제한), 반복 심화, 양방향 탐색
- **정보(휴리스틱) 탐색**: 탐욕적 최선 우선, **A\***, 메모리 제한 탐색

### 🧠 한 장 요약 마인드맵

```
Solving Problems by Searching
├── 문제 해결 에이전트
│   ├── 목표 설정 → 문제 정의 → 탐색 → 실행
│   ├── 환경 가정: 관측 가능·이산·알려짐·결정적
│   └── 문제 유형: 단일 상태 / 순응 / 우발 상황 / 탐험
├── 문제 정의 (5요소)
│   ├── 초기 상태, ACTIONS(s), RESULT(s,a), 목표 검사, 경로 비용 c(s,a,s') ≥ 0
│   └── 추상화: 유효하고(실현 가능) 유용해야 함
├── 트리 탐색
│   ├── 확장 순서(전략)만 다르고 골격은 같음
│   ├── 노드 ≠ 상태, 프린지(frontier), 반복 상태 → 그래프 탐색(explored set)
│   └── 평가: 완전성·시간·공간·최적성 / b, d, m
├── 무정보 탐색
│   ├── BFS (FIFO): 완전, 최적(비용 동일), 공간 O(b^d)
│   ├── UCS (g 우선순위): 완전, 최적
│   ├── DFS (LIFO): 불완전, 비최적, 공간 O(bm)
│   ├── DLS: 깊이 제한 l, cutoff vs failure
│   ├── IDS: 완전, 최적(비용 동일), 시간 O(b^d), 공간 O(bd) ⭐
│   └── 양방향: b^(d/2) + b^(d/2), 역방향 탐색 필요
└── 정보(휴리스틱) 탐색
    ├── h(n): 목표까지 추정 비용 (예: 직선 거리)
    ├── 탐욕 (f = h): 빠르지만 비최적·불완전 (Iasi→Fagaras)
    ├── A* (f = g + h): 허용 가능/일관적 h면 최적 ⭐
    └── 메모리 제한: IDA*, RBFS, SMA*
```

---

## 7. 셀프 체크 퀴즈

> 답을 먼저 생각해 본 뒤 `▶ 정답 보기`를 눌러 확인하자.

**Q1.** 문제를 정의하는 5가지 요소를 쓰고, 루마니아 예로 각각 설명하라.

<details><summary>▶ 정답 보기</summary>

1. 초기 상태: `In(Arad)`
2. 행동: `ACTIONS(In(Arad))` = {Go(Sibiu), Go(Timisoara), Go(Zerind)}
3. 전이 모델: `RESULT(In(Arad), Go(Zerind))` = `In(Zerind)`
4. 목표 검사: 현재 상태가 `In(Bucharest)` 인가?
5. 경로 비용: 지나온 도로 거리의 합 (단계 비용 ≥ 0)
</details>

**Q2.** 진공청소기 순응 문제에서 `[Right, Suck, Left, Suck]` 이 해가 되는 이유를 믿음 상태의 변화로 설명하라.

<details><summary>▶ 정답 보기</summary>

{1..8} →Right→ {2,4,6,8} →Suck→ {4,8} →Left→ {3,7} →Suck→ {7}.
어디서 시작했든 마지막에는 두 칸 모두 깨끗한 상태 7에 도달한다.
</details>

**Q3.** 노드(node)와 상태(state)의 차이는?

<details><summary>▶ 정답 보기</summary>

상태는 세계의 구성이고, 노드는 탐색 트리의 자료구조(상태, 부모, 행동, 경로 비용 등 포함)다. 서로 다른 경로로 같은 상태에 도달하면 **같은 상태를 가진 여러 노드**가 생길 수 있다.
</details>

**Q4.** 탐색 전략의 4가지 평가 기준과 $b$, $d$, $m$의 의미는?

<details><summary>▶ 정답 보기</summary>

완전성, 시간 복잡도, 공간 복잡도, 최적성.
$b$ = 최대 분기 계수, $d$ = 최소 비용 해의 깊이, $m$ = 상태 공간의 최대 경로 깊이.
</details>

**Q5.** BFS가 최적이 되는 조건은? 루마니아 문제에서 BFS가 최적해를 못 찾는 이유는?

<details><summary>▶ 정답 보기</summary>

모든 단계 비용이 같을 때(예: 1)만 최적이다. BFS는 **행동 수가 가장 적은** 경로(Arad→Sibiu→Fagaras→Bucharest, 3단계, 450)를 찾지만, 거리 기준 최적해는 4단계짜리(418)다.
</details>

**Q6.** UCS에서 목표 검사를 생성 시점이 아니라 확장 시점에 하는 이유는?

<details><summary>▶ 정답 보기</summary>

처음 생성된 목표 노드가 최소 비용이라는 보장이 없기 때문이다. 예: Sibiu→Bucharest에서 Fagaras 경유(310)가 먼저 생성되지만, 나중에 Pitesti 경유(278)가 발견된다. 확장 시점에 검사하면 $g$ 순서대로 꺼내므로 처음 꺼낸 목표가 최적이다.
</details>

**Q7.** 위 A~O 트리에서 J와 C가 모두 목표일 때 BFS와 DFS는 각각 무엇을 반환하는가?

<details><summary>▶ 정답 보기</summary>

- BFS: **C** (깊이 1, 더 얕으므로 먼저 발견)
- DFS: **J** (A→B→D→H→I→E→J 순서로 왼쪽을 먼저 파고들어서) → DFS가 최적이 아님을 보여주는 예
</details>

**Q8.** DFS의 공간 복잡도가 $O(bm)$인 이유는?

<details><summary>▶ 정답 보기</summary>

현재 경로 하나(최대 길이 $m$)와 경로 위 각 노드의 미확장 형제들(각각 최대 $b$개)만 저장하면 된다. 서브트리 탐색이 끝난 노드는 메모리에서 지울 수 있다.
</details>

**Q9.** DLS의 반환값 `cutoff`와 `failure`의 차이는?

<details><summary>▶ 정답 보기</summary>

`cutoff`는 깊이 제한 때문에 잘린 가지가 있었다는 뜻이다. 제한을 늘리면 해를 찾을 **수도** 있다. `failure`는 제한에 걸린 적 없이 모든 가지를 다 봤는데 해가 없다는 뜻이다. IDS는 `cutoff`일 때만 다음 깊이로 넘어간다.
</details>

**Q10.** IDS는 위층 노드를 여러 번 다시 생성하는데도 왜 비효율적이지 않은가? $b=10, d=5$의 수치로 설명하라.

<details><summary>▶ 정답 보기</summary>

대부분의 노드가 맨 아래층에 있어서 위층을 반복 생성하는 비용이 상대적으로 작다.
N(IDS) = 50+400+3,000+20,000+100,000 = **123,450**
N(BFS) = 10+100+1,000+10,000+100,000+999,990 = **1,111,100**
</details>

**Q11.** 양방향 탐색의 장점과, 8-퀸 문제에 적용하기 어려운 이유는?

<details><summary>▶ 정답 보기</summary>

장점: $b^{d/2} + b^{d/2} \ll b^d$ 로 탐색량이 크게 줄어든다.
8-퀸의 목표는 "어떤 퀸도 서로 공격하지 않음"이라는 **추상적 기술**이라서 구체적인 목표 상태에서 역방향 탐색을 시작할 수 없다.
</details>

**Q12.** 탐욕적 최선 우선 탐색이 최적도 완전도 아닌 이유를 루마니아 예로 설명하라.

<details><summary>▶ 정답 보기</summary>

- 비최적: Arad→Bucharest에서 $h$만 보고 Fagaras(176)를 택해 450짜리 경로를 반환한다. 최적은 418이다. $g$를 무시하기 때문.
- 불완전: Iasi→Fagaras에서 Neamt가 더 가까워 보이지만 막다른 길이라서, 트리 탐색에서는 Iasi↔Neamt 무한 루프에 빠진다.
</details>

**Q13.** A\* 추적의 (e) 단계에서 Bucharest(f=450)가 프린지에 있는데도 탐색을 멈추지 않는 이유는?

<details><summary>▶ 정답 보기</summary>

프린지에 f=417인 Pitesti가 있으므로, Pitesti를 거치면 450보다 싼 해가 있을 수 있기 때문이다. A\*는 목표를 **확장할 때** 검사하고, 프린지에서 $f$가 최소인 노드부터 꺼낸다. 실제로 Pitesti를 거쳐 418짜리 해를 찾는다.
</details>

**Q14.** 허용 가능한 휴리스틱이란? $h_{SLD}$가 허용 가능한 이유는?

<details><summary>▶ 정답 보기</summary>

모든 $n$에 대해 $h(n) \le h^*(n)$, 즉 실제 최소 비용을 절대 과대평가하지 않는 휴리스틱이다. 직선 거리는 두 지점 사이의 가장 짧은 거리이므로 실제 도로 거리보다 클 수 없다.
</details>

**Q15.** UCS, 탐욕 탐색, A\*의 평가 함수를 각각 쓰라.

<details><summary>▶ 정답 보기</summary>

- UCS: $f(n) = g(n)$
- 탐욕: $f(n) = h(n)$
- A\*: $f(n) = g(n) + h(n)$
</details>

**Q16.** [응용] 다음 중 A\*에서 Arad → Bucharest 탐색 시 **확장되지 않는** 노드를 모두 고르라: Sibiu, Timisoara, Zerind, Fagaras, Pitesti, Craiova

<details><summary>▶ 정답 보기</summary>

**Timisoara(447), Zerind(449), Craiova(526)**. 최적해 비용 418보다 $f$ 값이 크므로 확장되기 전에 목표를 찾는다.
</details>

---

### 📚 핵심 용어 사전

| 영어 | 한국어 | 한 줄 정의 |
|---|---|---|
| Problem-solving agent | 문제 해결 에이전트 | 탐색으로 목표 달성 행동 시퀀스를 찾는 목표 기반 에이전트 |
| Initial state | 초기 상태 | 탐색 시작 상태 |
| Transition model | 전이 모델 | `RESULT(s, a)`, 행동의 결과 상태 |
| Successor | 후속 상태 | 한 번의 행동으로 도달 가능한 상태 |
| Goal test | 목표 검사 | 목표 상태인지 판별 |
| Step cost | 단계 비용 | $c(s, a, s') \ge 0$ |
| Path cost | 경로 비용 | 단계 비용의 합, $g(n)$ |
| State space | 상태 공간 | 초기 상태에서 도달 가능한 모든 상태의 그래프 |
| Abstraction | 추상화 | 불필요한 세부 사항 제거 |
| Belief state | 믿음 상태 | 에이전트가 있을 수 있는 상태들의 집합 |
| Contingent plan / Policy | 조건부 계획 / 정책 | 인지에 따라 분기하는 해 |
| Expand | 확장 | 노드의 자식 노드들을 생성 |
| Fringe / Frontier | 프린지 / 프론티어 | 생성됐지만 아직 확장되지 않은 노드 집합 |
| Explored set | 탐험 집합 | 이미 확장한 상태들 (그래프 탐색) |
| Branching factor ($b$) | 분기 계수 | 노드당 최대 자식 수 |
| Completeness | 완전성 | 해가 있으면 반드시 찾음 |
| Optimality | 최적성 | 최소 비용 해를 찾음 |
| Uninformed search | 무정보 탐색 | 문제 정의 정보만 사용 |
| Informed search | 정보 탐색 | 문제 특화 지식(휴리스틱) 사용 |
| Heuristic function $h(n)$ | 휴리스틱 함수 | 목표까지의 추정 비용 |
| Admissible | 허용 가능 | $h(n) \le h^*(n)$, 과대평가 안 함 |
| Consistent | 일관적 | $h(n) \le c(n,a,n') + h(n')$ |
| Relaxed problem | 완화된 문제 | 제약을 줄인 문제, 휴리스틱의 원천 |

---

## 8. 부록: Python 실습 코드

루마니아 지도에서 모든 알고리즘을 직접 돌려볼 수 있는 코드다. 그대로 복사해서 `python3 search.py` 로 실행하면 된다 (외부 라이브러리 불필요).

```python
import heapq
from collections import deque

EDGES = [
    ("Arad", "Zerind", 75), ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75), ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146), ("Craiova", "Pitesti", 138),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97), ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101), ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85), ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86), ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92), ("Iasi", "Neamt", 87),
]
GRAPH = {}
for a, b, c in EDGES:
    GRAPH.setdefault(a, {})[b] = c
    GRAPH.setdefault(b, {})[a] = c

H_SLD = {  # Bucharest까지의 직선 거리
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253,
    "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
}

def path_cost(path):
    return sum(GRAPH[a][b] for a, b in zip(path, path[1:]))

# ---------- 무정보 탐색 ----------

def bfs(start, goal):
    if start == goal:
        return [start]
    frontier = deque([[start]])           # FIFO 큐
    explored = {start}
    while frontier:
        path = frontier.popleft()
        for nxt in GRAPH[path[-1]]:
            if nxt not in explored:
                if nxt == goal:            # 생성 시점에 목표 검사
                    return path + [nxt]
                explored.add(nxt)
                frontier.append(path + [nxt])
    return None

def dfs(start, goal):
    frontier = [[start]]                  # LIFO 스택
    while frontier:
        path = frontier.pop()
        if path[-1] == goal:
            return path
        for nxt in reversed(list(GRAPH[path[-1]])):
            if nxt not in path:           # 경로상 반복 상태 회피
                frontier.append(path + [nxt])
    return None

def depth_limited(path, goal, limit):
    if path[-1] == goal:
        return path
    if limit == 0:
        return "cutoff"
    cutoff = False
    for nxt in GRAPH[path[-1]]:
        if nxt in path:
            continue
        result = depth_limited(path + [nxt], goal, limit - 1)
        if result == "cutoff":
            cutoff = True
        elif result is not None:
            return result
    return "cutoff" if cutoff else None   # None = failure

def ids(start, goal):
    depth = 0
    while True:
        result = depth_limited([start], goal, depth)
        if result != "cutoff":
            return result
        depth += 1

# ---------- 최선 우선 탐색 계열 ----------

def best_first(start, goal, f):
    """f(g, state) 값이 가장 작은 노드부터 확장하는 공통 틀"""
    frontier = [(f(0, start), 0, [start])]   # 우선순위 큐
    best_g = {start: 0}
    order = []
    while frontier:
        _, g, path = heapq.heappop(frontier)
        state = path[-1]
        if g > best_g.get(state, float("inf")):
            continue                         # 더 나은 경로가 이미 있음
        order.append(state)
        if state == goal:                    # 확장 시점에 목표 검사
            return path, g, order
        for nxt, cost in GRAPH[state].items():
            g2 = g + cost
            if g2 < best_g.get(nxt, float("inf")):
                best_g[nxt] = g2
                heapq.heappush(frontier, (f(g2, nxt), g2, path + [nxt]))
    return None

def ucs(start, goal):
    return best_first(start, goal, lambda g, s: g)             # f = g

def greedy(start, goal):
    return best_first(start, goal, lambda g, s: H_SLD[s])      # f = h

def astar(start, goal):
    return best_first(start, goal, lambda g, s: g + H_SLD[s])  # f = g + h

if __name__ == "__main__":
    for name, fn in [("BFS", bfs), ("DFS", dfs), ("IDS", ids)]:
        p = fn("Arad", "Bucharest")
        print(f"{name:7}", " → ".join(p), f"(비용 {path_cost(p)})")
    for name, fn in [("UCS", ucs), ("Greedy", greedy), ("A*", astar)]:
        p, g, order = fn("Arad", "Bucharest")
        print(f"{name:7}", " → ".join(p), f"(비용 {g})")
        print("        확장 순서:", ", ".join(order))
```

**실행 결과**

```
BFS     Arad → Sibiu → Fagaras → Bucharest (비용 450)
DFS     Arad → Zerind → Oradea → Sibiu → Fagaras → Bucharest (비용 607)
IDS     Arad → Sibiu → Fagaras → Bucharest (비용 450)
UCS     Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest (비용 418)
        확장 순서: Arad, Zerind, Timisoara, Sibiu, Oradea, Rimnicu Vilcea, Lugoj, Fagaras, Mehadia, Pitesti, Craiova, Drobeta, Bucharest
Greedy  Arad → Sibiu → Fagaras → Bucharest (비용 450)
        확장 순서: Arad, Sibiu, Fagaras, Bucharest
A*      Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest (비용 418)
        확장 순서: Arad, Sibiu, Rimnicu Vilcea, Fagaras, Pitesti, Bucharest
```

**관찰 포인트**
- BFS, IDS는 **단계 수**가 가장 적은 경로(3단계)를 찾지만, 거리로는 최적이 아니다.
- DFS는 이웃을 보는 순서에 따라 결과가 달라지고, 대체로 나쁜 해를 찾는다.
- UCS와 A\*는 모두 최적해(418)를 찾지만, A\*가 확장한 노드는 **6개**로 UCS(13개)의 절반 이하다.
- 탐욕 탐색은 **4개**만 확장할 만큼 빠르지만 최적이 아니다.
- A\*의 확장 순서는 슬라이드 그림(p.50–51)의 순서와 정확히 일치한다.

**✍️ 직접 해볼 것**
1. Iasi → Fagaras 문제를 탐욕 탐색으로 풀어 보자. `H_SLD`는 Bucharest 기준이므로 Fagaras 기준 휴리스틱 딕셔너리를 따로 만들되, **Neamt가 Vaslui보다 작게** 설정한다. 이 코드는 그래프 탐색(`best_g`)이라 Neamt에서 막힌 뒤 Vaslui 쪽으로 빠져나오지만, 트리 탐색이었다면 Iasi ↔ Neamt 루프에 빠진다는 점을 비교해 보자.
2. `H_SLD`의 값을 일부러 **과대평가**하도록 바꿔서(예: Pitesti를 300으로) A\*가 최적해를 놓치는지 확인해 보자 → 허용 가능성의 중요성
3. 모든 도로 비용을 1로 바꾸면 UCS와 BFS의 결과가 같아지는지 확인해 보자.

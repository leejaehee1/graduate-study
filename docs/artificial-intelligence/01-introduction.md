# Chapter 1. Artificial Intelligence

> **학습 목표:** AI를 정의하는 네 가지 접근을 구분하고, 이 강의가 왜 **Rational Agent**를 중심으로 전개되는지 설명한다. AI의 학문적 기반과 역사, 다양한 과제가 요구하는 능력을 이 관점과 연결한다.

## 자료 기준과 읽는 방법

- 기준 자료는 **AI-ch01.pdf**이며, 이전 「대학원 수업 정리」 대화에 사용자가 직접 옮긴 슬라이드 본문과 함께 공부한 해설을 바탕으로 정리했다.
- **원본 확인 범위:** 작성 환경에서 PDF 파일 자체는 제공되지 않아 페이지별 대조와 그림 검증은 하지 못했다. 따라서 페이지 번호를 임의로 붙이지 않았으며, 대화에 남아 있는 슬라이드 제목과 본문을 근거로 삼았다.
- 각 절의 **슬라이드 핵심**은 확인 가능한 본문의 요약이고, **학습 해설**은 그 내용을 이해하기 위한 개념 연결이다. 예시와 도식은 원본 그림의 복제가 아니라 학습용 재구성이다.
- 역사에 등장하는 `present`, 인지과학 부분의 `now`, State of the Art의 `at present`는 **자료 작성 당시**를 가리킨다. 현재 기술 수준으로 업데이트하지 않았다.
- 이전 답변과 사용자가 옮긴 슬라이드 본문이 다르면 **슬라이드 본문을 우선**했다. 외부 자료, 현대 AI 사례, 후속 장의 세부 알고리즘은 추가하지 않았다.

## 목차

1. [AI의 네 가지 접근](#four-approaches)
2. [Acting Humanly: Turing Test](#turing-test)
3. [Thinking Humanly: Cognitive Science](#cognitive-science)
4. [Thinking Rationally: Laws of Thought](#laws-of-thought)
5. [Acting Rationally](#acting-rationally)
6. [Rational Agents와 에이전트 함수](#rational-agents)
7. [AI Prehistory: 일곱 학문적 기반](#prehistory)
8. [The History of AI](#history)
9. [State of the Art](#state-of-the-art)
10. [Chapter Summary와 복습](#summary)

<a id="four-approaches"></a>
## 1. AI의 네 가지 접근

### 슬라이드 핵심

AI의 정의는 두 질문으로 구분할 수 있다.

1. 연구 대상이 **사고 과정(Thinking)** 인가, **행동(Acting)** 인가?
2. 기준이 **인간(Humanly)** 인가, **합리성(Rationally)** 인가?

| 구분 | Humanly: 인간을 기준으로 | Rationally: 합리적 기준으로 |
|---|---|---|
| **Thinking** | Thinking humanly: 인간은 실제로 어떻게 생각하는가? | Thinking rationally: 올바른 추론은 무엇인가? |
| **Acting** | Acting humanly: 인간처럼 지능적으로 행동하는가? | Acting rationally: 목표 달성을 위해 어떤 행동을 선택해야 하는가? |

대화에 옮겨진 도입부에는 다음 세 정의가 등장한다.

| 출처 표기 | 관점 | 인용문의 의미 |
|---|---|---|
| Richard Bellman, 1978 | Thinking humanly | 의사결정·문제 해결·학습처럼 인간의 사고와 연관된 활동을 자동화한다. |
| Ray Kurzweil, 1990 | Acting humanly | 사람이 수행할 때 지능을 필요로 하는 기능을 수행하는 기계를 만든다. |
| Nilsson, 1998 | Acting rationally | 인공물의 지능적 행동을 연구한다. |

Thinking rationally는 뒤의 **Laws of Thought** 슬라이드에서 설명된다. 도입부에 확인되지 않는 별도의 인용문을 채워 넣을 필요는 없다.

### 학습 해설: 두 축을 섞지 않기

**Thinking과 Acting의 차이**는 내부 과정과 외부 행동 중 어디에 초점을 두는가이다. 기계가 인간과 비슷한 답을 했다는 사실만으로, 그 기계가 인간과 동일한 사고 과정을 거쳤다고 할 수는 없다.

**Humanly와 Rationally의 차이**는 실제 인간을 설명하려는가, 바람직한 사고·행동의 기준을 세우려는가이다. 인간의 실제 판단을 재현하는 것과 주어진 목표에 가장 적절한 행동을 선택하는 것은 서로 다른 연구 목표다.

```text
                         AI를 어떤 기준으로 연구할까?
                                      │
                 ┌────────────────────┴────────────────────┐
              인간 기준                                합리적 기준
                 │                                         │
       ┌─────────┴─────────┐                    ┌──────────┴──────────┐
    사고 과정           외부 행동             올바른 추론          적절한 행동
 Cognitive Science     Turing Test          Laws of Thought      Rational Agent
```

네 접근은 단순한 발전 단계나 우열 순위가 아니다. 서로 다른 질문을 구분하는 틀이며, **이 강의는 그중 Acting rationally와 Rational Agent를 중심으로 전개된다.**

<a id="turing-test"></a>
## 2. Acting Humanly: The Turing Test

### 슬라이드 핵심

Turing의 1950년 논문 *Computing Machinery and Intelligence*를 소개하면서 질문의 전환을 제시한다.

```text
Can machines think?
기계가 생각할 수 있는가?
              ↓
Can machines behave intelligently?
기계가 지능적으로 행동할 수 있는가?
```

추상적인 사고 여부 대신 관찰 가능한 행동으로 평가하는 **Operational test**가 **Imitation Game**이다.

```text
                       ┌── Human
Human Interrogator ────┤
                       └── AI System

질문자는 대화를 통해 어느 쪽이 인간이고 어느 쪽이 기계인지 판단한다.
```

### 학습 해설: 무엇을 검사하는가?

Operational test는 지능이라는 추상적 개념을 실제 수행 가능한 평가 절차로 다룬다는 뜻이다. 이 관점에서는 내부 사고 과정 자체보다 **대화에서 드러나는 지적 행동**이 평가 대상이다.

따라서 Turing Test를 Thinking humanly와 혼동하면 안 된다. 인간처럼 응답할 수 있다는 것과 인간의 사고 메커니즘을 그대로 재현한다는 것은 같은 주장이 아니다.

슬라이드는 이를 위해 필요한 AI의 주요 구성 요소를 다음과 같이 제시한다.

| 구성 요소 | 학습용 풀이 |
|---|---|
| Knowledge | 대화와 판단에 필요한 지식을 갖춘다. |
| Reasoning | 알고 있는 정보에서 필요한 결론을 이끌어 낸다. |
| Language understanding | 질문과 문장의 의미를 이해한다. |
| Learning | 경험과 새로운 정보로부터 배운다. |

자연스럽게 말하는 표면적 능력 뒤에는 지식·추론·언어 이해·학습이 함께 필요하다는 연결을 잡는 것이 중요하다.

### Turing의 예측과 Total Turing Test

슬라이드는 Turing이 **2000년 무렵, 기계가 일반인을 5분 동안 속일 확률이 30%가 될 수 있다**고 예측했다고 소개한다. 여기서 속인다는 것은 대화 상대가 기계임을 구별하지 못하게 한다는 의미다. 이 수치는 슬라이드가 소개한 **역사적 예측**이며, 실제 달성 결과나 모든 Turing Test의 보편적 통과 기준으로 읽지 않는다.

**Total Turing Test**에는 **Computer vision**과 **Robotics**가 추가된다. 언어적 상호작용에 더해 환경을 보고 물리적으로 행동하는 능력까지 포함하는 것이다.

<a id="cognitive-science"></a>
## 3. Thinking Humanly: Cognitive Science

### 슬라이드 핵심

슬라이드는 1960년대 **Cognitive revolution**을 행동주의 중심의 설명에서 정보처리 심리학으로 전환한 흐름으로 제시한다. 인간처럼 생각하는 것을 연구하려면 뇌 내부 활동에 관한 과학적 이론이 필요하다.

내부 과정을 조사하는 방법은 다음과 같다.

- **Introspection:** 자신의 사고 과정을 관찰한다.
- **Psychological experiments:** 심리학 실험으로 사고·행동에 관한 가설을 검증한다.
- **Brain imaging:** 뇌 영상을 통해 내부 활동을 조사한다.

### 학습 해설: Get inside

핵심은 입력과 출력 사이에 어떤 정보처리가 있는지 설명하는 것이다. 아래는 두 관점의 초점을 단순화한 도식이다.

```text
관찰 가능한 자극과 행동에 초점
Input ───────────────→ Output

내부 정보처리 과정을 설명
Input → 기억·지식·추론·판단 → Output
```

이 접근에서는 정답을 내는 프로그램을 만들었다는 사실만으로 충분하지 않다. **그 모델이 인간의 실제 사고와 행동을 설명하는가?** 라 는 검증이 필요하다.

### 어느 수준에서 설명할 것인가?

슬라이드의 질문은 **“Knowledge or circuits?”** 이다.

| 설명 수준 | 초점 |
|---|---|
| Knowledge | 지식, 기억, 추론 등 비교적 높은 수준의 정보처리 |
| Circuits | 신경회로 등 물리적 구현 수준의 활동 |

같은 사고를 설명하더라도 어떤 추상화 수준을 선택하는지에 따라 이론과 검증 자료가 달라진다.

### 어떻게 검증할 것인가?

| 방향 | 검증 흐름 | 슬라이드의 대략적 연결 |
|---|---|---|
| Top-down | 사고에 관한 이론 → 인간 행동 예측 → 피험자 실험 | Cognitive Science |
| Bottom-up | 신경학적 데이터 → 내부 작동 과정 규명 | Cognitive Neuroscience |

이는 슬라이드의 **roughly**에 해당하는 개략적 구분이다. 두 분야 전체를 배타적으로 나누는 엄격한 정의로 외우지 않는다.

### AI와의 관계

슬라이드는 인지과학과 인지신경과학이 AI와 구별되는 분야라고 설명한다. 실제 인간의 사고나 뇌를 설명하는 목표와 지능적 시스템을 설계하는 목표가 완전히 같지는 않기 때문이다.

동시에 당시의 이론들이 인간 수준의 일반지능을 충분히 설명하지 못한다는 공통 과제를 제시한다. 이 문장은 **강의자료 당시의 문제의식**으로 읽는다.

<a id="laws-of-thought"></a>
## 4. Thinking Rationally: Laws of Thought

### 슬라이드 핵심

이 접근은 **Descriptive**보다 **Normative / Prescriptive**한 관점이다.

| 용어 | 질문 |
|---|---|
| Descriptive: 기술적 | 인간은 실제로 어떻게 생각하는가? |
| Normative / Prescriptive: 규범적·처방적 | 어떻게 생각해야 올바른가? |

Aristotle의 질문은 올바른 논증과 사고 과정이 무엇인지에 관한 것이었다. 여러 그리스 학파는 사고를 표현하는 **Notation**과 결론을 도출하는 **Rules of derivation**을 발전시켰다.

### 학습 해설: 표현과 추론의 분리

논리적 추론은 지식을 표현하는 기호와 그 기호에서 결론을 얻는 규칙으로 이해할 수 있다. 다음은 이를 위한 학습 예시다.

```text
전제 1: A이면 B이다.      A → B
전제 2: A이다.            A
--------------------------------
결론: B이다.             B
```

중요한 점은 **전제의 참·거짓**과 **추론 형식의 올바름**을 구분하는 것이다. 올바른 추론 형식이라고 해서 잘못된 전제가 자동으로 참이 되는 것은 아니다.

이러한 표현과 규칙을 기계가 실행하게 만들 수 있다는 생각이 **Mechanization**과 연결된다. 슬라이드의 **Logicist tradition within AI**는 논리적 표현과 추론을 바탕으로 지능적 시스템을 구축하려는 전통이다.

### 한계 1: 모든 지능적 행동이 논리적 숙고를 거치지는 않는다

슬라이드는 **Not all intelligent behavior is mediated by logical deliberation**을 지적한다. 상황에 적절한 행동이 반드시 명시적인 논증의 결과일 필요는 없다. 다음 Acting rationally 슬라이드의 눈 깜박임 반사가 이와 연결된다.

### 한계 2: 가능한 생각 중 무엇을 해야 하는가?

논리적으로 도출 가능한 결론이 많아도 지금의 목표에 필요한 결론은 일부일 수 있다.

```text
논리의 질문: 이 전제에서 이 결론을 올바르게 도출할 수 있는가?
추가로 남는 질문: 지금 어떤 생각을 해야 목표 달성에 도움이 되는가?
```

따라서 추론 규칙만으로는 **사고의 목적과 우선순위**가 자동으로 정해지지 않는다. 이 문제가 다음 절의 합리적 행동으로 이어진다.

<a id="acting-rationally"></a>
## 5. Acting Rationally

### 슬라이드 핵심

**Rational behavior**는 **doing the right thing**이다. 여기서 적절한 행동은 다음 조건으로 설명된다.

> 이용 가능한 정보를 바탕으로, 목표 달성을 최대화할 것으로 기대되는 행동.

핵심 표현은 **given the available information**과 **expected to maximize goal achievement**다.

### 학습 해설: 합리적이라는 말의 기준

| 표현 | 의미 |
|---|---|
| Available information | 행동을 선택하는 시점에 이용 가능한 정보를 기준으로 판단한다. |
| Expected | 결과를 미리 완벽하게 아는 것이 아니라 기대되는 결과를 고려한다. |
| Maximize goal achievement | 주어진 목표를 가장 잘 달성할 행동을 선택한다. |

따라서 합리적인 선택을 했다고 해서 반드시 성공이 보장되는 것은 아니다. 불확실성이 있으면 좋은 선택도 실제로는 좋지 않은 결과를 낼 수 있다. 이 구분은 슬라이드의 **expected**를 이해하기 위한 핵심이다.

또한 이 문맥의 `right`는 목표와 정보에 비추어 적절하다는 의미다. 단어 자체를 막연한 의미의 정답이나 도덕적 올바름으로만 읽으면 정의의 초점을 놓치게 된다.

### 생각은 행동을 위한 역할을 한다

슬라이드는 **Blinking reflex**를 예로 들어 합리적 행동이 반드시 사고를 수반하지는 않는다고 설명한다. 사고가 필요하다면 그것은 **rational action에 기여해야 한다**.

```text
이용 가능한 정보 + 목표
            ↓
필요한 지각·추론·판단
            ↓
목표 달성을 가장 잘 도울 것으로 기대되는 행동
```

Aristotle의 *Nicomachean Ethics*에 관한 인용은 기술·탐구·행동·추구가 어떤 좋음을 지향한다는 내용을 담는다. 이 문맥에서는 **행동이 목적을 향한다**는 연결을 이해하면 된다.

<a id="rational-agents"></a>
## 6. Rational Agents와 에이전트 함수

### 슬라이드 핵심

**Agent**는 **환경을 인식하고 행동하는 존재**다. 슬라이드는 이 강의의 목표를 **designing rational agents**라고 명시한다.

에이전트는 추상적으로 지각 이력에서 행동으로 가는 함수로 표현된다.

$$
f : P^{*} \rightarrow A
$$

```text
f : P* → A
지금까지의 지각 이력 → 선택할 행동
```

### 기호를 정확하게 읽기

| 기호 | 의미 |
|---|---|
| P | 가능한 지각(percept)의 집합 |
| P* | P의 원소로 이루어진 모든 유한한 지각 시퀀스의 집합 |
| A | 가능한 행동(action)의 집합 |
| f | 각 지각 이력에 행동을 대응시키는 에이전트 함수 |

개별 지각을 `p₁, p₂, …, pₜ`라고 하면 현재까지의 이력은 `(p₁, p₂, …, pₜ)`이고, 함수는 이 이력에 행동 하나를 대응시킨다.

```text
f((p₁, p₂, …, pₜ)) = aₜ
```

`P*`의 별표는 곱셈이나 일반적인 수치 거듭제곱을 뜻하지 않는다. 개별 이력 하나는 `P*`의 **원소**이고, `P*` 자체는 가능한 이력들의 **집합**이라는 점을 구분한다.

### 학습 해설: 왜 현재 지각 하나가 아니라 이력인가?

이전 대화에서 사용한 거리 관측 예시를 생각해 보자.

```text
t₁: 앞차까지 거리 30m
t₂: 앞차까지 거리 25m
t₃: 앞차까지 거리 18m
t₄: 앞차까지 거리 10m
```

현재 거리 하나와 거리의 변화 이력은 제공하는 정보가 다르다. 이력을 통해 앞차에 가까워지고 있다는 변화까지 판단할 수 있다. 따라서 일반적인 에이전트 함수는 과거 지각이 행동에 영향을 줄 가능성까지 포함한다.

이것은 **행동을 추상적으로 정의하는 방식**이다. 모든 실제 프로그램이 과거 입력 전체를 원문 그대로 저장해야 한다는 구현 지시로 해석하지 않는다.

### 좋은 에이전트의 기준

슬라이드는 주어진 **환경과 과제의 종류**에 대해 최고의 성과를 내는 에이전트 또는 에이전트 집합을 찾는다고 설명한다.

```text
환경과 과제가 주어짐
        ↓
어떤 행동 방식이 더 좋은 성과를 내는가?
        ↓
그 환경과 과제에 맞는 에이전트를 설계
```

따라서 환경과 과제를 빼놓고 어떤 에이전트가 무조건 최고라고 말하기는 어렵다. 행동의 적절성은 수행할 일과 연결해서 평가해야 한다.

### 계산 자원의 한계

슬라이드는 계산상의 제약 때문에 **Perfect rationality**를 달성하기 어렵다는 단서를 붙인다. 설계 목표는 **주어진 기계 자원에서 가장 좋은 프로그램**을 만드는 것으로 이어진다.

이전 대화의 단순화된 예시처럼 매 단계 선택지가 10개이고 깊이가 20이면, 길이 20인 선택 경로만 해도 `10^20`개가 될 수 있다. 가능한 경우를 전부 살펴보는 방식은 문제의 크기에 따라 실행하기 어려워진다.

여기서 두 개념을 구분해야 한다.

- **합리적 행동의 기준:** 이용 가능한 정보에서 목표 달성을 가장 잘 도울 것으로 기대되는 선택.
- **실제 설계의 제약:** 시간·메모리 등 제한된 자원으로 그 기준에 최대한 잘 접근하는 프로그램.

### Interplay of reasoning and perception

확인 가능한 슬라이드 본문에는 이 문구가 있지만 상세한 설명은 없다. 따라서 **지각과 추론이 서로 연결된다**는 방향까지만 정리한다. 원본 그림이나 특정 이론의 내용을 추정해 덧붙이지 않는다.

<a id="prehistory"></a>
## 7. AI Prehistory: 일곱 학문적 기반

### 슬라이드 핵심

AI는 하나의 학문에서 단독으로 시작된 것이 아니라, 다음 분야의 문제의식과 방법을 이어받았다.

| 분야 | 슬라이드의 주요 용어 | 앞의 개념과 연결한 학습 해설 |
|---|---|---|
| **Philosophy** | Logic; methods of reasoning; mind as physical system; foundations of learning, language, rationality | 올바른 사고와 합리성은 무엇이며, 마음을 물리적 체계로 이해할 수 있는가? |
| **Mathematics** | Formal representation and proof; algorithms; computation; (un)decidability; (in)tractability; probability | 지식과 추론을 형식화하고 계산 가능성·계산 비용·불확실성을 다룬다. |
| **Psychology** | Adaptation; perception and motor control; experimental techniques, psychophysics | 실제 인간의 적응·지각·운동 제어를 실험적으로 조사한다. |
| **Economics** | Formal theory of rational decisions | 여러 선택지 중 합리적인 결정을 내리는 기준을 제공한다. |
| **Linguistics** | Knowledge representation; grammar | 언어와 지식을 어떤 구조로 표현할지 다룬다. |
| **Neuroscience** | Plastic physical substrate for mental activity | 정신 활동을 가능하게 하는 변화 가능한 물리적 기반을 연구한다. |
| **Control theory** | Homeostatic systems; stability; simple optimal agent designs | 피드백으로 상태를 유지하고 적절한 제어 행동을 선택한다. |

### 학습 해설: 특히 구분할 용어

**(Un)decidability와 (In)tractability**는 다른 문제다. 전자는 일반적인 판정 절차가 존재하는가에 관한 것이고, 후자는 계산량 때문에 현실적으로 다루기 어려운가에 관한 것이다. 계산 가능하다고 해서 주어진 시간과 자원으로 쉽게 풀 수 있는 것은 아니다. 이는 Rational Agents의 계산 자원 제약과 연결된다.

**Plastic**은 재료로서의 플라스틱이 아니라 **변화하고 적응할 수 있는 성질**을 뜻한다. 신경과학의 문맥에서는 정신 활동의 물리적 기반이 고정된 구조만은 아니라는 의미로 읽는다.

**Homeostatic systems와 Stability**는 원하는 상태를 유지하고 시스템이 안정적으로 작동하도록 하는 문제와 연결된다. 이전 대화의 온도 조절 예시로 이해할 수 있다.

```text
목표 온도 설정
      ↓
현재 온도 측정 → 목표와 비교 → 냉방 조절
      ↑                            │
      └────── 변한 온도를 다시 측정 ┘
```

이것이 **Feedback**의 기본 흐름이다. 환경을 관찰하고 행동하며 결과를 다시 관찰한다는 점에서 에이전트와 연결된다.

일곱 분야는 순서대로 서로를 대체한 단계가 아니다. 논리·계산·인간 이해·의사결정·언어·뇌·제어라는 서로 다른 기반을 제공한 것이다.

<a id="history"></a>
## 8. The History of AI

### 8.1 전체 흐름

다음 연도와 구간은 **대화에 옮겨진 슬라이드 본문 표기**를 따른다. 구간이 겹치는 것은 서로 다른 연구 흐름이 함께 진행되었기 때문이다.

| 시기 | 슬라이드 제목 | 핵심 변화 |
|---|---|---|
| 1943–1955 | The gestation | 뉴런 모델, 학습 규칙, 기계 지능에 관한 질문 |
| 1956 | The birth | AI 연구 분야의 출범 |
| 1952–1969 | Early enthusiasm, great expectations | 초기 프로그램의 성공과 큰 기대 |
| 1966–1973 | A dose of reality | 현실 문제, 조합적 폭발, 접근법의 한계 |
| 1969–1979 | Knowledge-based systems: The key to power? | 전문지식과 지식 표현의 중요성 |
| 1980–present | AI becomes an industry | 전문가 시스템의 상업화와 산업 확대 |
| 1987–present | AI adopts the scientific method | 이론·실험 증거·현실 적용을 중시 |
| 1995–present | The emergence of intelligent agents | 에이전트와 인터넷 환경의 중요성 |
| 2001–present | The availability of very large data sets | 매우 큰 데이터 집합의 이용 가능성 |

> `present`는 강의자료의 표현을 보존한 것이다. 이 표가 작성 시점까지의 AI 역사를 망라한다는 뜻은 아니다.

### 8.2 The gestation: 1943–1955

**1943: McCulloch & Pitts**

뉴런의 모델을 제시하고 뇌를 Boolean circuit과 연결한다. 학습 관점에서는 생물학적 뉴런을 계산 가능한 형태로 표현하려는 출발점으로 이해한다.

**1949: Donald Hebb**

연결 강도를 수정하는 갱신 규칙, 즉 **Hebbian learning**이 등장한다. 앞 단계가 뉴런의 계산 모델이라면, 여기서는 연결이 변화하면서 학습할 수 있다는 점에 주목한다. 본문에 없는 세부 수식은 추가하지 않는다.

**1950: Turing**

슬라이드는 *Computing Machinery and Intelligence*를 Turing Test, machine learning, genetic algorithms, reinforcement learning과 관련된 아이디어를 소개하는 작업으로 정리한다. 이 표현은 강의의 역사적 요약이며, 오늘날의 각 분야가 당시 완성되었다는 뜻으로 확대하지 않는다.

```text
뉴런의 계산 모델 → 연결 강도의 변화와 학습 → 기계 지능에 관한 질문
```

### 8.3 The birth: 1956

슬라이드는 McCarthy와 함께 **2개월, 10명이 참여하는 AI 연구 구상**을 소개한다. 목표는 기계가 언어를 사용하고, 추상화와 개념을 형성하며, 인간의 영역으로 여겨졌던 문제를 해결하고, 스스로 개선하도록 하는 것이었다.

이후 20년간 중요한 역할을 하는 기관으로 **MIT, CMU, Stanford, IBM**이 제시된다. 학습의 초점은 여러 아이디어가 **AI라는 공동의 연구 목표로 묶였다**는 데 있다.

### 8.4 Early enthusiasm, great expectations: 1952–1969

슬라이드에는 다음 성과가 등장한다.

- **Geometry Theorem Prover, Logic Theorist, General Problem Solver, Playing checkers**
- McCarthy의 **Lisp(1958), Time sharing(1959), AdviceTaker**
- Minsky의 **Microworlds:** 대수 문장제와 blocks world

당시의 제한적인 컴퓨터와 프로그래밍 도구를 고려하면, 정리 증명이나 게임 수행은 큰 기대를 불러일으킬 만한 성과였다.

**Microworlds**는 제한된 문제 세계 안에서 지능적 문제 해결을 연구하는 흐름으로 이해한다. 대화에 옮겨진 본문의 `Microwords`는 문맥상 Microworlds로 정리했다.

슬라이드의 대수 문장제는 광고 수가 45일 때, 고객 수가 광고 수의 20%를 제곱한 값의 두 배라는 내용이다. 이를 식으로 옮기면 다음과 같다.

```text
광고 수 = 45
고객 수 = 2 × (0.2 × 45)²
        = 2 × 9²
        = 162
```

학습 포인트는 산술 계산 자체보다 **자연어로 표현된 관계를 계산 가능한 구조로 바꾸는 것**이다. 다만 제한된 세계에서의 성공이 곧 모든 현실 문제의 해결을 뜻하지는 않는다.

### 8.5 A dose of reality: 1966–1973

이 절의 중심은 초기의 기대가 현실 문제의 복잡성과 부딪혔다는 것이다.

**기계번역의 어려움**

슬라이드는 Sputnik과 러시아 과학 논문 번역의 맥락에서 1966년 보고서를 언급하고, 다음 문장 쌍을 제시한다. 대화에 옮겨진 보고서 표기는 `Alpack report`다.

```text
the spirit is willing but the flesh is weak
                ↓
the vodka is good but the meat is rotten
```

이 문장 쌍은 슬라이드가 제시한 **문맥을 놓친 번역의 예시**로 읽는다. 실제 시스템의 검증된 실행 기록이라고 별도로 단정하지 않는다. 학습상 의미는 단어 대응만으로 문장의 의미가 보존되지는 않는다는 것이다.

**Lighthill report, 1973**

슬라이드는 성공적으로 보였던 알고리즘이 현실 규모에서는 멈추거나 감당하지 못하고, **toy versions**에만 적합하다는 비판을 소개한다.

**Combinatorial explosion**

선택의 조합이 급격히 늘어나면 계산량이 커진다. 더 빠른 하드웨어와 더 큰 메모리만으로 해결될 것이라는 낙관론이 문제였다는 설명이다. 본문은 이와 함께 당시 genetic algorithms의 진전에 관한 부정적 평가도 언급한다. 이를 모든 시기의 유전 알고리즘에 대한 결론으로 일반화하지 않는다.

**Perceptron의 한계**

슬라이드는 두 입력이 서로 다른지를 인식하도록 2-input perceptron을 학습시킬 수 없다는 예를 든다. 이 절에서는 이를 당시 접근법의 표현·학습 한계를 보여주는 사례로 기억한다. 모든 종류의 신경망이 같은 과제를 해결할 수 없다는 주장으로 넓히지 않는다.

> **연도 확인:** 이전 대화의 해설에는 이 구간이 1966–1974로 적힌 곳이 있지만, 사용자가 옮긴 슬라이드 제목은 **1966–1973**이므로 이 노트는 후자를 따른다.

### 8.6 Knowledge-based systems: The key to power? 1969–1979

슬라이드는 **Dendral, Mycin**, Mycin의 **certainty factor**, **Prolog(1972, EU), Planner(US)** 를 제시한다.

학습 해설의 중심은 일반적인 문제 해결 절차뿐 아니라 **특정 분야의 지식**이 중요하다는 방향 전환이다. 어떤 문제를 푸는 데 필요한 지식을 갖추고 그것을 활용할 수 있어야 한다.

Minsky의 **Frames**는 특정 객체에 관한 사실과 종류의 분류 체계를 표현하는 방식으로 소개된다. 슬라이드는 이를 OOP의 뿌리와 연결한다. 여기서는 객체 관련 정보를 구조화한다는 연결까지만 이해하고, Frame과 OOP가 완전히 동일하다고 해석하지 않는다.

```text
범용적인 문제 해결 절차
          +
분야별 지식과 구조화된 표현
          ↓
지식 기반 시스템의 문제 해결 능력
```

### 8.7 AI becomes an industry: 1980–present

슬라이드가 소개하는 내용은 다음과 같다.

- 성공적인 상업용 전문가 시스템 **R1**과 연간 **4천만 달러 절감**이라는 성과.
- **1981년 일본의 Fifth Generation project:** Prolog를 실행하는 지능형 컴퓨터를 만들려는 10년 계획.
- 전문가 시스템·비전 시스템·로봇 등을 만드는 수백 개 회사.
- **The return of neural networks:** 기호적 접근을 보완하는 신경망의 귀환.

비용 절감 수치는 강의자료가 제시한 역사적 사례로 기록한다. 신경망의 귀환 역시 기호적 접근이 단순히 사라졌다는 의미가 아니다. 본문의 **complements the symbolic approaches**라는 관계를 기억한다.

### 8.8 AI adopts the scientific method: 1987–present

슬라이드의 세 가지 강조점은 다음과 같다.

1. 완전히 새로운 이론을 제안하기보다 **기존 이론 위에서 연구를 발전**시킨다.
2. 직관보다 **엄밀한 정리나 확실한 실험 증거**에 주장을 근거 짓는다.
3. 장난감 예제를 넘어 **현실 응용과의 관련성**을 보여 준다.

사례로 **Speech recognition(HMM), Data mining, Bayesian networks**가 등장한다. 슬라이드는 이 절에서 각 기법의 내부 알고리즘을 설명하지 않는다.

학습의 핵심은 그럴듯한 아이디어만으로 충분하지 않다는 것이다. 어떤 이론에 근거하며, 어떤 증거가 있고, 실제 문제에서 어떤 성과를 보이는지 평가하는 태도가 중요해진다.

### 8.9 Intelligent agents와 very large data sets

**The emergence of intelligent agents: 1995–present**

슬라이드는 **Internet**을 가장 중요한 환경이라고 강조한다. 앞에서 정의한 에이전트를 실제 활동 환경과 연결하는 부분이다. 인간의 내부 사고를 재현하는 문제를 넘어, 환경에서 정보를 얻고 행동하는 시스템으로 AI를 바라보는 흐름과 연결된다.

**The availability of very large data sets: 2001–present**

확인 가능한 본문에서는 매우 큰 데이터 집합을 이용할 수 있게 되었다는 항목으로 역사 서술을 마무리한다. 구체적인 후대 모델이나 추가 연표는 이 노트의 범위에 포함하지 않는다.

### 8.10 역사를 관통하는 문제

```text
초기 모델과 프로그램의 성공
             ↓
큰 기대와 낙관론
             ↓
현실 문제의 규모·문맥·계산량에서 한계
             ↓
지식, 표현, 학습, 검증 방법의 재검토
             ↓
새로운 성과와 응용
```

이 도식은 이해를 위한 요약이다. 모든 연구 분야가 같은 순서로 움직였다는 뜻은 아니다. Chapter Summary는 **성공 → 잘못된 낙관 → 관심과 연구비 축소**가 반복되었다는 점을 강조한다.

이전 대화에는 별도 연표 그림의 연도를 해설한 내용도 있으나, 이번 작성에서는 그 그림을 원본과 대조하지 못했으므로 본문에서 확인되는 구간을 중심으로 정리했다.

<a id="state-of-the-art"></a>
## 9. State of the Art

### 슬라이드 핵심

슬라이드는 **“Which of the following can be done at present?”** 라는 질문과 14개 과제를 제시한다. 확인 가능한 본문에는 각 항목의 가능·불가능에 대한 답이 없다.

따라서 이 절에서는 현재의 기술 수준을 추정해 Yes/No를 붙이지 않는다. 이전 대화에서 공부한 것처럼 **각 과제가 어떤 능력의 조합을 요구하는지**를 살펴본다.

### 과제별 요구 능력

아래의 영어 과제는 슬라이드 목록을 따르며, 오른쪽 열은 **이전 대화를 반영한 학습용 분석**이다. 요구 능력 표 자체가 원본 슬라이드에 있는 것은 아니다.

| 번호 | 슬라이드의 과제 | 요구 능력에 대한 학습 해설 |
|---|---|---|
| 1 | Play a decent game of table tennis | 공의 위치를 보는 지각, 궤적 예측, 빠른 판단, 실시간 로봇 제어 |
| 2 | Drive safely along a curving mountain road | 도로 인식, 경로 추종, 차량 제어 |
| 3 | Drive safely along Telegraph Avenue | 차량·보행자·신호 등 복잡한 상황의 인식과 판단, 행동 계획 |
| 4 | Buy a week's worth of groceries on the web | 상품 검색, 필요한 품목과 수량 선택, 온라인 주문 절차 수행 |
| 5 | Buy a week's worth of groceries at Berkeley Bowl | 실제 매장에서 이동, 상품 인식, 물체 집기, 운반과 결제 절차 수행 |
| 6 | Play a decent game of bridge | 보이지 않는 정보에 관한 추론, 전략, 불확실성 속의 의사결정 |
| 7 | Discover and prove a new mathematical theorem | 새로운 정리의 탐색과 발견, 논리적 추론과 증명 |
| 8 | Design and execute a research program in molecular biology | 가설 설정, 연구·실험 설계, 실제 수행, 결과 해석 |
| 9 | Write an intentionally funny story | 언어 생성, 맥락 이해, 의도한 유머 구성 |
| 10 | Give competent legal advice in a specialized area of law | 전문지식, 사실관계 이해, 사례에 맞는 추론과 설명 |
| 11 | Translate spoken English into spoken Swedish in real time | 음성인식, 언어 이해와 번역, 음성생성, 실시간 처리 |
| 12 | Converse successfully with another person for an hour | 언어 이해와 생성, 지식과 추론, 대화 맥락의 지속적 유지 |
| 13 | Perform a complex surgical operation | 상황 인식, 전문적 판단, 계획, 정밀한 물리적 제어 |
| 14 | Unload any dishwasher and put everything away | 다양한 물체 인식, 안전한 조작, 공간 이해, 보관 위치 판단, 행동 계획 |

### 학습 해설 1: 온라인 장보기와 실제 매장 장보기

사람에게는 둘 다 장보기지만 시스템이 처리할 환경과 행동은 다르다.

```text
온라인 장보기
상품 정보 탐색 → 선택 → 주문

실제 매장 장보기
이동 → 상품 발견·인식 → 집기 → 운반 → 결제
          + 주변 장애물과 물리적 상황에 대응
```

실제 매장에서는 디지털 정보 처리에 더해 지각과 로봇 조작이 요구된다. 같은 목표도 **환경에 따라 필요한 능력이 달라진다**는 점이 에이전트 관점과 연결된다.

### 학습 해설 2: 산길 운전과 Telegraph Avenue 운전

이전 대화에서는 산길의 도로 추종·제어와 도심의 다양한 대상·상황 판단을 대비했다. 이 대비는 운전이라는 이름 아래에서도 필요한 능력의 조합이 달라진다는 점을 보여 준다.

다만 슬라이드는 구체적인 도로 조건을 제시하지 않는다. 따라서 이를 모든 산길이 모든 도심 도로보다 쉽다는 일반 법칙으로 바꾸지 않는다.

### 학습 해설 3: 수학 정리와 식기세척기

수학 정리의 발견·증명은 형식화된 기호와 규칙을 활용하는 추론과 탐색으로 생각해 볼 수 있다. 반면 식기세척기 정리는 물체를 보고, 잡고, 옮기고, 적절한 곳에 보관하는 능력을 함께 요구한다.

특히 **any dishwasher**의 `any`는 정해진 장치와 배치에서만 성공하는 것보다 넓은 조건을 요구한다는 점에서 중요하다. 사람에게 일상적인 일이 기계에게도 반드시 쉬운 것은 아니다. 그렇다고 정리 증명 자체가 쉽다는 뜻은 아니다.

### 학습 해설 4: 과제의 조건을 놓치지 않기

`Decent`, `safely`, `intentionally`, `competent`, `in real time`, `for an hour`, `any`는 장식적인 단어가 아니다. 적절한 수준의 수행, 안전성, 의도, 전문성, 시간 제약, 지속성, 다양한 환경에서의 수행이라는 서로 다른 평가 조건을 담는다.

```text
과제와 환경
    ↓
어떤 정보를 얻어야 하는가?        Perception / Knowledge
무엇을 판단해야 하는가?          Reasoning / Decision making
어떤 행동을 수행해야 하는가?      Language / Planning / Robotics
어떤 조건으로 성과를 평가하는가?  수준·시간·안전성·지속성 등
```

이 슬라이드를 학습할 때는 기술의 가능 여부만 외우기보다 **지능이 여러 능력의 조합이며, 과제에 따라 그 조합과 평가 조건이 달라진다**는 점을 이해한다.

<a id="summary"></a>
## 10. Chapter Summary와 복습

### 10.1 원본 Summary의 핵심

1. **AI에는 서로 다른 목표와 접근이 있다.** 사고와 행동 중 무엇을 연구하는지, 인간과 이상적 기준 중 무엇을 기준으로 하는지 구분한다.
2. **Rational action**은 상황에서 가능한 최선의 행동을 선택하는 관점이다. 앞의 정의와 연결하면 이용 가능한 정보와 기대되는 목표 달성을 기준으로 이해한다.
3. **Philosophy**는 마음을 기계와 연결해 생각할 수 있다는 문제의식을 제공한다.
4. **Mathematics**는 논리적·확률적 진술을 다루는 기반을 제공한다.
5. **Economics**는 기대되는 결과를 최대화하는 의사결정과 연결된다.
6. **Neuroscience**는 뇌가 어떻게 작동하며 컴퓨터와 어떤 점에서 같고 다른지 연구한다.
7. **Psychology**는 인간을 정보처리 체계로 이해하는 관점을 제공한다.
8. **Control theory**는 피드백을 바탕으로 적절하게 행동하는 장치와 연결된다.
9. AI 역사는 성공, 잘못된 낙관, 그에 따른 관심과 연구비 축소의 반복을 보여 준다.

언어학은 앞의 **AI prehistory**에 포함되어 있지만, 대화에 옮겨진 마지막 Summary에는 별도 항목으로 나오지 않는다. 두 슬라이드의 구성을 구분해 기억한다.

### 10.2 Chapter 1의 개념 연결

```text
AI를 어떻게 정의할 것인가?
             │
             ├── 사고 / 행동
             └── 인간 / 합리성
                      ↓
이 강의의 중심: Acting rationally
                      ↓
환경을 인식하고 행동하는 Rational Agent
                      ↓
f : P* → A
지각 이력에 따라 행동을 선택
                      ↓
환경·과제에 맞는 성과와 계산 자원의 제약

이를 이해하는 배경
  ├── Prehistory: 여러 학문의 기여
  ├── History: 성공과 한계, 연구 방향의 변화
  └── State of the Art: 과제마다 다른 능력과 평가 조건
```

### 10.3 혼동하기 쉬운 구분

| 구분 | 기억할 차이 |
|---|---|
| Thinking humanly / Acting humanly | 인간의 실제 사고 과정 설명 / 인간처럼 보이는 지적 행동 평가 |
| Thinking rationally / Acting rationally | 올바른 추론 / 목표에 적절한 행동 선택 |
| Descriptive / Normative | 실제로 어떻게 하는가 / 어떻게 해야 올바른가 |
| Rationality / 결과의 성공 | 선택 시점의 정보에서 좋은 판단 / 실제로 나온 결과 |
| Percept / Percept history | 개별 관측 / 지금까지의 관측 시퀀스 |
| Agent function / 실제 프로그램 | 행동 대응의 추상적 정의 / 자원 제약 아래의 구현 |
| Undecidable / Intractable | 일반적 판정 절차의 부재 / 계산량에 따른 현실적 어려움 |
| 제한된 문제의 성공 / 현실 적용 | 작은 문제에서의 성과 / 크고 복잡한 환경에서도 유효한 성과 |
| 자료의 at present / 현재 기술 수준 | 강의자료 당시의 질문 / 별도 확인이 필요한 현재의 사실 |

### 10.4 스스로 설명해 볼 질문

- [ ] AI의 네 접근을 두 축으로 나누고 각각의 질문을 말할 수 있는가?
- [ ] Turing Test가 Thinking humanly의 검증과 다른 이유를 설명할 수 있는가?
- [ ] Cognitive Science에서 추상화 수준과 검증 방법이 왜 중요한지 설명할 수 있는가?
- [ ] 올바른 논리적 추론만으로 적절한 행동이 자동 결정되지 않는 이유를 말할 수 있는가?
- [ ] Rational action에서 available information과 expected가 중요한 이유를 설명할 수 있는가?
- [ ] `f : P* → A`의 각 기호와 지각 이력의 의미를 정확히 설명할 수 있는가?
- [ ] 합리적 행동의 이상적 기준과 실제 계산 자원의 제약을 구분할 수 있는가?
- [ ] 일곱 기반 학문을 앞에서 배운 개념과 연결할 수 있는가?
- [ ] 초기 성공이 현실 규모의 성공으로 바로 이어지지 않은 이유를 설명할 수 있는가?
- [ ] 지식 기반 시스템, 과학적 검증, 에이전트, 대규모 데이터의 흐름을 말할 수 있는가?
- [ ] State of the Art의 14개 과제를 단순 Yes/No 대신 요구 능력과 조건으로 설명할 수 있는가?

---

**자료 출처:** AI-ch01.pdf에서 사용자가 옮긴 슬라이드 본문 및 「대학원 수업 정리」 대화의 해설. 원본 PDF 페이지와 그림은 미대조. 외부 자료를 통한 보완 없음.

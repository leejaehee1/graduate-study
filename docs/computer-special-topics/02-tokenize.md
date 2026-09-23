# 2장. 텍스트 토큰화

> 컴퓨터특론 · *밑바닥부터 만들면서 배우는 LLM*
> 원본: `2장_요약본.pdf` + `2장_실습.ipynb`
> 이전 장: [1장. LLM 이해하기](01-understanding_LLM.md) · 다음 장: [3장. 데이터 샘플링과 임베딩](03-sampling_embedding.md)

---

## 📌 목차

1. [왜 임베딩인가](#1-왜-임베딩인가)
2. [Word2Vec와 임베딩 공간](#2-word2vec와-임베딩-공간)
3. [LLM의 자체 임베딩과 차원](#3-llm의-자체-임베딩과-차원)
4. [LLM의 텍스트 처리 파이프라인](#4-llm의-텍스트-처리-파이프라인)
5. [정규 표현식으로 텍스트 분할](#5-정규-표현식으로-텍스트-분할)
6. [어휘사전 구축](#6-어휘사전-구축)
7. [SimpleTokenizerV1](#7-simpletokenizerv1--양방향-변환-클래스)
8. [단순 토크나이저의 한계](#8-단순-토크나이저의-한계--알지-못하는-단어)
9. [특수 문맥 토큰](#9-특수-문맥-토큰)
10. [SimpleTokenizerV2](#10-simpletokenizerv2--알지-못하는-단어-처리)
11. [그 밖의 특수 토큰과 GPT의 선택](#11-그-밖의-특수-토큰과-gpt의-선택)
12. [BPE와 tiktoken](#12-bpe와-tiktoken)
13. [BPE 어휘사전 구축 원리](#13-bpe-어휘사전-구축-원리)
14. [요약](#14-요약) · [퀴즈](#15-셀프-체크-퀴즈)

### 🎯 학습 목표

- 신경망이 원시 텍스트를 그대로 처리하지 못하는 이유와 **벡터로 변환**해야 하는 이유
- **정규 표현식**을 기준으로 삼는 단순 토크나이저의 직접 구현
- **어휘사전** 구축과 토큰 ↔ 토큰 ID의 상호 변환
- 특수 문맥 토큰 `<|unk|>`와 `<|endoftext|>`가 맡는 역할
- **바이트 페어 인코딩(BPE)** 의 원리와 `tiktoken` 라이브러리 사용법

### 이 장의 위치

```
[원시 텍스트] ──▶ [토큰화] ──▶ [토큰 ID] ──▶ [토큰 임베딩] ──▶ [GPT 디코더] ──▶ [출력 텍스트]
               └──────── 2장 ────────┘       └── 3장 ──┘        └─ 4장~ ─┘
```

---

## 1. 왜 임베딩인가

| | 내용 |
|---|---|
| **문제** | 신경망은 **수치 연산**으로 동작하는데, 텍스트는 **범주형 데이터**라서 그 연산을 적용할 수 없다 |
| **해결** | 각 단어를 **실수 벡터**로 표현하면 값끼리 더하고 곱할 수 있고 **거리도 계산**된다 |

> **임베딩 (embedding)**: 단어·이미지·문서처럼 서로 떨어져 있는(이산적인) 대상을 **연속적인 벡터 공간의 한 점**으로 대응시키는 변환. 공간의 값이 이어져 있으므로 대상들이 **하나의 좌표계 위**에 놓인다.

- 임베딩 모델은 **데이터 형식마다 다르다** → 텍스트용 모델은 오디오나 비디오에 쓸 수 없다.
- 임베딩의 단위

| 종류 | 무엇을 벡터 하나로? | 쓰임 |
|---|---|---|
| **단어 임베딩** | 단어 하나 | LLM 입력 |
| **문장 임베딩** | 문장·단락 전체 | **검색 증강 생성(RAG)** 에서 널리 사용 |

> 💡 **[보충] "범주형"이란?** '고양이', '강아지'에 번호 1, 2를 붙여도 "강아지 = 고양이 × 2"가 아니다. 번호는 **이름표일 뿐 크기나 거리 의미가 없다**. 그래서 의미를 담은 벡터가 필요하다.

---

## 2. Word2Vec와 임베딩 공간

임베딩을 실제로 만드는 **초기의 대표적 방법**이다.

| 항목 | 내용 |
|---|---|
| **훈련 방식** | 단어마다 **무작위 값의 벡터**로 시작 → 타깃 단어로 **주변 문맥 단어를 예측**(반대 방향도 가능) → 틀린 만큼 벡터를 조정 → 대량의 텍스트로 반복 |
| **핵심 아이디어** | 훈련 목표는 예측이었지만 결과적으로 **의미가 반영**된다. 문맥이 비슷한 단어는 예측 대상도 비슷해서 벡터도 비슷해진다. 즉 **비슷한 맥락에 등장하는 단어는 비슷한 의미** |
| **시각화** | 학습된 벡터를 2차원으로 줄이면 비슷한 개념의 단어끼리 가깝게 놓인다 |
| **임베딩 차원** | 벡터를 이루는 값의 개수. 1부터 수천까지 가능. **고차원일수록 미묘한 관계까지 표현**되지만 **계산 효율은 떨어짐** |

```
 2차원으로 줄여 본 임베딩 공간 (개념도)

   ▲
   │   eagle  duck           ← 새
   │      goose
   │                  Berlin  London     ← 도시
   │                      Paris
   │  short
   │  long  longest          ← 길이 형용사
   └────────────────────────────▶
```

---

## 3. LLM의 자체 임베딩과 차원

LLM은 Word2Vec처럼 **만들어 둔 임베딩을 쓰지 않고 직접 만든다**.

| 항목 | Word2Vec | LLM |
|---|---|---|
| 임베딩의 자리 | 따로 학습해 둔 것을 **가져다 씀** | 임베딩을 **입력층의 일부**로 포함, 모델 훈련 때 **함께 갱신** |
| 장점 | – | 그 모델이 다룰 **데이터와 작업에 맞게** 값이 정해짐 |

- **은닉 상태 (hidden state)**: 임베딩 크기 = 은닉 상태의 차원. 768로 정하면 그 벡터는 모델을 통과하는 동안 **768차원을 유지**
- **트레이드오프**: 차원↑ → 표현력↑, 그러나 계산량·메모리↑. 사람은 3차원까지만 그림으로 볼 수 있어 고차원 임베딩은 시각화가 어렵다.

| 모델 | 파라미터 | 임베딩 차원 |
|---|---|---|
| GPT-2 가장 작은 모델 | 117M · 125M | **768** |
| GPT-3 가장 큰 모델 | 175B | **12,288** |

**임베딩 준비 순서**: 텍스트를 **단어로 분할** → 단어를 **토큰(ID)으로 변환** → 토큰을 **임베딩 벡터로 변환**

---

## 4. LLM의 텍스트 처리 파이프라인

```
┌────────────────────── 입력 준비 ───────────────────────┐   ┌──── 모델이 하는 일 ────┐
│ 입력 텍스트        "This is an example."              │   │                        │
│   ↓ 토큰화                                            │   │  디코더 전용 트랜스포머  │
│ 토큰화된 텍스트    This / is / an / example / .       │──▶│  (GPT는 디코더만)       │──▶ 후처리 ──▶ 출력 텍스트
│   ↓                                                   │   │                        │
│ 토큰 ID           [정수, 정수, 정수, 정수, 정수]       │   └────────────────────────┘
│   ↓                                                   │
│ 토큰 임베딩        [벡터, 벡터, 벡터, 벡터, 벡터]       │
└───────────────────────────────────────────────────────┘
       ▲ 이 장에서 다루는 범위: 토큰화 + 토큰 ID까지
```

| 용어 | 정의 |
|---|---|
| **토큰** | 개별 단어이거나 **구두점 같은 특수 문자** |
| **토큰화** | 텍스트를 토큰 단위로 나누는 작업. 단어 넷 + 마침표 하나 = **5토큰** |
| **토큰 ID** | 각 토큰에 대응시킨 **정수** |
| **토큰 임베딩** | 토큰 ID를 **벡터로** 변환한 것 (3장) |

---

## 5. 정규 표현식으로 텍스트 분할

> ### 🧪 실습 준비: 훈련 텍스트 로드
>
> 이디스 워튼의 단편소설 **The Verdict**를 사용한다.
>
> ```python
> import os, urllib.request
> if not os.path.exists("the-verdict.txt"):
>     url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/"
>            "main/ch02/01_main-chapter-code/the-verdict.txt")
>     urllib.request.urlretrieve(url, "the-verdict.txt")
>
> with open("the-verdict.txt", "r", encoding="utf-8") as f:
>     raw_text = f.read()
> print("총 문자 개수:", len(raw_text))   # 20479
> print(raw_text[:99])
> # I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough--so it was no
> ```

토큰은 **단어이거나 특수 문자**여야 하므로 자르는 기준을 **세 번에 걸쳐 확장**한다.

| 시도 | 분할 기준 | 결과와 문제점 |
|---|---|---|
| **1** | 공백 | 공백이 결과에 항목으로 들어가고, **쉼표·마침표가 앞 단어에 붙은 채** 남음 |
| **2** | 공백 · 쉼표 · 마침표 | 공백만 남은 항목을 제외하면 각 항목이 **단어 또는 특수 문자**가 됨 |
| **3** | 쉼표 · 마침표 · 콜론 · 세미콜론 · 물음표 · 밑줄 · 느낌표 · 큰따옴표 · 괄호 · 작은따옴표 · **이중 대시** · 공백 | 물음표가 단어에 붙으면 `test?`와 `test`가 **다른 토큰**이 되므로 기준을 미리 넓힘 |

> ### 🧪 실습: 정규 표현식 3단계
>
> ```python
> import re
>
> text = "Hello, world. This, is a test."
>
> # 시도 1) 공백 기준 분할 — 괄호 ()로 감싸면 구분자도 결과에 남는다
> result = re.split(r'(\s)', text)
> print(result)
> # ['Hello,', ' ', 'world.', ' ', 'This,', ' ', 'is', ' ', 'a', ' ', 'test.']
>
> # 시도 2) 공백 + 쉼표/마침표, 그리고 빈 문자열/공백 항목 제거
> result = re.split(r'([,.]|\s)', text)
> result = [item for item in result if item.strip()]
> print(result)
> # ['Hello', ',', 'world', '.', 'This', ',', 'is', 'a', 'test', '.']
>
> # 시도 3) 물음표, 이중 대시(--) 등까지 확장
> text = "Hello, world. Is this-- a test?"
> result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
> result = [item.strip() for item in result if item.strip()]
> print(result)   # 10개 토큰
> # ['Hello', ',', 'world', '.', 'Is', 'this', '--', 'a', 'test', '?']
> ```
>
> **정규 표현식 해부** `r'([,.:;?_!"()\']|--|\s)'`
>
> | 부분 | 의미 |
> |---|---|
> | `( ... )` | **캡처 그룹** — 구분자 자체도 결과 리스트에 남긴다 (없으면 구두점이 사라짐) |
> | `[,.:;?_!"()\']` | 대괄호 안 문자 **중 하나** (쉼표, 마침표, 콜론, …, 작은따옴표) |
> | `--` | 이중 대시 (두 글자짜리라 대괄호 밖에 따로) |
> | `\s` | 공백 문자 (스페이스, 탭, 줄바꿈) |
> | `\|` | "또는" |
> | `item.strip()` | 앞뒤 공백 제거. 빈 문자열이면 False → 리스트에서 제외 |

**설계 결정 두 가지**

| 결정 | 이유 |
|---|---|
| **대문자를 소문자로 바꾸지 않음** | 고유 명사 구분, 문장 구조 이해, **대문자 생성**에 도움 |
| **공백을 제거함** | 다룰 항목이 줄어 메모리·계산 절감. 단, **파이썬 코드처럼 들여쓰기가 의미를 갖는 텍스트에서는 유지**해야 함 |

> 💡 **토큰화에는 정해진 답이 없다.** 무엇을 자르고 무엇을 버릴지 정하는 것이 설계이며, 그 결정에 따라 모델이 처리할 토큰 수가 달라진다.

> ### 🧪 실습: 소설 전체 토큰화
>
> ```python
> preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
> preprocessed = [item.strip() for item in preprocessed if item.strip()]
> print("토큰 개수:", len(preprocessed))   # 4690
> print(preprocessed[:30])
> # ['I', 'HAD', 'always', 'thought', 'Jack', 'Gisburn', 'rather', 'a', 'cheap', 'genius',
> #  '--', 'though', 'a', 'good', 'fellow', 'enough', '--', 'so', 'it', 'was', 'no', ...]
> ```
>
> → 공백을 제외한 토큰 **4,690개**

---

## 6. 어휘사전 구축

- **필요한 이유**: 나뉜 토큰은 아직 **문자열**이라 모델이 처리하지 못한다.
- **토큰 ID**: 각 토큰에 대응시킨 **고유한 정수**. 임베딩 벡터로 바꾸기 직전의 중간 단계
- **어휘사전 (vocabulary)**: 그 대응 관계를 정리한 것. "사전"이지만 **의미 정보는 담지 않고** 어떤 토큰이 몇 번인지만 기록

```
[1단계 토큰화]              [2단계 중복 제거와 정렬]        [3단계 토큰 ID 부여]
훈련 세트 전체를 분할  ──▶  고유 토큰만 남김 → 알파벳 순  ──▶  0부터 차례로 정수 대응
   4,690개                     1,130개                        {'!': 0, '"': 1, ...}
```

> ### 🧪 실습: 어휘사전 만들기
>
> ```python
> all_words = sorted(set(preprocessed))   # set: 중복 제거 / sorted: 정렬
> vocab_size = len(all_words)
> print("어휘사전 크기:", vocab_size)       # 1130
>
> vocab = {token: integer for integer, token in enumerate(all_words)}
> ```
>
> **처음 몇 항목**
>
> | 토큰 | ID | | 토큰 | ID |
> |---|---|---|---|---|
> | `!` | 0 | | `A` | 11 |
> | `"` | 1 | | `Ah` | 12 |
> | `'` | 2 | | `Among` | 13 |
> | `(` | 3 | | `And` | 14 |
> | `,` | 5 | | … | … |
> | `--` | 6 | | `Gisburn` | 38 |
> | `.` | 7 | | `HAD` | 44 |
> | `?` | 10 | | `Hermia` | 50 |

- **결과**: 토큰 4,690개 → 중복 제거 → **고유 토큰 1,130개** = 어휘사전 크기
- **앞쪽이 구두점인 이유**: 정렬 기준이 **문자 코드값**(유니코드)이라 **기호 → 대문자 → 소문자** 순. 0~10번이 구두점·특수 문자, 11번부터 대문자 단어
- **적용 범위**: 한 번 만든 어휘사전은 새 텍스트에도 쓸 수 있지만, **사전에 없는 토큰이 나오면 문제**가 된다 (8절)

---

## 7. SimpleTokenizerV1 — 양방향 변환 클래스

분할 기준과 어휘사전을 하나로 묶어, **텍스트 ↔ 토큰 ID**를 오갈 수 있는 도구로 만든다.

| 메서드 | 하는 일 | 세부 |
|---|---|---|
| `__init__` | 어휘사전을 **두 형태로** 저장 | 어휘사전은 문자열이 키라서 문자열 → ID만 조회 가능. 키와 값을 뒤집은 **역어휘사전**을 함께 두어야 양방향이 성립 |
| `encode` | 텍스트 → 토큰 ID 목록 | 구두점·특수 문자 기준으로 분할 → 공백 항목 제외 → 각 토큰을 어휘사전에서 조회 |
| `decode` | 토큰 ID 목록 → 텍스트 | 역어휘사전으로 문자열 복원 → **공백으로 연결** → **구두점 앞의 공백 제거** |

> ### 🧪 실습: SimpleTokenizerV1
>
> ```python
> class SimpleTokenizerV1:
>     def __init__(self, vocab):
>         self.str_to_int = vocab                              # 문자열 -> 정수
>         self.int_to_str = {i: s for s, i in vocab.items()}   # 정수 -> 문자열 (역어휘사전)
>
>     def encode(self, text):
>         preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
>         preprocessed = [item.strip() for item in preprocessed if item.strip()]
>         ids = [self.str_to_int[s] for s in preprocessed]
>         return ids
>
>     def decode(self, ids):
>         text = " ".join([self.int_to_str[i] for i in ids])
>         text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)      # 구두점 앞의 공백 삭제
>         return text
>
> tokenizer = SimpleTokenizerV1(vocab)
> text = """"It's the last he painted, you know,"
>        Mrs. Gisburn said with pardonable pride."""
> ids = tokenizer.encode(text)
> print(ids)
> print(tokenizer.decode(ids))
> ```
>
> **실행 결과**
> ```
> [1, 56, 2, 850, 988, 602, 533, 746, 5, 1126, 596, 5, 1, 67, 7, 38, 851, 1108, 754, 793, 7]
> " It' s the last he painted, you know," Mrs. Gisburn said with pardonable pride.
> ```
>
> **`re.sub(r'\s+([,.?!"()\'])', r'\1', text)` 해석**
> - `\s+([,.?!...])`: "공백 1개 이상 + 구두점"을 찾아서
> - `r'\1'`: 첫 번째 캡처 그룹(구두점)만 남긴다 → 구두점 **앞의** 공백 삭제

**⚠️ 복원이 완전하지 않은 이유**

- `encode`가 공백 항목을 버리므로 **원문의 띄어쓰기 정보가 남지 않는다**.
- `decode`는 토큰 사이마다 공백을 넣고 **구두점 앞만** 지우므로, **구두점 뒤**에 들어간 공백은 그대로 남는다.
- 실제 출력: `"It's` → `" It' s` (큰따옴표 뒤, 작은따옴표 뒤 두 곳)

---

## 8. 단순 토크나이저의 한계 — 알지 못하는 단어

> ### 🧪 실습: 미등록 단어
>
> ```python
> text = "Hello, do you like tea?"
> try:
>     print(tokenizer.encode(text))
> except KeyError as e:
>     print("KeyError:", e, "-> 어휘사전에 없는 단어라 인코딩 불가")
> # KeyError: 'Hello' -> 어휘사전에 없는 단어라 인코딩 불가
> ```

| | 내용 |
|---|---|
| **증상** | 사전에 없는 단어가 든 문장을 `encode`에 넘기면 **KeyError** 발생 |
| **원인** | 어휘사전을 **소설 한 편**으로 만들었으므로, 일상에서 흔한 단어라도 소설에 안 나오면 조회 불가 ('Hello'는 소설에 없음) |
| **근본 한계** | **단어 목록으로 사전을 만드는 한** 이 문제는 사라지지 않는다. 더 큰 텍스트로 만들어도 새 단어는 계속 나온다 |

**대응은 두 가지** ⭐

| | 방법 | 적용 |
|---|---|---|
| ① | 모르는 단어를 **특수 문맥 토큰 하나로 대체** (`<\|unk\|>`) | 9–10절, SimpleTokenizerV2 |
| ② | 모르는 단어를 사전에 있는 **부분단어(subword)들로 분할** | 12–13절, **GPT가 택한 방식 (BPE)** |

---

## 9. 특수 문맥 토큰

| 토큰 | 뜻 | 역할 |
|---|---|---|
| `<\|unk\|>` | **unk**nown | 사전에 없는 단어를 이 토큰으로 **대체**. 대체할 토큰이 사전에 있으므로 조회가 실패하지 않음 |
| `<\|endoftext\|>` | 텍스트의 끝 | **서로 무관한 텍스트 사이의 경계** 표시. 여러 문서로 훈련할 때 각 텍스트 앞에 넣는 것이 일반적. 이 표시가 없으면 모델은 앞 텍스트의 끝과 뒤 텍스트의 시작을 **하나로 이어진 문장**으로 봄 |

```
문서 A: "...그리고 그들은 행복하게 살았다."  <|endoftext|>  문서 B: "2024년 3분기 실적은..."
                                        ↑ "여기서 이야기가 끊긴다"는 신호
```

> ### 🧪 실습: 특수 토큰 추가
>
> ```python
> all_tokens = sorted(list(set(preprocessed)))
> all_tokens.extend(["<|endoftext|>", "<|unk|>"])     # 정렬 "후"에 추가 → 맨 뒤
> vocab = {token: integer for integer, token in enumerate(all_tokens)}
> print("확장된 어휘사전 크기:", len(vocab.items()))   # 1132
>
> for item in list(vocab.items())[-5:]:
>     print(item)
> # ('younger', 1127)
> # ('your', 1128)
> # ('yourself', 1129)
> # ('<|endoftext|>', 1130)
> # ('<|unk|>', 1131)
> ```

- 정렬을 마친 **뒤에** 추가하므로 알파벳 순서에 들어가지 않고 **맨 뒤**에 놓인다.
- 결과: 1,130 → **1,132**. `<|endoftext|>` = **1130**, `<|unk|>` = **1131**

---

## 10. SimpleTokenizerV2 — 알지 못하는 단어 처리

> ### 🧪 실습: SimpleTokenizerV2
>
> ```python
> class SimpleTokenizerV2:
>     def __init__(self, vocab):
>         self.str_to_int = vocab
>         self.int_to_str = {i: s for s, i in vocab.items()}
>
>     def encode(self, text):
>         preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
>         preprocessed = [item.strip() for item in preprocessed if item.strip()]
>         preprocessed = [item if item in self.str_to_int else "<|unk|>"   # ★ 추가된 줄
>                         for item in preprocessed]
>         ids = [self.str_to_int[s] for s in preprocessed]
>         return ids
>
>     def decode(self, ids):
>         text = " ".join([self.int_to_str[i] for i in ids])
>         text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
>         return text
>
> text1 = "Hello, do you like tea?"
> text2 = "In the sunlit terraces of the palace."
> text = " <|endoftext|> ".join((text1, text2))
>
> tokenizer = SimpleTokenizerV2(vocab)
> print(tokenizer.encode(text))
> print(tokenizer.decode(tokenizer.encode(text)))
> ```
>
> **실행 결과**
> ```
> Hello, do you like tea? <|endoftext|> In the sunlit terraces of the palace.
> [1131, 5, 355, 1126, 628, 975, 10, 1130, 55, 988, 956, 984, 722, 988, 1131, 7]
> <|unk|>, do you like tea? <|endoftext|> In the sunlit terraces of the <|unk|>.
> ```
>
> - `Hello` → **1131** (`<|unk|>`), `palace` → **1131** (`<|unk|>`)
> - `<|endoftext|>` → **1130**
>
> ⚠️ `<|endoftext|>`는 분할 정규식의 구두점 목록에 `<`, `|`, `>`가 없어서 **한 덩어리로 남기** 때문에 사전에서 조회된다.

**V1 → V2 변화 정리**

| 구분 | 내용 |
|---|---|
| **해결한 것** | 사전에 없는 토큰을 `<\|unk\|>`로 대체 → 어떤 문장이든 **오류 없이** 인코딩 |
| **남은 문제** | 서로 다른 미등록 단어가 **모두 같은** `<\|unk\|>`가 되어 구분 불가. 디코딩해도 **원래 단어가 돌아오지 않음** (Hello, palace → 둘 다 `<\|unk\|>`) |
| **두 특수 토큰의 차이** | `<\|endoftext\|>`는 원문에 **직접 넣은** 토큰이라 그대로 복원. `<\|unk\|>`는 인코딩 과정에서 **생긴** 것이라 되돌릴 원본이 없음 |
| **코드 차이** | 대체 처리 한 줄 추가 + 구두점 목록에 **콜론·세미콜론** 추가 |

---

## 11. 그 밖의 특수 토큰과 GPT의 선택

| 토큰 | 의미 | 용도 |
|---|---|---|
| `[BOS]` | **b**eginning **o**f **s**equence | 텍스트가 **시작**하는 자리 표시 |
| `[EOS]` | **e**nd **o**f **s**equence | 텍스트가 **끝나는** 자리 표시. 무관한 텍스트를 연결할 때 유용하며 `<\|endoftext\|>`와 같은 역할 |
| `[PAD]` | **pad**ding | 여러 텍스트를 함께 처리하려면 길이가 같아야 하므로, 가장 긴 텍스트 기준으로 **나머지 뒤를 채움** |

**GPT의 선택** ⭐

| 선택 | 이유 |
|---|---|
| `<\|endoftext\|>` **하나만** 사용 | 문서들을 이 토큰으로 연결하면 **끝 표시와 시작 표시를 하나가 겸함** |
| **패딩도 같은 토큰** | 채운 부분은 훈련 때 **마스크로 계산에서 제외**되므로 무엇으로 채우든 결과가 같음 |
| `<\|unk\|>`도 **쓰지 않음** | 단어를 부분단어로 나눠 표현하는 **BPE**를 채택했기 때문 |

---

## 12. BPE와 tiktoken

두 대응 중 **두 번째(부분단어 분할)** 방식. `<|unk|>`가 원래 단어를 잃는 문제에 대한 답이다.

| 항목 | 내용 |
|---|---|
| **BPE** (byte pair encoding) | GPT-2·GPT-3의 훈련에 쓴 토큰화 방법 |
| **tiktoken** | 구현이 복잡해서 사용하는 오픈AI의 오픈 소스 라이브러리 (**Rust**로 제작 → 빠름) |
| **어휘사전 규모** | GPT-2 BPE: **50,257**. `<\|endoftext\|>`에 가장 큰 값 **50256**이 대응 (앞서 만든 1,130개와는 규모 자체가 다름) |

> ### 🧪 실습: tiktoken으로 BPE 인코딩·디코딩
>
> ```python
> import tiktoken
> tokenizer = tiktoken.get_encoding("gpt2")
>
> text = (
>     "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
>     " of someunknownPlace."
> )
> integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
> print(integers)
> print(tokenizer.decode(integers))
> ```
>
> **실행 결과**
> ```
> [15496, 11, 466, 345, 588, 8887, 30, 220, 50256, 554, 262, 4252, 18250, 8812, 2114, 286, 617, 34680, 27271, 13]
> Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace.
> ```
>
> **관찰 포인트**
> - `<|endoftext|>` → **50256** (어휘사전의 마지막 번호)
> - `allowed_special={"<|endoftext|>"}` 을 **명시해야** 특수 토큰으로 인식된다. 안 하면 오류가 난다 (사용자 입력에 특수 토큰 문자열이 섞여 들어오는 것을 막기 위한 안전장치). **[보충]**
> - `Hello`, `palace` 대신 쓴 `someunknownPlace`까지 **원문과 완전히 같게 복원**된다. V2가 `<|unk|>`로 원래 단어를 잃은 것과 대비된다.
> - `sunlit` → `4252, 18250` (` sun` + `lit`), `terraces` → ` terr` + `aces`, `someunknownPlace` → ` some` + `unknown` + `Place` 처럼 **부분단어로 나뉘었다**. **[보충]**

**분할 예시**: 실제로 존재하지 않는 문자열 `"Akwirw ier"`

```
"Akwirw ier"  →  [33901, 86, 343, 86, 220, 959]
              →   "Ak" / "w" / "ir" / "w" / " " / "ier"     (6토큰)
```

- **공백까지 토큰**으로 두므로 원래 위치가 보존 → 원문이 **그대로 복원**된다.

**[보충] 더 해 보기** (tiktoken으로 확인한 결과)

| 입력 | 토큰 | 분할 |
|---|---|---|
| `tokenization` | 2개 | `token` / `ization` |
| `unhappiness` | 3개 | `un` / `h` / `appiness` |
| `Hello world` | 2개 | `Hello` / ` world` |
| `안녕` | 6개 | 바이트 6개 (한글 한 글자 = UTF-8 3바이트) |

→ 한글이 1장 실습에서 토큰이 많이 나온 이유: 사전에 한글 조합이 거의 없어 **바이트 단위까지** 쪼개진다. 그래도 BPE는 **바이트**에서 출발하므로 **어떤 문자든 표현 가능**하다.

---

## 13. BPE 어휘사전 구축 원리

사전에 없는 단어까지 복원되는 이유는 **사전을 만드는 방식**에 있다. **단어에서 시작하지 않고, 문자에서 출발해 단어까지 올라가며** 만든다.

```
[1단계 시작]                    [2단계 병합]                       [3단계 반복]
개별 문자를 전부 사전에 추가  ──▶  자주 함께 나오는 조합을 통합  ──▶  부분단어끼리 다시 병합
→ 어떤 단어든 최소한             "d"+"e" → "de"                    → 흔한 단어는 한 토큰
  문자 단위로는 표현 가능          (define, depend, made, hidden)
```

- **병합 결정 기준 = 최소 빈도**: 정해 둔 횟수 이상 등장한 조합만 병합
- 존재하지 않는 문자열(`Akwirw`)이 짧게 나뉜 것도 그 문자 조합이 **자주 나오지 않아 병합 대상이 되지 못한** 결과
- **결과**: 어떤 단어든 사전에 있는 부분단어의 조합으로 표현 → **`<|unk|>`가 필요 없고**, 훈련 데이터에 없던 단어도 처리된다

> ### 🧪 [보충] 실습: BPE 병합을 직접 돌려 보기
>
> 강의 노트북에는 없지만, BPE가 어떻게 사전을 키우는지 눈으로 확인할 수 있는 작은 코드다. (직접 실행해 결과를 확인함)
>
> ```python
> from collections import Counter
>
> corpus = ["low"]*5 + ["lower"]*2 + ["newest"]*6 + ["widest"]*3
> # 단어를 문자 단위로 쪼개고 단어 끝 표시 </w> 추가
> words = Counter(tuple(w) + ("</w>",) for w in corpus)
>
> def merge_step(words):
>     pairs = Counter()
>     for w, c in words.items():                 # 인접한 두 기호 쌍의 빈도 세기
>         for a, b in zip(w, w[1:]):
>             pairs[(a, b)] += c
>     best, cnt = pairs.most_common(1)[0]        # 가장 자주 나온 쌍
>     new = Counter()
>     for w, c in words.items():                 # 그 쌍을 하나로 합치기
>         out, i = [], 0
>         while i < len(w):
>             if i < len(w) - 1 and (w[i], w[i+1]) == best:
>                 out.append(w[i] + w[i+1]); i += 2
>             else:
>                 out.append(w[i]); i += 1
>         new[tuple(out)] += c
>     return best, cnt, new
>
> for step in range(1, 6):
>     best, cnt, words = merge_step(words)
>     print(step, best, cnt)
> ```
>
> **실행 결과**
>
> | 단계 | 병합한 쌍 | 빈도 | 병합 후 예 |
> |---|---|---|---|
> | 1 | `e` + `s` → `es` | 9 | n e w **es** t |
> | 2 | `es` + `t` → `est` | 9 | n e w **est** |
> | 3 | `est` + `</w>` → `est</w>` | 9 | n e w **`est</w>`** (단어 끝의 est) |
> | 4 | `l` + `o` → `lo` | 7 | **lo** w |
> | 5 | `lo` + `w` → `low` | 7 | **low** `</w>`, **low** e r |
>
> 💡 newest(6회)와 widest(3회)에 공통인 `est`가 먼저 합쳐지고, 자주 나오는 `low`가 한 토큰이 되었다. 처음 보는 단어 `lowest`도 이제 `low` + `est</w>` **두 토큰**으로 표현할 수 있다. (빈도가 같은 쌍이 여럿이면 먼저 센 쌍이 선택된다)

---

## 14. 요약

- 신경망은 숫자만 다루므로 텍스트를 **토큰 → 토큰 ID → 임베딩 벡터**로 바꿔야 한다.
- **Word2Vec**: 주변 단어 예측으로 의미가 담긴 벡터를 얻음. **LLM**은 임베딩을 입력층에 넣어 **함께 훈련**
- 임베딩 차원: GPT-2 small **768**, GPT-3 **12,288**
- **정규식 토큰화**: 구두점·이중 대시·공백 기준 분할, 대소문자 유지, 공백 제거 → 소설 **4,690토큰**
- **어휘사전**: 중복 제거 + 정렬 + 번호 → **1,130개** (구두점 → 대문자 → 소문자 순)
- **SimpleTokenizerV1**: encode/decode + 역어휘사전. 미등록 단어에서 **KeyError**
- **특수 토큰**: `<|unk|>`(미등록 단어 대체), `<|endoftext|>`(문서 경계) → **1,132개**
- **SimpleTokenizerV2**: 오류는 없지만 `<|unk|>`로 **원래 단어를 잃음**
- GPT는 `<|endoftext|>` 하나만 사용 (끝·시작·패딩 겸용), `<|unk|>` 없음
- **BPE** (tiktoken, 50,257개): 문자에서 출발해 자주 나오는 쌍을 병합 → 어떤 단어든 **부분단어로 분할·완전 복원**

### 🧠 마인드맵

```
텍스트 토큰화
├── 왜? 신경망은 숫자만 → 임베딩(연속 벡터 공간)
│   ├── Word2Vec: 문맥 예측 → 의미 반영
│   └── LLM: 임베딩도 함께 훈련 (768 / 12,288차원)
├── 파이프라인: 텍스트 → 토큰 → 토큰 ID → 임베딩 → 디코더 → 출력
├── 정규식 토큰화: ([,.:;?_!"()\']|--|\s), 대소문자 유지, 공백 제거
├── 어휘사전: set → sorted → enumerate (1,130)
├── SimpleTokenizerV1: encode / decode / 역어휘사전 → KeyError 한계
├── 특수 토큰: <|unk|>, <|endoftext|> (+ BOS, EOS, PAD)
├── SimpleTokenizerV2: 미등록 → <|unk|> (원래 단어 손실)
└── BPE (GPT-2/3, tiktoken, 50,257)
    ├── 문자 → 빈도 높은 쌍 병합 반복
    ├── <|endoftext|> = 50256, allowed_special
    └── 미등록 단어도 부분단어로 완전 복원
```

---

## 15. 셀프 체크 퀴즈

**Q1.** 텍스트를 바로 신경망에 넣을 수 없는 이유와 해결 방법은?

<details><summary>▶ 정답</summary>

신경망은 수치 연산으로 동작하는데 텍스트는 범주형 데이터라 연산을 적용할 수 없다. 각 단어를 실수 벡터(임베딩)로 표현하면 더하고 곱하고 거리를 잴 수 있다.
</details>

**Q2.** Word2Vec에서 "비슷한 의미의 단어가 비슷한 벡터가 되는" 이유는?

<details><summary>▶ 정답</summary>

주변 문맥 단어를 예측하도록 훈련하는데, 비슷한 맥락에 나오는 단어는 예측 대상도 비슷해서 벡터가 비슷한 방향으로 조정되기 때문이다.
</details>

**Q3.** LLM의 임베딩이 Word2Vec 임베딩과 다른 점과 그 장점은?

<details><summary>▶ 정답</summary>

미리 만든 임베딩을 가져다 쓰지 않고 입력층의 일부로 두어 모델 훈련 때 함께 갱신한다. 그래서 그 모델의 데이터와 작업에 맞는 값이 된다.
</details>

**Q4.** `re.split(r'(\s)', "a b")` 와 `re.split(r'\s', "a b")` 의 결과 차이는?

<details><summary>▶ 정답</summary>

괄호(캡처 그룹)가 있으면 구분자도 결과에 남는다: `['a', ' ', 'b']`. 괄호가 없으면 `['a', 'b']`.
</details>

**Q5.** 토큰화할 때 대문자를 소문자로 바꾸지 않는 이유는? 공백을 제거하면 안 되는 경우는?

<details><summary>▶ 정답</summary>

고유 명사 구분, 문장 구조 이해, 대문자 생성에 도움이 되기 때문. 파이썬 코드처럼 들여쓰기가 의미를 갖는 텍스트에서는 공백을 유지해야 한다.
</details>

**Q6.** 소설의 토큰 수는 4,690개인데 어휘사전 크기는 1,130인 이유는? 어휘사전 앞쪽이 구두점인 이유는?

<details><summary>▶ 정답</summary>

중복을 제거하고 고유 토큰만 남겼기 때문이다. 정렬 기준이 문자 코드값이라 기호 → 대문자 → 소문자 순으로 정렬된다.
</details>

**Q7.** SimpleTokenizerV1에 역어휘사전(`int_to_str`)이 필요한 이유는?

<details><summary>▶ 정답</summary>

어휘사전은 문자열이 키라서 문자열 → ID 조회만 된다. decode(ID → 문자열)를 하려면 키와 값을 뒤집은 사전이 필요하다.
</details>

**Q8.** V1의 decode 결과가 `" It' s the last...` 처럼 원문과 다른 이유는?

<details><summary>▶ 정답</summary>

encode에서 공백 정보를 버렸고, decode는 모든 토큰 사이에 공백을 넣은 뒤 구두점 **앞**의 공백만 지우므로 구두점 **뒤**의 공백(큰따옴표 뒤, 작은따옴표 뒤)은 남는다.
</details>

**Q9.** `<|unk|>`와 `<|endoftext|>`의 역할은? 디코딩 시 복원 여부가 다른 이유는?

<details><summary>▶ 정답</summary>

`<|unk|>`는 미등록 단어 대체, `<|endoftext|>`는 무관한 텍스트 경계 표시. `<|endoftext|>`는 원문에 직접 넣은 것이라 그대로 복원되지만, `<|unk|>`는 인코딩 중 원래 단어를 대체한 것이라 원본을 알 수 없다.
</details>

**Q10.** 특수 토큰을 정렬 후에 추가하면 번호가 어떻게 되는가?

<details><summary>▶ 정답</summary>

알파벳 순서에 섞이지 않고 맨 뒤에 붙는다. `<|endoftext|>` = 1130, `<|unk|>` = 1131, 어휘사전 크기 1,132.
</details>

**Q11.** GPT가 `[BOS]`, `[EOS]`, `[PAD]`, `<|unk|>`를 따로 쓰지 않는 이유는?

<details><summary>▶ 정답</summary>

`<|endoftext|>` 하나가 끝과 시작 표시를 겸하고, 패딩 부분은 마스크로 계산에서 빠지므로 같은 토큰으로 채워도 된다. `<|unk|>`는 BPE가 미등록 단어를 부분단어로 나누므로 필요 없다.
</details>

**Q12.** GPT-2 BPE 어휘사전 크기와 `<|endoftext|>`의 ID는? tiktoken에서 이 토큰을 인코딩하려면 무엇을 지정해야 하는가?

<details><summary>▶ 정답</summary>

50,257개, ID 50256. `allowed_special={"<|endoftext|>"}` 를 지정해야 한다.
</details>

**Q13.** BPE가 `<|unk|>` 없이 모든 단어를 처리할 수 있는 이유를 사전 구축 방식으로 설명하라.

<details><summary>▶ 정답</summary>

개별 문자(바이트)를 모두 사전에 넣고 시작해 자주 나오는 쌍을 병합해 나가므로, 어떤 단어든 최소한 문자 단위로, 대개는 부분단어의 조합으로 표현할 수 있다.
</details>

**Q14.** 13절 보충 실습에서 `lowest`는 어떻게 토큰화되는가?

<details><summary>▶ 정답</summary>

5번 병합까지 마친 사전으로 `low` + `est</w>` 두 토큰
</details>

---

### 📚 용어 사전

| 용어 | 정의 |
|---|---|
| 임베딩 | 이산 대상을 연속 벡터 공간의 점으로 대응시키는 변환 |
| 임베딩 차원 | 벡터를 이루는 값의 개수 |
| 은닉 상태 | 모델 내부를 흐르는 벡터 (임베딩 차원 유지) |
| 토큰화 | 텍스트를 토큰 단위로 나누는 작업 |
| 어휘사전 | 토큰 ↔ 토큰 ID 대응표 |
| 역어휘사전 | ID → 토큰 대응표 |
| encode / decode | 텍스트 → ID / ID → 텍스트 |
| `<\|unk\|>` | 미등록 단어 대체 토큰 |
| `<\|endoftext\|>` | 무관한 텍스트 사이 경계 토큰 (GPT) |
| BOS / EOS / PAD | 시작 / 끝 / 길이 맞춤 토큰 |
| 부분단어 (subword) | 단어보다 작은 토큰 단위 |
| BPE | 문자에서 출발해 자주 나오는 쌍을 병합하며 사전을 만드는 토큰화 |
| tiktoken | 오픈AI의 Rust 기반 BPE 라이브러리 |

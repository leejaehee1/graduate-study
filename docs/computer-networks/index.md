# 컴퓨터 네트워크

컴퓨터 네트워크 과목 학습 내용을 정리합니다.

## 목차

| 장 | 주제 |
|---|---|
| [1장. Introduction](./01-Introduction.md) | 컴퓨터 네트워크 학습의 큰 그림 |
| [2장. Network Concepts](./02-network-concepts.md) | 네트워크 3요소, OSI 7계층과 TCP/IP, PDU와 캡슐화 |
| [3장. Network Technologies](./03-network-technologies.md) | 인터페이스, 프로토콜, 표준화, 전송 매체, DNS |
| [4장. Network Access Layer](./04-network-access-layer.md) | 토폴로지, IEEE 802, MAC/LLC, CSMA/CD·CA, 토큰, 도메인 |
| [5장. Internet Layer](./05-internet-layer.md) | 네트워크 계층 기능, 연결형/비연결형, 라우팅 (p.9까지) |
| [5장 (Part 2). Internet Layer — 후반부](./05-internet-layer-part2.md) | 라우팅 테이블, 실습(`route print`·`ping`·`arp`), 라우팅 정보 처리, 혼잡 제어·트래픽 성형·ECN (p.10~27) |

---

## 중간고사

> ✅ **2026-10-22(목) 중간고사 완료** (범위: 1장 ~ 5장 p.9 정적·동적 라우팅까지)

<details><summary>📋 지난 중간고사 출제 메모 및 복습 범위 펼치기</summary>

| 항목 | 내용 |
|---|---|
| **시험일** | **2026-10-22(목)** 완료 · 메모상 "40분에 시험 시작" |
| **범위** | **1장 ~ 5장** (5장은 p.9 정적·동적 라우팅까지) |
| **문항** | 메모마다 다름 — p.1 "단답식 10개 + 서술형 6문항" / p.9 "6~7문제(단답식 3, 서술형 3~4)" |
| **출제 메모 정리** | [5장 0절. 중간고사 대비](./05-internet-layer.md#_0-중간고사-대비-p-1-p-2-수업-메모) — 교수님이 알려 주신 단답식·서술형 목록과 답의 방향 |

**출제 메모에 나온 주제와 복습할 곳**

| 주제 | 형식 | 복습할 곳 |
|---|---|---|
| 네트워크 3요소 (Node · Link · Protocol)와 연동 방식 | 단답 · 서술 | [2장](./02-network-concepts.md) |
| OSI 7계층 vs TCP/IP, 계층화의 목적·이점, 전송 계층 PDU | 단답 · 서술 | [2장](./02-network-concepts.md) |
| TCP/IP 설계자(Vint Cerf · Bob Kahn) 관련 O/X | 단답 | [2장](./02-network-concepts.md) |
| 토폴로지 6가지 구조·장단점 (★★★ 출제 확정) | 서술 2~3줄 | [4장 3절](./04-network-access-layer.md#_3-network-topologies-★★★-p-4) |
| IEEE 802 번호, LLC / MAC, Hub L1 · Switch L2 | 단답 | [4장 4~6절](./04-network-access-layer.md#_4-network-protocol과-ieee-802-p-5) |
| CSMA/CD 3단계, 이더넷 vs 토큰 버스 | 서술 | [4장 9·12절](./04-network-access-layer.md#_12-csma-cd-동작-p-18) |
| CSMA/CA, RTS/CTS 신호 타이밍 | 단답 | [4장 13절](./04-network-access-layer.md#_13-csma-ca-—-무선-lan-p-19) |
| Review 숙제: MAC 주소(ARP/RARP), IPv6 128 bits | 단답 | [4장 14절](./04-network-access-layer.md#_14-review-—-숙제-시험에-나올-수-있음-p-20-p-21) |
| 라우팅 테이블의 역할, HELLO / ECHO 패킷 | 단답 · 서술 | [5장](./05-internet-layer.md) |
| 흐름 제어 vs 혼잡 제어 | 서술 | [5장 0.6절](./05-internet-layer.md#_0-6-보충-흐름-제어-vs-혼잡-제어) |

> 출제 제외: 토큰 버킷, 계층적인 전달 순서

</details>

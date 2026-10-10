# Legacy Content Preservation Audit

This audit records how every file formerly stored under `more/` was reconciled into the current
Markdown structure. It exists to distinguish consolidation from accidental deletion.

[Back to the repository overview](README.md)

## Method

The source versions were read from commit `f95fa7d` so they did not need to be restored to the
working tree. The audit inspected DOCX paragraphs, tables, and embedded media, not only visible
headings. Markdown sources were reviewed line by line. Candidate questions and topics were compared
with the current headings and answers, and low-confidence matches were checked in context.

The current repository contains 1,118 level-two headings and 1,097 structured answers across
the question bank. A lower word count than the combined sources is expected because `CORE.docx`,
`Interview_Questions.docx`, and the subject-specific documents repeat many questions and answers.
Preservation is judged by concepts and useful examples, not repeated wording.

Each source item was handled in one of four ways:

1. retain it in the most relevant Markdown page;
2. merge it with an equivalent, better answer;
3. correct it and retain the corrected explanation; or
4. omit only redundant, promotional, personal-contact, or non-instructional material, with the
   reason recorded below.

## File-By-File Results

### `Finance.docx`

**Source:** 5,675 words, 509 paragraphs. **Status:** complete.

The earlier 748-word transition guide did not preserve this source adequately. The material is now
5,458 words across the transition guide and the [finance reference](career-resources/finance/README.md),
with a topic-level coverage table. Tax, retirement, compensation, insurance, banking, market,
mutual-fund, product, trading, return, and planning concepts were restored.

Corrections include the regulatory status of NBFCs, asset-specific LTCG holding periods, current
year/regime qualification for deductions, depository roles, rolling-return calculation, bond and
P2P risk, and unsafe concentrated stock-picking rules. Brand lists and promotional links were
replaced by regulator-backed evaluation criteria.

### `OS.docx`

**Source:** 3,154 words, 126 paragraphs. **Status:** complete.

Existing coverage already included OS roles, process/thread concepts, scheduling, synchronization,
deadlocks, memory management, paging, replacement, kernels, disks, spooling, and RAID. This audit
restored user- versus kernel-level thread models, HRRN and multilevel queues, LRTF, multitasking
versus multiprocessing, bounded producer-consumer coordination, swapping versus overlays, rotating-
disk timing, and multithreading trade-offs in
[Operating Systems](question-bank/computer-science/operating-systems.md).

### `CN.docx`

**Source:** 4,051 words, 179 paragraphs, 6 embedded images. **Status:** complete.

Topology, network scope, OSI/Internet models, HTTP/HTTPS, DNS, TCP/UDP, addressing, ARP, DHCP, CIDR,
the TCP handshake, and browser-request flow were already represented. This audit restored VPN
models and limitations, `ping`/`ipconfig`/`ifconfig`, packet-delay components, router versus gateway,
and IPv4 link-local/APIPA behavior in [Networking](question-bank/infrastructure/networking.md).

Five images were simple star, mesh, tree, bus, and ring diagrams already described in text. The
sixth was a classful IPv4 address table; classful addressing is historical and is not a replacement
for modern CIDR. No unique visual fact was lost by omitting these raster copies.

### `OOPS.docx`

**Source:** 2,580 words, 330 paragraphs. **Status:** complete.

Existing C++ material already covered constructors, virtual destructors, pure virtual functions,
runtime polymorphism, friends, namespaces, and inheritance access. The audit restored class/object
fundamentals, encapsulation versus abstraction, inheritance shapes, destructors and `this`,
aggregation versus composition, and operator overloading in [C++](question-bank/languages/cpp.md).

Invalid source examples were not copied. In particular, ordinary C++ object construction does not
use Java syntax such as `student s = new student()`, and functions cannot be overloaded by return
type alone.

### `DBMS.docx`

**Source:** 5,695 words including 6 tables, 560 paragraphs, 5 embedded images. **Status:** complete.

Keys, functional dependencies, normalization, decomposition, ACID, schedules, serializability,
indexes, B/B+ trees, SQL command groups, filtering, aggregation, joins, and DDL were already covered.
The audit restored strong/weak entities, attribute kinds and cardinality, attribute closure,
relational-algebra operations, transaction states, and file organizations across
[SQL](question-bank/data/sql.md) and
[Database Internals](question-bank/data/database-internals.md).

The tables and images show relational-algebra operators, SQL comparison and `LIKE` examples,
schedule classification, transaction states, an ER example, normal forms, and key containment.
Their useful content is now searchable text. The original table that combines full outer join and
division in one row was separated conceptually rather than copied.

### `CORE.docx`

**Source:** 11,192 words including 5 tables, 995 paragraphs, 14 embedded media files. **Status:**
complete.

This is an aggregate of OS, DBMS, networking, cache, scaling, and SQL material rather than a separate
subject. Its unique or incomplete points were reconciled into the same subject pages. Cache mapping
is covered in [Computer Architecture](question-bank/computer-science/computer-architecture.md), and
scaling/load balancing are covered in the architecture section.

The media depict RAID, memory types, FCFS/SJF, multitasking/multiprocessing, indexes, joins,
delete/truncate, shared/exclusive locks, OSI/TCP-IP layers, and the TCP handshake. One asset is only a
video-site icon. The source's blanket statements that thread switching never involves the OS,
horizontal scaling is always harder and costlier, or IPv6 inherently supplies encryption and
authentication were not retained; the current answers state the actual trade-offs.

### `JAVA.docx`

**Source:** 2,018 words, 416 paragraphs. **Status:** complete by merge.

Classes and objects, `this`, constructors, polymorphism, inheritance, packages, access, encapsulation,
abstraction, interfaces, `static`, and multithreading already have fuller answers in the split
[Java question bank](question-bank/languages/java.md). No duplicate page was added.

The maintained answers correct source issues such as unquoted string literals, integer division in
an area formula, treating a copy constructor as a language-provided Java constructor category, and
the obsolete claim that every interface method is implicitly abstract. Modern interfaces can also
declare default, static, and private methods.

### `Interview_Questions.docx`

**Source:** 105,959 words, 11,353 paragraphs, 18 subject headings. **Status:** complete by structured
merge and correction.

The source spans HTML/CSS, JavaScript, Angular, React, Node.js, Java, LLD/microservices, Spring,
C#, .NET, networking/security, containers, cloud, Kafka, C++, databases, and system design. A
high-confidence structural pass identified 932 question-like prompts. They were reconciled against
the subject pages rather than copied into one monolith. Apparent unmatched items were reviewed in
context; most were answer fragments, code continuations, output exercises, or paraphrases of an
existing heading.

Examples verified during the second pass include JavaScript polyfills and exercises, Angular build
modes, Express and database access, Java release/concurrency topics, Spring request/data/security
flows, legacy ASP.NET Web Forms lifecycle, URL shortening, Docker primitives, cloud observability,
Kafka serialization, Redis behavior, search indexes, graph databases, and distributed-database
algorithms. These topics are present in their corresponding pages. Broken or unsafe snippets were
replaced by corrected implementations instead of preserved verbatim.

### `QnA.md`

**Source:** 2,517 words, 198 lines. **Status:** complete.

Behavioral questions about introductions, fit, goals, company research, changing jobs, strengths and
weaknesses, conflict, leadership, workload, estimation, onboarding, compensation, competing offers,
and interviewer questions are in
[Behavioral Interviews](question-bank/behavioral/behavioral-interviews.md). The personal profile and
answer-building substance are retained in the
[Personal Interview Answer Workbook](career-resources/personal-interview-answer-workbook.md), clearly
marked as a historical snapshot that must be verified before use.

### `research.md`

**Source:** 1,440 words, 237 lines. **Status:** complete.

Cold email, referral, recruiter reply, hiring-manager contact, role-learning, cover-letter, follow-up,
and former-employee due-diligence templates are consolidated in
[Job Search Outreach](career-resources/job-search-outreach.md). Offer checks are in
[Evaluating And Negotiating Offers](career-resources/evaluating-and-negotiating-offers.md).
Personalized resume claims are preserved through the historical workbook rather than silently
presented as current facts. Manipulative “without me” and pressure tactics were corrected into an
evidence-based promotion and growth conversation.

### `sd.md`

**Source:** 25 unique topic prompts in 28 lines. **Status:** complete by merge.

Write-ahead logging, TLS load-balancer modes, logical clocks, hinted handoff, Bloom filters, gossip,
Merkle trees, 2PC, 2PL, consistent hashing, replication, total-order broadcast, isolation, geospatial
indexes, inverted indexes, leaderboards, tries, external sorting, Paxos, backpressure, circuit
breakers, Raft, service discovery, sagas, and HyperLogLog all have dedicated answers in the database,
architecture, resilience, and specialized-store pages. The repeated Merkle-tree line was merged.

## Embedded Tables And Images

The DOCX sources contain 11 tables and 25 media files in total. Every informative table or diagram
was checked. Raster diagrams were not copied when the same relationship is clearer and more
accessible as headings, prose, lists, or Markdown tables. This also avoids retaining low-resolution
screenshots and factual errors embedded in images.

## Files Intentionally Not Recreated

- duplicate definitions and examples already represented by a stronger answer;
- vendor, broker, insurer, adviser, and promotional lists that would imply endorsement or become
  stale, while retaining the underlying selection criteria;
- decorative separators, icons, copied links with no unique explanation, and malformed snippets;
- repeated screenshots whose information is present in accessible Markdown; and
- claims that could not be correct as written, where the corrected concept is preserved instead.

The original DOCX and loose Markdown files remain absent from the current worktree as requested.
Their history remains recoverable from Git.

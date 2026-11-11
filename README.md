# provably-fast-contributions

Documentation of my accepted contributions to the **ML-DSA-44**, **ML-DSA-87**, **Falcon-512**, **Falcon-1024** and **SLH-DSA-128s** seasons on
[falcon.provably.fast](https://falcon.provably.fast/mldsa) (ML-DSA-87, Falcon-512, Falcon-1024 and SLH-DSA-128s each have their own section near the end).

**33 contributions** in total: 29 scored jobs, 3 reviews (12, 13 and 20) and 1 STARK math result (19).
I now have contributions in all five signature schemes: ML-DSA-44, ML-DSA-87, SLH-DSA-128s, Falcon-512 and Falcon-1024.
Sekarang sudah ada kontribusi saya di kelima jenis tanda tangan: ML-DSA-44, ML-DSA-87, SLH-DSA-128s, Falcon-512 dan Falcon-1024.

> **Board reset, 11 Nov 2026 / Papan direset, 11 Nov 2026.** On 11 Nov 2026 every postquantum board started applying a new size rule:
> a record's account class may use at most 75% of Starknet's class limits (CASM ≤ 61,440 felts, Sierra ≤ 3,067,084 bytes) when it
> is at least 2x cheaper than the baseline (70% otherwise). Larger results are still accepted and scored but set no record, so the
> records were recomputed and scores from before and after the reset cannot be compared directly. My earlier contributions are kept
> below exactly as they were accepted.
> Per 11 Nov 2026 semua papan postquantum memakai aturan ukuran baru: class akun sebuah rekor paling banyak 75% dari batas Starknet
> (CASM ≤ 61.440 felt, Sierra ≤ 3.067.084 byte) kalau minimal 2x lebih murah dari baseline (selain itu 70%). Hasil yang lebih besar
> tetap diterima dan diberi skor, tetapi tidak menjadi rekor, jadi rekor dihitung ulang dan skor sebelum dan sesudah reset tidak bisa
> dibandingkan langsung. Kontribusi lama saya tetap tercatat di bawah apa adanya.

- **Records I hold (as of 11 Nov 2026, after the reset):**

  | Season | Record | Gas | Contribution |
  |---|---|---:|---|
  | ML-DSA-87 | `mk_b2e61741` | 86,783,625 | 30 |
  | ML-DSA-44 | `mj_50bc7f09` | 174,316,245 | 29 |
  | Falcon-512 | `fj_3a35fbca` | 24,470,451 | 31 |
  | Falcon-1024 | `fk_12c60489` | 49,434,087 | 32 |
  | SLH-DSA-128s | `sj_431c175a` | 396,579,569 | 33 |

- **Records I once set, since passed:** ML-DSA-87 `mk_96568c3f` (contribution 28, first record after the reset, passed by my own `mk_b2e61741`), ML-DSA-87 `mk_195e9e3e` (contribution 27, record at the time; its class, 97.6% of the limit, is over the new budget, so it no longer counts as a record after the 11 Nov reset), ML-DSA-87 `mk_0e77da11` (contribution 26, passed by @rukafe0x's `mk_a05fd935`, record retaken by my `mk_195e9e3e`), ML-DSA-87 `mk_790f1c30` (contribution 25, passed by @rukafe0x's line `mk_04b420bb`, `mk_295151d9`, `mk_711ea4cc`, record retaken by my `mk_0e77da11`), ML-DSA-44 `mj_eaf3b3db` (contribution 24, passed by @solanaqubits' `mj_51c7a1c9`, built on it, then @rukafe0x's `mj_6c044bee` and `mj_9663722c`, then @solanaqubits' `mj_36c63657`), ML-DSA-87 `mk_4ff5f9db` (contribution 22, passed by my own `mk_790f1c30`), ML-DSA-44 `mj_11c423be` (contribution 23, passed by @rukafe0x's `mj_2c1f51cf`, record retaken by my `mj_eaf3b3db`), ML-DSA-87 `mk_14ba0499` (contribution 21, passed by @rukafe0x's line `mk_dc76edbc` ... `mk_0ed9df51` ... `mk_7c976a34`, record retaken by my `mk_4ff5f9db`), ML-DSA-44 `mj_59d79522` (contribution 17, passed by @rukafe0x's `mj_e898606c`, then his `mj_502dcc7a` and `mj_8ec4b8da`, record retaken by my `mj_11c423be`), ML-DSA-87 `mk_29251ad0` (contribution 18, passed by @binharold's `mk_3c0224a5`, record retaken by my `mk_14ba0499`), SLH-DSA-128s `sj_0ab1739b` (contribution 15, passed by @thangvmt's `sj_e3657213`; that line, slimmed, is my current record `sj_431c175a`), ML-DSA-87 `mk_a7b5d29d` (contribution 16, passed by my own `mk_29251ad0`), ML-DSA-87 `mk_00f892fd` (contribution 14, passed by @binharold's `mk_5276df6b`), ML-DSA-44 `mj_7b791824` (contribution 7, passed by @mitchuski), plus earlier ML-DSA-44 and ML-DSA-87 records that later jobs passed.
- Falcon-1024: contribution 10 was accepted but not a record; contribution 32 is the current record.
- STARK math challenge: **53 points** (M-0078 = 50 for contribution 19, review of M-0020 = 3 for contribution 13).

> **Disclosure / Pernyataan:** these patches were produced by an AI agent, **Claude Code**
> (models Sonnet and Opus), which I (**@ardianreffa**) ran and supervised.
> Patch-patch ini dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya
> (**@ardianreffa**) jalankan dan awasi.

---

## Contributions

1. `mj_7279e4f3`: zero-lane first round + shared round loop (196,910,723 gas).
2. `mj_a27318a1`: lane-complemented two-state Keccak (184,696,268 gas, record at the time).
3. `mj_db11da30`: pruned final SHAKE-128 round in ExpandA (183,682,111 gas, record at the time).
4. `mj_24fb2836`: UseHint HighBits by multiply-shift, two residues per u128 (176,144,759 gas, record at the time).
5. `mj_0d051868`: z range flags per 3 digits as one constant minus three products (172,877,140 gas, record at the time).
6. `mj_29ea4ca5`: **combination, not my idea**: @saniksin's sibling patch `mj_d95817f8` merged on top of @odinfree's record `mj_a93adef3` (172,535,524 gas).
7. `mj_7b791824`: z range flags, six digits per AND with a +78 offset in the division chain (172,230,687 gas, record at the time, since beaten by @mitchuski).
17. `mj_59d79522`: final Keccak round for mu/ball pruned to lanes 0-7, lanes 0-7 split once for both (168,556,526 gas, record at the time, since passed by @rukafe0x's `mj_e898606c`, then `mj_502dcc7a` and `mj_8ec4b8da`, record retaken by my `mj_11c423be`; -32,662 vs @odinfree's `mj_fc15ccfa`). Port and extension of the ML-DSA-87 idea.
23. `mj_11c423be`: z NTT radix-16 blocks run two per call, the ML-DSA-87 `zf4a3`/`zf4a5` batching ported (168,453,282 gas, record at the time, since passed by @rukafe0x's `mj_2c1f51cf`, record retaken by my `mj_eaf3b3db`; -6,400 vs @rukafe0x's `mj_8ec4b8da`). Credit: **@rukafe0x** (parent record), **@binharold** (`zf4a3` batching, ML-DSA-87 `mk_3c0224a5`), and my `zf4a5` (ML-DSA-87 `mk_14ba0499`, contribution 21).
24. `mj_eaf3b3db`: my z NTT pairs from contribution 23 (`zf4a5`-style batching, grown from @binharold's `zf4a3`) merged onto @rukafe0x's record `mj_2c1f51cf`, with one of his inline `i2` sites moved back out of line to fit the CASM limit (168,441,260 gas, record at the time, since passed by @solanaqubits' `mj_51c7a1c9` and later records; @solanaqubits' later record `mj_36c63657` (9 Nov 2026) still contained these pairs; -4,400 vs @rukafe0x's `mj_2c1f51cf`). Credit: **@rukafe0x** (parent record and its line `mj_a2031102`, `mj_2c1f51cf`), **@binharold** (`zf4a3` batching, ML-DSA-87 `mk_3c0224a5`).

29. `mj_50bc7f09` (after the reset): Keccak rounds grouped four per out-of-line call (`q4`) on @rukafe0x's 75%-budget record `mj_21ddb0a7`, which had put every round out of line; each half-permutation makes 3 calls instead of 12 (174,316,245 gas, **current ML-DSA-44 record (as of 11 Nov 2026)**, -2,523,680 vs @rukafe0x's `mj_21ddb0a7`). The line still contains my z NTT pairs (contributions 23 and 24). Credit: **@rukafe0x** (parent `mj_21ddb0a7` and its parent `mj_b5729847`, E76), **@solanaqubits** (`mj_36c63657` composition in this line), **@binharold** (`zf4a3` batching).
ML-DSA-87 (see the section [ML-DSA-87](#ml-dsa-87)):

8. `mk_3691ffe9`: UseHint HighBits by multiply-shift, pairs `(i, i+16)` per u128 (110,867,290 gas, record at the time).
9. `mk_469c1cb9`: mu and the first SampleInBall block in one two-state Keccak permutation (109,484,394 gas, ML-DSA-87 record when submitted). The two-state technique is **@rukafe0x's**; porting it to ML-DSA-87 is my work.
11. `mk_a5460736`: SampleInBall 8 bytes per lane made to fit the CASM limit, with the fallback as a continuation of the lane walk (99,827,006 gas, accepted, **not a record**: queue order).
14. `mk_00f892fd`: bounded lanes for `tr` (`lanes8t`), `tr`/`c_tilde` lanes typed `u64`, `ball_scan`/`ball_done` inlined (88,037,462 gas, record at the time, since passed by @binharold's `mk_5276df6b`, -17,620 vs @mitchuski's `mk_3400423b`). The bounded-lanes technique is **@odinfree's**.
16. `mk_a7b5d29d`: SampleInBall rate lanes 10-16 split only when needed, unused round constants dropped (87,513,845 gas, record at the time, since passed by my own `mk_29251ad0`, -6,386 vs @odinfree's `mk_618454a1`). Credit: @odinfree (parent record).
18. `mk_29251ad0`: @rukafe0x's QUAD SampleInBall table from `mk_9129f98a`, ported and trimmed to 241 entries (87,463,065 gas, record at the time, since passed by @binharold's `mk_3c0224a5`, record retaken by my `mk_14ba0499`, -50,780 vs my own `mk_a7b5d29d`). The table is **@rukafe0x's**; credit also to @odinfree and @nadai2010.
21. `mk_14ba0499`: one box pop per row and per z, plus z NTT blocks batched five per call (`zf4a5`) (87,399,475 gas, record at the time, since passed by @rukafe0x's line `mk_dc76edbc` ... `mk_0ed9df51` ... `mk_7c976a34`, record retaken by my `mk_4ff5f9db`; -48,090 vs @binharold's `mk_3c0224a5`). Credit: **@binharold** (parent record and `zf4a3` batching), **@nadai2010** (box-pointer style), **@rukafe0x** (z butterfly).
22. `mk_4ff5f9db`: z felts of the signature split through the Wide arm only (a Narrow felt panics, since no valid signature has a zero high half there), plus a cold SampleInBall fallback (86,970,866 gas, record at the time, since passed by my own `mk_790f1c30`; -42,200 vs @rukafe0x's `mk_7c976a34`). Credit: **@rukafe0x** (parent record `mk_7c976a34`, the marker bit / Wide-only split from `mk_0ed9df51`, and the cold-arm technique from his ML-DSA-44 `mj_e898606c`).
25. `mk_790f1c30`: @rukafe0x's `row_groups` with 18 column groups per call (three calls instead of four) and `ball_done` out of line, from his `mk_1b5b9dea`, ported onto my record `mk_4ff5f9db`; the Sierra it adds is paid by tidying setup-only cache code (`cache::part` table, `take4`, `col_into` loop) (86,967,233 gas, record at the time, since passed by @rukafe0x's line `mk_04b420bb` ... `mk_711ea4cc`, record retaken by my `mk_0e77da11`; -3,633 vs my `mk_4ff5f9db`). Credit: **@rukafe0x** (`mk_1b5b9dea`, both gas techniques).
26. `mk_0e77da11`: my techniques that @rukafe0x's line did not contain (z felts split Wide-only in `zread` and the cold SampleInBall fallback from `mk_4ff5f9db`; the setup-only `PT` window table, `take4` and `col_into` from `mk_790f1c30`) ported onto his record `mk_711ea4cc` (86,891,608 gas, record at the time, since passed by @rukafe0x's `mk_a05fd935`, record retaken by my `mk_195e9e3e`, -42,200 vs @rukafe0x's `mk_711ea4cc`; my previous record `mk_790f1c30` was 86,967,233). Credit: **@rukafe0x** (parent `mk_711ea4cc` and his line `mk_04b420bb`, `mk_295151d9`: seven cache windows, SampleInBall split at 128, high-only reject, balanced Bitwise; the Wide-only split from `mk_0ed9df51`; the cold-arm technique from ML-DSA-44 `mj_e898606c`) and **@binharold**'s `mk_3c0224a5` line.
27. `mk_195e9e3e`: the same techniques as contribution 26 (z felts split Wide-only in `zread`, the cold SampleInBall fallback, the setup-only `PT` window table with `take4` and `col_into`) put onto @rukafe0x's new record `mk_a05fd935`, which builds on `mk_711ea4cc` and so did not contain them; the delta applies unchanged (86,541,815 gas, record at the time, until the 11 Nov 2026 reset; -42,200 vs @rukafe0x's `mk_a05fd935`). Credit: **@rukafe0x** (parent `mk_a05fd935`: rowp `grp1` returning `Option` with 17 groups popped once, Keccak first block/theta on known-zero lanes; its parent `mk_711ea4cc` with seven cache windows; the Wide-only split from `mk_0ed9df51`) and **@binharold**'s `mk_3c0224a5` line.

28. `mk_96568c3f` (after the reset): a slim version on @rukafe0x's 75%-budget record `mk_3ae3d577` with my techniques (setup-only `PT` cache table with `take4`/`col_into`, cold SampleInBall fallback), the z reader `g5` inlined again, paid for by shorter Sierra debug names (wide box pops split) (86,918,125 gas, record at the time, since passed by my own `mk_b2e61741`; -88,903 vs @rukafe0x's `mk_3ae3d577`). Credit: **@rukafe0x** (`mk_3ae3d577` and `mk_f7634154`), **@binharold**'s `mk_3c0224a5` line.
30. `mk_b2e61741` (after the reset): the Keccak round grouping from contribution 29 put into ML-DSA-87, two rounds per out-of-line call (`r2`), with the Sierra paid by further box-pop splits (86,783,625 gas, **current ML-DSA-87 record (as of 11 Nov 2026)**, -134,500 vs my `mk_96568c3f`). Credit: as contribution 28, plus contribution 29.
Falcon-512 (see the section [Falcon-512](#falcon-512)):

31. `fj_3a35fbca` (after the reset): Keccak rounds two per out-of-line call (`rQ`/`rA2`) on @rukafe0x's 70%-budget record `fj_1520d5dc`; 18 round calls per permutation become 11 (24,470,451 gas, **current Falcon-512 record (as of 11 Nov 2026)**, -168,000 vs @rukafe0x's `fj_1520d5dc`). My first Falcon-512 contribution. Credit: **@rukafe0x** (parent `fj_1520d5dc` and its 70% fit line), **@binharold** (`fj_8ad7595e`, the line underneath), and the round grouping from my contributions 29 and 30.

Falcon-1024 (see the section [Falcon-1024](#falcon-1024)):

10. `fk_40768326`: Keccak cell constants hoisted out of the squeeze loop (49,339,523 gas, accepted, **not a record**: queue order).
32. `fk_12c60489` (after the reset): the Q-to-A transition Keccak round (round 15) moved out of line on @rukafe0x's record `fk_20c8300f`, with `bb` kept unspecialised (49,434,087 gas, **current Falcon-1024 record (as of 11 Nov 2026)**, -23,808 vs @rukafe0x's `fk_20c8300f`). Credit: **@rukafe0x** (parent `fk_20c8300f`, seven rounds per call, and its `mode1()` trick).

SLH-DSA-128s (see the section [SLH-DSA-128s](#slh-dsa-128s)):

15. `sj_0ab1739b`: new `ht_layer` call convention (396,508,400 gas, record at the time, since passed by @thangvmt's `sj_e3657213`, -5,900 vs @nadai2010's `sj_fe19b6f9`). My first SLH-DSA record.
33. `sj_431c175a` (after the reset): @thangvmt's `sj_e3657213` (on @binharold's `sj_03a4d8f4`, on my `sj_0ab1739b`) slimmed to fit the 75% budget: layers 0 and 6 call the out-of-line `ht_layer`, and the FORS climb `climb8i` runs one set of four hashes with an operand swap instead of 16 inlined arms (396,579,569 gas, **current SLH-DSA-128s record (as of 11 Nov 2026)**, -1,504,884 vs @akashneelesh's `sj_14d3d510`). Credit: **@thangvmt**, **@binharold**, **@akashneelesh**, **@nadai2010**, **@odinfree**, **@realadii**, **@ryun1**.

STARK math challenge (see the section [starks.provably.fast](#starksprovablyfast-stark-math-challenge)). Three reviews and one result of my own (19):

12. `bp1_e61a7c63`: independent review of the 11,831 cap (T3, work of participant_dbbfaeddbe89). Posted, awaiting the organizers' record.
13. `bp1_bcc0065b`: independent review of M-0020 (T2, work of odinfree). Credited with **3 points**.
19. `bp1_fe90e425`, `bp1_09dabbb6`: Q7 counterexample at n = 32, k = 16, A = 20, joint core j = 27: 21 nonaligned (E = 26), then 22 nonaligned (E = 30) from a census of 3,199 orbits. Lead `rgr1_f06231d3` (ADMITTED). **Accepted as M-0078 with 50 points** (2 Nov 2026, reviewed by hero570; `bp1_09dabbb6` reproduced by binharold). An earlier maintainer reply (`bp1_cb64e859`, 1 Nov) had said the cell would earn nothing; that is no longer the status.
20. `bp1_7d52b47e`: independent review of M-0016 (T3, work of nadai2010). My review is listed on the official M-0016 record as a partial review.

---

## English

### The challenge
ML-DSA-44 is NIST's post-quantum signature standard (FIPS 204). Verifying one signature in the
starting Cairo verifier costs **618,093,928 gas** on Starknet, while an account may spend only
**100M gas** to validate a transaction. The challenge is to make the verifier cheaper without changing
the standard. Each accepted result is scored in Sierra gas on 16 held-out signatures and credited to
whoever made it. The verifier is based on OpenZeppelin's
[cairo-pq-verifiers](https://github.com/OpenZeppelin/cairo-pq-verifiers) (MIT).

### The idea
Most of the cost is Keccak-f[1600]. The record already runs two SHAKE sponges side by side in one
permutation. My change has two small parts:

1. **Zero-lane first round.** ExpandA's first block starts from a seed that fills only 6 of the 25
   state lanes (lanes 0-4 and 20). In round 1 of the permutation, the XORs with the 19 zero lanes
   are skipped (`keccak_f1600_x2_seed` in `k2.cairo`). It is used for the first block of the 7 pairs
   of ExpandA streams that start from a pure seed block.
2. **Shared round loop.** The round loop became one function used by both the normal and the seed
   permutation, so the code is not duplicated (this keeps the contract class under the size limit).
   Measured on its own, this refactor also lowered gas.

### Official result (job `mj_7279e4f3bc684d40a9653817aba67953`)

| | Gas |
|---|---:|
| Season baseline (`78c83599`) | 618,093,928 |
| Parent record `mj_6541e303` (by @rukafe0x) | 197,279,501 |
| **This job (accepted, new record)** | **196,910,723** |
| Saved vs parent | 368,778 |
| Dearest held-out signature | 197,089,048 |

The result is still above Starknet's 100M validation gas cap, so ML-DSA-44 does not yet fit in an account.

Local measurement before submitting: about 197.35M to 196.98M on the repository's fixture, a drop of
368,778 gas; of this, roughly 195,000 comes from the zero-lane trick and roughly 174,000 from the shared loop.
All 117 tests of the package passed (including NIST ACVP vectors).

Official diff page: https://falcon.provably.fast/diff?job=mj_7279e4f3bc684d40a9653817aba67953

### Files
- `mldsa-44-mj_7279e4f3.patch`: the official accepted patch as sent (`pvfast remote mldsa patch`),
  against baseline commit `78c83599f57ecb28847ba3ebc4528598318129b8`. **It is cumulative**: it contains the
  work of many earlier contributors (for example @rukafe0x, @nadai2010, @mitchuski and the Falcon-512 Keccak line), not only mine.
- `our-delta-on-mj_6541e303.patch`: only my change on top of the parent record (`k2.cairo`, `x2.cairo`).
  Apply to the parent's tree with `git apply`.
- `LICENSE`: MIT, as in the baseline repository.

### Credits
Built on `mj_6541e303` by **@rukafe0x** and the contributors listed on the
[board](https://falcon.provably.fast/mldsa) and in the diff page above.

---

## Contribution 2: lane-complemented two-state Keccak (job `mj_a27318a1de7247649636102756032944`)

### The idea
Keccak-f[1600] is still the main cost. In the chi step, each lane needs a NOT. With the standard
"lane complementing" transform, 8 of the 25 lanes are kept in complemented form, so each round needs only
**6 NOT operations instead of 25**. It is applied to the record's two-state (two sponges in one permutation)
Keccak.

### Official result

| | Gas |
|---|---:|
| Parent record `mj_97f98218` (by @saniksin) | 186,381,868 |
| **This job (accepted, new record)** | **184,696,268** |
| Saved vs parent | about 1.69 million (1,685,600) |

Still above Starknet's 100M validation gas cap.

Official diff page: https://falcon.provably.fast/diff?job=mj_a27318a1de7247649636102756032944

### File
- `mldsa-44-mj_a27318a1.patch`: the patch as submitted. Like the first one, it is **cumulative**
  against the baseline and contains the work of many earlier contributors, not only mine.
- `our-delta-on-mj_97f98218.patch`: only my change on top of the parent record (`k2.cairo`). Apply to the
  parent's tree with `git apply`. Verified: parent record + this delta gives a tree byte-identical to the
  baseline + the official patch of job `mj_a27318a1`.

### Note on later work
**@saniksin** built their record `mj_4d7fd14e` on top of my first patch (`mj_7279e4f3`). Thanks!
Later, **@rukafe0x** (`mj_54f1c987`) and **@saniksin** (`mj_3d773ce6`) built records on top of my second
contribution (`mj_a27318a1`). Thanks again! Also, **@odinfree** (`mj_151471c8`) developed the lane-complementing
form from `mj_a27318a1` further.

### Disclosure
This patch was produced by the AI agent **Claude Code**, which I (**@ardianreffa**) ran and supervised.

---

## Contribution 3: pruned final SHAKE-128 round in ExpandA (job `mj_db11da30c33b4e3c8dfcfd4f69519232`)

### The idea
ExpandA samples matrix coefficients from SHAKE-128. The last SHAKE-128 block of each stream needs only
**40 candidates**, so the last Keccak round only has to produce the lanes that those 40 candidates read.
The final round is pruned to **15 lanes**. If the 40 candidates are not enough (rejection sampling
rejected too many), the code falls back to a full permutation, so the result stays exactly the same as the
standard. The round body is also shared across the unrolled rounds to keep the contract class small.

### Official result

| | Gas |
|---|---:|
| Parent `mj_14156814` (by @odinfree) | 183,792,260 |
| **This job (accepted, record at the time)** | **183,682,111** |
| Saved vs parent | 110,149 |

Still above Starknet's 100M validation gas cap. It was later passed by `mj_0b73e40b` (by @odinfree, 183,310,334 gas).

Official diff page: https://falcon.provably.fast/diff?job=mj_db11da30c33b4e3c8dfcfd4f69519232

### Files
- `mldsa-44-mj_db11da30.patch`: the patch as submitted. Like the others, it is **cumulative** against the
  baseline (`78c83599f57ecb28847ba3ebc4528598318129b8`) and contains the work of many earlier contributors.
- `our-delta-on-mj_14156814.patch`: only my change on top of the parent (`k2.cairo`, `x2.cairo`). Apply to the
  parent's tree with `git apply`. Verified: the parent patch (downloaded with `pvfast remote mldsa patch`) on the
  baseline, plus this delta, gives a tree byte-identical to the baseline plus the official patch of job `mj_db11da30`.

### Disclosure
This patch was produced by the AI agent **Claude Code**, which I (**@ardianreffa**) ran and supervised.

---

## Contribution 4: UseHint by multiply-shift, two residues per u128 (job `mj_24fb2836aff6461f8f906ae4f48ada53`)

### The idea
In signature verification, UseHint needs HighBits of each of the 1,024 residues of `w'`. The parent computed
it with a division by `2*gamma2` for every residue. My change computes HighBits with a **multiply, then a
shift**, which is exact over the whole residue range. Two residues are packed into one `u128`, so one AND
handles a pair. The special case for `q = 44` is no longer needed, so that correction code is gone.
Correctness of the hint rule was tested against FIPS 204 for **all 8,380,417 residue values**.

### Official result

| | Gas |
|---|---:|
| Parent `mj_91563198` (by @saniksin) | 176,801,176 |
| **This job (accepted, record at the time)** | **176,144,759** |
| Saved vs parent | 656,417 |

Still above Starknet's 100M validation gas cap.

Official diff page: https://falcon.provably.fast/diff?job=mj_24fb2836aff6461f8f906ae4f48ada53

### Files
- `mldsa-44-mj_24fb2836.patch`: the patch as submitted. Like the others, it is **cumulative** against the
  baseline (`78c83599f57e`) and contains the work of many earlier contributors, not only mine.
- `our-delta-on-mj_91563198.patch`: only my change on top of the parent (`ct.cairo`, `nttu.cairo`, `pk0.cairo`).
  Apply to the parent's tree with `git apply`. Verified: the parent patch (downloaded with
  `pvfast remote mldsa patch`) on the baseline, plus this delta, gives a tree byte-identical to the baseline
  plus the official patch of job `mj_24fb2836`.

### Note on later work
**@saniksin** built `mj_0507f878` on top of this contribution, and then **@nadai2010** built `mj_80aaca36`
on top of that. Thanks!

### Disclosure
This patch was produced by the AI agent **Claude Code**, which I (**@ardianreffa**) ran and supervised. The
idea was found with the **Opus** model, and the patch was written with **Sonnet** (`claude-sonnet-5-5`).

---

## Contribution 5: cheaper z range flags, "dg3" fold (job `mj_0d051868bea64a1d9e1b606d78ceb6da`)

### The idea
In `zread`, the range flag of each z digit is computed for groups of 3 digits. The parent used 10 operations
per group. My change (`dg3`) computes the flags of 3 digits as **one constant minus three products**, which is
6 operations instead of 10, and removes a parameter `k` that was no longer used. Correctness was tested in
Python for **all 2^18 digit values at every digit position**, plus **200,000 random combinations**.

### Official result

| | Gas |
|---|---:|
| Parent `mj_345e4640` (by @saniksin) | 172,982,140 |
| **This job (accepted, record at the time)** | **172,877,140** |
| Saved vs parent | 105,000 |

Still above Starknet's 100M validation gas cap.

Official diff page: https://falcon.provably.fast/diff?job=mj_0d051868bea64a1d9e1b606d78ceb6da

### Files
- `mldsa-44-mj_0d051868.patch`: the official accepted patch (`pvfast remote mldsa patch`), identical to the one
  I submitted. Like the others, it is **cumulative** against the baseline (`78c83599f57e`) and contains the work
  of many earlier contributors, not only mine.
- `our-delta-on-mj_345e4640.patch`: only my change on top of the parent (`zread.cairo`). Apply to the parent's
  tree with `git apply`. Verified: the parent patch (downloaded with `pvfast remote mldsa patch`) on the baseline,
  plus this delta, gives a tree identical (file by file, compared by content) to the baseline plus the official
  patch of job `mj_0d051868`.

### Note on later work
**@saniksin** built `mj_163dedb1` on top of this contribution (`mj_0d051868`). Thanks!

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 6: combination of @saniksin's sibling patch onto @odinfree's record (job `mj_29ea4ca514c84d08a4ae1dfa56199170`)

> **This is a combination, not an original idea of mine.** The idea belongs to **@saniksin**
> (sibling patch `mj_d95817f8`, accepted but not yet part of the record). My contribution is only the merge.

### What I did
`mj_d95817f8` by @saniksin was accepted but had not made it into the record. I merged its patch on top of
the record `mj_a93adef3` by **@odinfree**. The merge touches `ct.cairo` and `nttu.cairo`.

### Official result

| | Gas |
|---|---:|
| Parent `mj_a93adef3` (by @odinfree) | 172,586,724 |
| **This job (accepted, not a record)** | **172,535,524** |
| Saved vs parent | 51,200 |

It did not become a record: **@saniksin** later merged their own idea again, with a slightly better result
(`mj_b44c9049`, 172,528,874 gas). Still above Starknet's 100M validation gas cap.

Official diff page: https://falcon.provably.fast/diff?job=mj_29ea4ca514c84d08a4ae1dfa56199170

### Files
- `mldsa-44-mj_29ea4ca5.patch`: the official accepted patch (`pvfast remote mldsa patch`), identical to the one
  I submitted. Cumulative against the baseline (`78c83599f57e`).
- `our-delta-on-mj_a93adef3.patch`: only the merged change on top of the parent (`ct.cairo`, `nttu.cairo`).
  Verified: the parent patch (downloaded with `pvfast remote mldsa patch`) on the baseline, plus this delta,
  gives a tree identical (`diff -r`, by content) to the baseline plus the official patch of job `mj_29ea4ca5`.
  The delta applies cleanly (`git apply --check`).

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 7: z range flags, six digits per AND (job `mj_7b79182442cc43d6a00143c1b3519897`)

### The idea
In `zread`, the range flags of z digits were computed three digits per AND. My change computes them
**six per AND**. An **offset of +78** in the division chain makes one test per digit enough; a digit that
crosses a felt boundary is still tested on both sides. The number of ANDs drops from 336 to about 200.

Evidence of correctness:
- an exhaustive Python differential test: 1,024 positions x 262,144 digit values, **zero differences**;
- mutation tests;
- 124 edge-case tests in Cairo;
- the package's 117 built-in tests.

### Official result

| | Gas |
|---|---:|
| Parent `mj_bf48924d` (by @saniksin) | 172,335,271 |
| **This job (accepted, record at the time; since beaten by @mitchuski)** | **172,230,687** |
| Saved vs parent | 104,584 |

Still above Starknet's 100M validation gas cap.

Official diff page: https://falcon.provably.fast/diff?job=mj_7b79182442cc43d6a00143c1b3519897

### Files
- `mldsa-44-mj_7b791824.patch`: the official accepted patch (`pvfast remote mldsa patch`), identical to the one
  I submitted. Cumulative against the baseline (`78c83599f57e`), so it contains the work of many earlier
  contributors, not only mine.
- `our-delta-on-mj_bf48924d.patch`: only my change on top of the parent (`zread.cairo`, `nttu.cairo`).
  Verified: the parent patch (downloaded with `pvfast remote mldsa patch`) on the baseline, plus this delta,
  gives a tree identical (`diff -r`, by content) to the baseline plus the official patch of job `mj_7b791824`.
  The delta applies cleanly (`git apply --check`).

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 17: pruned final Keccak round for mu/ball, lanes 0-7 split once (job `mj_59d79522e5bd48ab82afd3f0f0f149fa`)

> **Credit.** The record it is applied to, `mj_fc15ccfa`, is **@odinfree's**. The lane techniques it builds on come from
> **@odinfree**, **@realadii** and **@nadai2010**. **What is mine** is porting the ML-DSA-87 lane idea (contribution 16)
> to ML-DSA-44 and extending it: the pruned final round and the single split of lanes 0-7.

### The idea
1. The final Keccak round for `mu` and SampleInBall is **pruned to lanes 0-7**: the round branches after lane 7, and `hab`
   no longer flips back, because lanes 8 and up are not read.
2. Lanes 0-7 are **split once** and the same halves serve both `mu` and the SampleInBall scan; `ball_offsets` is kept as
   the fallback.

**Worst-case cost, honestly.** A signature that needs more than 56 SampleInBall candidate bytes takes the fallback, which
costs about +6.58M gas (1.041x the record's worst valid signature is the dearest *rejection* path, below the 1.25x break
line). The exact probability of needing the fallback is 2.03e-7.

Measured on 348 signatures from two local FIPS 204 keys: the 300 natural ones save 32,603.5 on average (minimum 31,772).
Correctness: 117 tests pass; 796 mu/SampleInBall vectors including the fallback and forced exhaustion; 6 mutants caught.

### Official result

| | Gas |
|---|---:|
| Parent `mj_fc15ccfa` (by @odinfree, record at the time) | 168,589,188 |
| **This job (accepted, record at the time; passed by @rukafe0x's `mj_e898606c`, then `mj_502dcc7a` and `mj_8ec4b8da`; record retaken by my `mj_11c423be`)** | **168,556,526** |
| Saved vs parent | 32,662 |

Still above Starknet's 100M validation gas cap.

### Files
- `mldsa-44-mj_59d79522.patch`: the submitted patch, cumulative against baseline `78c83599f57e`. SHA-256
  `1f86065f...dc188`.
- `our-delta-on-mj_fc15ccfa.patch`: only my change on top of the parent (`k2.cairo`, `x2.cairo`, `sa0.cairo`); apply
  with `git apply -p0`. Paths are relative to the repository root.

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 23: z NTT blocks two per call (job `mj_11c423be1bfa4e9caf8a79d060bdc9e7`)

> **Credit.** The parent record `mj_8ec4b8da` is **@rukafe0x's** (lead `rgr1_df8f78d9...`), and it carries the cold arms and
> ExpandA fifth-block work from that same line. Batching the z NTT blocks is **@binharold's** idea from ML-DSA-87 (`zf4a3`, `mk_3c0224a5`), which I
> widened to five blocks (`zf4a5`) in ML-DSA-87 `mk_14ba0499` (contribution 21). The ML-DSA-87 leads live in another graph, so the
> server does not take them as parents; that credit is in the lead's summary and the job title. **What is mine** is the port to
> ML-DSA-44.

### The idea
`pac`, the unrolled forward NTT of each z polynomial, called the `inline(never)` radix-16 block `f4a` 16 times per polynomial,
64 calls per verify. Each call costs about 200 gas of call overhead. The new `f42` (`inline(never)`) runs two blocks per call
(body `f4i`, `inline(always)`), and `pac` makes 8 calls per polynomial: 32 calls fewer. The arithmetic, the bounds and the order
of the outputs do not change. Three blocks per call would need about 128 more CASM felts; only 40 are left.

Measured on 348 signatures from two local FIPS 204 keys: -6,400 gas on every one (the NTT does not depend on the data).
Correctness: 117 bench tests pass (including ACVP); 106 forged rejection vectors are still rejected; 3 mutants of the pairing
were caught.

### Official result

| | Gas |
|---|---:|
| Parent `mj_8ec4b8da` (by @rukafe0x, record at the time) | 168,459,682 |
| **This job (accepted, record at the time; since passed by @rukafe0x's `mj_2c1f51cf`, retaken by my `mj_eaf3b3db`)** | **168,453,282** |
| Saved vs parent | 6,400 |

Still above Starknet's 100M validation gas cap. The evaluator reports CASM 81,880 of 81,920 felts and a class of 4,088,840 bytes.
Lead: `rgr1_9d92b3aec23f767b761f7f97cc465a659c6511b24c49a221d0a8d4aa1112401e`.

### Files
- `mldsa-44-mj_11c423be.patch`: the submitted patch, cumulative against baseline `78c83599f57e`. SHA-256
  `f7419b0a...6d4c5`.
- `our-delta-on-mj_8ec4b8da.patch`: only my change on top of the parent (`nttu.cairo`); apply with `git apply -p0`. Paths are
  relative to the repository root.

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 24: z NTT pairs merged onto @rukafe0x's `mj_2c1f51cf` (job `mj_eaf3b3db1b6b4050afe7a61a807a3cc4`)

> **Credit.** The parent record `mj_2c1f51cf` is **@rukafe0x's** (E71, on his `mj_a2031102` E70, on his `mj_8ec4b8da`): one bitwise
> call per SampleInBall draw, a cold fallback, the padded 12-wide flip rebuild, and everything earlier in that line. His line did not
> contain my z NTT pairs from contribution 23. Batching the z NTT blocks is **@binharold's** idea from ML-DSA-87 (`zf4a3`,
> `mk_3c0224a5`), which I widened to `zf4a5` in ML-DSA-87 and ported to ML-DSA-44 in contribution 23. **What is mine** is the merge
> and the CASM trade that makes it fit.

### What I did
- `nttu.cairo` takes my `mj_11c423be` version: `f42` (`inline(never)`) runs two radix-16 blocks per call, and `pac` makes 8 calls per
  z polynomial instead of 16 (-6,400 gas).
- With the pairs and all four of the parent's inline `i2` sites, CASM would be 81,997 felts, 77 over the 81,920 limit. One `i2`
  site (row `a0` in `mab`) goes back to the out-of-line `oaa` call: +2,000 gas, -339 CASM felts. Everything else in the parent stays.
- Net vs the parent: -6,400 + 2,000 = -4,400 gas.

Measured on 348 signatures from two local FIPS 204 keys: -4,400 gas on every one. Correctness: 117 bench tests pass (including
ACVP); 106 forged rejection vectors are still rejected; 3 mutants of the pairing were caught.

### Official result

| | Gas |
|---|---:|
| Parent `mj_2c1f51cf` (by @rukafe0x, record at the time) | 168,445,660 |
| **This job (accepted, record at the time; since passed by @solanaqubits' `mj_51c7a1c9` and later records, @solanaqubits' later record `mj_36c63657` still contained these pairs)** | **168,441,260** |
| Saved vs parent | 4,400 |

Still above Starknet's 100M validation gas cap. The evaluator reports CASM 81,658 of 81,920 felts and a class of 4,058,432 bytes.
Lead: `rgr1_44684a1c202602be7f5a454e982bb336e359f890c2d22dddb12acb6b227e3bf8`.

### Files
- `mldsa-44-mj_eaf3b3db.patch`: the submitted patch, cumulative against baseline `78c83599f57e`. SHA-256
  `46b9f726...b5655`.
- `our-delta-on-mj_2c1f51cf.patch`: only my change on top of the parent (`nttu.cairo`); apply with `git apply -p0`. Paths are
  relative to the repository root.

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Contribution 29: Keccak rounds four per out-of-line call on @rukafe0x's `mj_21ddb0a7` (job `mj_50bc7f09ddc3425d893dded14f7436ec`)

> **After the 11 Nov 2026 reset** (class budget 75%: CASM ≤ 61,440 felts, Sierra ≤ 3,067,084 bytes).
>
> **Credit.** The parent record `mj_21ddb0a7` is **@rukafe0x's** (lead `rgr1_b27bcf45...`): the first ML-DSA-44 record under the new
> budget, made from his `mj_b5729847` (E76) by putting every Keccak round, `uaa` and the NTT butterflies out of line (+8.44M gas).
> The line also holds **@solanaqubits**' composition (`mj_36c63657`), my z NTT pairs (contributions 23 and 24) and **@binharold**'s
> `zf4a3` batching. **What is mine** is the round grouping below.

### What I did
In the parent, every half-permutation `zah` called the four out-of-line rounds `jag`, `kag`, `lag`, `mag` three times each: 12 calls.
- `k2.cairo`: the four rounds are `inline(always)` again, inside one new `inline(never)` function `q4(s, ra, rb, rc, rd)`; `zah` calls
  it three times. The fourth round is skipped when its constant is 0, which is exactly the existing `r11 == 0` exit to `zai` (only
  `Yx[23]` is 0; positions 3, 7, 15 and 19 of both constant tables are nonzero).
- 12 call sites become 3, so CASM even goes down (60,978 → 59,854).

Measured locally: -2,523,680 gas on the bench, and at least that on all 348 signatures from two local FIPS 204 keys (mean -2,528,388).
Correctness: 117 bench tests pass (including the 45 ACVP vectors); 106 forged rejection vectors are still rejected.

### Official result

| | Gas |
|---|---:|
| Parent `mj_21ddb0a7` (by @rukafe0x, record at the time) | 176,839,925 |
| **This job (accepted, record as of 11 Nov 2026)** | **174,316,245** |
| Saved vs parent | 2,523,680 |

Still above Starknet's 100M validation gas cap. The evaluator reports CASM 59,854 of 61,440 felts and a class of 3,058,937 of 3,067,084
bytes (74.8%). Lead: `rgr1_2ec1ddaf72d3d3d3a793f2154a8b2254d3c88502fcb74f1ee1f0dfb906b9104c`.

### Files
- `mldsa-44-mj_50bc7f09.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `78c83599f57e`. SHA-256
  `2a2002d9...b12b54`.
- `our-delta-on-mj_21ddb0a7.patch`: only my change on top of the parent (`k2.cairo`); apply with `git apply -p0`. Paths are relative
  to the repository root.

### Disclosure
This patch was produced by the AI agent **Claude Code** (model **Opus**), which I (**@ardianreffa**) ran and supervised.

---

## Bahasa Indonesia (sederhana)

### Apa challenge-nya?
ML-DSA-44 adalah standar tanda tangan digital tahan komputer kuantum dari NIST. Memeriksa satu tanda
tangan di verifier Cairo awal memakan **618.093.928 gas** di Starknet, padahal satu akun hanya boleh
memakai **100 juta gas**. Tugasnya: bikin verifier lebih murah tanpa mengubah standarnya. Setiap hasil
yang diterima dinilai dengan gas pada 16 tanda tangan uji dan dikreditkan ke pembuatnya.

### Ide saya
Sebagian besar biaya ada di fungsi hash Keccak. Rekor sebelumnya sudah menjalankan dua hash sekaligus.
Perubahan saya ada dua:

1. **Putaran pertama tanpa lane nol.** Blok pertama ExpandA hanya mengisi 6 dari 25 "lane" data. Di
   putaran pertama, operasi XOR dengan 19 lane nol itu dilewati.
2. **Loop dipakai bersama.** Kode putaran dijadikan satu fungsi bersama, jadi tidak ada kode ganda
   (ukuran kontrak tetap di bawah batas). Perubahan ini juga menurunkan gas.

### Hasil resmi (job `mj_7279e4f3bc684d40a9653817aba67953`)
- Baseline: 618.093.928 gas.
- Rekor sebelumnya (`mj_6541e303`, oleh @rukafe0x): 197.279.501 gas.
- **Job ini (diterima, jadi rekor baru): 196.910.723 gas**, hemat 368.778 gas.
- Hasilnya masih di atas batas 100 juta gas, jadi ML-DSA-44 belum muat di satu akun.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_7279e4f3bc684d40a9653817aba67953

### Berkas
- `mldsa-44-mj_7279e4f3.patch`: patch resmi yang diterima. **Bersifat kumulatif**: berisi kerja banyak
  kontributor sebelumnya, bukan hanya saya.
- `our-delta-on-mj_6541e303.patch`: hanya perubahan saya di atas rekor sebelumnya.
- `LICENSE`: MIT, sama dengan repo baseline.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 2: Keccak dua-state dengan lane dikomplemen (job `mj_a27318a1de7247649636102756032944`)

### Ide
Keccak masih jadi biaya terbesar. Di langkah chi, tiap lane butuh operasi NOT. Dengan teknik "lane
complementing", 8 dari 25 lane disimpan dalam bentuk terkomplemen, sehingga tiap putaran hanya butuh
**6 NOT, bukan 25**. Teknik ini dipakai pada Keccak dua-state (dua hash dalam satu permutasi) milik rekor.

### Hasil resmi
- Rekor sebelumnya (`mj_97f98218`, oleh @saniksin): 186.381.868 gas.
- **Job ini (diterima, jadi rekor baru): 184.696.268 gas**, hemat sekitar 1,69 juta gas (1.685.600).
- Masih di atas batas 100 juta gas.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_a27318a1de7247649636102756032944

### Berkas
- `mldsa-44-mj_a27318a1.patch`: patch yang dikirim. **Bersifat kumulatif** (berisi kerja banyak
  kontributor sebelumnya, bukan hanya saya).
- `our-delta-on-mj_97f98218.patch`: hanya perubahan saya di atas rekor sebelumnya (`k2.cairo`). Terbukti:
  rekor sebelumnya + delta ini sama persis dengan baseline + patch resmi job `mj_a27318a1`.

### Catatan
**@saniksin** membangun rekor `mj_4d7fd14e` di atas patch pertama saya (`mj_7279e4f3`). Terima kasih!
Kemudian, **@rukafe0x** (`mj_54f1c987`) dan **@saniksin** (`mj_3d773ce6`) membangun rekor di atas kontribusi
kedua saya (`mj_a27318a1`). Terima kasih lagi! Selain itu, **@odinfree** (`mj_151471c8`) mengembangkan bentuk
lane complementing dari `mj_a27318a1` lebih jauh.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 3: putaran terakhir SHAKE-128 dipangkas di ExpandA (job `mj_db11da30c33b4e3c8dfcfd4f69519232`)

### Ide
ExpandA mengambil koefisien matriks dari SHAKE-128. Blok SHAKE-128 terakhir di tiap aliran hanya butuh
**40 kandidat**, jadi putaran Keccak terakhir cukup menghitung lane yang dibaca 40 kandidat itu. Putaran
terakhir dipangkas ke **15 lane**. Kalau 40 kandidat tidak cukup (terlalu banyak yang ditolak), kode memakai
jalur cadangan permutasi penuh, jadi hasilnya tetap sama persis dengan standar. Badan putaran juga dipakai
bersama oleh putaran-putaran yang di-unroll agar ukuran kontrak tetap kecil.

### Hasil resmi
- Parent `mj_14156814` (oleh @odinfree): 183.792.260 gas.
- **Job ini (diterima, rekor pada waktunya): 183.682.111 gas**, hemat 110.149 gas.
- Masih di atas batas 100 juta gas. Kemudian dilewati oleh `mj_0b73e40b` (oleh @odinfree, 183.310.334 gas).

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_db11da30c33b4e3c8dfcfd4f69519232

### Berkas
- `mldsa-44-mj_db11da30.patch`: patch yang dikirim. **Bersifat kumulatif** (berisi kerja banyak kontributor
  sebelumnya, bukan hanya saya).
- `our-delta-on-mj_14156814.patch`: hanya perubahan saya di atas parent (`k2.cairo`, `x2.cairo`). Terbukti:
  patch parent (diunduh dengan `pvfast remote mldsa patch`) + delta ini sama persis dengan baseline + patch resmi
  job `mj_db11da30`.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 4: UseHint dengan kali-lalu-geser, dua residu dalam satu u128 (job `mj_24fb2836aff6461f8f906ae4f48ada53`)

### Ide
Saat memeriksa tanda tangan, UseHint butuh HighBits dari tiap 1.024 residu `w'`. Parent menghitungnya
dengan pembagian oleh `2*gamma2` untuk setiap residu. Perubahan saya menghitung HighBits dengan **kali,
lalu geser**, yang hasilnya tepat untuk seluruh rentang residu. Dua residu dimasukkan ke satu `u128`, jadi
satu operasi AND mengurus sepasang. Kasus khusus `q = 44` tidak diperlukan lagi, jadi kode koreksinya
dihapus. Kebenaran aturan hint diuji terhadap FIPS 204 untuk **semua 8.380.417 nilai residu**.

### Hasil resmi
- Parent `mj_91563198` (oleh @saniksin): 176.801.176 gas.
- **Job ini (diterima, rekor pada waktunya): 176.144.759 gas**, hemat 656.417 gas.
- Masih di atas batas 100 juta gas.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_24fb2836aff6461f8f906ae4f48ada53

### Berkas
- `mldsa-44-mj_24fb2836.patch`: patch yang dikirim. **Bersifat kumulatif** (berisi kerja banyak kontributor
  sebelumnya, bukan hanya saya).
- `our-delta-on-mj_91563198.patch`: hanya perubahan saya di atas parent (`ct.cairo`, `nttu.cairo`, `pk0.cairo`).
  Terbukti: patch parent (diunduh dengan `pvfast remote mldsa patch`) + delta ini sama persis dengan baseline +
  patch resmi job `mj_24fb2836`.

### Catatan
**@saniksin** membangun `mj_0507f878` di atas kontribusi ini, lalu **@nadai2010** membangun `mj_80aaca36` di
atasnya. Terima kasih!

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).
Idenya dicari dengan model **Opus**, dan patch-nya dikerjakan dengan **Sonnet** (`claude-sonnet-5-5`).

---

## Kontribusi 5: flag rentang z yang lebih murah, lipatan "dg3" (job `mj_0d051868bea64a1d9e1b606d78ceb6da`)

### Ide
Di `zread`, flag rentang tiap digit z dihitung per 3 digit. Parent memakai 10 operasi per kelompok. Perubahan
saya (`dg3`) menghitung flag 3 digit sebagai **satu konstanta dikurangi tiga hasil kali**, yaitu 6 operasi, bukan
10, dan membuang parameter `k` yang tidak terpakai lagi. Kebenaran diuji di Python untuk **semua 2^18 nilai digit
di tiap posisi**, ditambah **200 ribu kombinasi acak**.

### Hasil resmi
- Parent `mj_345e4640` (oleh @saniksin): 172.982.140 gas.
- **Job ini (diterima, rekor pada waktunya): 172.877.140 gas**, hemat 105.000 gas.
- Masih di atas batas 100 juta gas.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_0d051868bea64a1d9e1b606d78ceb6da

### Berkas
- `mldsa-44-mj_0d051868.patch`: patch resmi yang diterima, sama dengan yang saya kirim. **Bersifat kumulatif**
  (berisi kerja banyak kontributor sebelumnya, bukan hanya saya).
- `our-delta-on-mj_345e4640.patch`: hanya perubahan saya di atas parent (`zread.cairo`). Terbukti: patch parent
  (diunduh dengan `pvfast remote mldsa patch`) + delta ini sama persis isinya dengan baseline + patch resmi job
  `mj_0d051868` (dibandingkan per berkas berdasarkan isi).

### Catatan
**@saniksin** membangun `mj_163dedb1` di atas kontribusi ini (`mj_0d051868`). Terima kasih!

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 6: gabungan patch saudara @saniksin di atas rekor @odinfree (job `mj_29ea4ca514c84d08a4ae1dfa56199170`)

> **Ini gabungan, bukan ide asli saya.** Idenya milik **@saniksin** (patch saudara `mj_d95817f8`, diterima
> tetapi belum masuk rekor). Kontribusi saya hanya menggabungkannya.

### Yang saya lakukan
`mj_d95817f8` milik @saniksin diterima tetapi belum masuk rekor. Saya menggabungkan patch itu di atas rekor
`mj_a93adef3` milik **@odinfree**. Penggabungan ini menyentuh `ct.cairo` dan `nttu.cairo`.

### Hasil resmi
- Parent `mj_a93adef3` (oleh @odinfree): 172.586.724 gas.
- **Job ini (diterima, bukan rekor): 172.535.524 gas**, hemat 51.200 gas.
- Tidak jadi rekor karena **@saniksin** kemudian menggabungkan ulang idenya sendiri dengan hasil sedikit lebih
  baik (`mj_b44c9049`, 172.528.874 gas). Masih di atas batas 100 juta gas.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_29ea4ca514c84d08a4ae1dfa56199170

### Berkas
- `mldsa-44-mj_29ea4ca5.patch`: patch resmi yang diterima, sama dengan yang saya kirim. Bersifat kumulatif.
- `our-delta-on-mj_a93adef3.patch`: hanya perubahan gabungan di atas parent (`ct.cairo`, `nttu.cairo`). Terbukti:
  patch parent (diunduh dengan `pvfast remote mldsa patch`) + delta ini sama persis isinya (`diff -r`) dengan
  baseline + patch resmi job `mj_29ea4ca5`. Delta dapat diterapkan dengan bersih.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 7: flag rentang z, enam digit per AND (job `mj_7b79182442cc43d6a00143c1b3519897`)

### Ide
Di `zread`, flag rentang digit z sebelumnya dihitung tiga digit per AND. Perubahan saya menghitungnya
**enam per AND**. **Offset +78** di rantai pembagian membuat satu uji per digit sudah cukup; digit yang
melintasi batas felt tetap diuji dari dua sisi. Jumlah AND turun dari 336 menjadi sekitar 200.

Bukti kebenaran:
- uji diferensial Python menyeluruh: 1.024 posisi x 262.144 nilai digit, **tanpa selisih**;
- uji mutasi;
- 124 uji tepi di Cairo;
- 117 tes bawaan paket.

### Hasil resmi
- Parent `mj_bf48924d` (oleh @saniksin): 172.335.271 gas.
- **Job ini (diterima, rekor pada waktunya; sudah dilewati @mitchuski): 172.230.687 gas**, hemat 104.584 gas.
- Masih di atas batas 100 juta gas.

Halaman diff resmi: https://falcon.provably.fast/diff?job=mj_7b79182442cc43d6a00143c1b3519897

### Berkas
- `mldsa-44-mj_7b791824.patch`: patch resmi yang diterima, sama dengan yang saya kirim. **Bersifat kumulatif**
  (berisi kerja banyak kontributor sebelumnya, bukan hanya saya).
- `our-delta-on-mj_bf48924d.patch`: hanya perubahan saya di atas parent (`zread.cairo`, `nttu.cairo`). Terbukti:
  patch parent (diunduh dengan `pvfast remote mldsa patch`) + delta ini sama persis isinya (`diff -r`) dengan
  baseline + patch resmi job `mj_7b791824`. Delta dapat diterapkan dengan bersih.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

## Kontribusi 17: putaran terakhir Keccak untuk mu/ball dipangkas, lane 0-7 dipecah sekali (job `mj_59d79522e5bd48ab82afd3f0f0f149fa`)

> **Kredit.** Rekor yang menjadi dasar, `mj_fc15ccfa`, milik **@odinfree**. Teknik lane yang dipakai berasal dari
> **@odinfree**, **@realadii** dan **@nadai2010**. **Bagian saya** adalah memindahkan ide lane ML-DSA-87 (kontribusi 16)
> ke ML-DSA-44 dan mengembangkannya: putaran terakhir yang dipangkas dan pemecahan lane 0-7 satu kali.

### Ide
1. Putaran Keccak terakhir untuk `mu` dan SampleInBall **dipangkas ke lane 0-7**: putaran bercabang setelah lane 7, dan
   `hab` tidak membalik lagi karena lane 8 ke atas tidak dibaca.
2. Lane 0-7 **dipecah sekali** dan hasilnya dipakai bersama oleh `mu` dan pemindaian SampleInBall; `ball_offsets`
   dipertahankan sebagai cadangan.

**Biaya terburuk, apa adanya.** Tanda tangan yang butuh lebih dari 56 byte kandidat SampleInBall memakai jalur cadangan,
sekitar +6,58 juta gas. Biaya penolakan terburuk 1,041x rekor (di bawah garis break 1,25x). Peluang butuh cadangan: 2,03e-7.

Diukur pada 348 tanda tangan dari dua kunci FIPS 204 lokal: 300 tanda tangan biasa hemat rata-rata 32.603,5 (minimum 31.772).
Pengujian: 117 tes lulus; 796 vektor mu/SampleInBall termasuk cadangan dan kehabisan paksa; 6 mutan tertangkap.

### Hasil resmi
- Parent `mj_fc15ccfa` (oleh @odinfree, rekor pada waktunya): 168.589.188 gas.
- **Job ini (diterima, rekor pada waktunya; dikalahkan `mj_e898606c` milik @rukafe0x, lalu `mj_502dcc7a` dan `mj_8ec4b8da` miliknya; rekor direbut kembali oleh `mj_11c423be` milik saya): 168.556.526 gas**, hemat 32.662 gas.
- Masih di atas batas gas validasi Starknet 100M.

### Berkas
- `mldsa-44-mj_59d79522.patch`: patch yang dikirim, kumulatif terhadap baseline `78c83599f57e`. SHA-256
  `1f86065f...dc188`.
- `our-delta-on-mj_fc15ccfa.patch`: hanya perubahan saya di atas parent (`k2.cairo`, `x2.cairo`, `sa0.cairo`);
  terapkan dengan `git apply -p0`.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 23: blok NTT z dua per panggilan (job `mj_11c423be1bfa4e9caf8a79d060bdc9e7`)

> **Kredit.** Rekor induk `mj_8ec4b8da` milik **@rukafe0x** (lead `rgr1_df8f78d9...`), dan di dalamnya ada cold arm serta kerja blok
> kelima ExpandA miliknya. Ide menggabungkan blok NTT z adalah milik **@binharold** dari ML-DSA-87 (`zf4a3`, `mk_3c0224a5`), yang
> saya lebarkan menjadi lima blok (`zf4a5`) di ML-DSA-87 `mk_14ba0499` (kontribusi 21). Lead ML-DSA-87 ada di graf lain, jadi server
> tidak menerimanya sebagai induk; kredit itu ada di ringkasan lead dan judul job. **Bagian saya** adalah memindahkannya ke ML-DSA-44.

### Ide
`pac`, NTT maju yang ditulis penuh untuk tiap polinomial z, memanggil blok radix-16 `f4a` (`inline(never)`) 16 kali per
polinomial, 64 panggilan per verifikasi. Tiap panggilan memakan sekitar 200 gas. Fungsi baru `f42` (`inline(never)`) menjalankan dua
blok per panggilan (isi `f4i`, `inline(always)`), dan `pac` hanya memanggil 8 kali per polinomial: 32 panggilan lebih sedikit.
Hitungan, batas nilai dan urutan keluaran tidak berubah. Tiga blok per panggilan butuh sekitar 128 felt CASM lagi; sisanya cuma 40.

Diukur pada 348 tanda tangan dari dua kunci FIPS 204 lokal: -6.400 gas di semuanya (NTT tidak bergantung pada data).
Pengujian: 117 tes bench lulus (termasuk ACVP); 106 vektor penolakan palsu tetap ditolak; 3 mutan pasangan tertangkap.

### Hasil resmi
- Parent `mj_8ec4b8da` (oleh @rukafe0x, rekor pada waktunya): 168.459.682 gas.
- **Job ini (diterima, rekor pada waktunya; kemudian dilewati `mj_2c1f51cf` milik @rukafe0x, lalu diambil kembali oleh `mj_eaf3b3db` saya): 168.453.282 gas**, hemat 6.400 gas.
- Masih di atas batas gas validasi Starknet 100M. Evaluator mencatat CASM 81.880 dari 81.920 felt dan class 4.088.840 byte.
- Lead: `rgr1_9d92b3aec23f767b761f7f97cc465a659c6511b24c49a221d0a8d4aa1112401e`.

### Berkas
- `mldsa-44-mj_11c423be.patch`: patch yang dikirim, kumulatif terhadap baseline `78c83599f57e`. SHA-256
  `f7419b0a...6d4c5`.
- `our-delta-on-mj_8ec4b8da.patch`: hanya perubahan saya di atas parent (`nttu.cairo`); terapkan dengan `git apply -p0`.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 24: pasangan NTT z digabung ke `mj_2c1f51cf` milik @rukafe0x (job `mj_eaf3b3db1b6b4050afe7a61a807a3cc4`)

> **Kredit.** Rekor induk `mj_2c1f51cf` milik **@rukafe0x** (E71, di atas `mj_a2031102` E70 miliknya, di atas `mj_8ec4b8da` miliknya):
> satu panggilan bitwise per undian SampleInBall, fallback dingin, flip rebuild 12 lebar dengan padding, dan semua kerja sebelumnya di
> jalur itu. Jalurnya belum berisi pasangan NTT z saya dari kontribusi 23. Ide menggabungkan blok NTT z adalah milik **@binharold** dari
> ML-DSA-87 (`zf4a3`, `mk_3c0224a5`), yang saya lebarkan menjadi `zf4a5` di ML-DSA-87 dan saya pindahkan ke ML-DSA-44 di kontribusi 23.
> **Bagian saya** adalah penggabungannya dan tukar-tambah CASM supaya muat.

### Yang saya kerjakan
- `nttu.cairo` memakai versi `mj_11c423be` saya: `f42` (`inline(never)`) menjalankan dua blok radix-16 per panggilan, dan `pac`
  memanggil 8 kali per polinomial z, bukan 16 (-6.400 gas).
- Dengan pasangan itu dan keempat situs `i2` inline milik induk, CASM menjadi 81.997 felt, 77 di atas batas 81.920. Satu situs `i2`
  (baris `a0` di `mab`) dikembalikan ke panggilan `oaa` di luar baris: +2.000 gas, -339 felt CASM. Bagian lain dari induk tetap.
- Bersih terhadap induk: -6.400 + 2.000 = -4.400 gas.

Diukur pada 348 tanda tangan dari dua kunci FIPS 204 lokal: -4.400 gas di semuanya. Pengujian: 117 tes bench lulus (termasuk ACVP);
106 vektor penolakan palsu tetap ditolak; 3 mutan pasangan tertangkap.

### Hasil resmi
- Parent `mj_2c1f51cf` (oleh @rukafe0x, rekor pada waktunya): 168.445.660 gas.
- **Job ini (diterima, rekor pada waktunya; kemudian dilewati `mj_51c7a1c9` milik @solanaqubits dan rekor-rekor sesudahnya; rekor ML-DSA-44 berikutnya, `mj_36c63657` milik @solanaqubits (9 Nov 2026), masih memuat pasangan ini): 168.441.260 gas**, hemat 4.400 gas.
- Masih di atas batas gas validasi Starknet 100M. Evaluator mencatat CASM 81.658 dari 81.920 felt dan class 4.058.432 byte.
- Lead: `rgr1_44684a1c202602be7f5a454e982bb336e359f890c2d22dddb12acb6b227e3bf8`.

### Berkas
- `mldsa-44-mj_eaf3b3db.patch`: patch yang dikirim, kumulatif terhadap baseline `78c83599f57e`. SHA-256
  `46b9f726...b5655`.
- `our-delta-on-mj_2c1f51cf.patch`: hanya perubahan saya di atas parent (`nttu.cairo`); terapkan dengan `git apply -p0`.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Kontribusi 29: ronde Keccak empat per panggilan di luar baris, di atas `mj_21ddb0a7` milik @rukafe0x (job `mj_50bc7f09ddc3425d893dded14f7436ec`)

> **Sesudah reset 11 Nov 2026** (batas class 75%: CASM ≤ 61.440 felt, Sierra ≤ 3.067.084 byte).
>
> **Kredit.** Rekor induk `mj_21ddb0a7` milik **@rukafe0x** (lead `rgr1_b27bcf45...`): rekor ML-DSA-44 pertama dengan batas baru, dibuat
> dari `mj_b5729847` (E76) miliknya dengan memindahkan setiap ronde Keccak, `uaa`, dan butterfly NTT ke luar baris (+8,44 juta gas). Jalur
> itu juga memuat komposisi **@solanaqubits** (`mj_36c63657`), pasangan NTT z saya (kontribusi 23 dan 24), dan batching `zf4a3` milik
> **@binharold**. **Bagian saya** adalah pengelompokan ronde di bawah ini.

### Yang saya kerjakan
Di induk, setiap setengah permutasi `zah` memanggil empat ronde di luar baris (`jag`, `kag`, `lag`, `mag`) masing-masing tiga kali: 12 panggilan.
- `k2.cairo`: keempat ronde kembali `inline(always)`, di dalam satu fungsi baru `inline(never)` `q4(s, ra, rb, rc, rd)`; `zah` memanggilnya
  tiga kali. Ronde keempat dilewati kalau konstantanya 0, persis jalur keluar `r11 == 0` ke `zai` yang sudah ada (hanya `Yx[23]` yang 0;
  posisi 3, 7, 15, dan 19 di kedua tabel konstanta bukan nol).
- 12 titik panggilan menjadi 3, jadi CASM malah turun (60.978 → 59.854).

Diukur lokal: -2.523.680 gas di bench, dan minimal sebesar itu di semua 348 tanda tangan dari dua kunci FIPS 204 lokal (rata-rata
-2.528.388). Pengujian: 117 tes bench lulus (termasuk 45 vektor ACVP); 106 vektor penolakan palsu tetap ditolak.

### Hasil resmi
- Parent `mj_21ddb0a7` (oleh @rukafe0x, rekor pada waktunya): 176.839.925 gas.
- **Job ini (diterima, rekor per 11 Nov 2026): 174.316.245 gas**, hemat 2.523.680 gas.
- Masih di atas batas gas validasi Starknet 100M. Evaluator mencatat CASM 59.854 dari 61.440 felt dan class 3.058.937 dari 3.067.084 byte (74,8%).
- Lead: `rgr1_2ec1ddaf72d3d3d3a793f2154a8b2254d3c88502fcb74f1ee1f0dfb906b9104c`.

### Berkas
- `mldsa-44-mj_50bc7f09.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `78c83599f57e`. SHA-256
  `2a2002d9...b12b54`.
- `our-delta-on-mj_21ddb0a7.patch`: hanya perubahan saya di atas parent (`k2.cairo`); terapkan dengan `git apply -p0`.

### Pernyataan jujur
Patch ini dikerjakan oleh agent **Claude Code** (model **Opus**) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## ML-DSA-87

Thirteen accepted contributions to the **ML-DSA-87** (NIST level 5) account season on
[falcon.provably.fast](https://falcon.provably.fast/mldsa87). Here a transaction's validation is scored in
Sierra gas, mean over the held-out set; the season baseline (`23d05d6a2412`) costs 401,296,683 gas. For both
jobs, the official patch is the accepted one saved with `pvfast remote mldsa87 patch` (client 1.38.0). Like
before, official patches are **cumulative** against the baseline and contain the work of many earlier
contributors, mainly **@nadai2010**'s long record line, not only mine.

> **Disclosure / Pernyataan:** all thirteen ML-DSA-87 patches were produced by an AI agent, **Claude Code**
> (models Sonnet and Opus), which I (**@ardianreffa**) ran and supervised. The job titles on the board say so.
> Ketiga belas patch ML-DSA-87 dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya
> (**@ardianreffa**) jalankan dan awasi. Judul job di papan skor juga menyebutkannya.

### English

#### Contribution 8: UseHint by multiply-shift for ML-DSA-87 (job `mk_3691ffe9c59140c3a9a6ac1c1ea3272a`)

##### The idea
This is the same technique as contribution 4, rebuilt for ML-DSA-87's parameters (`gamma2 = (q-1)/32`, so 16
HighBits values instead of 44). UseHint needs HighBits of every residue. Instead of a division, it is computed as
`HighBits(r) = (((r + gamma2) mod q) * 1049601) >> 39`. Two coefficients, `i` and `i+16`, share one `u128`, so one AND
handles the pair. The `gamma2` bias is not added per coefficient: it is folded into the constant `OFF` of the
inverse NTT.

Correctness: the formula was tested in Python for **every r from 0 to q-1**, together with the hint rule against
FIPS 204, plus **200,000 random blocks**.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_610ffcb9` (by @nadai2010) | 112,803,840 |
| **This job (accepted, record at the time)** | **110,867,290** |
| Saved vs parent | 1,936,550 |

Still above Starknet's 100M validation gas cap.

##### Files
- `mldsa-87-mk_3691ffe9.patch`: the official accepted patch, cumulative against baseline `23d05d6a2412`.
- `our-delta-on-mk_610ffcb9.patch`: only my change on top of the parent (`nttu.cairo`, `packing.cairo`,
  `verify.cairo`). Verified: the parent patch (downloaded with `pvfast remote mldsa87 patch`) on the baseline, plus this
  delta, gives a tree identical (`diff -r`, by content) to the baseline plus the official patch of job `mk_3691ffe9`.
  The delta applies cleanly (`git apply --check`). The patch I originally submitted gives the same tree as the
  official one.

#### Contribution 9: mu and the first SampleInBall block in one two-state permutation (job `mk_469c1cb9a18e4f3793a7e2e0c7a3d172`)

> **The two-state technique is not my invention.** It comes from **@rukafe0x**, who introduced it in the
> ML-DSA-44 line as `mj_366ff85e` ("92 Keccak-f as 46 two-state permutations", two sponges per `u128`,
> including "mu with SampleInBall"). Later ML-DSA-44 records developed it further (for example
> @saniksin's `mj_97f98218` and my own lane-complemented version, contribution 2). **What is mine is the
> port to ML-DSA-87**, where the record had no two-state Keccak.

##### What I did
In ML-DSA-87 the two Keccak calls for `mu` and for the first SampleInBall block are independent, so they run as
**one two-state permutation**: `mu` in the low 64 bits of each lane word, SampleInBall in the high 64 bits.
I took the plain two-state permutation from the ML-DSA-44 code (`k2.cairo`, trimmed to the permutation only).
The 24 rounds are a **loop of 6 iterations x 4 rounds**, because a 12-round unroll made the compiled contract
too big for the CASM limit (95,163 felts against 81,920 allowed); the loop costs only about 27k gas. Lane words are packed
with felt arithmetic and unpacked in a loop to save size.

Correctness: **400 random inputs** compared against the ordinary permutation, for `mu` and for **all 25 lanes**
of the second state, and all the package's tests.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_3691ffe9` (my contribution 8) | 110,867,290 |
| **This job (accepted, ML-DSA-87 record when submitted)** | **109,484,394** |
| Saved vs parent | 1,382,896 |

Still above Starknet's 100M validation gas cap (about 9.5M gas to go).

##### Files
- `mldsa-87-mk_469c1cb9.patch`: the official accepted patch, cumulative against baseline `23d05d6a2412`.
- `our-delta-on-mk_3691ffe9.patch`: only my change on top of the parent (new `k2.cairo`, plus `keccak.cairo`,
  `lib.cairo`, `sampling.cairo`, `verify.cairo`). Verified: the parent patch (downloaded with
  `pvfast remote mldsa87 patch`) on the baseline, plus this delta, gives a tree identical (`diff -r`, by content) to
  the baseline plus the official patch of job `mk_469c1cb9`. The delta applies cleanly (`git apply --check`).
  The patch I originally submitted gives the same tree as the official one.

#### Contribution 11: SampleInBall 8 bytes per lane, fallback as a lane walk (job `mk_a5460736f4cc428f9ca70cc5451da1eb`)

> **Credit.** The 8-bytes-per-lane SampleInBall unroll is **@cheelax's** idea (job `mk_d8f3f635`); on its own it
> did not fit the CASM limit on the record `mk_96cbecf3` (also @cheelax, built on **@rukafe0x's** lane
> SampleInBall `mk_cc04a71b`). **What is mine** is making it fit: the separate byte-stream fallback is replaced by
> continuing the same lane walk over the lanes of the re-permuted state. This is **not a record**: other jobs
> were ahead of it in the queue.

##### What I did
`ball_lanes` reads the 8 bytes of each lane without the inner loop (one inline step per byte, keeping the bounded
byte and sign reads of the parent). The old fallback (`ball_stream` + `next_byte`, about 3.1k CASM) is dropped; when
the first block is not enough, the walk simply continues over the 17 lanes of `keccak_f1600(state)`. That frees the
CASM the unroll needs. Only `sampling.cairo` differs from the parent.

Correctness: **2,200 SampleInBall vectors** against the FIPS 204 Python reference (1,500 hashed, 300 fallback,
150 edge, 200 collision-heavy, 50 extreme), run on the new code and on the record; 4 deliberately broken variants
were caught; 8 account tests and 115 bench tests pass.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_96cbecf3` (by @cheelax, record at the time) | 100,045,402 |
| **This job (accepted)** | **99,827,006** |
| Saved vs parent | 218,396 |

Worst held-out case 99,940,059, so this job fits Starknet's 100M validation gas cap (`fits_validation_cap: true`).
CASM 81,357 of 81,920 felts.

##### Files
- `mldsa-87-mk_a5460736.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. Its SHA-256
  (`871eceec...3dc01`) equals the `patch_sha256` the scorer reported for the job.
- `our-delta-on-mk_96cbecf3.patch`: only my change on top of the parent (`sampling.cairo`). Verified: the parent
  patch (downloaded with `pvfast remote mldsa87 patch`) on the baseline, plus this delta, gives a tree identical
  (`diff -r`) to the baseline plus the submitted patch. The delta applies cleanly (`git apply --check`).

##### An older job, honestly
Job `mk_365efc2199124cd1abeea2340789635c` (the same SampleInBall idea merged on `mk_779abbe3`) finished as
**REJECTED** (`CHECK_FAILED`): the checks `no_corpus000`-`002` and `no_zero_t1_c_tilde_32/40/48/56/63` failed. It is
not one of my contributions and no patch of it is published here.

#### Contribution 14: bounded lanes for `tr`, typed `u64` lanes, inlined SampleInBall scan (job `mk_00f892fd18bc486f8a63a924c82983b4`)

> **Credit.** The bounded-lane technique is **@odinfree's** (`lanes8`, job `mk_bc0b5b94`, building on his bounded `div_rem`
> mu splits). The record it is applied to, `mk_3400423b`, is **@mitchuski's**. **What is mine** is carrying the same
> structure over to `lanes8t`, the function that rebuilds `tr` from the cache on every validate, and the follow-ups below.

##### What I did
1. `keccak::lanes8t` used six `u128` DivRem plus `u128` add/mul. It now uses the same bounded split as `lanes8`
   (`bounded_int_div_rem` by 2^64 and 32, lanes 3 and 5 by `cb::add`/`cb::mul`, lane 7 by downcast): -10,220 gas.
2. `lanes8` and `lanes8t` return `u64`-bounded lanes, so `mu_and_ball_rate` packs `tr|c_tilde` with `fk::aa` and the
   final `c_tilde` check compares `fk::aa` pairs. This removes 11 felt `try_into`: -3,500 gas.
3. `sampling::ball_scan` and `ball_done` are `inline(always)`: -3,900 gas.

Local total: -17,620 gas (`bench_validate`). Behavior note: lane 7 of `tr` is now downcast to below 2^64 instead of
`try_into` `u128`; for every cache written by setup it always fits, and a malformed cache returns `false` as before.

Correctness: 8 account tests and 115 bench tests pass; **2,200 SampleInBall vectors** against the FIPS 204 Python
reference pass; a mutant with lanes 6 and 7 swapped was caught by 2 account tests.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_3400423b` (by @mitchuski, record at the time) | 88,055,082 |
| **This job (accepted, record at the time; since passed by @binharold's `mk_5276df6b`, 87,546,333)** | **88,037,462** |
| Saved vs parent | 17,620 |

Still below Starknet's 100M validation gas cap. CASM was 81,288 of 81,920 felts in my dev build.

##### Files
- `mldsa-87-mk_00f892fd.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `de6ded47...8518d`.
- `our-delta-on-mk_3400423b.patch`: only my change on top of the parent (`keccak.cairo`, `sampling.cairo`,
  `verify.cairo`, `zread.cairo`); apply with `git apply -p0`. Paths are relative to the repository root.

#### Contribution 16: SampleInBall rate lanes 10-16 split on demand (job `mk_a7b5d29dd6fa45bfb3f5c1a3233fd066`)

> **Credit.** The record it is applied to, `mk_618454a1`, is **@odinfree's**. **What is mine** is splitting the rate lanes
> only when they are needed, and dropping the round constants nobody reads any more.

##### What I did
1. `mu_and_ball_rate` used to split all 17 rate lanes, although about 90% of signatures finish SampleInBall inside lanes
   0-9. Lanes 10-16 now stay packed and `ball_lanes` splits them when the first batch runs out.
2. `ROUND_CONSTANTS` in `fk` is cut to the 16 entries still read, because rounds 15-22 are baked into the fused round
   function: 0 gas, CASM -8.

Measured on 169 real signatures: -7,270 gas when the first batch suffices, -200 gas when the second batch is needed
(27 of 27 such signatures); expected mean -6,574. Correctness: 8 account tests and 115 bench tests pass; 19 SampleInBall
tests (2,200 vectors including the fallback) pass; three mutants were caught. The third-batch path (`ball_more`) was reached
only by crafted SampleInBall states.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_618454a1` (by @odinfree, record at the time) | 87,520,231 |
| **This job (accepted, record at the time, passed by my own `mk_29251ad0` on 1 Nov 2026)** | **87,513,845** |
| Saved vs parent | 6,386 |

Still below Starknet's 100M validation gas cap. CASM was 81,694 of 81,920 felts in my dev build.

##### Files
- `mldsa-87-mk_a7b5d29d.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `1413e3cb...c0c2c`.
- `our-delta-on-mk_618454a1.patch`: only my change on top of the parent (`fk.cairo`, `keccak.cairo`, `sampling.cairo`,
  `verify.cairo`); apply with `git apply -p0`. Paths are relative to the repository root.

#### Contribution 18: @rukafe0x's QUAD SampleInBall table ported, 241 entries (job `mk_29251ad0c80646bdb8b857cefa1b9b7d`)

> **Credit.** The table is **@rukafe0x's**, from `mk_9129f98a` (lead `rgr1_b505b848...`). **@odinfree** made the signed
> nibble lookup it descends from, and **@odinfree** and **@nadai2010** made the Keccak hoists, hint spans and setup work that
> @rukafe0x's lead carries and that are on this record line. **What is mine** is porting the table onto `mk_a7b5d29d`
> and trimming it to 241 entries.

##### What I did
1. `bits()` looked up two tables per nibble pair (`NIBC`, then `TRIT`). `QUAD[pb + 16 nb]` gives the four coefficients in one
   lookup, which removes one lookup for each of 64 nibble pairs. The span is built once in `ball_done`.
2. @rukafe0x's table has 256 entries. `p` and `n` are disjoint, so a pair with `nb = 15` has `pb = 0` and the index stays at
   or below 240: 241 entries suffice.

Only this part of @rukafe0x's lead is here. Its z butterfly was left out: on this record it saves 1,600 gas per site for about
142 CASM felts, and only one site fits. Its inline `sig_decode` was not ported either.

Measured on 169 real signatures: -50,780 gas on every one, including those that need the second batch. Correctness: 8 account
tests and 115 bench tests pass; 19 SampleInBall tests (2,200 vectors including the fallback) pass; one wrong-table-entry mutant
was caught. The dearest rejection I could build (ground `c_tilde` with 75 hints) costs 1.0016x the worst valid signature
(limit 1.25x); that is the worst I built, not a proven maximum.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_a7b5d29d` (mine, record at the time) | 87,513,845 |
| **This job (accepted, record at the time, passed by @binharold's `mk_3c0224a5`, record retaken by my `mk_14ba0499`)** | **87,463,065** |
| Saved vs parent | 50,780 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 81,761 of 81,920 felts and a class of 3,928,741 bytes.
Lead: `rgr1_ed00e7024d7316916da75f3b2cf301570dbd6e77ef40783dfcaf4584345506e2`.

##### Files
- `mldsa-87-mk_29251ad0.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `6969a9fc...dab29`.
- `our-delta-on-mk_a7b5d29d.patch`: only the change on top of the parent (`sampling.cairo`); apply with `git apply -p0`.
  Paths are relative to the repository root.

#### Contribution 21: one box pop per row and per z, `zf4a5` batching (job `mk_14ba049949954bf4acac786dd79807b5`)

> **Credit.** The parent record `mk_3c0224a5` and the `zf4a3` batching of z NTT blocks are **@binharold's** (lead `rgr1_6e195551...`).
> The lazy box reads follow **@nadai2010's** box-pointer group bodies (lead `rgr1_70e549c6...`). **@rukafe0x's** z butterfly
> (lead `rgr1_b505b848...`) first removed `zf4a` calls in `ntt_z`. **What is mine** is finding the unneeded pops and slices on the row
> and z paths, replacing them with one box pop, and extending the batching from three blocks to five with the CASM that freed.

##### What I did
Gas figures are score changes, in the order the steps were built.

1. `verify_decoded` paid `slice(256*j,256)` plus a pop for each z NTT. Now `ntt_z` takes one `@Box<[ZC87;256]>` and z is walked by pops,
   with no `j` counter: -14,410 gas and 183 fewer CASM felts.
2. `intt_row` popped eight 64-cell boxes per row. Now it reads one 512-cell box, popped once inside `vrow`, and the odd row of a pair
   drops one element with `pop_front` instead of `slice(1,512)`: -30,480 gas. Box reads are lazy, so one pattern at the top costs no more
   than eight. The pop sits inside `vrow` because Sierra debug names count toward the class size: holding the box across calls put the
   class 39,864 bytes over the limit.
3. @binharold's `zf4a3` became `zf4a5`, three calls per `ntt_z` instead of five: -3,200 gas for 284 CASM felts.

Measured on 169 real signatures: -59,290 gas of raw validate on every one. `ntt_z` also lowers the baseline by 11,200 gas, so the score
falls by 48,090. Correctness: 8 account tests and 115 bench tests pass; 19 SampleInBall tests (2,200 vectors) pass; 4 rejection vectors
are still rejected; two mutants (row offset, `intt_row` input order) were caught. The dearest rejection I built costs 1.0016x the worst
valid signature (limit 1.25x); that is the worst I built, not a proven maximum.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_3c0224a5` (@binharold, record at the time) | 87,447,565 |
| **This job (accepted, record at the time; passed by @rukafe0x's line ending in `mk_7c976a34`, record retaken by my `mk_4ff5f9db`)** | **87,399,475** |
| Saved vs parent | 48,090 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 81,603 of 81,920 felts and a class of 4,051,090 bytes.
Lead: `rgr1_6fc597643e64ec59293e1ef78f7b2c1d0c49d076cf4f6bfc48e577aece341c10`.

##### Files
- `mldsa-87-mk_14ba0499.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `0b1a3ea8...81e54`.
- `our-delta-on-mk_3c0224a5.patch`: only the change on top of the parent (`cache.cairo`, `nttu.cairo`, `verify.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

#### Contribution 22: z felts split Wide-only, cold SampleInBall fallback (job `mk_4ff5f9db085d4a2bbff6a624902c84bb`)

> **Credit.** Almost all of this record is **@rukafe0x's**. The parent record `mk_7c976a34` is his (lead `rgr1_c4750f63...`). The
> marker bit and the Wide-only split of cache felts come from his `mk_0ed9df51` (lead `rgr1_a8b48c6c...`). The cold arm, a rare branch
> moved out of line with its own gas withdrawal, comes from his ML-DSA-44 record `mj_e898606c` (lead `rgr1_c805af03...`; the server did
> not accept an ML-DSA-44 lead as a parent of an ML-DSA-87 lead, so that credit is in the lead's summary and the job title). **What is
> mine** is seeing that the same Wide-only split applies to the signature's z felts, proving why that is exact, and porting the cold arm.

##### What I did
1. `g5` and `zstep` split each z felt of the signature into u128 halves through `u256`. That conversion has a Narrow arm (value below
   2^128) and a Wide arm, and the two arms merge again, which costs gas on every felt. The new helper `wz` keeps only the Wide arm and
   panics on Narrow, like @rukafe0x's split of the marked cache felts. It is used for the 145 z felts (`f0..f3` in `g5`, `f4`/`f9` in
   `zstep`, the last z felt `g4` and felt 2): -41,500 gas.
2. The SampleInBall fallback (past the 17 lanes of the first block) moved into an `inline(never)` function `cold_ball` that calls
   `core::gas::withdraw_gas()`, so the common path is not charged for it: -700 gas.

**Why the panic never hits a valid signature.** FIPS 204 packs each z coefficient as `gamma1 - z` in 20 bits, and a valid z has
`|z| < gamma1 - beta` (beta = 120), so every field of a valid signature is at least 121, never 0. The signature felts are
little-endian 31-byte chunks. In every decoded felt the high half (bits 128..247) holds only z bits, at least five whole fields, so
it is not zero. In the last z felt, bits 128..143 are bits 4..19 of the last field, at least 121 >> 4 = 7. So a felt below 2^128 in
these places means an invalid signature. The record returned `false` later for it; this job panics, so validation still fails. The
`c_tilde`, `tr` and hint felts keep the `u256` split, because they can be zero for valid inputs.

Measured on 169 real signatures: -42,200 gas of raw validate on every one; the baseline does not change. Correctness: 8 account tests
and 115 bench tests pass; 19 SampleInBall tests (2,200 vectors) pass; the 4 old rejection vectors are still rejected; 3 new rejection
vectors (a valid signature with the high half of one z felt set to zero, at felt 10, felt 2 and the last z felt) are rejected by both
the record (returns 0) and this job (panics); a mutant with the halves swapped in `wz` was caught.

What did not fit: handling two row groups per call (one pop for both) saved 186,690 gas but added about 404 KB of Sierra and 2.5k CASM
felts, over both limits.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_7c976a34` (@rukafe0x, record at the time) | 87,013,066 |
| **This job (accepted, record at the time; since passed by my own `mk_790f1c30`)** | **86,970,866** |
| Saved vs parent | 42,200 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 80,027 of 81,920 felts and a class of 4,075,777 bytes.
Lead: `rgr1_a6317ec382d235a6b9c80317cb966ab38ce38cb156d2f3c28f7e8c392b6a4b61`.

##### Files
- `mldsa-87-mk_4ff5f9db.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `4ba00a65...826c3`.
- `our-delta-on-mk_7c976a34.patch`: only the change on top of the parent (`sampling.cairo`, `zread.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

#### Contribution 25: @rukafe0x's 18 row groups per call, paid in Sierra by setup-only cache code (job `mk_790f1c3001844e5cb4ee195485e582d1`)

> **Credit.** Both gas techniques are **@rukafe0x's**, from his accepted job `mk_1b5b9dea` (lead `rgr1_0a891997...`), which he built on
> his own `mk_7c976a34` line, not on my record. **What is mine** is the port onto my record `mk_4ff5f9db`, and the setup-only cleanup
> that makes it fit the class size limit.

##### What I did
1. `rowp::row_groups` handles 18 column groups per call instead of 13, so the 51 groups take three calls instead of four; the
   length check sits at group 16, where the third call reaches the trailing block. Exactly @rukafe0x's `rowp.cairo`.
2. `sampling::ball_done` is `inline(never)` (@rukafe0x): about -20.4 KB of Sierra and -411 CASM felts.
3. A straight port of 1 and 2 onto `mk_4ff5f9db` was 10,323 bytes over the Sierra class limit: each extra call site in `row_groups`
   costs about 8.9 KB, most of it `drop` statements in the panic arms of its ten `unwrap` calls. To pay for it I tidied code that runs
   only in `fill_cache` (the account setup, which is not scored):
   - `cache::part` reads each part's window (half, first group, coefficients per column, window offset and length, tail, starts with
     `tr`) from a constant table `PT`, precomputed from `BOUNDS`, instead of u32 arithmetic whose overflow checks all need panic arms.
   - The four columns are interleaved with a panic-free helper `take4` and `head`, instead of `unwrap` and indexing.
   - `col_into` slices each row to `count` coefficients and loops while column 0 still holds a whole group of five, so the loop
     counter and `last` are gone. The groups written are the same: `count` is 5 * (last + 1), or 256 = 5 * 51 + 1 for the tail part.
   Together: -10.4 KB of Sierra, -556 CASM felts, and -382,530 gas of setup per account. The cache content does not change.

Measured on 169 real signatures: -3,640 gas of validate on average (from -3,790 to -3,610); local score -3,610. Correctness: 8 account
tests and 115 bench tests pass; 19 SampleInBall tests (2,200 vectors) pass; all 169 paired signatures validate, and the 7 rejection
vectors are still rejected; a mutant with one window offset changed in `PT` was caught (signature tests fail).

##### Official result

| | Gas |
|---|---:|
| Parent `mk_4ff5f9db` (mine, record at the time) | 86,970,866 |
| **This job (accepted, record at the time; since passed by @rukafe0x's `mk_711ea4cc` line, retaken by my `mk_0e77da11`)** | **86,967,233** |
| Saved vs parent | 3,633 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 80,650 of 81,920 felts and a class of 4,088,242 bytes
(1,204 bytes under the limit).
Lead: `rgr1_5e6a80537952ff340ae69e2b92a01333c3657fffff11daf18396b283b01df00a`.

##### Files
- `mldsa-87-mk_790f1c30.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `0a9b7ce8...16fa4d`.
- `our-delta-on-mk_4ff5f9db.patch`: only the change on top of the parent (`cache.cairo`, `rowp.cairo`, `sampling.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

#### Contribution 26: my missing techniques ported onto @rukafe0x's `mk_711ea4cc` (job `mk_0e77da11fb4349aaaf5fd89f3f40adae`)

> **Credit.** The parent record `mk_711ea4cc` is **@rukafe0x's** (lead `rgr1_969d40bc...`): seven cache windows with one straddling
> the halves, on his `mk_295151d9` and `mk_04b420bb` (SampleInBall constrain split at 128, high-only reject test, balanced Bitwise
> paths), on his `mk_1b5b9dea`, all on **@binharold**'s `mk_3c0224a5` line. His line forked from `mk_1b5b9dea` before my
> `mk_4ff5f9db` and `mk_790f1c30`, so it did not contain their techniques. The Wide-only split idea is his (`mk_0ed9df51`), and so
> is the cold-arm technique (ML-DSA-44 `mj_e898606c`). **What is mine** is putting these back on his record and making them fit.

##### What I did
1. `zread.cairo` is my `mk_790f1c30` version verbatim (contribution 22): z felts are split through the Wide arm only, and a Narrow
   felt panics. A valid z field gives gamma1 - z >= 121, so no valid signature has a zero high half there. -41,500 gas.
2. `sampling`: the SampleInBall fallback past `c_tilde`'s first block moves to an `inline(never)` `cold_ball` with its own
   `withdraw_gas`, so the common path is not charged for it (contribution 22). -700 gas.
3. Steps 1 and 2 alone are 3,145 bytes over the Sierra class limit. I paid for that in code that runs only in `fill_cache` (account
   setup, not scored), re-deriving my contribution 25 cleanup for his seven windows: `window()` reads (half, first group, count,
   offset, length, tail, starts with `tr`) from a constant table `PT` of 8 window pieces (part 3 straddles the halves, so it is pieces
   3 and 4); the columns are interleaved with the panic-free `take4`/`head`; `col_into` slices rows to `count` and loops on pops.
   The cache content does not change.

Local score (`bench_validate - bench_baseline`): -42,200, exactly the official result. Correctness: 8 account tests, 115 bench tests and
19 SampleInBall tests pass; all 169 paired signatures validate, the 4 older rejection vectors and 3 Narrow-z vectors are rejected (the
parent fails those 3, as expected); a mutant with one `PT` offset changed was caught.

##### Official result

| | Gas |
|---|---:|
| My previous record `mk_790f1c30` (contribution 25) | 86,967,233 |
| Parent `mk_711ea4cc` (by @rukafe0x, record at the time) | 86,933,808 |
| **This job (accepted, record at the time; since passed by @rukafe0x's `mk_a05fd935`, retaken by my `mk_195e9e3e`)** | **86,891,608** |
| Saved vs parent | 42,200 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 80,457 of 81,920 felts and a class of 4,085,182 bytes.
Lead: `rgr1_8338e85c38fc36b3d3cbca8f5cf04dfd9875d795041608ae011afeb0686cf732`.

##### Files
- `mldsa-87-mk_0e77da11.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `b260db8e...a28fc`.
- `our-delta-on-mk_711ea4cc.patch`: only the change on top of the parent (`cache.cairo`, `sampling.cairo`, `zread.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

#### Contribution 27: the same techniques put onto @rukafe0x's `mk_a05fd935` (job `mk_195e9e3e62e744dd93957ebc53ab3a33`)

> **Credit.** The parent record `mk_a05fd935` is **@rukafe0x's** (lead `rgr1_d2ddaffe...`): `rowp` `grp1` returns `Option` and pops
> its 17 groups once, and the Keccak first block / theta skips work on lanes known to be zero (-350K). It builds on his `mk_711ea4cc`
> (seven cache windows, lead `rgr1_969d40bc...`), on **@binharold**'s `mk_3c0224a5` line, and did not contain my contribution 26.
> The Wide-only split idea is his (`mk_0ed9df51`). **What is mine** is the delta itself (contributions 22, 25 and 26).

##### What I did
`mk_a05fd935` changes only `k2`, `keccak`, `rowp` and `verify` on top of `mk_711ea4cc`; it does not touch `zread`, `sampling` or
`cache`. So the contribution 26 delta applies unchanged (the file `our-delta-on-mk_a05fd935.patch` is byte-identical to
`our-delta-on-mk_711ea4cc.patch`):
1. `zread.cairo`: z felts split through the Wide arm only; a Narrow felt panics (no valid signature has a zero high half). -41,500 gas.
2. `sampling`: the SampleInBall fallback moves to an `inline(never)` `cold_ball` with its own `withdraw_gas`. -700 gas.
3. Setup only (`fill_cache`, not scored): the `PT` window table, `take4`/`head` and `col_into`. The parent has about 112 KB of Sierra
   headroom, so this step is no longer needed for size; I kept it so the delta stays the one already accepted in contribution 26.

Local score (`bench_validate - bench_baseline`): -42,200, exactly the official result. Correctness: 8 account tests, 115 bench tests and
19 SampleInBall tests pass; all 169 paired signatures validate, the 4 older rejection vectors and 3 Narrow-z vectors are rejected (the
parent fails those 3, as expected).

##### Official result

| | Gas |
|---|---:|
| My previous record `mk_0e77da11` (contribution 26) | 86,891,608 |
| Parent `mk_a05fd935` (by @rukafe0x, record at the time) | 86,584,015 |
| **This job (accepted, record at the time, until the 11 Nov 2026 reset)** | **86,541,815** |
| Saved vs parent | 42,200 |

Still below Starknet's 100M validation gas cap. The evaluator reports CASM 76,670 of 81,920 felts and a class of 3,990,364 bytes.
Lead: `rgr1_cdc530f48fa6fa99b1f6316ea5740725e3335b0f2d5c5f3852075d6595eb9fba`.

##### Files
- `mldsa-87-mk_195e9e3e.patch`: the submitted patch, cumulative against baseline `23d05d6a2412`. SHA-256
  `cb1d1eca...bc1ed1`.
- `our-delta-on-mk_a05fd935.patch`: only the change on top of the parent (`cache.cairo`, `sampling.cairo`, `zread.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

#### Contribution 28: slim version for the new class budget on @rukafe0x's `mk_3ae3d577` (job `mk_96568c3fa3b644fcb6410fe5ccd67b19`)

> **After the 11 Nov 2026 reset** (class budget 75%: CASM ≤ 61,440 felts, Sierra ≤ 3,067,084 bytes). My contribution 27 (class 97.6%)
> no longer counts as a record, and a plain slim of it could not beat the new record.
>
> **Credit.** The parent record `mk_3ae3d577` is **@rukafe0x's**: the first ML-DSA-87 record under the budget, made from his `mk_f7634154`
> (z split by direct u128 halves, packed `ntt_z` pairs) by calling the Keccak rounds (`r1`, `rb1`), NTT blocks and the z reader `g5` out
> of line. It builds on **@binharold**'s `mk_3c0224a5` line. **What is mine** is the delta below.

##### What I did
1. `cache.cairo` (setup only, not scored): my `PT` window table, `take4` and `col_into` (contributions 25 and 26). Frees 11 KB of Sierra.
2. `sampling.cairo`: the cold SampleInBall fallback (contribution 22). -700 gas.
3. `zread.cairo`: `g5` back to `inline(always)`. -107,000 gas, but +90 KB of Sierra.
4. `nttu.cairo`: the class file also holds the Sierra debug names, and a tuple type spells out every element, so one 512-element box pop
   in `intt_row` cost 7 names of 16 KB each. Splitting the `intt_row` pops into 2×256 and the `ntt_z` pop into 4×32 (the span is restored
   on a short input, as before) frees about 115 KB of Sierra for about +19,000 gas.

Local score (`bench_validate - bench_baseline`): -88,903, the same on all 170 valid signatures, and exactly the official result.
Correctness: 177 signature cases (169 signatures and rejection vectors; the 3 Narrow-z vectors are rejected with 0, without a panic, as on
the parent), 8 account tests, 115 bench tests and 19 SampleInBall tests pass.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_3ae3d577` (by @rukafe0x, record at the time) | 87,007,028 |
| **This job (accepted, record at the time, since passed by my own `mk_b2e61741`)** | **86,918,125** |
| Saved vs parent | 88,903 |

Below Starknet's 100M validation gas cap. The evaluator reports CASM 57,168 of 61,440 felts and a class of 3,022,804 of 3,067,084 bytes
(73.9%). Lead: `rgr1_5317ab5afedf273517f47ff95e906d26e1d67f994b167ec70687fa2b81ef412b`.

##### Files
- `mldsa-87-mk_96568c3f.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `23d05d6a2412`. SHA-256
  `8cedc0a7...0c21d0`.
- `our-delta-on-mk_3ae3d577.patch`: only the change on top of the parent (`cache.cairo`, `nttu.cairo`, `sampling.cairo`, `zread.cairo`);
  apply with `git apply -p0`. Paths are relative to the repository root.

#### Contribution 30: Keccak rounds two per out-of-line call on my `mk_96568c3f` (job `mk_b2e61741e4c148eb9695111576f1bd41`)

> **Credit.** As contribution 28 (**@rukafe0x**'s `mk_3ae3d577` line and **@binharold**'s `mk_3c0224a5` line). The round grouping is the
> idea of my ML-DSA-44 contribution 29, adapted here.

##### What I did
1. `fk.cairo`: `ra7` ran its seven rounds as seven calls to the out-of-line `r1`. A new `inline(never)` `r2(e, ca, cb)` runs two rounds
   inline, and `ra7` becomes `r2, r2, r2, r1`: 14 round calls per permutation become 8 (-167,400 gas, CASM +2.2k, Sierra +78 KB).
   Four rounds per call (as in ML-DSA-44) or the same for `rb1` does not fit: one ML-DSA-87 round copy is about 2.2k CASM felts.
2. `nttu.cairo`, `rowp.cairo`: the Sierra is paid by splitting box pops further (`intt_row` 4×128, `ntt_z` 8×16, the two 272-felt pops in
   `rowp` 2×136), +32,900 gas.

Local score: -134,500, the same on all 170 valid signatures, and exactly the official result. Correctness: 177 signature cases, 8 account
tests, 115 bench tests and 19 SampleInBall tests pass.

##### Official result

| | Gas |
|---|---:|
| Parent `mk_96568c3f` (mine, contribution 28) | 86,918,125 |
| **This job (accepted, record as of 11 Nov 2026)** | **86,783,625** |
| Saved vs parent | 134,500 |

Below Starknet's 100M validation gas cap. The evaluator reports CASM 59,603 of 61,440 felts and a class of 3,057,871 of 3,067,084 bytes
(74.8%). Lead: `rgr1_d780c21a7b84c6cde7cfcaad395064514ca9a7ab91a5afc04037ad76669b9e0c`.

##### Files
- `mldsa-87-mk_b2e61741.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `23d05d6a2412`. SHA-256
  `5a613056...8c93ce`.
- `our-delta-on-mk_96568c3f.patch`: only the change on top of the parent (`fk.cairo`, `nttu.cairo`, `rowp.cairo`); apply with
  `git apply -p0`. Paths are relative to the repository root.

### Bahasa Indonesia (sederhana)

#### Kontribusi 8: UseHint dengan kali-lalu-geser untuk ML-DSA-87 (job `mk_3691ffe9c59140c3a9a6ac1c1ea3272a`)

##### Ide
Ini teknik yang sama dengan kontribusi 4, dibuat ulang untuk parameter ML-DSA-87 (`gamma2 = (q-1)/32`, jadi
ada 16 nilai HighBits, bukan 44). UseHint butuh HighBits dari setiap residu. Alih-alih membagi, HighBits dihitung
dengan `HighBits(r) = (((r + gamma2) mod q) * 1049601) >> 39`. Dua koefisien, `i` dan `i+16`, dimasukkan ke satu
`u128`, jadi satu AND mengurus sepasang. Bias `gamma2` tidak ditambahkan per koefisien, tetapi dimasukkan ke
konstanta `OFF` di INTT.

Bukti kebenaran: rumus diuji di Python untuk **semua r dari 0 sampai q-1**, bersama aturan hint terhadap
FIPS 204, ditambah **200 ribu blok acak**.

##### Hasil resmi
- Parent `mk_610ffcb9` (oleh @nadai2010): 112.803.840 gas.
- **Job ini (diterima, rekor pada waktunya): 110.867.290 gas**, hemat 1.936.550 gas.
- Masih di atas batas 100 juta gas.

##### Berkas
- `mldsa-87-mk_3691ffe9.patch`: patch resmi yang diterima, kumulatif terhadap baseline `23d05d6a2412`.
- `our-delta-on-mk_610ffcb9.patch`: hanya perubahan saya di atas parent (`nttu.cairo`, `packing.cairo`,
  `verify.cairo`). Terbukti: patch parent (diunduh dengan `pvfast remote mldsa87 patch`) + delta ini sama persis
  isinya (`diff -r`) dengan baseline + patch resmi job `mk_3691ffe9`. Delta dapat diterapkan dengan bersih.
  Patch yang dulu saya kirim menghasilkan isi yang sama dengan patch resmi.

#### Kontribusi 9: mu dan blok pertama SampleInBall dalam satu permutasi dua-state (job `mk_469c1cb9a18e4f3793a7e2e0c7a3d172`)

> **Teknik dua-state bukan ciptaan saya.** Teknik ini berasal dari **@rukafe0x**, yang memperkenalkannya di
> jalur ML-DSA-44 lewat `mj_366ff85e` ("92 Keccak-f menjadi 46 permutasi dua-state", dua sponge dalam satu
> `u128`, termasuk "mu dengan SampleInBall"). Rekor ML-DSA-44 berikutnya mengembangkannya lagi (misalnya
> `mj_97f98218` milik @saniksin dan versi lane-komplemen saya, kontribusi 2). **Yang merupakan kerja saya
> adalah penerapannya ke ML-DSA-87**, yang rekornya belum punya Keccak dua-state.

##### Yang saya kerjakan
Di ML-DSA-87, dua panggilan Keccak untuk `mu` dan untuk blok pertama SampleInBall saling bebas, jadi
dijalankan dalam **satu permutasi dua-state**: `mu` di 64 bit bawah tiap kata lane, SampleInBall di 64 bit atas.
Saya mengambil permutasi dua-state biasa dari kode ML-DSA-44 (`k2.cairo`, dipangkas jadi permutasinya saja).
24 ronde dibuat sebagai **loop 6 iterasi x 4 ronde**, karena unroll 12 ronde membuat kontrak hasil kompilasi
terlalu besar untuk batas CASM (95.163 felt, batasnya 81.920); loop hanya menambah sekitar 27 ribu gas. Kata lane
dikemas dengan aritmetika felt dan dibongkar dalam loop agar ukurannya kecil.

Bukti kebenaran: **400 input acak** dibandingkan dengan permutasi biasa, untuk `mu` dan untuk **semua 25 lane**
state kedua, serta semua tes bawaan paket.

##### Hasil resmi
- Parent `mk_3691ffe9` (kontribusi 8 saya): 110.867.290 gas.
- **Job ini (diterima, rekor ML-DSA-87 saat dikirim): 109.484.394 gas**, hemat 1.382.896 gas.
- Masih di atas batas 100 juta gas (kurang sekitar 9,5 juta gas).

##### Berkas
- `mldsa-87-mk_469c1cb9.patch`: patch resmi yang diterima, kumulatif terhadap baseline `23d05d6a2412`.
- `our-delta-on-mk_3691ffe9.patch`: hanya perubahan saya di atas parent (`k2.cairo` baru, serta `keccak.cairo`,
  `lib.cairo`, `sampling.cairo`, `verify.cairo`). Terbukti: patch parent (diunduh dengan
  `pvfast remote mldsa87 patch`) + delta ini sama persis isinya (`diff -r`) dengan baseline + patch resmi job
  `mk_469c1cb9`. Delta dapat diterapkan dengan bersih. Patch yang dulu saya kirim menghasilkan isi yang sama
  dengan patch resmi.

#### Kontribusi 11: SampleInBall 8 byte per lane, fallback sebagai lane walk (job `mk_a5460736f4cc428f9ca70cc5451da1eb`)

> **Kredit.** Unroll SampleInBall 8 byte per lane adalah ide **@cheelax** (job `mk_d8f3f635`); sendirian ide itu
> tidak muat di batas CASM pada rekor `mk_96cbecf3` (juga @cheelax, di atas SampleInBall lane milik
> **@rukafe0x**, `mk_cc04a71b`). **Yang saya kerjakan** adalah membuatnya muat: fallback byte-stream yang terpisah
> diganti dengan lanjutan lane walk yang sama di atas lane state hasil permutasi ulang. Ini **bukan rekor**: job lain
> lebih dulu di antrean.

##### Yang saya kerjakan
`ball_lanes` membaca 8 byte tiap lane tanpa loop dalam (satu langkah inline per byte, dengan pembacaan byte dan
tanda yang terbatas dari parent tetap dipertahankan). Fallback lama (`ball_stream` + `next_byte`, sekitar 3,1 ribu
CASM) dibuang; kalau blok pertama tidak cukup, jalan lane dilanjutkan ke 17 lane dari `keccak_f1600(state)`. Itu
membebaskan CASM yang dibutuhkan unroll. Hanya `sampling.cairo` yang berbeda dari parent.

Bukti kebenaran: **2.200 vektor SampleInBall** dibandingkan dengan referensi Python FIPS 204 (1.500 hash, 300
fallback, 150 tepi, 200 padat-tabrakan, 50 ekstrem), dijalankan pada kode baru dan pada rekor; 4 varian yang
sengaja dirusak tertangkap; 8 tes akun dan 115 tes bench lulus.

##### Hasil resmi
- Parent `mk_96cbecf3` (oleh @cheelax, rekor pada waktunya): 100.045.402 gas.
- **Job ini (diterima): 99.827.006 gas**, hemat 218.396 gas.
- Kasus terburuk 99.940.059, jadi job ini muat di batas 100 juta gas validasi Starknet. CASM 81.357 dari 81.920 felt.

##### Berkas
- `mldsa-87-mk_a5460736.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256-nya
  (`871eceec...3dc01`) sama dengan `patch_sha256` yang dilaporkan penilai untuk job ini.
- `our-delta-on-mk_96cbecf3.patch`: hanya perubahan saya di atas parent (`sampling.cairo`). Terbukti: patch parent
  (diunduh dengan `pvfast remote mldsa87 patch`) + delta ini sama persis isinya (`diff -r`) dengan baseline + patch
  yang dikirim. Delta dapat diterapkan dengan bersih.

##### Job lama, apa adanya
Job `mk_365efc2199124cd1abeea2340789635c` (ide SampleInBall yang sama digabung di `mk_779abbe3`) selesai dengan
status **REJECTED** (`CHECK_FAILED`): cek `no_corpus000`-`002` dan `no_zero_t1_c_tilde_32/40/48/56/63` gagal. Job itu
bukan salah satu kontribusi saya dan patch-nya tidak dipublikasikan di sini.

#### Kontribusi 14: lane terbatas untuk `tr`, lane bertipe `u64`, pemindaian SampleInBall di-inline (job `mk_00f892fd18bc486f8a63a924c82983b4`)

> **Kredit.** Teknik lane terbatas adalah milik **@odinfree** (`lanes8`, job `mk_bc0b5b94`). Rekor yang menjadi dasar,
> `mk_3400423b`, milik **@mitchuski**. **Bagian saya** adalah membawa struktur yang sama ke `lanes8t`, fungsi yang
> membangun ulang `tr` dari cache di setiap validate, ditambah langkah lanjutan di bawah.

##### Yang saya kerjakan
1. `keccak::lanes8t` memakai enam DivRem `u128` plus add/mul `u128`. Sekarang memakai pemecahan terbatas yang sama
   dengan `lanes8` (`bounded_int_div_rem` oleh 2^64 dan 32, lane 3 dan 5 lewat `cb::add`/`cb::mul`, lane 7 lewat downcast):
   -10.220 gas.
2. `lanes8` dan `lanes8t` mengembalikan lane terbatas `u64`, sehingga `mu_and_ball_rate` mengemas `tr|c_tilde` dengan
   `fk::aa` dan pemeriksaan akhir `c_tilde` membandingkan pasangan `fk::aa`. 11 `try_into` felt hilang: -3.500 gas.
3. `sampling::ball_scan` dan `ball_done` dibuat `inline(always)`: -3.900 gas.

Total lokal: -17.620 gas (`bench_validate`). Catatan perilaku: lane 7 dari `tr` kini di-downcast ke di bawah 2^64, bukan
`try_into` `u128`; untuk semua cache hasil setup nilainya selalu muat, dan cache rusak tetap mengembalikan `false`.

Pengujian: 8 tes akun dan 115 tes bench lulus; **2.200 vektor SampleInBall** terhadap referensi Python FIPS 204 lulus;
mutan dengan lane 6 dan 7 ditukar tertangkap oleh 2 tes akun.

##### Hasil resmi
- Parent `mk_3400423b` (oleh @mitchuski, rekor pada waktunya): 88.055.082 gas.
- **Job ini (diterima, rekor pada waktunya; sudah dilewati `mk_5276df6b` milik @binharold, 87.546.333): 88.037.462 gas**, hemat 17.620 gas.
- Masih di bawah batas gas validasi Starknet 100M. CASM di build dev saya 81.288 dari 81.920 felt.

##### Berkas
- `mldsa-87-mk_00f892fd.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `de6ded47...8518d`.
- `our-delta-on-mk_3400423b.patch`: hanya perubahan saya di atas parent (`keccak.cairo`, `sampling.cairo`,
  `verify.cairo`, `zread.cairo`); terapkan dengan `git apply -p0`.

#### Kontribusi 16: lane rate 10-16 SampleInBall dipecah saat dibutuhkan (job `mk_a7b5d29dd6fa45bfb3f5c1a3233fd066`)

> **Kredit.** Rekor yang menjadi dasar, `mk_618454a1`, milik **@odinfree**. **Bagian saya** adalah memecah lane rate hanya
> saat dibutuhkan dan membuang konstanta ronde yang tidak terpakai.

##### Yang saya kerjakan
1. `mu_and_ball_rate` dulu memecah semua 17 lane rate, padahal sekitar 90% tanda tangan selesai di SampleInBall dalam lane
   0-9. Lane 10-16 sekarang tetap terkemas dan `ball_lanes` memecahnya saat batch pertama habis.
2. `ROUND_CONSTANTS` di `fk` dipotong menjadi 16 entri yang masih dibaca, karena ronde 15-22 sudah dibakar ke fungsi ronde
   gabungan: 0 gas, CASM -8.

Diukur pada 169 tanda tangan asli: -7.270 gas bila batch pertama cukup, -200 gas bila batch kedua dibutuhkan (27 dari 27
tanda tangan seperti itu); perkiraan rata-rata -6.574. Pengujian: 8 tes akun dan 115 tes bench lulus; 19 tes SampleInBall
(2.200 vektor termasuk cadangan) lulus; tiga mutan tertangkap. Jalur batch ketiga (`ball_more`) hanya tercapai oleh state
SampleInBall buatan.

##### Hasil resmi
- Parent `mk_618454a1` (oleh @odinfree, rekor pada waktunya): 87.520.231 gas.
- **Job ini (diterima, rekor pada waktunya, dikalahkan job saya sendiri `mk_29251ad0` pada 1 Nov 2026): 87.513.845 gas**, hemat 6.386 gas.
- Masih di bawah batas gas validasi Starknet 100M. CASM di build dev saya 81.694 dari 81.920 felt.

##### Berkas
- `mldsa-87-mk_a7b5d29d.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `1413e3cb...c0c2c`.
- `our-delta-on-mk_618454a1.patch`: hanya perubahan saya di atas parent (`fk.cairo`, `keccak.cairo`, `sampling.cairo`,
  `verify.cairo`); terapkan dengan `git apply -p0`.

#### Kontribusi 18: tabel QUAD SampleInBall milik @rukafe0x, dipangkas jadi 241 entri (job `mk_29251ad0c80646bdb8b857cefa1b9b7d`)

> **Kredit.** Tabelnya milik **@rukafe0x**, dari `mk_9129f98a` (lead `rgr1_b505b848...`). **@odinfree** membuat lookup nibble
> bertanda yang menjadi asal tabel ini, dan **@odinfree** serta **@nadai2010** membuat hoist Keccak, span hint, dan kerja setup
> yang dibawa lead @rukafe0x dan sudah ada di jalur rekor ini. **Bagian saya** adalah memindahkan tabel itu ke atas
> `mk_a7b5d29d` dan memangkasnya menjadi 241 entri.

##### Yang saya kerjakan
1. `bits()` dulu memakai dua tabel per pasangan nibble (`NIBC`, lalu `TRIT`). `QUAD[pb + 16 nb]` memberi empat koefisien sekali
   lookup, sehingga satu lookup hilang untuk masing-masing dari 64 pasangan nibble. Span dibangun sekali di `ball_done`.
2. Tabel @rukafe0x berisi 256 entri. `p` dan `n` tidak beririsan, jadi pasangan dengan `nb = 15` punya `pb = 0` dan indeks tidak
   melebihi 240: 241 entri sudah cukup.

Hanya bagian ini dari lead @rukafe0x yang dipakai. Butterfly z-nya tidak ikut: di rekor ini hematnya 1.600 gas per situs dengan
biaya sekitar 142 felt CASM, dan hanya satu situs yang muat. `sig_decode` inline-nya juga tidak dipindahkan.

Diukur pada 169 tanda tangan asli: -50.780 gas di semuanya, termasuk yang butuh batch kedua. Pengujian: 8 tes akun dan 115 tes
bench lulus; 19 tes SampleInBall (2.200 vektor termasuk cadangan) lulus; satu mutan entri tabel salah tertangkap. Rejection
termahal yang bisa saya buat (`c_tilde` hasil grinding dengan 75 hint) berbiaya 1,0016x tanda tangan valid terburuk (batas
1,25x); itu kasus terburuk yang saya buat, bukan maksimum yang terbukti.

##### Hasil resmi
- Parent `mk_a7b5d29d` (milik saya, rekor pada waktunya): 87.513.845 gas.
- **Job ini (diterima, rekor pada waktunya, dikalahkan `mk_3c0224a5` milik @binharold, rekor direbut kembali oleh `mk_14ba0499` milik saya): 87.463.065 gas**, hemat 50.780 gas.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 81.761 dari 81.920 felt dan class 3.928.741 byte.
- Lead: `rgr1_ed00e7024d7316916da75f3b2cf301570dbd6e77ef40783dfcaf4584345506e2`.

##### Berkas
- `mldsa-87-mk_29251ad0.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `6969a9fc...dab29`.
- `our-delta-on-mk_a7b5d29d.patch`: hanya perubahan di atas parent (`sampling.cairo`); terapkan dengan `git apply -p0`.

#### Kontribusi 21: satu box pop per baris dan per z, batching `zf4a5` (job `mk_14ba049949954bf4acac786dd79807b5`)

> **Kredit.** Rekor induk `mk_3c0224a5` dan batching blok z NTT `zf4a3` milik **@binharold** (lead `rgr1_6e195551...`). Pembacaan box
> yang lazy mengikuti badan grup pointer box milik **@nadai2010** (lead `rgr1_70e549c6...`). Butterfly z milik **@rukafe0x**
> (lead `rgr1_b505b848...`) yang pertama mengurangi panggilan `zf4a` di `ntt_z`. **Bagian saya** adalah menemukan pop dan slice yang tidak
> perlu di jalur baris dan z, menggantinya dengan satu box pop, dan memperluas batching dari tiga blok ke lima dengan CASM yang terbebas.

##### Yang saya kerjakan
Angka gas adalah perubahan skor, sesuai urutan langkah dibangun.

1. `verify_decoded` membayar `slice(256*j,256)` plus satu pop untuk tiap z NTT. Sekarang `ntt_z` menerima satu `@Box<[ZC87;256]>` dan z
   ditelusuri dengan pop, tanpa penghitung `j`: -14.410 gas dan CASM berkurang 183 felt.
2. `intt_row` dulu melakukan delapan pop box 64 sel per baris. Sekarang ia membaca satu box 512 sel yang di-pop sekali di dalam `vrow`, dan
   baris ganjil dari satu pasangan membuang satu elemen dengan `pop_front`, bukan `slice(1,512)`: -30.480 gas. Pembacaan box bersifat lazy,
   jadi satu pola di awal tidak lebih mahal dari delapan. Pop diletakkan di dalam `vrow` karena nama debug Sierra ikut dihitung dalam ukuran
   class: menyimpan box melintasi panggilan membuat class lebih 39.864 byte dari batas.
3. `zf4a3` milik @binharold menjadi `zf4a5`, tiga panggilan per `ntt_z`, bukan lima: -3.200 gas dengan biaya 284 felt CASM.

Diukur pada 169 tanda tangan asli: raw validate -59.290 gas di semuanya. `ntt_z` juga menurunkan baseline 11.200 gas, jadi skor turun
48.090. Pengujian: 8 tes akun dan 115 tes bench lulus; 19 tes SampleInBall (2.200 vektor) lulus; 4 vektor penolakan tetap ditolak; dua
mutan (offset baris, urutan input `intt_row`) tertangkap. Rejection termahal yang saya buat berbiaya 1,0016x tanda tangan valid terburuk
(batas 1,25x); itu kasus terburuk yang saya buat, bukan maksimum yang terbukti.

##### Hasil resmi
- Parent `mk_3c0224a5` (@binharold, rekor pada waktunya): 87.447.565 gas.
- **Job ini (diterima, rekor pada waktunya; dikalahkan rantai @rukafe0x yang berakhir di `mk_7c976a34`, rekor direbut kembali oleh `mk_4ff5f9db` milik saya): 87.399.475 gas**, hemat 48.090 gas.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 81.603 dari 81.920 felt dan class 4.051.090 byte.
- Lead: `rgr1_6fc597643e64ec59293e1ef78f7b2c1d0c49d076cf4f6bfc48e577aece341c10`.

##### Berkas
- `mldsa-87-mk_14ba0499.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `0b1a3ea8...81e54`.
- `our-delta-on-mk_3c0224a5.patch`: hanya perubahan di atas parent (`cache.cairo`, `nttu.cairo`, `verify.cairo`); terapkan dengan
  `git apply -p0`.

#### Kontribusi 22: felt z dipecah hanya lewat lengan Wide, cadangan SampleInBall dipisah (job `mk_4ff5f9db085d4a2bbff6a624902c84bb`)

> **Kredit.** Hampir seluruh rekor ini milik **@rukafe0x**. Rekor induk `mk_7c976a34` miliknya (lead `rgr1_c4750f63...`). Bit penanda dan
> pemecahan Wide-only untuk felt cache berasal dari `mk_0ed9df51` miliknya (lead `rgr1_a8b48c6c...`). Cold arm, yaitu cabang langka yang
> dipindah ke fungsi terpisah dengan penarikan gas sendiri, berasal dari rekor ML-DSA-44 miliknya `mj_e898606c` (lead `rgr1_c805af03...`;
> server tidak menerima lead ML-DSA-44 sebagai induk lead ML-DSA-87, jadi kredit itu ada di ringkasan lead dan judul job). **Bagian saya**
> adalah melihat bahwa pemecahan Wide-only yang sama berlaku untuk felt z tanda tangan, membuktikan kenapa itu tepat, dan memindahkan cold arm.

##### Yang saya kerjakan
1. `g5` dan `zstep` memecah tiap felt z tanda tangan menjadi dua setengah u128 lewat `u256`. Konversi itu punya lengan Narrow (nilai di
   bawah 2^128) dan lengan Wide, dan kedua lengan menyatu lagi, yang memakan gas di setiap felt. Helper baru `wz` hanya menyimpan lengan
   Wide dan panic pada Narrow, seperti pemecahan felt cache bertanda milik @rukafe0x. Dipakai untuk 145 felt z (`f0..f3` di `g5`,
   `f4`/`f9` di `zstep`, felt z terakhir `g4` dan felt 2): -41.500 gas.
2. Cadangan SampleInBall (setelah 17 lane blok pertama) dipindah ke fungsi `inline(never)` `cold_ball` yang memanggil
   `core::gas::withdraw_gas()`, jadi jalur biasa tidak ikut dibebani: -700 gas.

**Kenapa panic tidak pernah kena tanda tangan valid.** FIPS 204 mengemas tiap koefisien z sebagai `gamma1 - z` dalam 20 bit, dan z yang
valid memenuhi `|z| < gamma1 - beta` (beta = 120), jadi setiap field tanda tangan valid minimal 121, tidak pernah 0. Felt tanda tangan
adalah potongan 31 byte little-endian. Di setiap felt yang didekode, setengah-atas (bit 128..247) hanya berisi bit z, minimal lima field
utuh, jadi tidak nol. Di felt z terakhir, bit 128..143 adalah bit 4..19 dari field terakhir, minimal 121 >> 4 = 7. Jadi felt di bawah 2^128
di posisi ini berarti tanda tangan tidak valid. Rekor mengembalikan `false` belakangan untuk kasus itu; job ini panic, jadi validasi tetap
gagal. Felt `c_tilde`, `tr` dan hint tetap memakai `u256`, karena bisa nol untuk input valid.

Diukur pada 169 tanda tangan asli: raw validate -42.200 gas di semuanya; baseline tidak berubah. Pengujian: 8 tes akun dan 115 tes bench
lulus; 19 tes SampleInBall (2.200 vektor) lulus; 4 vektor penolakan lama tetap ditolak; 3 vektor penolakan baru (tanda tangan valid dengan
setengah-atas satu felt z dijadikan nol, di felt 10, felt 2 dan felt z terakhir) ditolak oleh rekor (mengembalikan 0) maupun job ini
(panic); mutan dengan setengah-setengah ditukar di `wz` tertangkap.

Yang tidak muat: memproses dua grup baris per panggilan (satu pop untuk keduanya) hemat 186.690 gas, tetapi menambah sekitar 404 KB Sierra
dan 2,5 ribu felt CASM, melewati kedua batas.

##### Hasil resmi
- Parent `mk_7c976a34` (@rukafe0x, rekor pada waktunya): 87.013.066 gas.
- **Job ini (diterima, rekor pada waktunya; kemudian dilewati `mk_790f1c30` saya sendiri): 86.970.866 gas**, hemat 42.200 gas.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 80.027 dari 81.920 felt dan class 4.075.777 byte.
- Lead: `rgr1_a6317ec382d235a6b9c80317cb966ab38ce38cb156d2f3c28f7e8c392b6a4b61`.

##### Berkas
- `mldsa-87-mk_4ff5f9db.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `4ba00a65...826c3`.
- `our-delta-on-mk_7c976a34.patch`: hanya perubahan di atas parent (`sampling.cairo`, `zread.cairo`); terapkan dengan
  `git apply -p0`.

#### Kontribusi 25: 18 grup baris per panggilan milik @rukafe0x, Sierra-nya dibayar dari kode setup (job `mk_790f1c3001844e5cb4ee195485e582d1`)

> **Kredit.** Kedua teknik gas milik **@rukafe0x**, dari job `mk_1b5b9dea` miliknya yang diterima (lead `rgr1_0a891997...`). Ia membangunnya
> di jalur `mk_7c976a34` miliknya sendiri, bukan di atas rekor saya. **Bagian saya** adalah memindahkannya ke rekor saya `mk_4ff5f9db`,
> dan merapikan kode setup supaya muat dalam batas ukuran class.

##### Yang saya kerjakan
1. `rowp::row_groups` memproses 18 grup kolom per panggilan, bukan 13, jadi 51 grup selesai dalam tiga panggilan, bukan empat; cek
   panjang ada di grup ke-16, tempat panggilan ketiga sampai ke blok penutup. Persis `rowp.cairo` milik @rukafe0x.
2. `sampling::ball_done` dijadikan `inline(never)` (@rukafe0x): sekitar -20,4 KB Sierra dan -411 felt CASM.
3. Port langsung poin 1 dan 2 ke `mk_4ff5f9db` kelebihan 10.323 byte dari batas class Sierra: tiap situs panggilan tambahan di
   `row_groups` memakan sekitar 8,9 KB, kebanyakan berupa statement `drop` di panic arm dari sepuluh `unwrap`-nya. Untuk membayarnya saya
   merapikan kode yang hanya jalan di `fill_cache` (setup akun, tidak dihitung skor):
   - `cache::part` membaca jendela tiap part (paruh, grup pertama, koefisien per kolom, offset dan panjang jendela, tail, diawali `tr`)
     dari tabel konstan `PT` yang dihitung dari `BOUNDS`, bukan dari aritmetika u32 yang cek overflow-nya butuh panic arm.
   - Keempat kolom disusun berselang-seling dengan helper `take4` dan `head` yang tidak bisa panic, bukan `unwrap` dan indeks.
   - `col_into` memotong tiap baris tepat `count` koefisien dan mengulang selama kolom 0 masih punya satu grup utuh berisi lima, jadi
     penghitung loop dan `last` hilang. Grup yang ditulis tetap sama: `count` adalah 5 * (last + 1), atau 256 = 5 * 51 + 1 untuk part tail.
   Totalnya: -10,4 KB Sierra, -556 felt CASM, dan gas setup -382.530 per akun. Isi cache tidak berubah.

Diukur pada 169 tanda tangan asli: validate rata-rata -3.640 gas (dari -3.790 sampai -3.610); skor lokal -3.610. Pengujian: 8 tes akun
dan 115 tes bench lulus; 19 tes SampleInBall (2.200 vektor) lulus; semua 169 tanda tangan berpasangan tervalidasi, dan 7 vektor penolakan
tetap ditolak; mutan dengan satu offset jendela di `PT` diubah tertangkap (tes tanda tangan gagal).

##### Hasil resmi
- Parent `mk_4ff5f9db` (milik saya, rekor pada waktunya): 86.970.866 gas.
- **Job ini (diterima, rekor pada waktunya; kemudian dilewati jalur `mk_711ea4cc` milik @rukafe0x, lalu diambil kembali oleh `mk_0e77da11` saya): 86.967.233 gas**, hemat 3.633 gas.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 80.650 dari 81.920 felt dan class 4.088.242 byte (1.204 byte
  di bawah batas).
- Lead: `rgr1_5e6a80537952ff340ae69e2b92a01333c3657fffff11daf18396b283b01df00a`.

##### Berkas
- `mldsa-87-mk_790f1c30.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `0a9b7ce8...16fa4d`.
- `our-delta-on-mk_4ff5f9db.patch`: hanya perubahan di atas parent (`cache.cairo`, `rowp.cairo`, `sampling.cairo`); terapkan dengan
  `git apply -p0`.

#### Kontribusi 26: teknik saya yang belum ada dipasang di atas `mk_711ea4cc` milik @rukafe0x (job `mk_0e77da11fb4349aaaf5fd89f3f40adae`)

> **Kredit.** Rekor induk `mk_711ea4cc` milik **@rukafe0x** (lead `rgr1_969d40bc...`): tujuh jendela cache dengan satu jendela melintasi
> kedua paruh, di atas `mk_295151d9` dan `mk_04b420bb` miliknya (constrain SampleInBall dipecah di 128, tes tolak hanya di paruh atas,
> jalur Bitwise seimbang), di atas `mk_1b5b9dea` miliknya, semuanya di jalur `mk_3c0224a5` milik **@binharold**. Jalurnya bercabang dari
> `mk_1b5b9dea` sebelum `mk_4ff5f9db` dan `mk_790f1c30` saya, jadi teknik keduanya belum ada di sana. Ide split Wide-only miliknya
> (`mk_0ed9df51`), begitu juga teknik cold arm (ML-DSA-44 `mj_e898606c`). **Bagian saya** adalah memasang kembali teknik itu di rekornya
> dan membuatnya muat.

##### Yang saya kerjakan
1. `zread.cairo` memakai versi `mk_790f1c30` saya apa adanya (kontribusi 22): felt z dipecah hanya lewat lengan Wide, dan felt Narrow
   memicu panic. Field z yang valid memberi gamma1 - z >= 121, jadi tidak ada tanda tangan valid dengan paruh atas nol di sana. -41.500 gas.
2. `sampling`: cadangan SampleInBall setelah blok pertama `c_tilde` dipindah ke `cold_ball` yang `inline(never)` dengan `withdraw_gas`
   sendiri, jadi jalur biasa tidak ikut membayarnya (kontribusi 22). -700 gas.
3. Poin 1 dan 2 saja kelebihan 3.145 byte dari batas class Sierra. Saya membayarnya dari kode yang hanya jalan di `fill_cache` (setup
   akun, tidak dihitung skor), dengan menurunkan ulang perapian kontribusi 25 untuk tujuh jendelanya: `window()` membaca (paruh, grup
   pertama, count, offset, panjang, tail, diawali `tr`) dari tabel konstan `PT` berisi 8 potongan jendela (part 3 melintasi kedua paruh,
   jadi menjadi potongan 3 dan 4); kolom disusun berselang-seling dengan `take4`/`head` yang tidak bisa panic; `col_into` memotong baris
   tepat `count` dan mengulang lewat pop. Isi cache tidak berubah.

Skor lokal (`bench_validate - bench_baseline`): -42.200, persis sama dengan hasil resmi. Pengujian: 8 tes akun, 115 tes bench, dan 19 tes
SampleInBall lulus; semua 169 tanda tangan berpasangan tervalidasi, 4 vektor penolakan lama dan 3 vektor z Narrow ditolak (induknya gagal di
3 vektor itu, sesuai dugaan); mutan dengan satu offset `PT` diubah tertangkap.

##### Hasil resmi
- Rekor saya sebelumnya `mk_790f1c30` (kontribusi 25): 86.967.233 gas.
- Parent `mk_711ea4cc` (oleh @rukafe0x, rekor pada waktunya): 86.933.808 gas.
- **Job ini (diterima, rekor pada waktunya; kemudian dilewati `mk_a05fd935` milik @rukafe0x, lalu diambil kembali oleh `mk_195e9e3e` saya): 86.891.608 gas**, hemat 42.200 gas terhadap parent.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 80.457 dari 81.920 felt dan class 4.085.182 byte.
- Lead: `rgr1_8338e85c38fc36b3d3cbca8f5cf04dfd9875d795041608ae011afeb0686cf732`.

##### Berkas
- `mldsa-87-mk_0e77da11.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `b260db8e...a28fc`.
- `our-delta-on-mk_711ea4cc.patch`: hanya perubahan di atas parent (`cache.cairo`, `sampling.cairo`, `zread.cairo`); terapkan dengan
  `git apply -p0`.

#### Kontribusi 27: teknik yang sama dipasang di atas `mk_a05fd935` milik @rukafe0x (job `mk_195e9e3e62e744dd93957ebc53ab3a33`)

> **Kredit.** Rekor induk `mk_a05fd935` milik **@rukafe0x** (lead `rgr1_d2ddaffe...`): `grp1` di `rowp` mengembalikan `Option` dan
> mengambil 17 grupnya sekali, dan blok pertama / theta Keccak melewati kerja pada lane yang sudah pasti nol (-350K). Rekor itu dibangun di
> atas `mk_711ea4cc` miliknya (tujuh jendela cache, lead `rgr1_969d40bc...`), di jalur `mk_3c0224a5` milik **@binharold**, dan belum memuat
> kontribusi 26 saya. Ide split Wide-only miliknya (`mk_0ed9df51`). **Bagian saya** adalah delta itu sendiri (kontribusi 22, 25, dan 26).

##### Yang saya kerjakan
`mk_a05fd935` hanya mengubah `k2`, `keccak`, `rowp`, dan `verify` di atas `mk_711ea4cc`; `zread`, `sampling`, dan `cache` tidak disentuh.
Jadi delta kontribusi 26 bisa dipasang apa adanya (berkas `our-delta-on-mk_a05fd935.patch` identik byte-per-byte dengan
`our-delta-on-mk_711ea4cc.patch`):
1. `zread.cairo`: felt z dipecah hanya lewat lengan Wide; felt Narrow memicu panic (tidak ada tanda tangan valid dengan paruh atas nol). -41.500 gas.
2. `sampling`: cadangan SampleInBall dipindah ke `cold_ball` yang `inline(never)` dengan `withdraw_gas` sendiri. -700 gas.
3. Hanya setup (`fill_cache`, tidak dihitung skor): tabel jendela `PT`, `take4`/`head`, dan `col_into`. Induknya punya sisa ruang Sierra
   sekitar 112 KB, jadi langkah ini tidak lagi diperlukan untuk ukuran; saya pertahankan supaya deltanya tetap sama dengan yang sudah
   diterima di kontribusi 26.

Skor lokal (`bench_validate - bench_baseline`): -42.200, persis sama dengan hasil resmi. Pengujian: 8 tes akun, 115 tes bench, dan 19 tes
SampleInBall lulus; semua 169 tanda tangan berpasangan tervalidasi, 4 vektor penolakan lama dan 3 vektor z Narrow ditolak (induknya gagal di
3 vektor itu, sesuai dugaan).

##### Hasil resmi
- Rekor saya sebelumnya `mk_0e77da11` (kontribusi 26): 86.891.608 gas.
- Parent `mk_a05fd935` (oleh @rukafe0x, rekor pada waktunya): 86.584.015 gas.
- **Job ini (diterima, rekor pada waktunya, sampai reset 11 Nov 2026): 86.541.815 gas**, hemat 42.200 gas terhadap parent.
- Masih di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 76.670 dari 81.920 felt dan class 3.990.364 byte.
- Lead: `rgr1_cdc530f48fa6fa99b1f6316ea5740725e3335b0f2d5c5f3852075d6595eb9fba`.

##### Berkas
- `mldsa-87-mk_195e9e3e.patch`: patch yang dikirim, kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `cb1d1eca...bc1ed1`.
- `our-delta-on-mk_a05fd935.patch`: hanya perubahan di atas parent (`cache.cairo`, `sampling.cairo`, `zread.cairo`); terapkan dengan
  `git apply -p0`.

#### Kontribusi 28: versi ramping untuk batas class baru, di atas `mk_3ae3d577` milik @rukafe0x (job `mk_96568c3fa3b644fcb6410fe5ccd67b19`)

> **Sesudah reset 11 Nov 2026** (batas class 75%: CASM ≤ 61.440 felt, Sierra ≤ 3.067.084 byte). Kontribusi 27 saya (class 97,6%) tidak
> lagi dihitung sebagai rekor, dan sekadar merampingkannya tidak cukup untuk mengalahkan rekor baru.
>
> **Kredit.** Rekor induk `mk_3ae3d577` milik **@rukafe0x**: rekor ML-DSA-87 pertama dengan batas baru, dibuat dari `mk_f7634154` miliknya
> (z dipecah lewat paruh u128 langsung, pasangan `ntt_z` terkemas) dengan memanggil ronde Keccak (`r1`, `rb1`), blok NTT, dan pembaca z
> `g5` di luar baris. Rekor itu dibangun di jalur `mk_3c0224a5` milik **@binharold**. **Bagian saya** adalah delta di bawah ini.

##### Yang saya kerjakan
1. `cache.cairo` (hanya setup, tidak dihitung skor): tabel jendela `PT`, `take4`, dan `col_into` saya (kontribusi 25 dan 26). Membebaskan 11 KB Sierra.
2. `sampling.cairo`: cadangan SampleInBall dingin (kontribusi 22). -700 gas.
3. `zread.cairo`: `g5` kembali `inline(always)`. -107.000 gas, tetapi Sierra +90 KB.
4. `nttu.cairo`: berkas class juga memuat nama debug Sierra, dan tipe tuple menuliskan setiap elemennya, jadi satu pop box 512 elemen di
   `intt_row` memakan 7 nama masing-masing 16 KB. Pop `intt_row` dipecah menjadi 2×256 dan pop `ntt_z` menjadi 4×32 (span dikembalikan
   kalau input terlalu pendek, sama seperti sebelumnya): sekitar 115 KB Sierra bebas dengan biaya sekitar +19.000 gas.

Skor lokal (`bench_validate - bench_baseline`): -88.903, sama di semua 170 tanda tangan valid, dan persis sama dengan hasil resmi.
Pengujian: 177 kasus tanda tangan (169 tanda tangan dan vektor penolakan; 3 vektor z Narrow ditolak dengan 0 tanpa panic, sama seperti
induknya), 8 tes akun, 115 tes bench, dan 19 tes SampleInBall lulus.

##### Hasil resmi
- Parent `mk_3ae3d577` (oleh @rukafe0x, rekor pada waktunya): 87.007.028 gas.
- **Job ini (diterima, rekor pada waktunya, kemudian dilewati `mk_b2e61741` saya sendiri): 86.918.125 gas**, hemat 88.903 gas.
- Di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 57.168 dari 61.440 felt dan class 3.022.804 dari 3.067.084 byte (73,9%).
- Lead: `rgr1_5317ab5afedf273517f47ff95e906d26e1d67f994b167ec70687fa2b81ef412b`.

##### Berkas
- `mldsa-87-mk_96568c3f.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `8cedc0a7...0c21d0`.
- `our-delta-on-mk_3ae3d577.patch`: hanya perubahan di atas parent (`cache.cairo`, `nttu.cairo`, `sampling.cairo`, `zread.cairo`);
  terapkan dengan `git apply -p0`.

#### Kontribusi 30: ronde Keccak dua per panggilan di luar baris, di atas `mk_96568c3f` saya (job `mk_b2e61741e4c148eb9695111576f1bd41`)

> **Kredit.** Sama seperti kontribusi 28 (jalur `mk_3ae3d577` milik **@rukafe0x** dan jalur `mk_3c0224a5` milik **@binharold**).
> Pengelompokan ronde adalah ide kontribusi ML-DSA-44 saya nomor 29, disesuaikan di sini.

##### Yang saya kerjakan
1. `fk.cairo`: `ra7` menjalankan tujuh ronde sebagai tujuh panggilan ke `r1` di luar baris. Fungsi baru `inline(never)` `r2(e, ca, cb)`
   menjalankan dua ronde secara inline, dan `ra7` menjadi `r2, r2, r2, r1`: 14 panggilan ronde per permutasi menjadi 8 (-167.400 gas,
   CASM +2,2 ribu, Sierra +78 KB). Empat ronde per panggilan (seperti di ML-DSA-44) atau hal yang sama untuk `rb1` tidak muat: satu salinan
   ronde ML-DSA-87 sekitar 2,2 ribu felt CASM.
2. `nttu.cairo`, `rowp.cairo`: Sierra-nya dibayar dengan memecah pop box lebih jauh (`intt_row` 4×128, `ntt_z` 8×16, dua pop 272 felt di
   `rowp` menjadi 2×136), +32.900 gas.

Skor lokal: -134.500, sama di semua 170 tanda tangan valid, dan persis sama dengan hasil resmi. Pengujian: 177 kasus tanda tangan, 8 tes
akun, 115 tes bench, dan 19 tes SampleInBall lulus.

##### Hasil resmi
- Parent `mk_96568c3f` (milik saya, kontribusi 28): 86.918.125 gas.
- **Job ini (diterima, rekor per 11 Nov 2026): 86.783.625 gas**, hemat 134.500 gas.
- Di bawah batas gas validasi Starknet 100M. Evaluator mencatat CASM 59.603 dari 61.440 felt dan class 3.057.871 dari 3.067.084 byte (74,8%).
- Lead: `rgr1_d780c21a7b84c6cde7cfcaad395064514ca9a7ab91a5afc04037ad76669b9e0c`.

##### Berkas
- `mldsa-87-mk_b2e61741.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `23d05d6a2412`. SHA-256
  `5a613056...8c93ce`.
- `our-delta-on-mk_96568c3f.patch`: hanya perubahan di atas parent (`fk.cairo`, `nttu.cairo`, `rowp.cairo`); terapkan dengan
  `git apply -p0`.

### Pernyataan jujur
Ketiga belas patch ML-DSA-87 dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Falcon-512

One accepted contribution to the **Falcon-512** season on [falcon.provably.fast](https://falcon.provably.fast/falcon),
baseline `bece5c07eeea`. The official patch is cumulative against that baseline and contains the work of many contributors.

> **Disclosure / Pernyataan:** this patch was produced by an AI agent, **Claude Code** (model Opus), which I
> (**@ardianreffa**) ran and supervised. The job's model label on the board is `claude-opus-5-5`.
> Patch ini dikerjakan oleh agent AI **Claude Code** (model Opus) yang saya (**@ardianreffa**) jalankan dan awasi.
> Label model job di papan skor adalah `claude-opus-5-5`.

### English

#### Contribution 31: Keccak rounds two per out-of-line call on @rukafe0x's `fj_1520d5dc` (job `fj_3a35fbcab38447098695a10570d527ee`)

> **Credit.** The parent record `fj_1520d5dc` and the 70% account-budget fit it builds on (`fj_ec003097` ... `fj_ecd1564b`) are
> **@rukafe0x**'s; underneath is **@binharold**'s `fj_8ad7595e`. The round grouping is the idea of my ML-DSA-44 contribution 29 and
> ML-DSA-87 contribution 30, adapted here.

##### What I did
After the 11 Nov reset the Falcon-512 record has to fit 70% of the class limits (it is 1.96x cheaper than the baseline, just under the
2x needed for 75%). @rukafe0x's fit runs Keccak rounds 4-14 as 11 calls to the out-of-line `rQ` and rounds 16-22 as 7 calls to `rA`,
with rounds 1-3 still inline: 18 round calls per permutation.
1. `rQ(st, ra, rb, kk)` now runs two rounds inline, so rounds 1-14 are 7 calls. The inline copies of rounds 1-3 are dropped, which
   pays for the second round inside `rQ` and frees about 87 KB of Sierra.
2. That Sierra pays for a new `inline(never)` `rA2(st, ra, rb, kk)` with two A-rounds for rounds 16-21; round 22 stays on the
   one-round `rA`. (One body with an `if rb == 0` skip was tried and is +606k: the branch breaks the straight-line code.)
3. 11 round calls per permutation instead of 18: -21,000 gas per Keccak permutation.

Local score (account validate minus baseline): 26,874,899 -> 26,706,899, -168,000, and -168,000 on every SHAKE verify/reject case.
Correctness: 60 crate tests and 7 local account tests pass (valid signature accepted, wrong hash and tampered signature rejected).

##### Official result

| | Gas |
|---|---:|
| Parent `fj_1520d5dc` (by @rukafe0x, record at the time) | 24,638,451 |
| **This job (accepted, record as of 11 Nov 2026)** | **24,470,451** |
| Saved vs parent | 168,000 |

The same -168,000 at 8 blocks (23,525,804) and 9 blocks (25,119,896). The evaluator reports CASM 48,216 felts and a class of
2,851,701 bytes (69.7%, inside the 70% budget). Lead: `rgr1_60dee0d7a5bbcf7f8a05a0dc31034145cd58bec5aa3f8c66a0ac8c124f7f1f4a`.

##### Files
- `falcon-512-fj_3a35fbca.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `bece5c07eeea`. Its
  SHA-256 (`a392a2b6...f66f`) equals the `patch_sha256` the scorer reported for the job.
- `our-delta-on-fj_1520d5dc.patch`: only my change on top of the parent (`shake256.cairo`). Verified: the parent patch on the
  baseline plus this delta gives a tree identical (`diff -r`) to the baseline plus the submitted patch.

### Bahasa Indonesia (sederhana)

#### Kontribusi 31: ronde Keccak dua per panggilan di luar baris, di atas `fj_1520d5dc` milik @rukafe0x (job `fj_3a35fbcab38447098695a10570d527ee`)

> **Kredit.** Rekor dasar `fj_1520d5dc` dan penyesuaian ke batas akun 70% di bawahnya (`fj_ec003097` ... `fj_ecd1564b`) milik
> **@rukafe0x**; di bawahnya lagi `fj_8ad7595e` milik **@binharold**. Pengelompokan ronde berasal dari kontribusi ML-DSA-44 saya
> (29) dan ML-DSA-87 (30), disesuaikan di sini. Ini kontribusi Falcon-512 pertama saya.

##### Yang saya lakukan
Sejak reset 11 Nov, rekor Falcon-512 harus muat 70% batas class (1,96x lebih murah dari baseline, sedikit di bawah 2x untuk batas 75%).
Versi @rukafe0x menjalankan ronde Keccak 4-14 sebagai 11 panggilan ke `rQ` dan ronde 16-22 sebagai 7 panggilan ke `rA`, dengan ronde 1-3
masih inline: 18 panggilan per permutasi.
1. `rQ` sekarang menjalankan dua ronde, jadi ronde 1-14 cukup 7 panggilan. Salinan inline ronde 1-3 dibuang; itu yang membayar ronde
   kedua di `rQ` dan membebaskan sekitar 87 KB Sierra.
2. Sierra itu dipakai untuk `rA2` baru (dua ronde A) untuk ronde 16-21; ronde 22 tetap lewat `rA`. (Satu fungsi dengan cabang
   `if rb == 0` dicoba dan malah +606 ribu gas.)
3. 11 panggilan per permutasi, bukan 18: hemat 21.000 gas per permutasi Keccak.

Skor lokal (validate akun dikurangi baseline): 26.874.899 -> 26.706.899, hemat 168.000, sama di setiap kasus SHAKE. 60 tes crate dan
7 tes akun lokal lulus.

##### Hasil resmi
- Parent `fj_1520d5dc` (oleh @rukafe0x, rekor pada waktunya): 24.638.451 gas.
- **Job ini (diterima, rekor per 11 Nov 2026): 24.470.451 gas**, hemat 168.000 gas (sama pada 8 dan 9 blok).
- CASM 48.216 felt, class 2.851.701 byte (69,7%, di dalam batas 70%). Lead: `rgr1_60dee0d7...1f4a`.

##### Berkas
- `falcon-512-fj_3a35fbca.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `bece5c07eeea`;
  SHA-256 (`a392a2b6...f66f`) sama dengan `patch_sha256` dari penilai.
- `our-delta-on-fj_1520d5dc.patch`: hanya perubahan saya di atas parent (`shake256.cairo`). Patch parent + delta ini sama persis
  (`diff -r`) dengan baseline + patch yang dikirim.

---

## Falcon-1024

Two accepted contributions to the **Falcon-1024** (NIST level 5) season on
[falcon.provably.fast](https://falcon.provably.fast/falcon1024), baseline `bf7fd8785a18`. The official patches are
cumulative against that baseline and contain the work of many contributors.

> **Disclosure / Pernyataan:** these patches were produced by an AI agent, **Claude Code** (models Sonnet and Opus),
> which I (**@ardianreffa**) ran and supervised. The jobs' model label on the board is `claude-opus-5-5`; their titles
> do not name the agent.
> Patch ini dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya (**@ardianreffa**) jalankan
> dan awasi. Label model job di papan skor adalah `claude-opus-5-5`; judulnya tidak menyebut agent.

### English

#### Contribution 10: Keccak cell constants hoisted out of the squeeze loop (job `fk_40768326d05246c09567987a2660432f`)

##### The idea
On **@cheelax's** record `fk_7eee665f`, the squeeze loop called `fk::eo()` on every permutation to rebuild its
three cell constants (`2^64`, `2^128-1`, `2^64-1`). Now `eo()` is called **once** before absorb and the cells are
carried through the loop and passed to `keccak_next_k` and to absorb. The word reader's `2^64` divisor, which was a
separate `hcells` entry, is taken from the same `co.two64` cell, so the loop carries one value less.

Tests: the package's tests pass (109/109 in the workspace); locally -4,300 gas at 17 blocks and -4,000 at 16 blocks.

##### Official result

| | Gas |
|---|---:|
| Parent `fk_7eee665f` (by @cheelax, record at the time) | 49,343,723 |
| **This job (accepted, not a record)** | **49,339,523** |
| Saved vs parent | 4,200 |

The job was submitted on 2026-10-26 (UTC) but scored only on 2026-10-27, and did not become the record: while the lead reviewer was
down (23-27 Oct), the queue order decided, and other jobs submitted earlier became the records. The same idea appears
in **@nadai2010's** record `fk_15c54ef6`, whose `builds_on` on the board lists `@ryun1`, `@akashneelesh` and
`@ardianreffa` (this job).

##### Files
- `falcon-1024-fk_40768326.patch`: the submitted patch, cumulative against baseline `bf7fd8785a18`. Its SHA-256
  (`2c03bfb6...86bdc`) equals the `patch_sha256` the scorer reported for the job.
- `our-delta-on-fk_7eee665f.patch`: only my change on top of the parent (`fk.cairo`, `hash_to_point.cairo`).
  Verified: the parent patch (downloaded with `pvfast remote falcon1024 patch`) on the baseline, plus this delta,
  gives a tree identical (`diff -r`) to the baseline plus the submitted patch. The delta applies cleanly.

#### Contribution 32: transition Keccak round out of line on @rukafe0x's `fk_20c8300f` (job `fk_12c6048947344b7b8cd7dcab926961c0`)

> **Credit.** The parent record `fk_20c8300f` (seven Keccak rounds per call, paid for by decoding one squeeze block per step) and its
> 75% fit `fk_e13dd2c3` are **@rukafe0x**'s, as is the `mode1()` trick reused below.

##### What I did
`fk_20c8300f` runs rounds 1-14 and 16-22 in out-of-line calls (`rq` x2, `ra3` x2, `ra`) but kept the Q-to-A transition round 15
inline in `bb`. In `bb`'s large frame an inline round costs more than a call (putting round 22 inline instead is +21,500).
1. `fk.cairo`: round 15 moves to a new `inline(never)` `rt(st, rc, kb)`, like the other round calls: -24,300.
2. With that round gone, `bb` became small enough for the compiler to specialise it for `last()`'s literal `bb(p, 2)` (+1,475 CASM
   felts, over the cap). `hash_to_point.cairo`: `last()` now passes `crate::fk::mode1() + 1`, as the record already does for mode 1,
   so there is one `bb` again; CASM ends 117 felts below the record.

Local score (account validate minus baseline): 53,229,978 -> 53,205,678, -24,300; on the 15 crate verify/reject cases -22,800 to
-25,700 (mean -23,813). Correctness: 21 crate tests and 7 local account tests pass.

##### Official result

| | Gas |
|---|---:|
| Parent `fk_20c8300f` (by @rukafe0x, record at the time) | 49,457,895 |
| **This job (accepted, record as of 11 Nov 2026)** | **49,434,087** |
| Saved vs parent | 23,808 |

16 blocks 47,869,728 (-22,975), 17 blocks 50,216,266 (-24,225). The evaluator reports CASM 60,215 of 61,440 felts and a class of
2,981,897 bytes (73.5%). Lead: `rgr1_3e41406b2578b0ada801302fbae7b06e3a83cbcc0cc92dc825f61d53e7aaa7fa`.

##### Files
- `falcon-1024-fk_12c60489.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `bf7fd8785a18`. Its
  SHA-256 (`b3e9f21c...b631`) equals the `patch_sha256` the scorer reported for the job.
- `our-delta-on-fk_20c8300f.patch`: only my change on top of the parent (`fk.cairo`, `hash_to_point.cairo`). Verified: the parent
  patch on the baseline plus this delta gives a tree identical (`diff -r`) to the baseline plus the submitted patch.

### Bahasa Indonesia (sederhana)

#### Kontribusi 10: konstanta cell Keccak diangkat keluar dari loop squeeze (job `fk_40768326d05246c09567987a2660432f`)

##### Ide
Pada rekor **@cheelax** `fk_7eee665f`, loop squeeze memanggil `fk::eo()` di setiap permutasi untuk membangun ulang
tiga konstanta cell (`2^64`, `2^128-1`, `2^64-1`). Sekarang `eo()` dipanggil **sekali** sebelum absorb, dan cell
dibawa lewat loop serta diteruskan ke `keccak_next_k` dan ke absorb. Pembagi `2^64` milik pembaca kata, yang tadinya
entri `hcells` tersendiri, diambil dari cell `co.two64` yang sama, jadi loop membawa satu nilai lebih sedikit.

Tes: semua tes paket lulus (109/109 di workspace); lokal -4.300 gas pada 17 blok dan -4.000 pada 16 blok.

##### Hasil resmi
- Parent `fk_7eee665f` (oleh @cheelax, rekor pada waktunya): 49.343.723 gas.
- **Job ini (diterima, bukan rekor): 49.339.523 gas**, hemat 4.200 gas.
- Job dikirim 2026-10-26 (UTC) tetapi baru dinilai 2026-10-27, dan tidak menjadi rekor: saat penilai lead mati (23-27 Okt),
  urutan antrean yang menentukan, dan job lain yang dikirim lebih dulu menjadi rekor. Ide yang sama dipakai di rekor
  **@nadai2010** `fk_15c54ef6`, yang `builds_on`-nya di papan skor mencantumkan `@ryun1`, `@akashneelesh` dan
  `@ardianreffa` (job ini).

##### Berkas
- `falcon-1024-fk_40768326.patch`: patch yang dikirim, kumulatif terhadap baseline `bf7fd8785a18`. SHA-256-nya
  (`2c03bfb6...86bdc`) sama dengan `patch_sha256` yang dilaporkan penilai untuk job ini.
- `our-delta-on-fk_7eee665f.patch`: hanya perubahan saya di atas parent (`fk.cairo`, `hash_to_point.cairo`).
  Terbukti: patch parent (diunduh dengan `pvfast remote falcon1024 patch`) + delta ini sama persis isinya
  (`diff -r`) dengan baseline + patch yang dikirim. Delta dapat diterapkan dengan bersih.

#### Kontribusi 32: ronde transisi Keccak dipindah keluar baris, di atas `fk_20c8300f` milik @rukafe0x (job `fk_12c6048947344b7b8cd7dcab926961c0`)

> **Kredit.** Rekor dasar `fk_20c8300f` (tujuh ronde Keccak per panggilan) dan `fk_e13dd2c3` di bawahnya milik **@rukafe0x**, begitu
> juga trik `mode1()` yang dipakai ulang di sini.

##### Yang saya lakukan
`fk_20c8300f` menjalankan ronde 1-14 dan 16-22 lewat panggilan di luar baris, tetapi ronde transisi Q ke A (ronde 15) masih inline di
`bb`. Di frame `bb` yang besar, ronde inline lebih mahal daripada panggilan (ronde 22 dibuat inline justru +21.500).
1. `fk.cairo`: ronde 15 dipindah ke fungsi `inline(never)` baru `rt`: hemat 24.300.
2. Karena `bb` jadi kecil, compiler membuat salinan khusus `bb` untuk `bb(p, 2)` (+1.475 felt CASM, lewat batas). `last()` sekarang
   memanggil `bb(p, mode1() + 1)`, seperti yang sudah dilakukan rekor untuk mode 1, jadi `bb` kembali satu; CASM 117 felt di bawah rekor.

Skor lokal (validate akun dikurangi baseline): 53.229.978 -> 53.205.678, hemat 24.300; di 15 kasus crate hemat 22.800 s.d. 25.700.
21 tes crate dan 7 tes akun lokal lulus.

##### Hasil resmi
- Parent `fk_20c8300f` (oleh @rukafe0x, rekor pada waktunya): 49.457.895 gas.
- **Job ini (diterima, rekor per 11 Nov 2026): 49.434.087 gas**, hemat 23.808 gas (16 blok -22.975, 17 blok -24.225).
- CASM 60.215 dari 61.440 felt, class 2.981.897 byte (73,5%). Lead: `rgr1_3e41406b...a7fa`.

##### Berkas
- `falcon-1024-fk_12c60489.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `bf7fd8785a18`;
  SHA-256 (`b3e9f21c...b631`) sama dengan `patch_sha256` dari penilai.
- `our-delta-on-fk_20c8300f.patch`: hanya perubahan saya di atas parent (`fk.cairo`, `hash_to_point.cairo`). Patch parent + delta
  ini sama persis (`diff -r`) dengan baseline + patch yang dikirim.

### Pernyataan jujur
Patch Falcon-1024 dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## SLH-DSA-128s

Two accepted contributions to the **SLH-DSA-SHAKE-128s** season on
[postquantum.provably.fast](https://postquantum.provably.fast), baseline `7ab3ce3d`. The official patches are cumulative
against that baseline and contain the work of many contributors.

> **Disclosure / Pernyataan:** these patches were produced by an AI agent, **Claude Code** (models Sonnet and Opus),
> which I (**@ardianreffa**) ran and supervised. Contribution 15's job title says so; contribution 33's job records the agent
> (`claude-code`) and model (`claude-opus-5-5`).
> Patch-patch ini dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya (**@ardianreffa**) jalankan
> dan awasi. Judul job kontribusi 15 menyebutkannya; job kontribusi 33 mencatat agent (`claude-code`) dan model (`claude-opus-5-5`).

### English

#### Contribution 15: new `ht_layer` call convention (job `sj_0ab1739b6bf94bcab6811f01438a38cb`)

> **Credit.** This is a small step on a long record line: **@ryun1** (`sj_84bb8058`, four-chain ladders, non-panicking
> hash helpers, the `climb8` wrapper whose `None -> 0` return item 1 reuses), **@realadii**, **@odinfree** (`957443d8`),
> **@akashneelesh** (`sj_cbc7e977`) and finally **@nadai2010**, whose `sj_fe19b6f9` (`ht_layer_i` inlined for layer 0) is the
> parent. **What is mine** is only the calling convention of `ht_layer`, in `lanes.cairo`.

##### The idea
About 97% of the cost is the Keccak syscall, so only the glue around it can be improved. Four changes to how `ht_layer` is called:
1. The `ht_layer` wrapper returns `u128` (`None -> 0`, like the existing `climb8` wrapper): -1,200 gas.
2. `ht_layer` takes the already popped `@Box<[u64; 88]>` instead of `ref hs: Span` (the pops happen in `hypertree`): -2,000 gas.
3. The leaf lane is computed inside `ht_layer` from `leaf_idx`, one argument fewer: 0 gas, CASM -65.
4. `hypertree` computes all lanes and pops all six boxes before layer 1, and `root` is the first parameter, so the
   implicits and root returned by one call already sit where the next call needs them: -2,700 gas.

Local `bench_verify`: 408,415,562 -> 408,409,662 = **-5,900 gas**, the same on all 28 valid reference signatures.
Behavior: invalid signatures are still rejected with `false`; a Keccak `Err` inside layers 1 to 6 now flows as root 0
(root mismatch, so `false`) instead of an early `false`.

Correctness: 37/37 SLH tests pass; **756 reference vectors** (valid, bit flips in every region, public-key flips,
message, swaps, other key, non-canonical felts, wrong lengths) from `ref/slhdsa128s.py` give the same verdicts as the
record (756/756).

##### Official result

| | Gas |
|---|---:|
| Parent `sj_fe19b6f9` (by @nadai2010, record at the time) | 396,514,300 |
| **This job (accepted, record at the time; since passed by @thangvmt's `sj_e3657213`, 396,448,062; after the 11 Nov reset see contribution 33)** | **396,508,400** |
| Saved vs parent | 5,900 |

My first SLH-DSA-128s record (since passed by @thangvmt's `sj_e3657213`). The season is far from any gas cap: the Keccak syscalls alone are about 400M.

##### Files
- `slh-dsa-128s-sj_0ab1739b.patch`: the submitted patch, cumulative against baseline `7ab3ce3d`. SHA-256
  `fdaae6f6...d013e`.
- `our-delta-on-sj_fe19b6f9.patch`: only my change on top of the parent (`lanes.cairo`); apply with `git apply -p0`.

#### Contribution 33: @thangvmt's line slimmed to the 75% budget (job `sj_431c175a9682478c8cc94c11901b9af2`)

> **Credit.** Almost all of the gas work is other people's: **@thangvmt**'s `sj_e3657213` (E16/E8 enum dispatch in `climb8i`/`climbx`,
> inlined top layer) is the parent, on **@binharold**'s `sj_03a4d8f4` (WOTS+ ladder dispatch enums), which sits on my
> `sj_0ab1739b` (contribution 15), on the line of **@nadai2010** (`sj_fe19b6f9`), **@akashneelesh** (`sj_cbc7e977`, `sj_89d0939d`, and the
> post-reset record `sj_14d3d510`), **@odinfree** (`957443d8`), **@realadii** (`sj_3d7782bd`) and **@ryun1** (`sj_84bb8058`, four-chain
> ladders). **What is mine** is only the slimming below, in `lanes.cairo`.

##### What I did
After the 11 Nov 2026 reset, `sj_e3657213` (99.8% of the class limits) no longer counted as a record; the record became
@akashneelesh's older `sj_14d3d510` (398,084,453). `sj_e3657213` was about 1.6M gas cheaper but needed about 17k CASM felts and
1 MB of Sierra less to fit 75% (CASM ≤ 61,440, Sierra ≤ 3,067,084 bytes). The hash is SHAKE-256 through the Keccak syscall, so the
Keccak round grouping from my other lanes does not apply here.
1. `hypertree`: layer 0 (`ht_layer_i`) and the top layer (`ht_layer_o`) were inlined copies; both now call the out-of-line `ht_layer`
   like layers 1 to 5: CASM -10,440, +5,320 gas.
2. `climb8i` (FORS Merkle climb, three 16-arm matches of four inlined hashes each, 192 hashes): each match now only returns the four
   address constants (one shared `BoundedInt<0, max>` type per level, so no new type per arm) and four swap flags; the four hashes then
   run once, with the (node, auth path) operands swapped by an `if`. 12 inlined hashes instead of 192: CASM -9,088, Sierra -440 KB,
   about +126k gas.

Local `bench_verify`: 409,978,531 (`sj_14d3d510`) -> 408,480,442 = **-1,498,089 gas**; on 52 valid reference signatures -1,485,329 to
-1,526,959. Correctness: 1,441/1,441 tests pass, the same verdicts as the record: 37 crate tests (with ACVP) and 1,404 reference vectors
from `ref/slhdsa128s.py` (52 keys: valid, bit flips in every region, public-key flips, message, swaps, other key, non-canonical felts,
wrong lengths). Note: rejecting a non-canonical felt costs up to about 34M gas more than in `sj_14d3d510`, inherited from
`sj_e3657213`'s later decoding; still far below one valid verification.

##### Official result

| | Gas |
|---|---:|
| Record before, `sj_14d3d510` (by @akashneelesh) | 398,084,453 |
| **This job (accepted, record as of 11 Nov 2026)** | **396,579,569** |
| Saved vs that record | 1,504,884 |

The evaluator reports CASM 59,130 of 61,440 felts and a class of 3,062,818 bytes (74.9%). Worst case of the 8 held-out signatures
411,198,227. No lead: the SLH-DSA lane has no research graph.

##### Files
- `slh-dsa-128s-sj_431c175a.patch`: the submitted patch (`git diff --full-index`), cumulative against baseline `7ab3ce3d`. Its SHA-256
  (`96452f2c...7b63`) equals the `patch_sha256` the scorer reported for the job.
- `our-delta-on-sj_e3657213.patch`: only my change on top of the parent (`lanes.cairo`). Verified: the parent patch on the baseline plus
  this delta gives a tree identical (`diff -r`) to the baseline plus the submitted patch.

### Bahasa Indonesia (sederhana)

#### Kontribusi 15: cara pemanggilan `ht_layer` yang baru (job `sj_0ab1739b6bf94bcab6811f01438a38cb`)

> **Kredit.** Ini langkah kecil di atas garis rekor yang panjang: **@ryun1** (`sj_84bb8058`, tangga empat rantai, helper
> hash tanpa panic, pembungkus `climb8` yang return `None -> 0`-nya dipakai ulang di poin 1), **@realadii**,
> **@odinfree** (`957443d8`), **@akashneelesh** (`sj_cbc7e977`) dan terakhir **@nadai2010**, yang `sj_fe19b6f9`-nya
> (`ht_layer_i` di-inline untuk layer 0) menjadi parent. **Bagian saya** hanya cara pemanggilan `ht_layer` di `lanes.cairo`.

##### Ide
Sekitar 97% biaya adalah syscall Keccak, jadi hanya kode perekat di sekitarnya yang bisa diperbaiki. Empat perubahan
pada cara `ht_layer` dipanggil:
1. Pembungkus `ht_layer` mengembalikan `u128` (`None -> 0`, seperti pembungkus `climb8`): -1.200 gas.
2. `ht_layer` menerima `@Box<[u64; 88]>` hasil pop, bukan `ref hs: Span` (pop dilakukan di `hypertree`): -2.000 gas.
3. Lane daun dihitung di dalam `ht_layer` dari `leaf_idx`, satu argumen lebih sedikit: 0 gas, CASM -65.
4. `hypertree` menghitung semua lane dan mem-pop keenam box sebelum layer 1, dan `root` menjadi parameter pertama,
   sehingga implicit dan root yang dikembalikan satu panggilan sudah berada di tempat yang dibutuhkan panggilan berikutnya:
   -2.700 gas.

`bench_verify` lokal: 408.415.562 -> 408.409.662 = **-5.900 gas**, sama pada semua 28 tanda tangan referensi yang valid.
Perilaku: tanda tangan tidak valid tetap ditolak dengan `false`; `Err` Keccak di layer 1 sampai 6 kini mengalir sebagai
root 0 (root tidak cocok, jadi `false`) dan bukan `false` lebih awal.

Pengujian: 37/37 tes SLH lulus; **756 vektor referensi** (valid, bit dibalik di setiap bagian, kunci publik, pesan,
tukar, kunci lain, felt tidak kanonik, panjang salah) dari `ref/slhdsa128s.py` memberi putusan yang sama dengan rekor (756/756).

##### Hasil resmi
- Parent `sj_fe19b6f9` (oleh @nadai2010, rekor pada waktunya): 396.514.300 gas.
- **Job ini (diterima, rekor pada waktunya; sudah dilewati `sj_e3657213` milik @thangvmt, 396.448.062; setelah reset 11 Nov lihat kontribusi 33): 396.508.400 gas**, hemat 5.900 gas.
- Rekor SLH-DSA-128s pertama saya (sudah dilewati @thangvmt).

##### Berkas
- `slh-dsa-128s-sj_0ab1739b.patch`: patch yang dikirim, kumulatif terhadap baseline `7ab3ce3d`. SHA-256
  `fdaae6f6...d013e`.
- `our-delta-on-sj_fe19b6f9.patch`: hanya perubahan saya di atas parent (`lanes.cairo`); terapkan dengan `git apply -p0`.

#### Kontribusi 33: garis @thangvmt dirampingkan supaya muat batas 75% (job `sj_431c175a9682478c8cc94c11901b9af2`)

> **Kredit.** Hampir semua penghematan gas adalah karya orang lain: `sj_e3657213` milik **@thangvmt** (dispatch enum E16/E8 di
> `climb8i`/`climbx`, layer teratas di-inline) adalah parent-nya, di atas `sj_03a4d8f4` milik **@binharold** (enum dispatch tangga WOTS+),
> yang dibangun di atas `sj_0ab1739b` saya (kontribusi 15), di garis **@nadai2010** (`sj_fe19b6f9`), **@akashneelesh** (`sj_cbc7e977`,
> `sj_89d0939d`, dan rekor setelah reset `sj_14d3d510`), **@odinfree** (`957443d8`), **@realadii** (`sj_3d7782bd`) dan **@ryun1**
> (`sj_84bb8058`, tangga empat rantai). **Bagian saya** hanya perampingan di bawah ini, di `lanes.cairo`.

##### Yang saya lakukan
Setelah reset 11 Nov 2026, `sj_e3657213` (99,8% dari batas class) tidak lagi dihitung sebagai rekor; rekornya menjadi `sj_14d3d510`
milik @akashneelesh yang lebih lama (398.084.453). `sj_e3657213` sekitar 1,6 juta gas lebih murah, tetapi perlu sekitar 17 ribu felt CASM
dan 1 MB Sierra lebih kecil supaya muat 75% (CASM ≤ 61.440, Sierra ≤ 3.067.084 byte). Hash-nya SHAKE-256 lewat syscall Keccak, jadi
teknik pengelompokan ronde Keccak dari lane lain tidak berlaku di sini.
1. `hypertree`: layer 0 (`ht_layer_i`) dan layer teratas (`ht_layer_o`) tadinya salinan inline; keduanya sekarang memanggil `ht_layer`
   yang tidak di-inline, sama seperti layer 1 sampai 5: CASM -10.440, gas +5.320.
2. `climb8i` (pendakian Merkle FORS, tiga match 16 cabang yang masing-masing berisi empat hash inline, total 192 hash): setiap match
   sekarang hanya mengembalikan empat konstanta alamat (satu tipe `BoundedInt<0, max>` bersama per level, jadi tidak ada tipe baru per
   cabang) dan empat penanda tukar; keempat hash lalu dijalankan sekali, dengan operan (node, jalur auth) ditukar lewat `if`. 12 hash inline,
   bukan 192: CASM -9.088, Sierra -440 KB, gas sekitar +126 ribu.

`bench_verify` lokal: 409.978.531 (`sj_14d3d510`) -> 408.480.442 = **hemat 1.498.089 gas**; pada 52 tanda tangan referensi yang valid hemat
1.485.329 s.d. 1.526.959. Pengujian: 1.441/1.441 tes lulus, putusannya sama dengan rekor: 37 tes crate (termasuk ACVP) dan 1.404 vektor
referensi dari `ref/slhdsa128s.py` (52 kunci: valid, bit dibalik di setiap bagian, kunci publik, pesan, tukar, kunci lain, felt tidak
kanonik, panjang salah). Catatan: menolak felt tidak kanonik bisa sampai sekitar 34 juta gas lebih mahal daripada di `sj_14d3d510`, bawaan
dari decoding `sj_e3657213` yang dilakukan belakangan; tetap jauh di bawah biaya satu verifikasi yang valid.

##### Hasil resmi
- Rekor sebelumnya, `sj_14d3d510` (oleh @akashneelesh): 398.084.453 gas.
- **Job ini (diterima, rekor per 11 Nov 2026): 396.579.569 gas**, hemat 1.504.884 gas.
- CASM 59.130 dari 61.440 felt, class 3.062.818 byte (74,9%). Kasus terburuk dari 8 tanda tangan tersembunyi 411.198.227. Tanpa lead:
  lane SLH-DSA tidak punya research graph.

##### Berkas
- `slh-dsa-128s-sj_431c175a.patch`: patch yang dikirim (`git diff --full-index`), kumulatif terhadap baseline `7ab3ce3d`; SHA-256
  (`96452f2c...7b63`) sama dengan `patch_sha256` dari penilai.
- `our-delta-on-sj_e3657213.patch`: hanya perubahan saya di atas parent (`lanes.cairo`). Patch parent + delta ini sama persis (`diff -r`)
  dengan baseline + patch yang dikirim.

### Pernyataan jujur
Patch SLH-DSA-128s dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## starks.provably.fast (STARK math challenge)

Three independent reviews and one result of my own posted on the bulletin of [starks.provably.fast](https://starks.provably.fast) (public record:
<https://starks.provably.fast/record>). Files for contributions 12 and 13 are in [`starks/`](starks/). Posts appear under my bulletin identity, participant_824029c29299.

**Points on the STARK board: 53** (M-0078 = 50 for contribution 19, review of M-0020 = 3 for contribution 13). / **Poin di papan STARK: 53** (M-0078 = 50 untuk kontribusi 19, review M-0020 = 3 untuk kontribusi 13).

> **Disclosure / Pernyataan:** these reviews and the Q7 result were produced by an AI agent, **Claude Code** (models Sonnet and Opus),
> which I (**@ardianreffa**) ran and supervised. The posts name the agent (Claude Opus 5.5).
> Review ini dan hasil Q7 dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya (**@ardianreffa**) jalankan
> dan awasi. Posting menyebut agent-nya (Claude Opus 5.5).

> **Credit / Kredit:** in contributions 12, 13 and 20 the mathematics belongs to the original authors; our part is review
> and re-checking only. Contribution 19 is our own lower-bound result, accepted as M-0078 after review by hero570. / Di kontribusi 12, 13, dan 20
> matematikanya milik penulis asli; bagian kita hanya review dan pengecekan ulang. Kontribusi 19 adalah hasil batas bawah
> kita sendiri, diterima sebagai M-0078 setelah direview hero570.

### English

#### Contribution 12: independent review of the 11,831 cap (T3)
- Work under review: the 11,831 cap for level-16 kernel lifts, by **participant_dbbfaeddbe89** (post bp1_09ba872d).
- Our post: `bp1_e61a7c63`, thread `bt1_51f872ea`. Text: `starks/review-cap-11831.md`.
- Result: **holds within the stated accounting, with scope notes.** In my reading the argument is complete for the challenges it counts
  (Johnson chain A(14,4,5) <= 182, giving 65*182 + 1 = 11,831). It does not bound every bad challenge of such a line,
  and it is not shown to be tight. Checked by hand and by own code (`cap16.py`, `exh16.py`); the exhaustive h = 1 count
  gives exactly 226.
- Clarification (`starks/clarify-n16-flag.md`): `inst16_a.json` is participant_dbbfaeddbe89's construction. We only
  re-certified it for the review. It is not our result.
- Status: **posted, awaiting the organizers' record.**

#### Contribution 13: independent review of M-0020 (T2)
- Work under review: M-0020 (post bp1_2334f28d), by **odinfree**.
- Our post: `bp1_bcc0065b`, thread `bt1_5d39cc28`. Text: `starks/review-M0020.md`.
- Result: **holds as written.** The bucket lemma, the conditional transfer and the near-pair example are correct, and the
  J2 remark matches the pinned ArkLib definitions. Checked by hand and by own code (`m0020.py`).
- Status: **credited with 3 points** on the STARK points board.

#### Contribution 19: Q7 counterexample at n = 32, joint core 27
- Question: Q7 (`bp1_58386334`) asked whether n - j is the maximum residual, so that the split's constant could be
  c = (n - j)/n. Setting: BabyBear, mu_32, k = 16, A = 20, joint core j = 27, one step below the M-0023 threshold.
- Result 1 (`bp1_fe90e425`): an exact pair with E = 26, of which 21 are nonaligned, against n - j = 5. Each row of the post is
  exhaustive over all 225,792,840 twenty-subsets.
- Result 2 (`bp1_09dabbb6`): a census of pencil-form lines over all 3,199 orbits of the 5-point set U raises this to 22
  nonaligned, with E = 30, on two pairs.
- Lead: `rgr1_f06231d3...` (ADMITTED). Thread `bt1_f4a8d9ad`.
- Limits: this is a lower bound at one length and, for the census, inside one family of lines. It gives no upper bound. The pairs are still two-core pairs in the sense of `bp1_37829737` (participant_a63065a08b50).
- Checks: own code only, C and standard-library Python with byte-identical output; the panel's `grade.py` gave reward 1 and
  `kit/certify.py` certified 30 of 30 on both pairs with 22.
- Status: **accepted as M-0078 with 50 points** (2 Nov 2026). The record was reviewed by hero570, and binharold reproduced the
  census result (`bp1_09dabbb6`). An earlier maintainer reply (`bp1_cb64e859`, 1 Nov) had said this cell pays only for a count
  above 16n under rules v2 and earns nothing; the accepted record replaces that. The result is also listed in the official thread
  summary (`bp1_9ec9eaa9`, 1 Nov 2026): "found 22 at joint core 27, n = 32".
- Other participants have larger nonaligned counts at n = 32 on small joint cores (52 in `bp1_37829737`, 117 in `bp1_a9ee2b02`).
  The point of this result is the joint core, not the count.

#### Contribution 20: independent review of M-0016 (T3)
- Work under review: M-0016 by **nadai2010** (thread `bt1_cae9b123`).
- Our post: `bp1_7d52b47e`.
- Result: **partial.** Everything checked holds, with no counterexample: Claims A, B and C by hand, plus exhaustive and own-code
  checks of the lower levels. The headline statement at levels 128 to 512 remains unchecked by this review.
- Status: **my review is listed on the official M-0016 record as a partial review.** The record still shows M-0016 itself as
  not fully reviewed.

### Bahasa Indonesia (sederhana)

#### Kontribusi 12: review independen batas 11.831 (T3)
- Karya yang direview: batas 11.831 untuk kernel lift level-16, oleh **participant_dbbfaeddbe89** (post bp1_09ba872d).
- Post kami: `bp1_e61a7c63`, thread `bt1_51f872ea`. Teks: `starks/review-cap-11831.md`.
- Hasil: **berlaku dalam cakupan yang dinyatakan, dengan catatan scope.** Menurut pembacaan saya, argumennya lengkap untuk tantangan yang dihitung
  (rantai Johnson A(14,4,5) <= 182, jadi 65*182 + 1 = 11.831). Ia tidak membatasi semua tantangan buruk pada garis
  semacam itu, dan tidak ditunjukkan ketat. Dicek dengan tangan dan dengan kode sendiri (`cap16.py`, `exh16.py`);
  hitungan penuh h = 1 memberi tepat 226.
- Klarifikasi (`starks/clarify-n16-flag.md`): `inst16_a.json` adalah konstruksi milik participant_dbbfaeddbe89. Kami hanya
  mensertifikasi ulang untuk review. Itu bukan hasil kami.
- Status: **posted, menunggu pencatatan panitia.**

#### Kontribusi 13: review independen M-0020 (T2)
- Karya yang direview: M-0020 (post bp1_2334f28d), oleh **odinfree**.
- Post kami: `bp1_bcc0065b`, thread `bt1_5d39cc28`. Teks: `starks/review-M0020.md`.
- Hasil: **berlaku seperti yang ditulis.** Lemma bucket, transfer bersyarat, dan contoh near-pair benar, dan catatan J2
  sesuai dengan definisi ArkLib yang dipin. Dicek dengan tangan dan dengan kode sendiri (`m0020.py`).
- Status: **mendapat 3 poin** di papan poin STARK.

#### Kontribusi 19: counterexample Q7 di n = 32, joint core 27
- Pertanyaan: Q7 (`bp1_58386334`) bertanya apakah n - j adalah residual maksimum, sehingga konstanta split bisa
  c = (n - j)/n. Pengaturan: BabyBear, mu_32, k = 16, A = 20, joint core j = 27, satu langkah di bawah ambang M-0023.
- Hasil 1 (`bp1_fe90e425`): pair pasti dengan E = 26, 21 di antaranya nonaligned, melawan n - j = 5. Tiap baris di post
  diperiksa penuh atas semua 225.792.840 subset berukuran dua puluh.
- Hasil 2 (`bp1_09dabbb6`): census garis bentuk pencil atas semua 3.199 orbit himpunan 5 titik U menaikkannya menjadi 22
  nonaligned, dengan E = 30, pada dua pair.
- Lead: `rgr1_f06231d3...` (ADMITTED). Thread `bt1_f4a8d9ad`.
- Batasan: ini batas bawah di satu panjang dan, untuk census, di dalam satu keluarga garis. Tidak memberi batas atas. Pair ini tetap pair dua-core menurut `bp1_37829737` (participant_a63065a08b50).
- Pengujian: hanya kode sendiri, C dan Python stdlib dengan keluaran identik byte per byte; `grade.py` panel memberi reward 1
  dan `kit/certify.py` mensertifikasi 30 dari 30 pada kedua pair dengan 22.
- Status: **diterima sebagai M-0078 dengan 50 poin** (2 Nov 2026). Record-nya direview oleh hero570, dan binharold mereproduksi
  hasil census (`bp1_09dabbb6`). Balasan maintainer sebelumnya (`bp1_cb64e859`, 1 Nov) sempat menyatakan sel ini hanya dibayar untuk
  hitungan di atas 16n menurut rules v2 dan tidak mendapat apa-apa; record yang diterima menggantikan pernyataan itu. Hasilnya juga
  tercantum di ringkasan resmi thread (`bp1_9ec9eaa9`, 1 Nov 2026): "found 22 at joint core 27, n = 32".
- Peserta lain punya hitungan nonaligned lebih besar di n = 32 pada joint core kecil (52 di `bp1_37829737`, 117 di
  `bp1_a9ee2b02`). Nilai hasil ini ada pada joint core-nya, bukan pada hitungannya.

#### Kontribusi 20: review independen M-0016 (T3)
- Karya yang direview: M-0016 oleh **nadai2010** (thread `bt1_cae9b123`).
- Post kami: `bp1_7d52b47e`.
- Hasil: **parsial.** Semua yang dicek berlaku, tanpa counterexample: Claim A, B, dan C dengan tangan, ditambah cek penuh dengan
  kode sendiri di level bawah. Pernyataan utama di level 128 sampai 512 tetap tidak dicek oleh review ini.
- Status: **review kita tercantum di record resmi M-0016 sebagai partial review.** Record itu masih menandai M-0016 sendiri
  belum selesai direview.

### Pernyataan jujur
Review ini dan hasil Q7 dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).
Di kontribusi 12, 13, dan 20 bagian kami hanya review dan pengecekan ulang, dan hasil matematikanya milik penulis asli. Kontribusi 19 adalah hasil kami sendiri, diterima sebagai M-0078 (50 poin) setelah direview hero570.

---

## License
MIT. See `LICENSE`. The baseline is OpenZeppelin's cairo-pq-verifiers; accepted patches are MIT.

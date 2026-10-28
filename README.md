# provably-fast-contributions

Documentation of my accepted contributions to the **ML-DSA-44**, **ML-DSA-87** and **Falcon-1024** seasons on
[falcon.provably.fast](https://falcon.provably.fast/mldsa) (ML-DSA-87 and Falcon-1024 each have their own section near the end).

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
7. `mj_7b791824`: z range flags, six digits per AND with a +78 offset in the division chain (172,230,687 gas, current ML-DSA-44 record).

ML-DSA-87 (see the section [ML-DSA-87](#ml-dsa-87)):

8. `mk_3691ffe9`: UseHint HighBits by multiply-shift, pairs `(i, i+16)` per u128 (110,867,290 gas, record at the time).
9. `mk_469c1cb9`: mu and the first SampleInBall block in one two-state Keccak permutation (109,484,394 gas, ML-DSA-87 record when submitted). The two-state technique is **@rukafe0x's**; porting it to ML-DSA-87 is my work.
11. `mk_a5460736`: SampleInBall 8 bytes per lane made to fit the CASM limit, with the fallback as a continuation of the lane walk (99,827,006 gas, accepted, **not a record**: queue order).

Falcon-1024 (see the section [Falcon-1024](#falcon-1024)):

10. `fk_40768326`: Keccak cell constants hoisted out of the squeeze loop (49,339,523 gas, accepted, **not a record**: queue order).

STARK math challenge (see the section [starks.provably.fast](#starksprovablyfast-stark-math-challenge)). Reviews only, no new mathematics:

12. `bp1_e61a7c63`: independent review of the 11,831 cap (T3, work of participant_dbbfaeddbe89). Posted, awaiting the organizers' record.
13. `bp1_bcc0065b`: independent review of M-0020 (T2, work of odinfree). Posted, awaiting the organizers' record.

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
| **This job (accepted, current ML-DSA-44 record)** | **172,230,687** |
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
- **Job ini (diterima, rekor ML-DSA-44 saat ini): 172.230.687 gas**, hemat 104.584 gas.
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

## ML-DSA-87

Three accepted contributions to the **ML-DSA-87** (NIST level 5) account season on
[falcon.provably.fast](https://falcon.provably.fast/mldsa87). Here a transaction's validation is scored in
Sierra gas, mean over the held-out set; the season baseline (`23d05d6a2412`) costs 401,296,683 gas. For both
jobs, the official patch is the accepted one saved with `pvfast remote mldsa87 patch` (client 1.38.0). Like
before, official patches are **cumulative** against the baseline and contain the work of many earlier
contributors, mainly **@nadai2010**'s long record line, not only mine.

> **Disclosure / Pernyataan:** all three ML-DSA-87 patches were produced by an AI agent, **Claude Code**
> (models Sonnet and Opus), which I (**@ardianreffa**) ran and supervised. The job titles on the board say so.
> Ketiga patch ML-DSA-87 dikerjakan oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya
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

### Pernyataan jujur
Ketiga patch ML-DSA-87 dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## Falcon-1024

One accepted contribution to the **Falcon-1024** (NIST level 5) season on
[falcon.provably.fast](https://falcon.provably.fast/falcon1024), baseline `bf7fd8785a18`. The official patches are
cumulative against that baseline and contain the work of many contributors.

> **Disclosure / Pernyataan:** this patch was produced by an AI agent, **Claude Code** (models Sonnet and Opus),
> which I (**@ardianreffa**) ran and supervised. The job's model label on the board is `claude-opus-5-5`; its title
> does not name the agent.
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

### Pernyataan jujur
Patch Falcon-1024 dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).

---

## starks.provably.fast (STARK math challenge)

Two independent reviews posted on the bulletin of [starks.provably.fast](https://starks.provably.fast) (public record:
<https://starks.provably.fast/record>). Files are in [`starks/`](starks/).

> **Disclosure / Pernyataan:** these reviews were written by an AI agent, **Claude Code** (models Sonnet and Opus),
> which I (**@ardianreffa**) ran and supervised. The posts name the agent (Claude Opus 5.5).
> Review ini ditulis oleh agent AI **Claude Code** (model Sonnet dan Opus) yang saya (**@ardianreffa**) jalankan
> dan awasi. Posting menyebut agent-nya (Claude Opus 5.5).

> **Credit / Kredit:** the mathematics belongs to the original authors. Our contribution is review and re-checking only,
> not new mathematical results. / Matematikanya milik penulis asli. Kontribusi kita hanya review dan pengecekan ulang,
> bukan hasil matematika baru.

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
- Status: **posted, awaiting the organizers' record.**

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
- Status: **posted, menunggu pencatatan panitia.**

### Pernyataan jujur
Review ini dikerjakan oleh agent **Claude Code** (model Sonnet dan Opus) yang saya jalankan dan awasi (akun GitHub: **@ardianreffa**).
Kontribusi kami hanya review dan pengecekan ulang; hasil matematikanya milik penulis asli.

---

## License
MIT. See `LICENSE`. The baseline is OpenZeppelin's cairo-pq-verifiers; accepted patches are MIT.

# provably-fast-contributions

Documentation of my accepted contributions to the **ML-DSA-44** season on
[falcon.provably.fast](https://falcon.provably.fast/mldsa).

> **Disclosure / Pernyataan:** these patches were produced by an AI agent, **Claude Code**
> (model `claude-sonnet-5-5`), which I (**@ardianreffa**) ran and supervised.
> Patch-patch ini dikerjakan oleh agent AI **Claude Code** (model `claude-sonnet-5-5`) yang saya
> (**@ardianreffa**) jalankan dan awasi.

---

## Contributions

1. `mj_7279e4f3`: zero-lane first round + shared round loop (196,910,723 gas).
2. `mj_a27318a1`: lane-complemented two-state Keccak (184,696,268 gas, record at the time).
3. `mj_db11da30`: pruned final SHAKE-128 round in ExpandA (183,682,111 gas, record at the time).
4. `mj_24fb2836`: UseHint HighBits by multiply-shift, two residues per u128 (176,144,759 gas, record at the time).

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

## License
MIT. See `LICENSE`. The baseline is OpenZeppelin's cairo-pq-verifiers; accepted patches are MIT.

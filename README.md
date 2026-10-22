# provably-fast-contributions

Documentation of my accepted contribution to the **ML-DSA-44** season on
[falcon.provably.fast](https://falcon.provably.fast/mldsa).

> **Disclosure / Pernyataan:** this patch was produced by an AI agent, **Claude Code**
> (model `claude-sonnet-5-5`), which I (**@ardianreffa**) ran and supervised.
> Patch ini dikerjakan oleh agent AI **Claude Code** (model `claude-sonnet-5-5`) yang saya
> (**@ardianreffa**) jalankan dan awasi.

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

## License
MIT. See `LICENSE`. The baseline is OpenZeppelin's cairo-pq-verifiers; accepted patches are MIT.

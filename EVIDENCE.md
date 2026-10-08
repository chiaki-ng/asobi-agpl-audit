# Evidence index — Asobi

- [Release hashes](evidence/releases.json): 29 historical examined release samples. Version gaps remain; 1.5 has its own pin in the integration record.
- [Earlier findings](evidence/earlier-findings.json): the six newly added analysis samples, missing later markers and unchanged bundled-note hashes.
- [Per-line attribution](evidence/attribution.json): pinned v1.9.9 history for the four cited source ranges; retained source lines remain subject to upstream terms. This is authorship history, not proof every line was copied.
- [Current key-update integration](evidence/key-update-integration.json): all three measured functions, including zero-direct-reference results. Four direct sites share one containing caller.
- [Swift verification summaries](evidence/swift-comparison-verification.json): input pins and native coverage measurements. Bulk ranges/decompilations are withheld; these summaries alone do not independently prove semantic matches.
- [PSStream January 2026 build](evidence/psstream-steam-build.json): hashes (SHA-256 and Steam-manifest SHA-1), step labels, identifiers and the three authored log lines shared with Asobi 1.1–1.5, plus the Mac App Store 1.1.5 strings comparison. The binaries are withheld at the rights holder's request.
- [Developer notes](evidence/developer-notes.json): the five Markdown notes in store releases 1.0–1.3, each sealed by Apple's code signature (signature → `CodeResources` → note SHA-256), with the 35 lines that mention Chiaki quoted. Check with `tools/verify_notes_seal.py`.
- [Removals](evidence/removals.json): every Chiaki/PSStream string removed in 1.1.9, 1.2 and 1.4.2 with its replacement, and per-release counts.
- [Android](evidence/android.json): 1.0.3, 1.0.7 and 1.1.1 package, native-library and signing-certificate hashes; key-position functions, launch-spec template, `CHIAKI` string, licence scan. The `takion.proto` descriptor is excluded as protocol material.
- [Lineage markers](evidence/lineage-markers.json): when each Chiaki/chiaki-ng marker entered upstream, and its author.
- [Linked libraries](evidence/linked-libraries.json): per-release bundled dependencies; Jerasure FEC in every examined executable.
- [1.5 notices scan](evidence/notices-1.5.json): no AGPL, Chiaki or source notice; only the publisher's copyright and a “Proprietary” model licence.
- [Pylux check](evidence/pylux-check.json): negative; no copying from Pylux's public source is claimed.
- [Current CTRL bound excerpt](evidence/ctrl-bound-excerpt.asm): the 1 MiB comparison and rejection label. It is a short analytical excerpt, not the complete framing implementation.

## Source anchors and comparison outcomes

Reference: [chiaki-ng v1.9.9 commit](https://github.com/chiaki-ng/chiaki-ng/tree/4c2643f9b9b5c10907dbe82669f4d428ea86147d). Relevant ranges: holepunch.c 1507–1556; session.c 561–582 and 611–639; ctrl.c 307–490. [2023 microphone/key-position commit](https://github.com/chiaki-ng/chiaki-ng/commit/6fc4b8f6e4aec5a93cc8761ce41f212c8c6813ca), [2024 STUN-list commit](https://github.com/chiaki-ng/chiaki-ng/commit/143425f58c32be9772c37a463b24d3df98e5d36d).

| Family | 1.1.8 | 1.5 | Finding and limit |
| --- | --- | --- | --- |
| ACCEPT construction | 0x1003ac998 | 0x100456258 | Compiled sequence proceeds to a 30-second wait and RESULT; pre-send counter increment and continuing-error branches differ from C. |
| RESULT construction | 0x1003cb6ac | 0x1004798a8 | Metadata resolves reqId/error fields. Optional connection defaults and complete policy remain unresolved. |
| Cancellation cleanup | 0x1003c494c | 0x10047006c | Compiled throwing continuation resumption exists; absence of cancellation is not alleged. |
| CTRL receive/stream | 0x1002defc8 | 0x100328af8 | Early callback slices and later ordered-stream state differ from the cited C accumulated-buffer loop. |
| Candidate fallback | 0x1003f1728 | 0x1004a8d34 | Current prefix tests persist; complete ranking and confirmation equivalence remain open. |

The 1.1.9 comparison locates corresponding operation families after exact citation removal; it is not a claim of byte-identical full functions. The 1.5 prefix helper at 0x1004d3f48 builds a first-three-components string for four dotted components; it does not independently prove the entire subnet policy or a source-expression match.

## Sony client comparison

[Windows client check](evidence/sony-windows-client.json): Sony PS Remote Play for Windows 9.5.0.08040, the client the developer named as his main source, from Sony's public installer. It has Sony's NP signaling and stun.playstation.net, and none of the chiaki-ng choices below. A heuristic x64 key-position search found no match.

[macOS client check](evidence/sony-mac-client.json): Sony PS Remote Play for Mac 9.5.0; none of the Chiaki markers.

[Three-way comparison](evidence/sony-three-way.json) of Sony PS Remote Play 9.5.0, chiaki-ng (pinned `4c2643f9`) and Asobi. Sony uses NP signaling, `stun.playstation.net` and a ring-buffer key position; Asobi uses none of these. Asobi carries chiaki-ng choices that Sony lacks: the always-online-stun list, the three-response port-increment cases, 75/8 port guesses, `size + size % 16` and the moonlight-first STUN list. Session messages common to all three are treated as protocol. The ACCEPT wait and Senkusha fallback were not comparable. URLs and constants are evidence of copying, not standalone protected expression.

## Dated publisher evidence

October 6 observations refer to [the publisher site](https://asobiapp.com/) and [its legal page](https://asobiapp.com/legal.html), plus supplied About/legal screenshots. The About view identifies 1.5 without a build number. Screenshots, bulk page captures and correspondence are withheld here; absence of visible notices is a bounded observer report, not a complete UI inspection. The developer's independent-implementation position and prior private-inspection offer are acknowledged in FINDINGS.md.

PSStream/Pylux strings and step labels remain separate Asobi provenance context. The compared public Pylux snapshot postdates the early Asobi release. On October 8 the historical PSStream build was checked: PSStream 2.9.8, uploaded to Steam on 2026-01-14 (BuildID 21499345), contains all 16 compared step labels and all eight identifiers. It also contains three authored log lines (`=== Kamaji Step 0.5c Response ===`, `=== Centralized Authorization Check ===`, `Detected platform from Kamaji session:`) that every examined Asobi release from 1.1 through 1.5 carries verbatim, after the word “PSStream” was removed in 1.1.9 and 1.2. A Mac App Store copy of Asobi 1.1.5, bought by Forward Technologies, lists all 41 Chiaki/PSStream lines of iOS 1.1.5, including the four chiaki-ng source citations; its executable hash is their statement until the app is supplied. PSStream was sold on Steam from 2025-11-02. Its discontinuation was announced on 2026-01-16; the project continues as Pylux under AGPL-3.0. It was publicly sold before Asobi 1.1 (packaged 2026-02-13), the first release carrying PSStream markers. Forward Technologies has authorized pursuit of its rights in this Asobi case; that authorization does not independently establish the technical derivation claim. This curated package omits the underlying bulk string collection and cannot independently establish that separate claim from its summary alone.

# Method and reproduction

These are static measurements from unchanged supplied executables, pinned by SHA-256. No app was executed. Association with original store packages is based on recorded identity, resource and selected-region comparisons. It does not independently authenticate every instruction or verify Apple signatures.

Native analysis used Apple's otool, ARM64 branch/address decoding and LC_FUNCTION_STARTS. Asobi's targeted decompilations used Ghidra 12.1.4 with Java 21 and no full automatic analysis. Decompiled Swift types/registers/async continuations are imperfect; native instructions control the observations. Portal's byte continuity masks only BL call-address fields where specified, preserving every other bit. Source comparisons and attribution use pinned commits linked in EVIDENCE.md.

## Verify this publication package

Run `python3 tools/verify_public.py`. SHA256SUMS hashes the transformed public files, not the omitted private originals. The manifest itself is protected by the fresh Git commit. These checks establish snapshot consistency, not truth of every interpretation or guaranteed removal of every conceivable identifier.

## Check the developer-notes seal

With any App Store IPA of Asobi 1.0–1.3, run `python3 tools/verify_notes_seal.py STORE.ipa`. It reads the code signature's CodeDirectory, confirms that special slot −3 equals the SHA-256 of `_CodeSignature/CodeResources`, and that each bundled Markdown note matches its sealed hash. It reads no purchaser metadata and executes nothing. The executable's encryption does not cover these files or the signature.

## Recheck a supplied executable range

Obtain a matching executable independently and verify its hash against evidence/releases.json or the integration record. Do not put inputs inside the public repository. Use:

```sh
python3 tools/inspect_function.py --binary INPUT --expected-sha256 SHA256 --address ADDRESS --size BYTE_COUNT
```

For a comparison add `--compare-binary OTHER_INPUT --compare-sha256 OTHER_SHA256 --compare-address OTHER_ADDRESS`. Output gives exact and BL-only-normalized hashes and match results. Portal's microphone reference uses 2.10 widget address 0x100226638, size 224; current main uses 0x1009f8524. Use the precise main/widget input hashes in the evidence. The tool does not prove function boundaries or correspondence to upstream source; those are separate recorded measurements.

Public raw evidence is deliberately limited. Screenshots, private messages, app archives, account material, bulk captures, full decompilations and most large disassembly ranges are withheld. Those omitted exhibits cannot be independently inspected from this edition; request a suitable controlled review if needed. Publisher observations remain dated October 6, 2026, not a fresh live-site inspection at publication time.

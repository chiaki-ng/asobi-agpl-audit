# Selected case exhibits

The first two images are **user-supplied screenshots of public GitHub comments**, and section 5 has four cropped screenshots of public Reddit comments. The four IPA images are readable renderings of exact text and member names extracted from named iOS packages, not screenshots of the app running. Each IPA image identifies its ZIP member or executable and input SHA-256. Matching package hashes and their limited original-store association are in [release evidence](evidence/releases.json). The source packages are withheld. The excerpts avoid account data and full binaries.

## 0. The public denial

The user supplied these two screenshots of [GitHub issue #725](https://github.com/chiaki-ng/chiaki-ng/issues/725) on October 8. They show the developer's March 25 and March 26 comments; the first visibly carries GitHub's “Last edited” label. The screenshots' pixels are unchanged, and only ICC/XMP metadata was removed for publication. [Original and published hashes and the pixel check](evidence/github-screenshots.json) document that handling. The [dated GitHub API snapshot](evidence/developer-statements-issue-725.json) preserves issue dates, both comment IDs, full text, edit times and permalinks. Neither screenshot alone is a third-party historical archive.

[Open March 25 screenshot at full resolution](evidence/github-screenshots/march-25-denial.png)

![GitHub issue 725 showing the developer's March 25 denial](evidence/github-screenshots/march-25-denial.png)

[Open March 26 screenshot at full resolution](evidence/github-screenshots/march-26-swift-statement.png)

![GitHub issue 725 showing the developer's March 26 Swift statement](evidence/github-screenshots/march-26-swift-statement.png)

## 1. The bundled note

Asobi 1.1.8 contains `Payload/AsobiMobile.app/IMPLEMENTATION_SUMMARY.md` and `TAKION_FIXES.md`. The selected lines describe the implementation as based on Chiaki and cite its `takion.c` file. The [note hashes and signature chain](evidence/developer-notes.json) provide the stronger check: Apple's signature seals these resources in the examined original store packages.

![Selected lines from developer notes inside the Asobi 1.1.8 IPA](evidence/ipa-exhibits/01-bundled-chiaki-note.png)

## 2. The executable's source citations

Four log strings stored in the Asobi 1.1.8 executable identify Chiaki source files and line ranges. The [attribution record](evidence/attribution.json) maps those ranges to a pinned chiaki-ng version and distinguishes authors. A source citation is strong provenance evidence; it does not show that every cited instruction was copied.

![Four source-range citations stored in the Asobi 1.1.8 executable](evidence/ipa-exhibits/02-executable-source-citations.png)

## 3. The 1.1.9 edit

These paired strings are read directly from the Asobi 1.1.8 and 1.1.9 executables. The source references disappear while the surrounding operation names remain. [The complete measured changes](evidence/removals.json) include other Chiaki and PSStream references. This comparison establishes a wording change, not the developer's motive.

![Paired executable strings before and after Chiaki source references were removed](evidence/ipa-exhibits/03-citation-removal.png)

## 4. The notes disappear

All five selected Markdown members are in the Asobi 1.3 IPA and absent from the 1.3.1 IPA. Their [per-release hashes and seal checks](evidence/developer-notes.json) show they were unchanged through 1.3. This is a ZIP member comparison; it does not by itself say why they were removed.

![Five bundled Markdown note files present in Asobi 1.3 and absent in 1.3.1](evidence/ipa-exhibits/04-bundled-notes-removed.png)

## 5. On Reddit

These four images are crops of user-supplied screenshots of the live Reddit pages, taken on October 11, 2026. Each is cropped to the comment column; the pixels are unchanged and metadata was removed ([hashes and crop boxes](evidence/reddit-screenshots.json)). The [archived text and permalinks](evidence/developer-statements-reddit.md) are the fuller record.

February 14, the day after Asobi 1.1 shipped the chiaki-ng line citations, replying to a request to respect the AGPL:

![u/inchenzo on February 14: No code has been used from Chiaki in Asobi](evidence/reddit-screenshots/2026-02-14-no-chiaki-code-o5dexul.png)

March 29, his weekly report after Street Pea closed issue #725 relying on his assurance. The archive, copied 23 seconds after posting, reads “conversation of an official third-party”; the live post now reads “confirmation from”:

![u/inchenzo on March 29: Being validated by streetpea](evidence/reddit-screenshots/2026-03-29-validated-by-streetpea-1s6uzta.png)

April 13:

![u/inchenzo on April 13: I don’t use Chiaki (so no AGPL to deal with)](evidence/reddit-screenshots/2026-04-13-no-agpl-to-deal-with-ofwe9am.png)

September 26, replying to the developer of Horizon Stream, a Quest app based on Android Chiaki, whose comment has since been deleted. The archived first version read only “This is an original implementation. Never seen your app before tbh. Good luck with it.” The edited live version adds “chiaki isn't used here (which has been validated by StreetPea himself)”:

![u/inchenzo on September 26, edited: chiaki isn't used here (which has been validated by StreetPea himself)](evidence/reddit-screenshots/2026-09-26-original-implementation-edited-pc7ddg6.png)

To reproduce the images from independently obtained matching packages, install Pillow and run `python3 tools/render_ipa_exhibits.py --ipa-1-1-8 <file> --ipa-1-1-9 <file> --ipa-1-3 <file> --ipa-1-3-1 <file> --out <folder>`. The script checks each input hash and `Info.plist` version, selects only the displayed archive members and strings, and writes PNGs without source paths or embedded metadata.

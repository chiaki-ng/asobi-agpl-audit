# Asobi: findings and limits

Reviewed October 7, 2026; PSStream build added October 8. Technical evidence and license-compliance inquiry, not a final infringement determination. Claimant/authorized representative: Street Pea; see RIGHTS-HOLDERS.md for scope. App: Asobi: Remote Play; publisher Inside Internet; Apple ID 6754204833; bundle `com.insideinternet.Asobi`.

This audit is maintained by the chiaki-ng project. Street Pea is its maintainer and a copyright holder, pursuing their own rights. xlanor has also authorized representation, but no xlanor-authored code was identified in Asobi, so xlanor is not named in the Asobi drafts (see RIGHTS-HOLDERS.md). Forward Technologies has also authorized Street Pea to pursue its PSStream/Pylux rights in the Asobi case. Other contributors are not represented without their authorization.

## Measured evidence

**The developer's statements.** On chiaki-ng issue #725 (March 25–26, 2026) the developer wrote: “I'm not using any Chiaki code”; “All these steps can be found just as fine via the Windows remote play client where I got most of my info from”; and “My implementation is written entirely in Swift, no Chiaki or PSStream code is compiled, linked, or included.”

His own shipped code contradicts these statements:

1. **His bundled notes.** Releases 1.0–1.3 ship developer notes describing Asobi as “a pure Swift version of Chiaki's PlayStation Remote Play streaming protocol”. That includes builds packaged after the public denial. The notes were deleted in 1.3.1 (about April 30).
2. **His log messages cite chiaki-ng source by file and line.** Releases 1.1–1.1.8 log messages such as “DATA ACCEPT exchange (Chiaki holepunch.c:1507-1556)”. These ranges match only chiaki-ng v1.9.7–v1.9.9. They come from neither psn-api nor Sony's client.
3. **The references were removed, but the implementation stayed.** Release 1.1.9, packaged about a day after the GitHub denial, deleted the word “Chiaki” from these messages. A `CHIAKI` constant was removed in 1.4.2. The chiaki-ng-derived implementation remains in the current release, 1.5.
4. **Neither Sony client contains the chiaki-ng choices Asobi carries.** This includes the Windows client he named as his main source. See the comparison below.

These are documented contradictions between the developer's statements and his shipped code. No claim about motive is made.

The audit covers 29 examined historical iOS releases from 1.0 through 1.4.3, with gaps explicitly retained, plus separately measured iOS 1.5. The historical analysis packages passed the recorded identity, resource and selected-region comparisons against matching original Apple packages. This supports association but does not independently authenticate every instruction or verify Apple signatures.

Bundled developer notes describe a Swift implementation based on Chiaki. Examined 1.1–1.1.8 releases contain four exact chiaki-ng source-range citations. Per-line history separates my contributions from other authors' work. Actual ACCEPT/RESULT and CTRL operation families have been recovered, with relevant behavior traced through citation removal in 1.1.9 and into 1.5. Compiled message layouts, cancellation, ACK handling and current validation/crypto paths are documented. Counter order, error handling and receive architecture differ from the cited C; a complete protected-expression translation of every cited block is not established.

The 2023 key-position adjustment and 2024 STUN-list choice associated with my commits corroborate later-fork provenance. A 1.5 key-update function has four direct call sites from one containing function. Names, protocol constants, URLs and an arithmetic expression alone are not the protected works claimed. The six earlier releases newly examined on October 7 preserve Chiaki-labelled code and notes but do not move the observed later citations/key-position pattern or PSStream markers before 1.1.

## Contrary evidence and unresolved questions

To separate protocol requirements from chiaki-ng’s own implementation choices, I analyzed both of Sony’s official PS Remote Play clients: iOS 9.5.0, and Windows 9.5.0.08040, the client the developer named as his main source. Both do NAT traversal through Sony’s own NP signaling library and use Sony’s own STUN host (stun.playstation.net). The iOS client tracks key position with a keystream ring buffer. Asobi uses none of these Sony mechanisms. It instead carries the following chiaki-ng-specific choices, which neither Sony client has:

| Implementation choice | chiaki-ng | Sony PS Remote Play (iOS and Windows) | Asobi |
| --- | --- | --- | --- |
| STUN hosts fetched from the always-online-stun GitHub list (my 2024 change) | Yes | No | From 1.1.5; still in 1.5 |
| Port increment derived from three STUN responses by address pattern: A/A/B, A/B/A, A/B/B and same-address unequal increments, with the same formula in each case (my code) | Yes | No | From 1.1.8; still in 1.5 |
| 75 port guesses on random NAT allocation; 8 predicted guesses otherwise (my code) | Yes | No | From 1.1 / 1.1.3 |
| Key position advanced by size + size % 16 (my 2023 change) | Yes | No (iOS: ring-buffer design, pattern absent; Windows: no match by heuristic) | Yes, including 1.5 |
| Hard-coded public STUN list led by stun.moonlight-stream.org, then Google stun–stun4 (chiaki-ng, another author) | Yes | No | From 1.0 |

The PSN session messages (OFFER/ACCEPT/RESULT) appear in all three and are treated as protocol, not claimed. The matched choices are not required to interoperate, since Sony’s client works without them. They therefore indicate derivation from chiaki-ng rather than from the protocol or Sony’s app. Individual constants and URLs are offered as evidence of copying, not as independently protected expression. The port-allocation decision structure is offered as both.

The developer's March account says private code inspection was offered, which I acknowledge. A private inspection offer is not by itself a demonstrated recipient source-delivery mechanism.

October 6 checks of the supplied 1.5 About/legal views and inspected publisher pages found no visible Chiaki/AGPL acknowledgement or corresponding-source access. The About screen shows 1.5 without a build number. These are bounded historical observations, not absence from every screen or channel. PSStream/Pylux is a separately identified authorized rights-holder claim in this Asobi case; PSStream's January 14, 2026 Steam build (2.9.8) already contains the step numbering, identifiers and three log lines that Asobi carries from 1.1 through 1.5, so the order no longer depends on Pylux's later source ([measurement](evidence/psstream-steam-build.json)). The authorized rights holders are identified below and in RIGHTS-HOLDERS.md; the technical limitations still apply to each claim.

Full protected-expression comparison, complete combined-work scope, actual source delivery and separate permission remain unresolved. No app execution or source rebuild was performed. A source request, Apple complaint or GitHub update has not been sent by this preparation.

## Requested resolution

Please identify the authority for distributing any covered contributions; the matching release-to-source commit mapping; the applicable license and notices; covered changes and integration source; necessary build materials under the license's exclusions; and the source-access directions given to recipients. If separate permission or existing compliance materials apply, please identify them for assessment. My preferred resolution is demonstrated compliance.

If the shipped implementation incorporates protected expression from my contributions and no separate permission applies, the applicable AGPL-3.0 conditions require notices, licensing of the covered combined work and complete Corresponding Source through an appropriate §6 distribution mechanism. Covered translations/modifications are included; independent works in a genuine aggregate are excluded. Section 6(d)'s online-download option requires equivalent source access without further charge and clear directions. The project's OpenSSL exception permits its specified combination while retaining applicable conditions and its specified source requirement. Attribution alone is insufficient. Charging is permitted. The actual covered-work boundary and any separate permission still require assessment. See the [license text](https://www.gnu.org/licenses/agpl-3.0.html).

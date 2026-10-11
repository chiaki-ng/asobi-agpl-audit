# Issue #725: preserved thread

Captured 2026-10-11T20:32:45Z from GitHub's public API, before any update was posted. This is a readable copy of [issue-725-thread.json](issue-725-thread.json); the JSON is the record. Comment text is shown verbatim in code blocks. Live issue: https://github.com/chiaki-ng/chiaki-ng/issues/725

## Issue: Asobi (Mac App Store) is using Chiaki — no attribution, paid & closed source

Opened by **GrumpyGenesis** at 2026-03-16T00:53:17Z · closed 2026-03-25T15:46:40Z · body SHA-256 `4f2a6736988deb8e0145b210e898fc9bf00865c2f495a0857feab59bfc9ccfc3`

````text
# Asobi (Mac App Store) is using Chiaki — no attribution, paid & closed source

Hey Chiaki devs — are you aware of **Asobi**? It’s a **paid**, **closed-source** Remote and Cloud Play client on the Mac App Store (and other Apple platforms). They’re **clearly using your code**. I ran `strings` on the binary and it’s full of your source file names, line numbers, and protocol strings. There’s no LICENSE or attribution to Chiaki anywhere. They also reference **PSStream** all over the place, so they’ve likely reverse‑engineered that for cloud play too.

**Why this is stealing:** Chiaki is AGPL. They’re selling a closed-source app with your code (or a direct derivative), no source offer, no credit. That’s a license violation and passing off your work as their product.

I was considering paying for Asobi. At first I thought it looked cool, but now I'm realizing it's stealing and I don't want to support it. Maybe you should send them a DMCA and report them to Apple? I thought Apple was pretty responsive to that, what are your thoughts? Am I missing something here? If you could at least reach out and get them to open source it, that would be cool since the overall layout of the app seems nice
````

## Comment 4071386738 by streetpea

2026-03-16T23:55:28Z · [permalink](https://github.com/chiaki-ng/chiaki-ng/issues/725#issuecomment-4071386738) · SHA-256 `6f76b569dcd9fe1b66b399d432c188678cc43d6e026a1a3ff67fb9b12535948c`

````text
I created a dmca request with apple. I'll see what they say
````

## Comment 4127373247 by rijnbeek

2026-03-25T15:09:36Z · last edited 2026-03-25T15:43:23Z · [permalink](https://github.com/chiaki-ng/chiaki-ng/issues/725#issuecomment-4127373247) · SHA-256 `8df2dd41a73961987da2c8ea36df462c50e22107fc565af600eb8c1c3483252f`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

(see link https://www.npmjs.com/package/psn-api)

The whole codebase is written in swift. 

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.

.. I also don't appreciate my backend strings floating around like this.
````

## Comment 4127685258 by streetpea

2026-03-25T15:47:38Z · [permalink](https://github.com/chiaki-ng/chiaki-ng/issues/725#issuecomment-4127685258) · SHA-256 `bebf8259ff06ca0ad7c05e095e296f32adb09ac88c63c0d7d215545f2204c0dd`

````text
Since it doesn't seem Asobi is using chiaki-ng after discussing with @rijnbeek , I'll close this.
````

## Comment 4132649734 by GrumpyGenesis

2026-03-26T08:29:36Z · last edited 2026-03-26T08:47:22Z · [permalink](https://github.com/chiaki-ng/chiaki-ng/issues/725#issuecomment-4132649734) · SHA-256 `6aff57dbeafcb2fe55ca3843c89c8cf8d9882f7aaa5d3d99fa113abd22e7c5ff`

````text
> P.S. If there are any questions, feel free to ask.

Hey @rijnbeek / @streetpea, thanks, I would be happy to go through it.

> I'm not using any Chiaki code [...] other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

So let’s look at these in Asobi:

```
- Starting CTRL receive loop (Chiaki ctrl.c:307-490)...
- Step 4: DATA holepunch (Chiaki session.c:561-582)
- Step 4.5: SENKUSHA on DATA socket (Chiaki session.c:611-639)
- STEP 9: DATA ACCEPT exchange (Chiaki holepunch.c:1507-1556)
```

These are direct references to specific Chiaki source files and exact line ranges. This is not coming from psn-api. These are Chiaki file names and corresponding line numbers.

That strongly indicates the implementation is derived from Chiaki rather than independently developed, which would trigger GPL obligations.

> The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

PSStream itself is based on Chiaki and uses the same licensing. I too looked into it when it was briefly released before being taken down.

> All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

This is not accurate. PS5 cloud streaming is not available in the Windows client. The fact that you do not seem to know that is strong evidence this was not reverse engineered from it.

Additionally, the behavior here clearly comes from PSStream, as shown by:

```
- with fallback values (per PSStream binary)
- but got sessionId - continuing (PSStream behavior)
- Per PSStream: BANG with ECDH keys is required for encryption
```

Referencing PSStream specific behavior and fallback logic suggests the binary was used as an implementation source. If the implementation was derived from that rather than independently developed, that would also raise GPL concerns.

At this point, the overlap with both Chiaki and PSStream is significant enough that this does not look like an independent implementation.

I am honestly surprised this was closed @streetpea considering how directly this maps back to Chiaki.

To be clear, I think Asobi looks pretty cool. This is not meant to be unfair or overly aggressive. It is just frustrating to see GPL licensed projects reused in a way that appears proprietary. I wish that effort was given back to the community rather than taken from it.

> I also don't appreciate my backend strings floating around like this.

The concern is that those strings directly demonstrate the linkage to Chiaki and PSStream as implementation sources.
````

## Comment 4132929950 by rijnbeek

2026-03-26T09:13:09Z · [permalink](https://github.com/chiaki-ng/chiaki-ng/issues/725#issuecomment-4132929950) · SHA-256 `6243ac90a647af6404be37add817e198bdf1fc8ce8fc6adf9c2de297697a79a5`

````text
My implementation is written entirely in Swift, no Chiaki or PSStream code is compiled, linked, or included. @streetpea and I discussed this, and he was satisfied. I respect his judgment as the maintainer and copyright holder.
````

## Revision history of the developer's March 25 comment

Captured 2026-10-11T20:31:52Z from GitHub's public edit history. Each revision is the full comment text as of that edit.

### Revision 1: 2026-03-25T15:09:36Z by rijnbeek

SHA-256 `d635166458b672d15938043a5cb9368a31a59c4f82456bdbdd23d01e67177c50`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the big-endian/base64 encoded ID which incidentally has named that id chiaki-id.

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I most of my info from.

/v

P.S. If there are any questions feel free to ask.
````

### Revision 2: 2026-03-25T15:12:12Z by rijnbeek

SHA-256 `fd13e1e9563b53f2e5373d3b8e89d23880da8ffb8884135f054d304158153b4f`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the big-endian/base64 encoded ID which incidentally has named that id chiaki-id.

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.
````

### Revision 3: 2026-03-25T15:12:46Z by rijnbeek

SHA-256 `b8769219841fe7cc72c75ac642d61fa0666d724c591cb9504f87cf87e3367333`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.
````

### Revision 4: 2026-03-25T15:13:55Z by rijnbeek

SHA-256 `64265b8136efb184895526d9663854384c3144c066880c5f45371c83385c7e70`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.
````

### Revision 5: 2026-03-25T15:19:09Z by rijnbeek

SHA-256 `65e84a6a215cc73cd88174474e6b55dedd9e5e82a4eed8df00e7be352a69c955`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

(see link https://www.npmjs.com/package/psn-api)

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.
````

### Revision 6: 2026-03-25T15:22:04Z by rijnbeek

SHA-256 `63194b8875edad4a1f74f75a61b04f91eddf678a6db0e2c741d22c76b3923452`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

(see link https://www.npmjs.com/package/psn-api)

The whole codebase is written in swift. It's not like I'm wrapping chiaki like another remote play app on the app store named Portal.

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.

.. I also don't appreciate my backend strings floating around like this.
````

### Revision 7: 2026-03-25T15:43:23Z by rijnbeek

SHA-256 `8df2dd41a73961987da2c8ea36df462c50e22107fc565af600eb8c1c3483252f`

````text
Hi!

Asobi dev here, I just stumbled upon this.

I'm not using any Chiaki code. That said, what I am using is the Windows Playstation Remote play client ID, which Chiaki uses as well. And all the other references are from the psn-api library I use for obtaining the little-endian/base64 encoded ID which incidentally has named that id chiaki-id.

(see link https://www.npmjs.com/package/psn-api)

The whole codebase is written in swift. 

The PSStream info also has no merit here either, I'm using the same info that that developer used and more. I'm also not sure what this has to do with Chiaki since that has no relation with it.

All these steps can be found just as fine via the Windows remote play client where I got most of my info from.

/v

P.S. If there are any questions feel free to ask. 

P.P.S If it were the case in relation to using Chiaki -> I wouldn't have so many issues with timeouts/internet remote play.

.. I also don't appreciate my backend strings floating around like this.
````

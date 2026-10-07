Binary SHA256: 401d41cbe773f315bef411216d7eb65d54407cf51ced63f0e0a5977c7860ddf0
Native otool -tvV; LC_FUNCTION_STARTS range 0x1001657ec–0x100165bd4
0000000100165a1c	cmp	w28, #0x100, lsl #12
0000000100165a20	b.hi	0x100165aac
0000000100165b08	adrp	x3, 2896 ; 0x100cb5000
0000000100165b0c	add	x3, x3, #0xbe0 ; literal pool for: "CTRL payload size %u exceeds sane max (%u) \342\200\224 rejecting"

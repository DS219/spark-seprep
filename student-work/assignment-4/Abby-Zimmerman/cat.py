import textwrap

message = "Midterms suck, so here's some dancing cats! feel better"
lines = textwrap.wrap(message, 30)
#speech bubble dimensions
width = max(len(line) for line in lines)
print(" " + "-" * width)
for line in lines:
    print(f"< {line.ljust(width)} >")
print(" " + "-" * width)

#print cats
print(r"""
♪
　　　　∧＿∧　　　♪
　　　 （´・ω・｀∩
　　 　　o　　　,ﾉ
　　　　Ｏ＿　.ﾉ
♪　　　 　 (ノ

　　　　∧＿∧　♪
　　　 ∩・ω・｀）
　　　 |　　 ⊂ﾉ
　　　｜　　 _⊃　　♪
　　　 し ⌒
""")

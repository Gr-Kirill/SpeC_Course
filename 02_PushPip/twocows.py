import cowsay 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message1")
parser.add_argument("-f", default="default")
parser.add_argument("-e", default="oo")
parser.add_argument("-n", action="store_false")
parser.add_argument("message2")
parser.add_argument("-F", default="default")
parser.add_argument("-E", default="oo")
parser.add_argument("-N", action="store_false")

args = parser.parse_args()

cow1 = cowsay.cowsay(message=args.message1, cow=args.f, eyes=args.e, wrap_text=args.n)
cow2 = cowsay.cowsay(message=args.message2, cow=args.F, eyes=args.E, wrap_text=args.N)

cow1_lines = cow1.split('\n')
cow2_lines = cow2.split('\n')

max_lines = max(len(cow1_lines), len(cow2_lines))
max_str = len(max(cow1_lines, key=len))

res_cow1 = [''] * (max_lines - len(cow1_lines))
res_cow2 = [''] * (max_lines - len(cow2_lines))

res_cow1.extend(cow1_lines)
res_cow2.extend(cow2_lines)

for line1, line2 in zip(res_cow1, res_cow2):
    print(line1 + " "*(max_str-len(line1)+1) + line2)

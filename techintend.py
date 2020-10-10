import re

fun = """void func(int a, int b)
printf(“ Hello World”);
if (a==a)
vod f(int a)
}"""


def rule_1_violation(string):
    fun_prot = re.compile(r'.* .*\(.*\)')
    rule_brases_1 = re.compile(r'.* .*\(.*\){')
    for line_no, lin in enumerate(string.splitlines()):
        if fun_prot.search(lin):
            if rule_brases_1.search(lin):
                continue
            else:
                yield "rule [1] is violated at line [{}]".format(line_no+1)


def rule_2_violation(string):
    fun_prot = re.compile(r'.* .*\(.*\)')
    for lin_No, line in enumerate(string.splitlines()):
        if fun_prot.search(line):
            print(line.index(line[0]))


def rule_3_violation_comp(string):
    com_proto = re.compile(r'if')
    con_right = re.compile(r'\d==.*')
    for li, line in enumerate(string.splitlines()):
        if com_proto.search(line):
            if con_right.search(line):
                continue
            else:
                yield "rule [3] is violated at line [{}]".format(li+1)


print('hello {}'.format(1))

print(fun.index('o'))
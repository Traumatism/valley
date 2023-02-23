import random

from io import StringIO
from typing import Tuple, Dict, List

SYS_syscall = 0
SYS_exit    = 1
SYS_fork    = 2
SYS_read    = 3
SYS_write   = 4
SYS_open    = 5
SYS_close   = 6


class Compiler:
    """ Compiler """

    def __init__(self, entrypoint: str = "_start") -> None:
        self.output = StringIO()

        self.entrypoint = entrypoint

        self.variables: List[str] = []

        self.functions: Dict[str, List[str]] = {
            self.entrypoint: list()
        }


    def puts(self, scope: str, message: str):
        """ Add a print instruction """
        message = message.replace("\\", "\\\\")

        msg, msg_len = self.add_variable_str(message)

        self.mov(scope, "x0", 1)
        self.adr(scope, "x1", msg)
        self.mov(scope, "x2", msg_len)

        self.syscall(scope, SYS_write)

    def exit(self, scope: str, status: int):
        """ Add an exit instruction """

        self.mov(scope, "x0", status)
        self.syscall(scope, SYS_exit)

    def generate_variable_name(self, prefix: str) -> str:
        """ Generate a new variable """

        name = "%s_%d" % (
            prefix, random.randint(1000, 9999)
        )

        if name in self.variables:
            return self.generate_variable_name(prefix)

        self.variables.append(name)

        return name

    def add_variable_str(self, value: str) -> Tuple[str, str]:
        """ Add a new string variable """

        name = self.generate_variable_name("str")

        self.functions[name] = [
            '.asciz "%s"' % value,
            "%(name)s_len = . - %(name)s" % {"name": name},
        ]

        return name, "%s_len" % name

    def syscall(self, scope: str, syscall_number: int):
        """ Make a syscall """

        self.mov(scope, "X16", syscall_number)
        self.svc(scope, SYS_syscall)

    def add(self, scope: str, rd, rn, operand):
        self.functions[scope].append(
            "add %s, %s, %s" % (rd, rn, operand)
        )

    def svc(self, scope: str, imm):
        self.functions[scope].append("svc %s" % imm)

    def adr(self, scope: str, rd, label):
        self.functions[scope].append("adr %s, %s" % (rd, label))

    def mov(self, scope: str, rd, operand):
        self.functions[scope].append("mov %s, %s" % (rd, operand))

    def compile(self) -> str:
        indents = 0
        INDENT  = "    "

        self.output.write(".globl %s\n" % self.entrypoint)
        self.output.write(".align 2\n")
        self.output.write("\n%s:\n" % self.entrypoint)
        indents += 1

        for instruction in self.functions[self.entrypoint]:
            self.output.write("%s%s\n" % (INDENT * indents, instruction))

        indents -= 1

        del self.functions[self.entrypoint]

        for name, instructions in self.functions.items():
            self.output.write("\n%s:\n" % name)
            indents += 1

            for instruction in instructions:
                self.output.write("%s%s\n" % (INDENT * indents, instruction))

            indents += 1

        return self.output.getvalue()


if __name__ == "__main__":
    compiler = Compiler()

    scope = compiler.entrypoint

    compiler.puts(scope, "Hello, world !\n")
    compiler.exit(scope, 0)

    print(compiler.compile())

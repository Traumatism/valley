import random

from io import StringIO
from typing import Tuple, Dict, List

from valley.syscall import SYS_syscall, SYS_write, SYS_exit


class Compiler:
    def __init__(self, entrypoint: str = "_start") -> None:
        self.output = StringIO()

        self.entrypoint = entrypoint

        self.points: Dict[str, List[str]] = {}

        self.output.write(".globl %s\n" % entrypoint)
        self.output.write(".align 2\n")

        self.variables = []
        self.points[entrypoint] = []

    def puts(self, scope: str, message: str):
        message = message.replace("\\", "\\\\")

        msg, msg_len = self.add_variable_str(message)

        self.mov(scope, "x0", 1)
        self.adr(scope, "x1", msg)
        self.mov(scope, "x2", msg_len)

        self.syscall(scope, SYS_write)

    def exit(self, scope: str, status: int):

        self.mov(scope, "x0", status)
        self.syscall(scope, SYS_exit)

    def generate_variable_name(self, prefix: str) -> str:
        name = "%s_%d" % (prefix, random.randint(1000, 9999))

        if name in self.variables:
            return self.generate_variable_name()

        self.variables.append(name)
        return name

    def add_variable_str(self, value: str) -> Tuple[str, str]:
        name = self.generate_variable_name("str")

        self.points[name] = [
            '.asciz "%s"' % value,
            "%(name)s_len = . - %(name)s" % {"name": name},
        ]

        return name, "%s_len" % name

    def syscall(self, scope: str, syscall_number: int):
        self.mov(scope, "X16", syscall_number)
        self.svc(scope, SYS_syscall)

    def add(self, scope: str, rd, rn, operand):
        self.points[scope].append("add %s, %s, %s" % (rd, rn, operand))

    def svc(self, scope: str, imm):
        self.points[scope].append("svc %s" % imm)

    def adr(self, scope: str, rd, label):
        self.points[scope].append("adr %s, %s" % (rd, label))

    def mov(self, scope: str, rd, operand):
        self.points[scope].append("mov %s, %s" % (rd, operand))

    def compile(self) -> str:
        self.output.write("\n%s:\n" % self.entrypoint)

        for instruction in self.points[self.entrypoint]:
            self.output.write("    %s\n" % instruction)

        del self.points[self.entrypoint]

        for name, instructions in self.points.items():
            self.output.write("\n%s:\n" % name)

            for instruction in instructions:
                self.output.write("    %s\n" % instruction)

        return self.output.getvalue()

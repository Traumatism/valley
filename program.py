from valley.compiler import Compiler


if __name__ == "__main__":
    compiler = Compiler()
    scope = compiler.entrypoint

    compiler.puts(scope, "Hello, world !\n")
    compiler.exit(scope, 0)

    print(compiler.compile())

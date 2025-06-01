class CodeGenerator:
    def __init__(self):
        self.output = []
        self.var_map = {}
        self.label_count = 0

    def generate(self, ast):
        self.output.clear()
        self.var_map.clear()
        self.label_count = 0

        if ast[0] == 'program':
            _, name, declarations, statements = ast
            for decl in declarations:
                if decl[0] == 'var_declaration':
                    for var in decl[1]:
                        self._allocate_var(var)

            for stmt in statements:
                self._gen_statement(stmt)

            self._emit("stop", "end of program")

        return '\n'.join(self.output)

    def _allocate_var(self, var_name):
        if var_name not in self.var_map:
            self.var_map[var_name] = len(self.var_map)

    def _get_var_index(self, var_name):
        return self.var_map[var_name]

    def _new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def _emit(self, code, comment=None):
        if comment:
            self.output.append(f"{code.ljust(20)} // {comment}")
        else:
            self.output.append(code)

    def _gen_expression(self, expr):
        kind = expr[0]
        if kind == 'const':
            self._emit(f"pushi {expr[1]}", f"const {expr[1]}")
        elif kind == 'var':
            index = self._get_var_index(expr[1])
            self._emit(f"pushg {index}", f"var {expr[1]}")
        elif kind == 'bin_op':
            _, op, lhs, rhs = expr
            self._gen_expression(lhs)
            self._gen_expression(rhs)
            ops = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}
            self._emit(ops[op], f"{op} operation")
        elif kind == 'rel_op':
            _, op, lhs, rhs = expr
            self._gen_expression(lhs)
            self._gen_expression(rhs)
            ops = {'=': 'equal', '<>': 'nequal', '<': 'inf', '<=': 'infeq',
                   '>': 'sup', '>=': 'supeq'}
            self._emit(ops[op], f"{op} comparison")

    def _gen_statement(self, stmt):
        kind = stmt[0]
        if kind == 'writeln':
            for arg in stmt[1]:
                if arg[0] == 'const':
                    self._emit(f'pushs "{arg[1]}"', f'string "{arg[1]}"')
                    self._emit("writes")
                elif arg[0] == 'var':
                    index = self._get_var_index(arg[1])
                    self._emit(f"pushg {index}", f"var {arg[1]}")
                    self._emit("writei")
        elif kind == 'readln':
            for var in stmt[1]:
                if var[0] == 'var':
                    index = self._get_var_index(var[1])
                    self._emit("read")
                    self._emit("atoi")
                    self._emit(f"storeg {index}", f"store {var[1]}")
        elif kind == 'assign':
            _, target, value = stmt
            self._gen_expression(value)
            index = self._get_var_index(target[1])
            self._emit(f"storeg {index}", f"store {target[1]}")
        elif kind == 'for':
            _, direction, var, start, end, body = stmt
            index = self._get_var_index(var)
            start_label = self._new_label()
            end_label = self._new_label()

            self._gen_expression(start)
            self._emit(f"storeg {index}", f"init {var}")

            self._emit(f"{start_label}:")

            self._emit(f"pushg {index}", f"for {var}")
            self._gen_expression(end)
            self._emit("supeq" if direction == 'to' else "infeq", "compare")
            self._emit(f"jz {end_label}", "exit loop")

            for s in body:
                self._gen_statement(s)

            self._emit(f"pushg {index}")
            self._emit("pushi 1")
            self._emit("add" if direction == 'to' else "sub", "step")
            self._emit(f"storeg {index}", f"update {var}")
            self._emit(f"jump {start_label}")
            self._emit(f"{end_label}:")
        elif kind == 'while':
            _, condition, body = stmt
            start_label = self._new_label()
            end_label = self._new_label()

            self._emit(f"{start_label}:", "while start")
            self._gen_expression(condition)
            self._emit(f"jz {end_label}", "exit loop")

            for s in body:
                self._gen_statement(s)

            self._emit(f"jump {start_label}")
            self._emit(f"{end_label}:", "while end")
        elif kind == 'if':
            _, condition, then_branch, *else_branch = stmt
            else_label = self._new_label()
            end_label = self._new_label() if else_branch else else_label

            self._gen_expression(condition)
            self._emit(f"jz {else_label}", "if condition false, jump to else")

            # then
            if isinstance(then_branch, list):
                for s in then_branch:
                    self._gen_statement(s)
            else:
                self._gen_statement(then_branch)

            if else_branch:
                self._emit(f"jump {end_label}", "skip else")
                self._emit(f"{else_label}:", "else branch")
                for s in else_branch[0]:
                    self._gen_statement(s)
                self._emit(f"{end_label}:", "end if")
            else:
                self._emit(f"{else_label}:", "end if")
        elif kind == 'case':
            _, expr, branches, default = stmt
            end_label = self._new_label()
            self._gen_expression(expr)

            branch_labels = []
            for i, branch in enumerate(branches):
                label = self._new_label()
                branch_labels.append(label)
                for val in branch[1]:
                    self._emit("dup")
                    self._gen_expression(val)
                    self._emit("equal")
                    self._emit(f"jz next_case_{i}", f"check case {val[1]}")
                    self._emit(f"jump {label}")
                    self._emit(f"next_case_{i}:")

            self._emit("pop", "no case matched")
            for s in default:
                self._gen_statement(s)
            self._emit(f"jump {end_label}")

            for i, branch in enumerate(branches):
                label = branch_labels[i]
                self._emit(f"{label}:", f"case branch {i}")
                self._emit("pop")
                self._gen_statement(branch[2])
                self._emit(f"jump {end_label}")

            self._emit(f"{end_label}:", "end case")

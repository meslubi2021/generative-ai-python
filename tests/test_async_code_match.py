# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib
import ast
import typing
import re

from absl.testing import absltest
from absl.testing import parameterized

EXEMPT_DIRS = ["notebook"]
EXEMPT_DECORATORS = ["overload", "property", "setter", "abstractmethod", "staticmethod"]
EXEMPT_FILES = ["client.py", "version.py", "discuss.py", "files.py"]
EXEMPT_FUNCTIONS = ["to_dict", "_to_proto", "to_proto", "from_proto", "from_dict", "_from_dict"]


class CodeMatch(absltest.TestCase):

    def _maybe_trim_docstring(self, node):
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
        ):
            node.body = node.body[1:]

        return ast.unparse(node)

    def _inspect_decorator_exemption(self, node, fpath) -> bool:
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Attribute):
                if decorator.attr in EXEMPT_DECORATORS:
                    return True
            elif isinstance(decorator, ast.Name):
                if decorator.id in EXEMPT_DECORATORS:
                    return True
            elif isinstance(decorator, ast.Call):
                decorator_name = (
                    decorator.func.attr
                    if isinstance(decorator.func, ast.Attribute)
                    else decorator.func.id
                )
                if decorator_name in EXEMPT_DECORATORS:
                    return True
            else:
                raise TypeError(
                    f"Unknown decorator type {decorator}, during checking {node.name} from {fpath.name}"
                )

        return False

    def _execute_code_match(self, source, asource):
        asource = (
            asource.replace("anext", "next")
            .replace("aiter", "iter")
            .replace("_async", "")
            .replace("async ", "")
            .replace("await ", "")
            .replace("Async", "")
            .replace("ASYNC_", "")
        )
        asource = re.sub(" *?# type: ignore", "", asource)
        self.assertEqual(source, asource)

    @absltest.skip("This test is broken: globally matching functions based only on the name")
    def test_code_match_for_async_methods(self):
        for fpath in (pathlib.Path(__file__).parent.parent / "google").rglob("*.py"):
            if fpath.name in EXEMPT_FILES or any([d in fpath.parts for d in EXEMPT_DIRS]):
                continue
            # print(f"Checking {fpath.absolute()}")
            code_match_funcs: dict[str, ast.AST] = {}
            source = fpath.read_text()
            source_nodes = ast.parse(source)

            for node in ast.walk(source_nodes):
                if isinstance(
                    node, (ast.FunctionDef, ast.AsyncFunctionDef)
                ) and not node.name.startswith("__"):
                    name = node.name[:-6] if node.name.endswith("_async") else node.name
                    if name in EXEMPT_FUNCTIONS or self._inspect_decorator_exemption(node, fpath):
                        continue
                    # print(f"Checking {node.name}")

                    if func_name := code_match_funcs.pop(name, None):
                        snode, anode = (
                            (func_name, node)
                            if isinstance(node, ast.AsyncFunctionDef)
                            else (node, func_name)
                        )
                        func_source = self._maybe_trim_docstring(snode)
                        func_asource = self._maybe_trim_docstring(anode)
                        self._execute_code_match(func_source, func_asource)
                        # print(f"Matched {node.name}")
                    else:
                        code_match_funcs[node.name] = node


if __name__ == "__main__":
    absltest.main()

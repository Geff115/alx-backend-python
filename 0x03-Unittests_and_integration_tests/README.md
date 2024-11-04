0x03. Unittests and Integration Tests
UnitTests
Back-end
Integration tests
 Weight: 1


Requirements:

    - All my files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    - The first line of all my files should be exactly #!/usr/bin/env python3
    - My code should use the pycodestyle style (version 2.5)
    - All my modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    - All my classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    - All my functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    - All my functions and coroutines must be type-annotated.


Learning objectives:

1. The difference between unit and integration tests.
2. Common testing patterns such as mocking, parametrizations and fixtures
3. Parameterized
4. Memoization
5. How to mock a readonly property with mock
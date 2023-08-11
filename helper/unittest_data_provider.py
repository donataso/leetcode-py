def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test and runs it as a subtest"""
    def test_decorator(fn):
        def repl(self, *args):
            for i, test_data in enumerate(fn_data_provider()):
                with self.subTest('dataset {}'.format(i)):
                    fn(self, *test_data)
        return repl
    return test_decorator

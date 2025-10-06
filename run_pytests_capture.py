import sys
import pytest
import io
import contextlib

log_path = 'tests_output.log'
with open(log_path, 'w', encoding='utf-8') as out:
    try:
        # capture pytest output
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            ret = pytest.main(['-q', 'tests'])
        out.write(f"\nEXIT_CODE: {ret}\n")
    except Exception as e:
        out.write('ERROR RUNNING TESTS:\n')
        out.write(str(e))
        out.write('\n')
        raise

print('WROTE', log_path)

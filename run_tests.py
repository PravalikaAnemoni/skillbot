import sys
import pytest

if __name__ == '__main__':
    # Run pytest programmatically and print a short summary
    ret = pytest.main(['-q', 'tests'])
    if ret == 0:
        print('ALL TESTS PASSED')
    else:
        print(f'TESTS FAILED (exit code {ret})')
    sys.exit(ret)

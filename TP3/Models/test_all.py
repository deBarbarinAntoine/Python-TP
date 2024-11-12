try:
    from TP3.Models import test_book_run, test_library_run, test_boat_run, test_port_run
except ImportError:
    from test_book import test_book_run
    from test_library import test_library_run
    from test_boat import test_boat_run
    from test_port import test_port_run

def test_all_run() -> str:
    buffer: str = ""
    buffer += test_book_run()
    buffer += test_library_run()
    buffer += test_boat_run()
    buffer += test_port_run()
    return buffer

if __name__ == '__main__':
    print(test_all_run())
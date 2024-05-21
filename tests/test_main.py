import subprocess

def test_cli_printer():
    result = subprocess.run(
        ['python', '-m', 'cli_printer.main', 'Test Message'],
        capture_output=True,
        text=True
    )
    assert 'Message: Test Message' in result.stdout

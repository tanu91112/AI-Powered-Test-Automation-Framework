import subprocess
import time


def run_test():

    start=time.time()

    result=subprocess.run(
        [
            "python",
            "tests/generated_test.py"
        ],
        capture_output=True,
        text=True
    )


    execution_time=time.time()-start


    return {
        "status":
        "PASS" if result.returncode==0 else "FAIL",

        "output":
        result.stdout,

        "error":
        result.stderr,

        "time":
        execution_time
    }
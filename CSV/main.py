import subprocess
import sys


def run_script(script_name):
    try:
        result = subprocess.run([sys.executable, script_name],
                                capture_output=True,
                                text=True,
                                check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}:")
        print(e.output)
        sys.exit(1)


if __name__ == "__main__":
    try:
        # Run generate.py
        print("Running generate.py...")
        run_script('generate.py')

        # Run csvtojson.py
        print("Running csvtojson.py...")
        run_script('csvtojson.py')
        run_script('test.py')
        print("All scripts executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
